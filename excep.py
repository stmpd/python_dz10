def check(operation, args):
    try:
        return operation(args)
    except Exception as exception:
        return exception
