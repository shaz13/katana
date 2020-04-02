import os
import pickle
import pandas as pd
import logging
import json

from numpy.random import RandomState
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from datetime import datetime
from flask_restx import Namespace, Resource, fields
from apis.config import MODEL_ROOT, TEMP_CSV

api = Namespace('train', description='Namespace for training')
#  using a common logger for success/failure/tracebacks
#  that's how we can fetch a previously defined logger in logging_config files
logger = logging.getLogger("werkzeug")

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

        msg = {
            "training_info": {
                "started_at": str(start_time),
                "completed_at": str(end_time),
                "elapsed_time":  str((end_time - start_time).total_seconds())
            },
            "model_score": score,
            "success": "Training pipeline successful"
        }

        logger.info(json.dumps(msg))
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
            logger.info(json.dumps({
                "message": f"Successfully saved model at {path_to_file} :)"
            }))
            
            return {
                "message": f"Successfully saved model at {path_to_file} :)"
            }
        else:
            return {
                "message": "Failed to save the model :("
            }
