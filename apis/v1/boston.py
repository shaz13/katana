import uuid
from loguru import logger
from fastapi.routing import APIRouter
from apis.models.base import TrainingStatusResponse
from apis.models.house import BostonHouseRequestModel, BostonHouseResponseModel
from core.trainer import BostonHousePriceTrainerInstance

router = APIRouter(prefix="/boston")
# Load trained model. Dummy model being trained on startup...
logger.info("Training/Loading iris classification model")
trainer = BostonHousePriceTrainerInstance()
boston_model = trainer.train()
logger.info("Training completed")


@router.post(
    "/trainModel", tags=["boston"], response_model=TrainingStatusResponse
)
async def boston_train():
    training_id = uuid.uuid1()
    # Queue training / start training via RabbitMQ, Queue, etc..
    # Add task here
    # Track the id in a database
    return {
        "trainingId": str(training_id),
        "status": "Training started",
    }


@router.post(
    "/predictPrice", tags=["boston"], response_model=BostonHouseResponseModel
)
async def boston_price_prediction(body: BostonHouseRequestModel):
    request = body.dict()
    payload = [x for x in request.values()]
    prediction = boston_model.predict([payload])
    result = {"predictionId": str(uuid.uuid1()), "predictedPrice": prediction}
    return result
