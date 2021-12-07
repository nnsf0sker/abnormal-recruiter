from random import choice
from random import randint
from typing import Dict
from typing import List

from models.answer_response import AnswerResponse
from models.question import Question


class BinaryQuestion(Question):
    question_text: List[str] = ["Да или нет?"]
    possible_answers: Dict[str, str] = {
        "да": ["Хуй нааа!"],
        "нет": ["Пидора ответ"]
    }

    @staticmethod
    def _get_unknown_answer_response():
        return AnswerResponse(
            tag="unknown_answer",
            message=choice(BinaryQuestion.repeat_please_message),
            action="repeat"
        )

    def _get_incorrect_answer_response(self, answer):
        return AnswerResponse(
            tag="incorrect_answer",
            message=choice(self.possible_answers[answer.lower()]),
            action="break"
        )

    @staticmethod
    def _get_correct_answer_response():
        return AnswerResponse(
            tag="correct_answer",
            message="Ok",
            action="continue"
        )

    @staticmethod
    def _is_answer_correct() -> bool:
        return bool(randint(0, 1))

    def check_answer(self, answer: str, context: dict) -> AnswerResponse:
        # TODO: Убрать это в декоратор
        if self._is_answer_explicit(answer, context):
            return BinaryQuestion._get_explicit_response()

        if answer.lower() not in self.possible_answers:
            return BinaryQuestion._get_unknown_answer_response()

        if not self._is_answer_correct():
            return self._get_incorrect_answer_response(answer)

        else:
            return self._get_correct_answer_response()

