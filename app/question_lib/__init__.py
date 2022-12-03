from .model import QuestionLib, QuestionLibHeader

from pathlib import Path


class LIBS:
    headers: dict[str, QuestionLibHeader]

    def load_headers(self) -> dict[str, QuestionLibHeader]:
        self.headers = {
            file.stem: QuestionLibHeader.parse_file(file)
            for file in Path("data/question_libs").iterdir()
        }
    
    @staticmethod
    async def load_lib(lib_name:str):
        return QuestionLib.parse_file(Path("data/question_libs").joinpath(f"{lib_name}.json"))
