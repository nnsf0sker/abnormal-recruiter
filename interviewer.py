from typing import Dict
from typing import List

from dialog import Dialog
from questions.binary_questions.tatoo_question import TattooQuestion
from questions.name_question import NameQuestion
from questions.serious_questions.national_question import NationalQuestion


class Interviewer:
    def __init__(self):
        self.users: Dict[str, Dialog] = {}

    def start_interview(self, user_id: str) -> List[str]:
        current_dialog = Dialog(questions=[
            NameQuestion(),
            # TattooQuestion(),
            # TattooQuestion(),
            # TattooQuestion(),
            TattooQuestion(),
            NationalQuestion()
        ])
        self.users[user_id] = current_dialog
        text_to_reply = current_dialog.ask_question()
        return [text_to_reply]

    def process_answer(self, user_id: str, answer: str) -> List[str]:
        current_dialog = self.users[user_id]
        response_message = current_dialog.push_answer(answer)
        current_question_text = current_dialog.ask_question()
        return [response_message, current_question_text]

    def finish_interview(self, user_id: str) -> List[str]:
        del self.users[user_id]
        return []
