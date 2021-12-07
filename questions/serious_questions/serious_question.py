from random import choice
from typing import Dict
from typing import List

from models.answer_response import AnswerResponse
from models.question import Question


class SeriousQuestion(Question):
    question_text: List[str] = [
        "<Текст вопроса №1>", "<Текст вопроса №2>", "<Текст вопроса №3>"
    ]
    correct_answer = "правильный ответ"
    possible_answers: Dict[str, str] = {
        "правильный ответ": ["Вы ответили правильно"],
        "неправильный ответ": ["Вы ответили неправильно"]
    }

    @staticmethod
    def _get_unknown_answer_response():
        return AnswerResponse(
            tag="unknown_answer",
            message=choice(SeriousQuestion.repeat_please_message),
            action="repeat"
        )

    def _get_incorrect_answer_response(self, answer):
        return AnswerResponse(
            tag="incorrect_answer",
            message=choice(self.possible_answers[answer.lower()]),
            action="break"
        )

    def _get_correct_answer_response(self, answer):
        return AnswerResponse(
            tag="correct_answer",
            message=choice(self.possible_answers[answer.lower()]),
            action="continue"
        )

    def _is_answer_correct(self, answer: str) -> bool:
        return answer.lower() == self.correct_answer

    def check_answer(self, answer: str, context: dict) -> AnswerResponse:
        # TODO: Убрать это в декоратор
        if self._is_answer_explicit(answer, context):
            return SeriousQuestion._get_explicit_response()

        if answer.lower() not in self.possible_answers:
            return SeriousQuestion._get_unknown_answer_response()

        if not self._is_answer_correct(answer):
            return self._get_incorrect_answer_response(answer)

        else:
            return self._get_correct_answer_response(answer)

