from pydantic import BaseModel, Field


class IrisFlowerRequestModel(BaseModel):
    sepalLength: float = Field(example=12, description="Sepal length in cms")
    sepalWidth: float = Field(example=4, description="Sepal width in cms")
    petalLength: float = Field(example=17, description="Petal length in cms")
    petalWidth: float = Field(example=7, description="Sepal width in cms")


class IrisPredictionResponseModel(BaseModel):
    predictionId: str = "f75ef3b8-f414-422c-87b1-1e21e684661c"
    classification: str = "virginica"
