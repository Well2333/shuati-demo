import json
from pathlib import Path


def test_parse_question() -> None:
    from .model import (
        SAQsQuestion,
        NestedQuestion,
        SelectQuestion,
        JudgmentQuestion,
        CompletionQuestion,
        MultiSelectQuestion,
        parse_questions,
    )

    with open(
        Path(__file__)
        .parents[1]
        .joinpath("data", "question_libs", "example_question_lib.json"),
        encoding="utf8",
    ) as f:
        data = json.load(f)
    parsed_item = [parse_questions(i) for i in data["questions"].values()]
    assert len(parsed_item) == 6
    assert isinstance(parsed_item[0], SelectQuestion)
    assert isinstance(parsed_item[1], MultiSelectQuestion)
    assert isinstance(parsed_item[2], JudgmentQuestion)
    assert isinstance(parsed_item[3], CompletionQuestion)
    assert isinstance(parsed_item[4], SAQsQuestion)
    assert isinstance(parsed_item[5], NestedQuestion)

    subquestions = parsed_item[5].subquestions
    assert len(subquestions) == 3
    assert all(
        isinstance(subquestion, SelectQuestion) for subquestion in subquestions
    )
