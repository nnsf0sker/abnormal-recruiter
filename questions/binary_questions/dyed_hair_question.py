from typing import Dict
from typing import List


class DyedHairQuestion:
    question_text: List[str] = [
        "Красили ли Вы когда либо волосы?"
    ]
    possible_answers: Dict[str, str] = {
        "да": [
            "К сожалению, мы не сможем продолжить с Вами общение по вакансии, так как, согласно политике нашей "
            "компании, Вы "
        ],
        "нет": [
            "К сожалению, мы не сможем продолжить с Вами общение по вакансии, так как Ваш найм "
            "ведёт к нарушению земельного кодекса Российской Федерации.\n"
            "Дело в том, что наша секретарь Альфюша иногда приводит своего сына Барфангаздиза на работу, а он "
            "в свои семь уже ортодоксальный марксист. Так вот, недавно лидер его школьной коммунистической партии "
            "Перчелнорнаш (первый человек на орбите - наш) "
            "выяснил, что злые демократы с некрашенными волосами специально устроили их милому школьному предприятию "
            "по производству краски для волос из гуаши и акварели диверсию, отключив свет после окончания уроков. В "
            "ответ Барфангаздис со своим другом Сунь Вынем (это очень многонациональная школа) пообещали захватить "
            "школьную площадку для постройки там светлого будущего и собственной фабрики.\n",
            "Если он увидит Вас с некрашенными волосами в офисе, это эскалирует конфликт, чего наше миролюбивое ИП "
            "никак допустить не может.\n"
            "Таким образом, к сожалению, мы не может пригласить Вас на работу в наш дружный коллектив."
        ]
    }