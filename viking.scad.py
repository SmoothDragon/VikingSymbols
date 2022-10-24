#!/usr/bin/env python3

import json
import solid
import numpy as np

d = 1.7
knot = {
  "description":"Trefoil Valknut.",
  "info": "Coordinates are Eisenstein integers.",
  "path": [
    [0, 0, 0],
    [1, 1, 0],
    [1+d, 1+d, -.1],
    [2+d, 2+d, 0],
    [2+d, 1, 0],
    [1+d, 1, 0],
    [1, 1, -.1],
    [0, 1, 0],
    [1+d, 2+d, 0],
    [1+d, 1, -.1],
    [1+d, 0, 0],
    [0, 0, 0],

    # [2, 0, 0],
    # [3, 0, 0],
    # [2, 1, 0],
    # [1, 2, 0],
  ] 
}

def eisenstein(x,y):
    a = x-y/2
    b = y*np.sqrt(3)/2
    return a,b

r = .35


# knot = json.load(open('conwayKnot.json'))
# print(knot)
# print(dir(solid))
ball = solid.sphere(r, segments=6)
ball = solid.rotate([0, 0, 30])(ball)

points = [[*eisenstein(*point[:2]), point[2]] for point in knot['path']]
# print(points)
balls = [solid.translate(p)(ball) for p in points]
bars = [solid.hull()(a,b) for a,b in zip(balls, balls[1:])]
result = solid.union()(*bars)
result = solid.scale(10)(result)

print(solid.scad_render(result))
