import time
from loguru import logger
from fastapi.routing import APIRouter
from core.pipeline import MaskLanguageModelPipe
from apis.models.base import TrainingStatusResponse
from apis.models.masklang import (
    MaskLanguageModelRequestModel,
    MaskLanguageModelResponseModel
)
from typing import List

router = APIRouter(prefix="/mask")
# Load trained model. Dummy model being trained on startup...
logger.info("Training/Loading Mask language model")
masking_pipeline = MaskLanguageModelPipe()
logger.info("Model load completed")

# Warm loading / Warm up
start = time.time()
logger.info("Model warm loading...")
masking_pipeline.predict("[MASK] I am good")
end = time.time()
logger.info(f"Model warm loading completed in {round(end-start,2)} secs")


@router.post(
    "/predictMask",
    tags=["langmask"],
    response_model=List[MaskLanguageModelResponseModel],
)
async def mask_lang_prediction(payload: MaskLanguageModelRequestModel):
    text = payload.text
    logger.info(f"Recieved payload as {text}")
    logger.info(f"Processing predictions...")
    predictions = masking_pipeline.predict(text)
    for pred in predictions:
        pred["orginal_sequence"] = text
    logger.info(f"Processed successfully")
    return predictions
