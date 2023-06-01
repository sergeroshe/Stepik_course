from random import choice

ANSWERS = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']
USER_NAME_PROMPT = 'Введи свое имя:\n'
EXCLAMATION_SIGN = '!'
USER_NAME_GREETING = 'Добро пожаловать, '
CONTINUE_GAME_PROMPT = 'Хочешь задать еще один вопрос?\nНажми ENTER,' \
                       ' если ДА\n"1", затем ENTER, если НЕТ\n'
ENTER_QUESTION_PROMPT = 'Введи свой вопрос:\n'
IGNORE_QUESTION_LIST = ['где', 'когда', 'почему', 'сколько', 'кто',
                        'с кем', 'кого', 'зачем', 'почему', 'чего',
                        'как', 'какой', 'каком', 'какую', 'какие', 'какого']
IMPOSSIBLE_QUESTION_ERROR = 'Я могу ответить только на вопрос, требующий ответа ДА или НЕТ'
NO_RESPONSE = '1'
FAREWELL_MESSAGE = 'Возвращайся если возникнут вопросы!'


def game_run():
    game_is_on = True
    while game_is_on:
        question = input(ENTER_QUESTION_PROMPT).lower()
        question_is_not_correct = True
        while question_is_not_correct:
            is_question_impossible = False
            for word in IGNORE_QUESTION_LIST:
                if word in question:
                    is_question_impossible = True
            if is_question_impossible:
                print(IMPOSSIBLE_QUESTION_ERROR)
            if not is_question_impossible:
                question_is_not_correct = False
            else:
                question = input(ENTER_QUESTION_PROMPT).lower()

        answer = choice(ANSWERS)
        print(answer)

        continue_game = input(CONTINUE_GAME_PROMPT)
        game_is_on = continue_game != NO_RESPONSE

    print(FAREWELL_MESSAGE)


def main():
    user_name = input(USER_NAME_PROMPT)
    print(f'{USER_NAME_GREETING}{user_name}{EXCLAMATION_SIGN}')
    game_run()


main()
