from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apis.v1.iris import router as iris_ns


app = FastAPI(title="Katana ML FastAPI Serving ⚡", version=1.0)

app.include_router(iris_ns)


@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse("/docs")
