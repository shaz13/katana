from pydantic import BaseModel, Field


class MaskLanguageModelRequestModel(BaseModel):
    predictionId: str = "f75ef3b8-f414-422c-87b1-1e21e684661c"
    text: str = "Am I a [MASK] person if I save my green planet?"


class MaskLanguageModelResponseModel(BaseModel):
    score: float = 0.1
    token: int = 100
    token_str: str = "token string"
    orginal_sequence: str = "Sequence with [MASK]"
    sequence: str = "Sequence with [MASK] replaced with token word"
