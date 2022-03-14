import random
import numpy as np
import noise

scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
shape = (100,100)


def empty_map(size):
    created = []
    for i in range(size):
        created.append([0 for y in range(size)])
    return created



MAP = empty_map(100)


def add_color(world):
    color_world = empty_map(100)
    for i in range(100):
        for j in range(100):
            if world[i][j] < -0.05:
                color_world[i][j] = 0
            elif world[i][j] < 0:
                color_world[i][j] = 1
    print(color_world)
    return color_world


def create_map():
    
    for i in range(100):
        for j in range(100):
            MAP[i][j] = noise.pnoise2(i/scale, 
                                        j/scale, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        repeatx=100, 
                                        repeaty=100, 
                                        base=0)                       
    return add_color(MAP)



