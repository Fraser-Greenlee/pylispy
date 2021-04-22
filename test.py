from pdb import set_trace
from operator import add, sub, gt
from pylispy import (
    c, d, IF
)

c(add, (sub, 3, 2), 1)

c(
    IF, (gt, (sub, 3, 2), 0)
        (print, 'yes')
    (print, 'no')
)

set_trace()
