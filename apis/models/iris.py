from pydantic import BaseModel, Field


class IrisFlowerRequestModel(BaseModel):
    prediction_id: str = "f75ef3b8-f414-422c-87b1-1e21e684661c"
    sepal_length: float = 12
    sepal_width: float = 4
    petal_length: float = 17
    petal_width: float = 3


class IrisPredictionResponseModel(BaseModel):
    prediction_id: str = "f75ef3b8-f414-422c-87b1-1e21e684661c"
    classification: str = "virginica"
