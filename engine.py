import random


def create_map():
    
    MAP = []
    for i in range(100):
        MAP.append([0 for y in range(100)])
    with open("map.py", "w+") as o:
        o.write(str(MAP))
    return MAP