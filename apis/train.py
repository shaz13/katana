import os
import pickle
import pandas as pd

from numpy.random import RandomState
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from datetime import datetime
from flask_restplus import Namespace, Resource, fields
from apis.config import MODELS_ROOT, TEMP_CSV

api = Namespace('train', description='Namespace for training')

@api.route('/fit')
class Train(Resource):

    def get(self):
        return self.train() # {'success': 'Training pipeline successful',}

    def train(self, file=None, target_var=None):

        # curretnly it's having nothing as i/p
        start_time = datetime.now()

        if target_var is None:
            response = "Outcome"
        else:
            response = target_var

        if file is None: # sample file
            df = pd.read_csv(TEMP_CSV)
        else:
            df = pd.read_csv(file)

        train, valid = self._split_dataset(df, 0.20, 12345)
        predictors   = df.columns[:-1]
        
        clf = LogisticRegression(C=0.1, solver='lbfgs')
        clf.fit(X=train[predictors], y=train[response])

        self._persist_to_disk(clf, MODELS_ROOT)
        validation_predictions = clf.predict_proba(valid[predictors])[:, 1]
        score = round(roc_auc_score(valid[[response]], validation_predictions), 3)

        return {
            "success": "Training pipeline successful",
            "msg" : f"Succesfully Trained in {datetime.now() - start_time}", #.seconds
            "metric" : f"roc_auc_score -: {score}",
            "status_code" : 200,
            }

    def _split_dataset(self, df, validation_percentage, seed):
        
        state = RandomState(seed)
        validation_indexes = state.choice(df.index, 
                                          int(len(df.index) * validation_percentage), 
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
                "msg" : f"Successfully saved model at {path_to_file} :)"
                }
        else:
            return {
                "msg" : "Failed to save the model :("
                }
