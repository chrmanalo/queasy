import functools

SEPARATOR = 16*'####'

def trace(func):
<<<<<<< HEAD
    """Decorates a function to show its trace. Copied from https://www.markaicode.com/en/easy-trace-code-in-python/"""
=======
    """Decorates a function to show its trace."""
>>>>>>> 4c1e3581d25be8a7f05ad3b3b42db076f995c842

    @functools.wraps(func)
    def tracefunc_closure(*args, **kwargs):
        """Closure of trace()"""
        result = func(*args, **kwargs)
        print(SEPARATOR)
        print(f'Tracing {func.__name__}()...')
        print(f'args=\t{args}\n')
        print(f'kwargs=\t{kwargs}\n')
        print(f'result=\t{result}\n')
        print(SEPARATOR)
        return result

    return tracefunc_closure