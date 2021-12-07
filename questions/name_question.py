from random import choice

from models.question import Question
from models.answer_response import AnswerResponse


class NameQuestion(Question):
    question_text = [
        "Ваше имя?",
        "Как Вас зовут?",
        "Как Ваше имя?",
        "Как я могу к Вам обращаться?",
    ]
    good_response_message = [
        "Прекрасное имя!",
        "Будем знакомы.",
        "Приятно познакомиться.",
        "Очень красивое имя.",
        "Хорошо.",
        "Отлично.",
        "Замечательно"
    ]

    def __init__(self):
        self._prev_errors = []
        self._max_errors = 3
        self.question = choice(NameQuestion.question_text)

    @staticmethod
    def _get_rare_name_answer_response():
        return AnswerResponse(
            tag="rare_name",
            message="Ооо, меня тоже так зовут!",
            action="continue"
        )

    @staticmethod
    def _get_famous_name_answer_response():
        return AnswerResponse(
            tag="famous_name",
            message="Ага, а фамилия Бонопарт!",
            action="break"
        )

    @staticmethod
    def _get_usual_name_answer_response():
        return AnswerResponse(
            tag="usual_name",
            message=choice(NameQuestion.good_response_message),
            action="continue"
        )

    def check_answer(self, answer: str, context: dict) -> AnswerResponse:
        if self._is_answer_explicit(answer, context):
            return NameQuestion._get_explicit_response()

        if "Рафаэль" in answer:
            return NameQuestion._get_rare_name_answer_response()

        elif "Наполеон" in answer:
            return NameQuestion._get_famous_name_answer_response()

        else:
            return NameQuestion._get_usual_name_answer_response()

    # TODO: Find better func name
    def _all_errors_response(self):  # -> (str, Optional[Question]):
        if len(self._prev_errors) == 3:
            self.question = "Ты вообще нормально отвечать не будешь, да? Ладно, го дальше."
            return 0
        else:
            self.question = "Заебал, нормально отвечай, да? Как твоё имя?"
            return 1
