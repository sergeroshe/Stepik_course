from random import choice

ANSWERS = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']
USER_NAME_PROMPT = 'Введи свое имя:\n'
EXCLAMATION_SIGN = '!'
USER_NAME_GREETING = 'Добро пожаловать, '
CONTINUE_GAME_PROMPT = 'Хочешь задать еще один вопрос?\nНажми ЛЮБУЮ КЛАВИШУ, затем ENTER,' \
                       ' если ДА\n"1", затем ENTER, если НЕТ\n'
ENTER_QUESTION_PROMPT = 'Введи свой вопрос:\n'
NO_RESPONSE = '1'
FAREWELL_MESSAGE = 'Возвращайся если возникнут вопросы!'


def game_run():
    game_is_on = True
    while game_is_on:
        question = input(ENTER_QUESTION_PROMPT).lower()
        answer = choice(ANSWERS)
        print(answer)

        continue_game = input(CONTINUE_GAME_PROMPT)
        game_is_on = continue_game != NO_RESPONSE
        # if continue_game == NO_RESPONSE:
        #     game_is_on = False
    print(FAREWELL_MESSAGE)


def main():
    user_name = input(USER_NAME_PROMPT)
    print(f'{USER_NAME_GREETING}{user_name}{EXCLAMATION_SIGN}')
    game_run()


main()
