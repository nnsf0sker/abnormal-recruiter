from typing import Dict
from typing import List

from questions.binary_questions.binary_question import BinaryQuestion


class HandSideQuestion(BinaryQuestion):
    question_text: List[str] = ["Что идёт сначала: sin или cos?"]
    possible_answers: Dict[str, str] = {
        "sin": [],
        "cos": []
    }
