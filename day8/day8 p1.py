import itertools
import math

junction_boxes = []
edges = []

input_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

lines = input_data.strip().split('\n')

for line in lines:
    pts = line.strip().split(',')
    x, y, z = map(int, pts)

junction_boxes.append((x, y, z))

loadednum = len(junction_boxes)

for i, j in itertools.combinations(range(loadednum), 2):

    (x1, y1, z1) = junction_boxes[i]
    (x2, y2, z2) = junction_boxes[j]

    dist = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

    edges.append((distance_squared, i, j))

edges.sort()

parent = list(range(loadednum))

sizeset = [1] * N


