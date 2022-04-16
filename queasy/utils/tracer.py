import functools

SEPARATOR = 16*'####'

def trace(func):
    """Decorates a function to show its trace. Copied from https://www.markaicode.com/en/easy-trace-code-in-python/"""

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