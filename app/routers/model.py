from pathlib import Path

from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

from ..question_lib import LIBS
from ..question_lib.model import QuestionLibHeader, QuestionLib


router = APIRouter(prefix="/libs")


@router.get(
    "/all",
    response_model=dict[str, QuestionLibHeader],
    response_description="获取到所有题库简要信息",
    tags=['libs'],
    description="获取所有题库，为一个 `object`，键为题库 ID，值为题库简要信息",
    name="获取所有题库简要信息",
)
async def get_all_libs():
    return LIBS.load_headers()


@router.get(
    "/get",
    response_model=QuestionLib,
    responses={
        404: {
            "description": "题库不存在",
        }
    },
    response_description="获取到题库",
    tags=['libs'],
    description="获取指定题库",
    name="获取指定题库",
)
async def get_lib(name: str):
    try:
        return LIBS.load_lib(name)
    except Exception:
        return JSONResponse(
            status_code=404, content={"message": "Question Lib not found"}
        )
