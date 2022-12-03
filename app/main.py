import uvicorn
from fastapi import FastAPI,UploadFile

from .routers import router
from .utils.log import LOGGING_CONFIG

app = FastAPI(
    debug=True,
    title="shuati-demo",
    description="shuati-demo",
    openapi_tags=[
        {
            "name": "libs",
            "description": "题库相关操作",
        }
    ],
)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, log_config=LOGGING_CONFIG)
UploadFile.read()