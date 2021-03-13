#
# MIT License
# 
# Copyright (c) 2021 Mohammad Shahebaz
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
from fastapi.routing import APIRouter
from apis.models.iris import IrisFlowerRequestModel, IrisPredictionResponseModel
from core.trainer import IrisTrainerInstance

router = APIRouter(prefix='/iris')
labels = ['Setosa', 'Versicolor', 'Virginica']
    # Load trained model. Dummy model being trained on startup...
trainer = IrisTrainerInstance()
trainer.load_data()
iris_model = trainer.train_linear_model()

    
@router.post("/trainModel", tags=['iris'],)
async def  iris_train():
    return {
        "training_id" : "056b5d3d-f983-4cd3-8fbd-20b8dad24e0f",
        "status": "Training started"
    }

@router.post("/predictClass", tags=['iris'], response_model=IrisPredictionResponseModel)
async def  iris_prediction(iris: IrisFlowerRequestModel):
    payload = [iris.sepal_length, 
               iris.sepal_width, 
               iris.petal_length, 
               iris.petal_width]
    prediction = iris_model.predict([payload])
    target  =labels[prediction[0]]
    result = {
        "prediction_id" : iris.prediction_id,
        "classification" : target
    }
    return result

