from typing import List
from typing import Optional

from models.question import Question


class Dialog:
    def __init__(self, questions: List[Question]):
        self.context = {}
        self.questions = questions
        if not self.questions:
            self.is_finished = True
        else:
            self._current_question: Question = questions[0]
            self.is_finished = False

    def get_next_response(self):
        return self._current_question.ask_question()

    def iter_next_question(self):
        try:
            del self.questions[0]
            self._current_question = self.questions[0]
        except IndexError:
            self._current_question = None
            self.is_finished = True

    def push_answer(self, answer) -> str:
        if self.is_finished:
            raise Exception("Dialog has been already finished")

        answer_response = self._current_question.check_answer(answer, self.context)

        if answer_response.action == "continue":
            self.iter_next_question()

        elif answer_response.action == "break":
            self._current_question = None

        elif answer_response.action == "repeat":
            pass

        else:
            raise Exception(f"Unknown answer_response.action: {answer_response.action}")

        return answer_response.message

    def ask_question(self) -> Optional[str]:
        if self._current_question:
            return self._current_question.ask_question()
        else:
            return None
