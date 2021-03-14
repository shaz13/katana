from pydantic import BaseModel


class TrainingStatusResponse(BaseModel):
    training_id: str = "056b5d3d-f983-4cd3-8fbd-20b8dad24e0f"
    status: str = "Training  queued"
