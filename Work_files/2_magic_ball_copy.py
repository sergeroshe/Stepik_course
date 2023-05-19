from random import choice

GREETING = 'Привет Мир, я Магический Шар, и я знаю ответ на любой твой вопрос.'
USER_NAME_PROMPT = 'Введите ваше имя:\n'
ENTER_QUESTION_PROMPT = 'Введите ваш вопрос:\n'
FAREWELL_MESSAGE = 'Возвращайся если возникнут вопросы!'
CONTINUE_GAME_PROMPT = 'Хотите задать еще один вопрос?\nНажмите "1", затем ENTER,' \
                       ' если ДА\nНажмите любую клавишу, затем ENTER, если НЕТ\n'
IGNORE_QUESTION_LIST = ['где', 'когда', 'почему', 'сколько', 'кто', 'с кем', 'кого', 'зачем', 'почему', 'чего']
YES_RESPONSE = '1'
YES_OR_NO_ERROR_MESSAGE = 'Я могу ответить только на вопрос, требующий ответа ДА или НЕТ'
CHAR_ERROR_MESSAGE = 'Ваш вопрос должен содержать хотя бы одну букву или цифру!'
ANSWERS = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']


def main():
    print(GREETING)

    user_name = input(USER_NAME_PROMPT)
    game_is_on = True
    while game_is_on:
        question = input(ENTER_QUESTION_PROMPT).lower()
        answer = choice(ANSWERS)
        for c in question:
            if c.isalnum():
                for word in IGNORE_QUESTION_LIST:
                    if word in question:
                        answer = YES_OR_NO_ERROR_MESSAGE
                break
            else:
                answer = CHAR_ERROR_MESSAGE
                break
        print(answer)

        continue_game = input(CONTINUE_GAME_PROMPT)
        if continue_game != YES_RESPONSE:
            game_is_on = False
    print(FAREWELL_MESSAGE)


main()
