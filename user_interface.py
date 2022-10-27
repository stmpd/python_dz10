from telegram import Update
from telegram.ext import CallbackContext


def tele_print(update: Update, context: CallbackContext, output):
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)


def show_greetings():
    welcome = "Добро пожаловать в PyCalcoBot!"
    return welcome


def king_menu():
    return "1 - Деление\n2 - Целочисленное деление\n3 - Остаток от деления\n4 - Умножение\n5 - Возведение в степень\n6 - Квадратный корень\n7 - Вычетание\n8 - Сложение\n0 - выход\nВыберите нужную операцию: "


def enter_real_argument():
    return "Введите вещественный аргумент: "


def enter_complex_argument():
    return "Введите комлексный аргумент, <вещественная часть> и <комплексная часть> разделены пробелом: "


def show_result(result):
    result_show = f"Результат: {result}"
    return result_show


def ask_for_complexity():
    return "Использовать ли комплексные аргументы? [Да] или [Нет]"


def show_error(error):
    error_show = f"Произошла ошибка: {error}"
    return error_show


def show_goodbye():
    bye = "Работа программы завершена!"
    return bye