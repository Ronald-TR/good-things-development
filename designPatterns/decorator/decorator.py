def hello_decorator(func):
    def argsfunc(*args, **kwargs):
        return func(*args, **kwargs) + ' ==> hello decorator!'
    return argsfunc
