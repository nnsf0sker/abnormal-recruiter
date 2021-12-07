from random import choice
from typing import List

from models.answer_response import AnswerResponse


# будущие_вопросы = [
#     "Есть ли у Вас домашние питомцы?"
#     "Курите ли Вы?"
#     "Есть ли у Вас тутаировки?"
#     "Верите ли Вы в Бога?"
#     "Два дважды" "4" "22" "2 2", "два два"
#     "Готовы ли Вы работать "
# ]


class AnswerError(Exception):
    pass


class ExplicitAnswer(AnswerError):
    def __init__(self, explicit_parts: List[str]):
        super(ExplicitAnswer, self).__init__()
        self.explicit_parts = explicit_parts


class Question:
    repeat_please_message = [
        "Некорректный ответ, давайте попробуем ещё раз, пожалуйста."
    ]
    guaranteed_explicit_parts = [
        "хуйня",
        "хуёв",
        "пизда",
        "мудак",
        "пиздец"
        "еблан",
        "ебать",
        "ебля",
        "ёбан"
    ]
    suspecting_explicit_parts = [
        "хуй",
        "пизд",
        "муд",
        "еба",
        "ебл"
    ]
    response_for_explicit = [
        "Что Вы себе позволяете!? Лучше закончим наше общение, пока Вы больше ничего не наговорили.",
    ]
    question_text: List[str]

    def ask_question(self) -> str:
        return choice(self.question_text)

    def check_answer(self, answer: str, context: dict) -> AnswerResponse:
        pass

    @staticmethod
    def _get_explicit_response():
        return AnswerResponse(tag="explicit", message=choice(Question.response_for_explicit), action="break")

    # TODO: refactor function
    def _find_explicit_parts(self, answer: str) -> dict:
        found_guaranteed_explicit_parts = [
            explicit_part
            for explicit_part in Question.guaranteed_explicit_parts
            if explicit_part in answer.lower()
        ]
        found_suspecting_explicit_parts = [
            explicit_part
            for explicit_part in Question.suspecting_explicit_parts
            if explicit_part in answer.lower()
        ]
        return {
            "found_guaranteed_explicit_parts": found_guaranteed_explicit_parts,
            "found_suspecting_explicit_parts": found_suspecting_explicit_parts
        }

    def _is_answer_explicit(self, answer: str, context: dict) -> bool:
        explicit_parts = self._find_explicit_parts(answer)
        if explicit_parts["found_guaranteed_explicit_parts"]:
            return True
        if len(explicit_parts["found_suspecting_explicit_parts"]) > 2:
            return True
        return False
