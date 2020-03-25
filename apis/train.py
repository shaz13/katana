import os
import pickle
import pandas as pd
import hashlib
import keras
import numpy as np
import tensorflow as tf

from apis import parsers
from apis.model import SimpleModel
from numpy.random import RandomState
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from datetime import datetime
from flask_restplus import Namespace, Resource, fields, abort
from apis.config import MODEL_ROOT, TEMP_CSV, APP_ROOT, DL_MODEL
from werkzeug.utils import secure_filename
from datetime import datetime

api = Namespace('train', description='Namespace for training')
graph = tf.get_default_graph()

dl = SimpleModel()
model = dl._create_model()
model.load_weights(DL_MODEL)

@api.route('/UCIDiabetes')
class TrainLogisticClassifier(Resource):

	def post(self):
		return self.train(target_var="Outcome")

	def train(self, file=None, target_var=None):

		# curretnly it's having nothing as i/p
		start_time = datetime.now()

		if target_var is None:
			response = "Outcome"
		else:
			response = target_var

		if file is None:  # sample file
			df = pd.read_csv(TEMP_CSV)
		else:
			df = pd.read_csv(file)

		train, valid = self._split_dataset(df, 0.20, 12345)
		predictors = [x for x in df.columns if x not in [response]]
		clf = LogisticRegression(C=0.1, solver='lbfgs')
		clf.fit(X=train[predictors], y=train[response])
		end_time = datetime.now()
		self._persist_to_disk(clf, MODEL_ROOT)
		validation_predictions = clf.predict_proba(valid[predictors])[:, 1]
		score = round(roc_auc_score(
			valid[[response]], validation_predictions), 3)

		return {
			"training_info": {
				"started_at": str(start_time),
				"completed_at": str(end_time),
				"elapsed_time":  str((end_time - start_time).total_seconds())
			},
			"model_score": score,
			"success": "Training pipeline successful"
		}, 200

	def _split_dataset(self, df, validation_percentage, seed):

		state = RandomState(seed)
		validation_indexes = state.choice(df.index,
										  int(len(df.index) *
											  validation_percentage),
										  replace=False
										  )
		training_set = df.loc[~df.index.isin(validation_indexes)].copy()
		validation_set = df.loc[df.index.isin(validation_indexes)].copy()

		return training_set, validation_set

	def _persist_to_disk(self, classifier, path_to_file):

		with open(path_to_file, "wb") as f:
			pickle.dump(classifier, f)

		if os.path.isfile(path_to_file):
			return {
				"message": f"Successfully saved model at {path_to_file} :)"
			}
		else:
			return {
				"message": "Failed to save the model :("
			}

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'bmp']
def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@api.route('/upload')
class my_file_upload(Resource):
	@api.expect(parsers.file_upload)
	def post(self):
		args = parsers.file_upload.parse_args()
		if args['img_file'].mimetype in ['image/jpeg', 'image/png', 'image/jpg']:
			destination = APP_ROOT / 'dataset' / 'medias'
			if not os.path.exists(destination):
				os.makedirs(destination)

			ext = '.' + args['img_file'].mimetype.split('/')[1]
			img_file = f'{destination}' + hashlib.sha256(str(datetime.now()).encode('utf-8')).hexdigest() + ext
			img_file = img_file.lower()
			args['img_file'].save(img_file)

			img_array = dl.process_image(fname=img_file)
			img_array = np.reshape(img_array, (1,28,28,1))

			with graph.as_default():
				preds = model.predict(img_array)
				print(preds, np.argmax(preds, axis = 1))
				classes = np.argmax(preds, axis = 1)[0]
		else:
			abort(404)
		return {'status': f'Image File Was Successfully Uploaded! And it seems to belong to Class -> {classes}'}
