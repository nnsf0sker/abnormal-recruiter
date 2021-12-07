from typing import Dict
from typing import List

from questions.binary_questions.binary_question import BinaryQuestion


class HandSideQuestion(BinaryQuestion):
    question_text: List[str] = ["Вы левша или правша?"]
    possible_answers: Dict[str, str] = {
        "левша": [],
        "правша": []
    }
