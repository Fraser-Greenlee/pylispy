'''
    Impliments list based execution & manipulation.
'''
from types import (
    FunctionType as function,
)
from typing import Any


class ControlFlowClass:
    def __call__(self) -> Any:
        raise NotImplementedError()


class IF(ControlFlowClass):
    def __init__(self, *codes) -> None:
        self.codes = codes

    def __call__(self) -> Any:
        cond, t_case, f_case = self.codes
        if c(*cond):
            return c(*t_case)
        return c(*f_case)


def car(*codes):
    return codes[0]


def cdr(*codes):
    return codes[1:]


def _process_args(args):
    lowest_level_args = []
    for arg in args:
        if type(arg) is tuple:
            lowest_level_args.append(
                c(*arg)
            )
        else:
            lowest_level_args.append(arg)
    return lowest_level_args


def c(method, *args):
    '''
        Stand in for a cons code object.

        cLisp equivilant: ()

        Excpets an operator (+, eq) followed by arguments.
        Operations are ran recursively.
    '''
    if type(method) is function:
        args = _process_args(args)
        return method(*args)
    if type(method) is ControlFlowClass:
        return method(*args)()


class d():
    '''
        Stand in for a cons data object.

        cLisp equivilant: '()

        You can nest cons-code inside the data list.
    '''
    def __init__(self, *data_list) -> None:
        self.data_list = data_list
