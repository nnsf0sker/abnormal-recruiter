from dataclasses import dataclass


@dataclass()
class AnswerResponse:
    tag: str
    message: str
    action: str
