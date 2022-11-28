import uvicorn
from fastapi import FastAPI

from .routers import router

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
    uvicorn.run("app.main:app")
