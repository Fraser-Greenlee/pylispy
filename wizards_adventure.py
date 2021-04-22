from pdb import set_trace
from operator import add, sub, gt, eq
from pylispy import (
    c, d, IF
)


def s(txt: str):
    return txt.split()


old_map = map


def map(*args):
    return list(old_map(*args))


def append(*args):
    return sum(args, [])


NODES = {
    'living-room': s('you are in the living-room. '
                     'a wizard is snoring loudly on the couch.'),
    'garden': s('you are in a beautiful garden. '
                'there is a well in front of you.'),
    'attic': s('you are in the attic. '
               'there is a giant welding torch in the corner.')
}

EDGES = {
    'living-room': (
        s('garden west door'),
        s('attic upstairs ladder'),
    ),
    'garden': s('living-room east door'),
    'attic': s('living-room downstairs ladder')
}

OBJECTS = s('whiskey bucket frog chain')

OBJECT_LOCATIONS = {
    'whiskey': 'living-room',
    'bucket': 'living-room',
    'chain': 'garden',
    'frog': 'garden'
}



(defun describe-objects (loc objs obj-loc) (labels ((describe-obj (obj)
`(you see a ,obj on the floor.)))
(apply #'append (mapcar #'describe-obj (objects-at loc objs obj-loc)))))


def objects_at(loc: str, objs: list, obj_locs: dict):
    return filter(
        lambda obj: obj_locs[obj] == loc,
        objs
    )


def describe_objects(loc: str, objs: list, obj_locs: dict):
    def describe_obj(obj: list):
        s('you see a') + [obj] + s('on the floor.')
    return sum(map(describe_obj,
                        map(objects_at, loc, objs, obj_locs)
            ), [])


def describe_location(location: str, nodes: dict):
    return nodes[location]


def describe_path(edge: list):
    return s('there is a') + [edge[2]] + s('going') + [edge[1]] + s('from here.')


def describe_paths(location: str, edges: dict):
    return sum(map(describe_path, edges[location]), [])


def alt_describe_paths(location: str, edges: dict):
    return c(sum, (map, describe_path, edges[location]), [])


print(1)
