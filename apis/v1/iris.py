import uuid
from fastapi.routing import APIRouter
from apis.models.iris import IrisFlowerRequestModel
from apis.models.iris import IrisPredictionResponseModel
from apis.models.base import TrainingStatusResponse
from core.trainer import IrisTrainerInstance

router = APIRouter(prefix="/iris")
labels = ["Setosa", "Versicolor", "Virginica"]
# Load trained model. Dummy model being trained on startup...
trainer = IrisTrainerInstance()
trainer.load_data()
iris_model = trainer.train()


@router.post(
    "/trainModel", tags=["iris"], response_model=TrainingStatusResponse
)
async def iris_train():
    training_id = uuid.uuid1()
    # Queue training / start training via RabbitMQ, Queue, etc..
    # Add task here
    # Track the id in a database
    return {
        "training_id": training_id,
        "status": "Training started",
    }


@router.post(
    "/predictFlower", tags=["iris"], response_model=IrisPredictionResponseModel
)
async def iris_prediction(iris: IrisFlowerRequestModel):
    payload = [
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width,
    ]
    prediction = iris_model.predict([payload])
    target = labels[prediction[0]]
    result = {"prediction_id": iris.prediction_id, "classification": target}
    return result
