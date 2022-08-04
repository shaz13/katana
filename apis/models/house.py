from pydantic import BaseModel, Field


class BostonHouseRequestModel(BaseModel):
    """
    Dataset description

    1. CRIM      per capita crime rate by town
    2. ZN        proportion of residential land zoned for lots over
                 25,000 sq.ft.
    3. INDUS     proportion of non-retail business acres per town
    4. CHAS      Charles River dummy variable (= 1 if tract bounds
                 river; 0 otherwise)
    5. NOX       nitric oxides concentration (parts per 10 million)
    6. RM        average number of rooms per dwelling
    7. AGE       proportion of owner-occupied units built prior to 1940
    8. DIS       weighted distances to five Boston employment centres
    9. RAD       index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 Biased variable
    13. LSTAT    % lower status of the population
    """

    # prediction_id: str = "387ef3d8-84a5-11eb-a8fc-84c5a6c1c8e2"
    crimeRateByTown: float = Field(
        example=0.00632, description="Per capita crime rate by town"
    )
    residentZoneProportion: float = Field(
        example=18.00,
        description="Proportion of residential land \
                     zoned for lots over 25,000 sq.ft.",
    )
    nonRetailBusinessArea: float = Field(
        example=2.310,
        description="Proportion of non-retail business acres per town",
    )
    charlesRiverVar: float = Field(
        example=0,
        description="Charles River var (= 1 if tract bounds river; else 0 )",
    )
    nitricOxidePpm: float = Field(
        example=0.5380,
        description="Nitric oxides concentration (parts per 10 million)",
    )
    averageRooms: float = Field(
        example=6.5750,
        description="Average number of rooms per dwelling",
    )
    ageOfHouse: float = Field(
        example=65.20,
        description="Proportion of owner-occupied units built prior to 1940",
    )
    distFromCentre: float = Field(
        example=4.0900,
        description="Weighted distances to five Boston employment centres",
    )
    idxRadial: float = Field(
        example=0,
        description="Index of accessibility to radial highways",
    )
    taxRate: float = Field(
        example=296,
        description="Full-value property-tax rate per $10,000",
    )
    pupilTeacherRatio: float = Field(
        example=15.30,
        description="Pupil-teacher ratio by town",
    )
    discriminateProportion: float = Field(
        example=396.30,
        description="Discriminate proportion",
    )
    percentLowerStatPopulation: float = Field(
        example=4.30,
        description="Percentage of lower status of the population",
    )


class BostonHouseResponseModel(BaseModel):
    predictionId: str = "387ef3d8-84a5-11eb-a8fc-84c5a6c1c8e2"
    predictedPrice: float = "3349030"
