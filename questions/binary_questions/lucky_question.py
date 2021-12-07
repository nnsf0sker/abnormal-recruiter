from typing import Dict
from typing import List

from questions.binary_questions.binary_question import BinaryQuestion


class LuckyQuestion(BinaryQuestion):
    question_text: List[str] = ["Давайте уж начистоту. Просто угадайте цифру от 1 до 4, которую я загадал."]
    possible_answers: Dict[str, str] = {
        "1": [],
        "2": [],
        "3": [],
        "4": []
    }
