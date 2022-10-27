from enum import Enum
import model_mult
import model_div
import model_sqrt
import model_pow
import model_sub
import model_sum
import compl
from info import token
import user_interface as ui
import excep
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

MENU, COMPLEXITY, REAL_ARGUMENT, COMPLEX_ARGUMENT = range(4)


class OperationType(Enum):
    EXIT = 0
    DIVIDE = 1
    DIVIDE_INTEGER = 2
    REMINDER = 3
    MULTIPLY = 4
    POWER = 5
    SQRT = 6
    SUBTRACTION = 7
    SUM = 8


args = []
current_operation: OperationType = OperationType.EXIT


def parse_menu_input(arg):
    return OperationType(int(arg))


def parse_float(arg):
    return float(arg)


def check_yes_or_no(arg):
    if arg.lower() == "да" or arg.lower() == "нет":
        return arg.lower()
    else:
        return Exception(f"{arg}")


def execute_operation(args2):
    match args2[0]:
        case OperationType.DIVIDE:
            model_div.init(args2[1], args2[2])
            return model_div.division()
        case OperationType.DIVIDE_INTEGER:
            model_div.init(args2[1], args2[2])
            return model_div.integer_division()
        case OperationType.REMINDER:
            model_div.init(args2[1], args2[2])
            return model_div.remainder_division()
        case OperationType.MULTIPLY:
            model_mult.init(args2[1], args2[2])
            return model_mult.multiply()
        case OperationType.POWER:
            model_pow.init(args2[1], args2[2])
            return model_pow.my_pow()
        case OperationType.SQRT:
            model_sqrt.init(args2[1])
            return model_sqrt.my_sqrt()
        case OperationType.SUBTRACTION:
            model_sub.init(args2[1], args2[2])
            return model_sub.sub()
        case OperationType.SUM:
            model_sum.init(args2[1], args2[2])
            return model_sum.my_sum()


def start(update: Update, context: CallbackContext) -> int:
    ui.tele_print(update=update, context=context, output=ui.show_greetings())
    ui.tele_print(update=update, context=context, output=ui.king_menu())
    return 0


def on_next(update: Update, context: CallbackContext) -> int:
    operation_type = excep.check(OperationType, update.message.text)
    match operation_type:
        case OperationType.EXIT:
            ui.tele_print(update=update, context=context, output=ui.show_goodbye())
            return ConversationHandler.END
        case OperationType.DIVIDE:
            pass
        case OperationType.MULTIPLY:
            pass
        case OperationType.POWER:
            pass
        case OperationType.SUBTRACTION:
            pass
        case OperationType.SUM:
            pass
        case OperationType.DIVIDE_INTEGER:
            pass
        case OperationType.REMINDER:
            pass
        case OperationType.SQRT:
            pass
        case _:
            ui.tele_print(update=update, context=context, output=ui.show_error(operation_type))
    return 0


def parse_complex_arg(str_arg):
    args1 = str_arg.split(" ")
    return compl.get_compl(float(args1[0]), float(args1[1]))


def start_calc(update: Update, context: CallbackContext) -> int:
    ui.tele_print(update=update, context=context, output=ui.show_greetings())
    ui.tele_print(update=update, context=context, output=ui.king_menu())
    return MENU


def handle_menu(update: Update, context: CallbackContext) -> int:
    global args
    args = []
    global current_operation
    current_operation = excep.check(parse_menu_input, update.message.text)
    if current_operation == OperationType.EXIT:
        ui.tele_print(update=update, context=context, output=ui.show_goodbye())
        return ConversationHandler.END
    elif isinstance(current_operation, OperationType):
        ui.tele_print(update=update, context=context, output=ui.ask_for_complexity())
        return COMPLEXITY
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(current_operation))
    return MENU
   

def handle_complexity(update: Update, context: CallbackContext) -> int:
    use_complexity = excep.check(check_yes_or_no, update.message.text)
    if use_complexity == "да":
        ui.tele_print(update=update, context=context, output=ui.enter_complex_argument())
        return COMPLEX_ARGUMENT
    elif use_complexity == "нет":
        ui.tele_print(update=update, context=context, output=ui.enter_real_argument())
        return REAL_ARGUMENT
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(f"{use_complexity} - Да/Нет"))
        return COMPLEXITY


def handle_real_argument(update: Update, context: CallbackContext) -> int:
    arg = excep.check(parse_float, update.message.text)
    if isinstance(arg, float):
        args.append(arg)
        if current_operation == OperationType.SQRT:
            operation_args = []
            operation_args.append(current_operation)
            operation_args.extend(args)
            result = excep.check(execute_operation, operation_args)
            if isinstance(result, Exception):
                ui.tele_print(update=update, context=context, output=ui.show_error(result))
            else:
                ui.tele_print(update=update, context=context, output=ui.show_result(result))
                ui.tele_print(update=update, context=context, output=ui.king_menu())
                return MENU
        else:
            if len(args) < 2:
                ui.tele_print(update=update, context=context, output=ui.enter_real_argument())
                return REAL_ARGUMENT
            else:
                operation_args = []
                operation_args.append(current_operation)
                operation_args.extend(args)
                result = excep.check(execute_operation, operation_args)
                if isinstance(result, Exception):
                    ui.tele_print(update=update, context=context, output=ui.show_error(result))
                else:
                    ui.tele_print(update=update, context=context, output=ui.show_result(result))
                    ui.tele_print(update=update, context=context, output=ui.king_menu())
                    return MENU
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(f"{arg} - не число"))
        return REAL_ARGUMENT

def handle_complex_argument(update: Update, context: CallbackContext) -> int:
    arg = excep.check(parse_complex_arg, update.message.text)
    if isinstance(arg, complex):
        args.append(arg)
        if current_operation == OperationType.SQRT:
            operation_args = []
            operation_args.append(current_operation)
            operation_args.extend(args)
            result = excep.check(execute_operation, operation_args)
            if isinstance(result, Exception):
                ui.tele_print(update=update, context=context, output=ui.show_error(result))
            else:
                ui.tele_print(update=update, context=context, output=ui.show_result(result))
                ui.tele_print(update=update, context=context, output=ui.king_menu())
                return MENU
        else:
            if len(args) < 2:
                ui.tele_print(update=update, context=context, output=ui.enter_complex_argument())
                return COMPLEX_ARGUMENT
            else:
                operation_args = []
                operation_args.append(current_operation)
                operation_args.extend(args)
                result = excep.check(execute_operation, operation_args)
                if isinstance(result, Exception):
                    ui.tele_print(update=update, context=context, output=ui.show_error(result))
                else:
                    ui.tele_print(update=update, context=context, output=ui.show_result(result))
                    ui.tele_print(update=update, context=context, output=ui.king_menu())
                    return MENU
    else:
        ui.tele_print(update=update, context=context, output=ui.show_error(f"{arg} - не число"))
        return COMPLEX_ARGUMENT
def cancel(update: Update, context: CallbackContext) -> int:
    ui.tele_print(update=update, context=context, output=ui.show_goodbye())
    return ConversationHandler.END
def main():
    updater = Updater(token)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(Filters.all, handle_menu)],
            COMPLEXITY: [MessageHandler(Filters.all, handle_complexity)],
            REAL_ARGUMENT: [MessageHandler(Filters.all, handle_real_argument)],
            COMPLEX_ARGUMENT: [MessageHandler(Filters.all, handle_complex_argument)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
     )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

    
if __name__ == '__main__':
    main()