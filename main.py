from dialog import Dialog
from questions.binary_questions.tatoo_question import TattooQuestion
from questions.name_question import NameQuestion
from questions.serious_questions.religion_question import ReligionQuestion

if __name__ == "__main__":
    current_dialog = Dialog(questions=[
        ReligionQuestion(),
        NameQuestion(),
        TattooQuestion(),
        TattooQuestion(),
        TattooQuestion(),
        TattooQuestion()

    ])

    current_dialog.context["sex"] = "male"

    current_question_text = current_dialog.ask_question()

    while current_question_text:
        print(current_question_text)
        answer = input()
        response_message = current_dialog.push_answer(answer)
        current_question_text = current_dialog.ask_question()
        print(response_message)
