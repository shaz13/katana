from loguru import logger
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apis.v1.iris import router as iris_ns


# Initialize logging
logger.add("./logs/katana.log", rotation="500 MB")
logger.info("Initializing application : Katana")

app = FastAPI(title="Katana ML FastAPI Serving ⚡", version=1.0)
logger.info("Adding Iris namespace route")
app.include_router(iris_ns)


@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse("/docs")
