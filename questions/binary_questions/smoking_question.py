from typing import Dict
from typing import List


class SmokingQuestion:
    question_text: List[str] = [
        "Курили ли Вы за последние полгода (сигареты, вейпы, кальяны и подобное)?"
    ]
    possible_answers: Dict[str, str] = {
        "да": [
            "",
        ],
        "нет": [
            ""
        ]
    }