from random import choice

ANSWERS = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']
GREETING = 'Привет Мир, я Магический Шар, и я знаю ответ на любой твой вопрос.'
USER_NAME_GREETING = 'Добро пожаловать, '
USER_NAME_PROMPT = 'Введите ваше имя:\n'
ENTER_QUESTION_PROMPT = 'Введите ваш вопрос:\n'
CONTINUE_GAME_PROMPT = 'Хотите задать еще один вопрос?\nНажмите "1", затем ENTER,' \
                       ' если ДА\nНажмите любую клавишу, затем ENTER, если НЕТ\n'
IGNORE_QUESTION_LIST = ['где', 'когда', 'почему', 'сколько', 'кто', 'с кем', 'кого', 'зачем', 'почему', 'чего']
YES_RESPONSE = '1'
IMPOSSIBLE_QUESTION_ERROR = 'Я могу ответить только на вопрос, требующий ответа ДА или НЕТ'
NO_CHAR_ERROR_MESSAGE = 'Ваш вопрос должен содержать хотя бы одну букву или цифру!'
NO_QUESTION_MARK_ERROR = 'Ваш вопрос должен содержать вопросительный знак!'
FAREWELL_MESSAGE = 'Возвращайся если возникнут вопросы!'
OBLIGATORY_SIGN = '?'
EXCLAMATION_SIGN = '!'


def main():
    print(GREETING)
    user_name = input(USER_NAME_PROMPT) + EXCLAMATION_SIGN
    print(USER_NAME_GREETING + user_name)
    game_is_on = True
    while game_is_on:
        question = input(ENTER_QUESTION_PROMPT).lower()
        question_is_not_correct = True
        while question_is_not_correct:
            no_letters_in_question = True
            no_question_mark = True
            impossible_question = False
            for c in question:
                if c.isalnum():
                    no_letters_in_question = False
                if c == OBLIGATORY_SIGN:
                    no_question_mark = False
            for word in IGNORE_QUESTION_LIST:
                if word in question:
                    impossible_question = True
            if impossible_question:
                print(IMPOSSIBLE_QUESTION_ERROR)
            elif no_letters_in_question:
                print(NO_CHAR_ERROR_MESSAGE)
            elif no_question_mark:
                print(NO_QUESTION_MARK_ERROR)
            if not no_letters_in_question and not no_question_mark and not impossible_question:
                question_is_not_correct = False
            else:
                question = input(ENTER_QUESTION_PROMPT).lower()

        answer = choice(ANSWERS)
        print(answer)

        continue_game = input(CONTINUE_GAME_PROMPT)
        if continue_game != YES_RESPONSE:
            game_is_on = False
    print(FAREWELL_MESSAGE)


main()
