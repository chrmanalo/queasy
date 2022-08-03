from typing import TypeVar, Callable, Sequence
from functools import reduce

T = TypeVar('T')

def pipeline(
    value: T,
    function_pipeline: Sequence[Callable[[T], T]]
) -> T:
    '''A generic Unix-like pipeline copied from https://samroeca.com/python-function-pipelines.html

    :param value: the value you want to pass through a pipeline
    :param function_pipeline: an ordered list of functions that
        comprise your pipeline
    '''
    return reduce(lambda v, f: f(v), function_pipeline, value)
