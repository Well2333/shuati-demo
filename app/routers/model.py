from pathlib import Path
from typing import Any, Type, Literal

from fastapi.routing import APIRouter
from pydantic import BaseModel, validator
from fastapi.responses import JSONResponse


class Question(BaseModel):
    """
    题目基本数据


    - **options**: 题目类型：单选、多选、判断、填空、简答、嵌套问题
    - **content**: 题目内容: markdown（子问题中为 None）
    - **analysis**: 题目解析: markdown
    """

    type: Literal[
        "Select", "MultiSelect", "Judgment", "Completion", "SAQs", "Nested"
    ]
    """题目类型"""
    content: str | None = ""
    """题目内容: markdown（子问题中为 None）"""
    analysis: str | None = None
    """题目解析: markdown"""


class SelectQuestion(Question):
    """
    单选题，`answer` 中的 "A" 对应 `options` 中的第 1 个选项，其他选项以此类推。

    - **options**: 选项：list[markdown]
    - **answer**: 答案
    """

    type: Literal["Select"]

    options: list[str]
    """选项: list[markdown]"""
    answer: str
    """答案"""


class MultiSelectQuestion(Question):
    """
    多选题，`answer` 中至少包含两个英文字母。

    - **options**: 选项：list[markdown]
    - **answer**: 答案
    - **ordered**: `ordered` 为 `true` 时，判断答案时将会额外判断其排列顺序是否与 `answer` 中的答案一致。
    """

    type: Literal["MultiSelect"]

    options: list[str]
    """选项：list[markdown]"""
    answer: str
    """答案"""
    ordered: bool
    """`ordered` 为 `true` 时，判断答案时将会额外判断其排列顺序是否与 `answer` 中的答案一致。"""


class JudgmentQuestion(Question):
    """
    判断题，判断对错。

    - **answer**: 答案
    """

    type: Literal["Judgment"]

    answer: bool
    """答案"""


class CompletionQuestion(Question):
    """
    填空题。

    - **gaps**: 空缺数量
    - **answer**: 答案: list[markdown]
    - **is_absolute**: 如果 `is_absolute=false` 此处将不会进行对错判断，答案将作为参考答案（主观题）。
      `is_absolute=true` 时将作为绝对答案进行比较（客观题）。
    """

    type: Literal["Completion"]

    gaps: int
    """空缺数量"""
    answer: list[str]
    """答案: list[markdown]"""
    is_absolute: bool
    """
    如果 `is_absolute=false` 此处将不会进行对错判断，答案将作为参考答案（主观题）。
    `is_absolute=true` 时将作为绝对答案进行比较（客观题）。
    """


class SAQsQuestion(Question):
    """
    简答题。

    - **answer**: 答案

    - **is_absolute**: 如果 `is_absolute=false` 此处将不会进行对错判断，答案将作为参考答案（主观题）。
      `is_absolute=true` 时将作为绝对答案进行比较（客观题）。
    """

    type: Literal["SAQs"]

    answer: str
    """答案"""
    is_absolute: bool
    """
    如果 `is_absolute=false` 此处将不会进行对错判断，答案将作为参考答案（主观题）。
    `is_absolute=true` 时将作为绝对答案进行比较（客观题）。
    """


class NestedQuestion(Question):
    """
    嵌套题型通常用于一个题干对应多个问题的题型。
    其中的 `subquestions` 可内含至少一个前文所介绍的题型，各个问题间的题型也可不同。
    但考虑到用户的阅读体验和渲染方案，嵌套问题中将不能包含嵌套问题。

    - **subquestions**: 子问题
    """

    type: Literal["Nested"]

    subquestions: list[Question]
    """子问题"""


QuestionType = (
    SelectQuestion
    | MultiSelectQuestion
    | JudgmentQuestion
    | CompletionQuestion
    | SAQsQuestion
    | NestedQuestion
)
QUESTION_TYPES: dict[str, Type[QuestionType]] = {
    "Select": SelectQuestion,
    "MultiSelect": MultiSelectQuestion,
    "Judgment": JudgmentQuestion,
    "Completion": CompletionQuestion,
    "SAQs": SAQsQuestion,
    "Nested": NestedQuestion,
}


def parse_questions(question: dict[str, Any]) -> QuestionType:
    type_ = question.get("type")
    if type_ is None:
        raise ValueError("Type of the question is None.")
    question_type = QUESTION_TYPES.get(type_, None)
    if question_type is None:
        raise TypeError(f"No such type: {type_}")
    if question_type is NestedQuestion:
        question["subquestions"] = [
            parse_questions(i) for i in question["subquestions"]
        ]
    return question_type.parse_obj(question)


class QuestionLib(BaseModel):
    """
    题库

    - **name**: 题库名
    - **version**: 题库版本
      建议采用 `YYYYMMDD-当日修改次数` 进行命名，
      例如：1919 年 8 月 10 日第 1 次修改为 `19190810-1`
    - **description**: 题库简介
    - **author**: 题库作者信息
    - **license**: 题库开源协议，默认为 `cc-by-nc-sa` 协议即
      [`署名-非商业性使用-相同方式共享`](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)
      协议。

      关于知识共享协议可参考 <https://creativecommons.org/choose/> 了解并选择，
      以保障您的作品在遭到非法用途时可以合法进行维护权力。
    - **tags**: 题库标签
    - **questions**: 题库内的问题，另见以 Question 为命名的模型
    """

    name: str
    """题库名"""
    version: str | None = None
    """
    题库版本
    建议采用 `YYYYMMDD-当日修改次数` 进行命名，
    例如：1919 年 8 月 10 日第 1 次修改为 `19190810-1`
    """
    description: str | None = None
    """题库简介"""
    author: str | None = None
    """题库作者信息"""
    license: str = "MIT"
    """
    题库开源协议，默认为 `cc-by-nc-sa` 协议即
    `署名-非商业性使用-相同方式共享`
    (https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 协议。

    关于知识共享协议可参考 <https://creativecommons.org/choose/> 了解并选择，
    以保障您的作品在遭到非法用途时可以合法进行维护权力。
    """
    tags: list[str]
    """题库标签"""
    questions: dict[str, QuestionType]
    """题库内的问题"""

    @validator("questions", pre=True)
    def parse_questions(cls, v):
        for k, v_ in v.items():
            v[k] = parse_questions(v_)
        return v


LIBS: dict[str, QuestionLib] = {
    file.stem: QuestionLib.parse_file(file)
    for file in Path("data/question_libs").iterdir()
}

router = APIRouter(prefix="/libs")


@router.get(
    "/all",
    response_model=dict[str, QuestionLib],
    response_description="获取到所有题库",
    tags=['libs'],
    description="获取所有题库，为一个 `object`，键为题库 ID，值为题库内容",
    name="获取所有题库",
)
async def get_all_libs():
    return LIBS


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
    if lib := LIBS.get(name):
        return lib
    return JSONResponse(
        status_code=404, content={"message": "Question Lib not found"}
    )
