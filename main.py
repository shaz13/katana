from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apis.v1.iris import router as iris_ns


app = FastAPI(title="Katana Fast API Serving", version=1.0)

app.include_router(iris_ns)


# @app.get("/", tags=["redirect"])
# async def redirect():
#     return RedirectResponse("/docs")
