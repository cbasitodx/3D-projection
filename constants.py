import numpy as np
import math

#AUXILIAR MATRICES

PROJECTION_MATRIXR3R2 = np.array(
    [[1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]]
)

ALLONES_R3MATRIX = np.ones((3,3), dtype=object)

ALLONES_R3VECT = np.ones((3,1), dtype=object)

def get_rotR3_X(i):
    ROTATION_MATRIXR3_X = np.array(
        [[1, 0, 0],
        [0, math.cos(i), -math.sin(i)],
        [0, math.sin(i), math.cos(i)]]
    )
    return ROTATION_MATRIXR3_X

def get_rotR3_Y(i):
    ROTATION_MATRIXR3_Y = np.array(
        [[math.cos(i), 0, math.sin(i)],
        [0, 1, 0],
        [-math.sin(i), 0, math.cos(i)]]
    )
    return ROTATION_MATRIXR3_Y

def get_rotR3_Z(i):
    ROTATION_MATRIXR3_Z = np.array(
        [[math.cos(i), -math.sin(i), 0],
        [math.sin(i), math.cos(i), 0],
        [0, 0, 1]]
    )
    return ROTATION_MATRIXR3_Z

#CUBE VECTORS I
cv1 = np.array(
    [[-1],
    [-1],
    [1]]
, dtype=object)
cv2 = np.array(
    [[1],
    [-1],
    [1]]
, dtype=object)
cv3 = np.array(
    [[1],
    [1],
    [1]]
, dtype=object)
cv4 = np.array(
    [[-1],
    [1],
    [1]]
, dtype=object)
cv5 = np.array(
    [[-1],
    [1],
    [-1]]
, dtype=object)
cv6 = np.array(
    [[1],
    [1],
    [-1]]
, dtype=object)
cv7 = np.array(
    [[-1],
    [-1],
    [-1]]
, dtype=object)
cv8 = np.array(
    [[1],
    [-1],
    [-1]]
, dtype=object)

#Cube I list of vectors
vect_list_c1 = [cv1, cv2, cv3, cv4, cv5, cv6, cv7, cv8]

#CUBE VECTORS II
c2v1 = np.array(
    [[1],
    [0],
    [0]]
, dtype=object)
c2v2 = np.array(
    [[0],
    [1],
    [0]]
, dtype=object)
c2v3 = np.array(
    [[0],
    [0],
    [1]]
, dtype=object)
c2v4 = np.array(
    [[1],
    [1],
    [0]]
, dtype=object)
c2v5 = np.array(
    [[0],
    [1],
    [1]]
, dtype=object)
c2v6 = np.array(
    [[1],
    [0],
    [1]]
, dtype=object)
c2v7 = np.array(
    [[0],
    [0],
    [0]]
, dtype=object)
c2v8 = np.array(
    [[1],
    [1],
    [1]]
, dtype=object)

#Cube II list of vectors
vect_list_c2 = [c2v1, c2v2, c2v3, c2v4, c2v5, c2v6, c2v7, c2v8]

#PRISM VECTORS I
pv1 = np.array(
    [[1],
    [0],
    [1]]
, dtype=object)
pv2 = np.array(
    [[1],
    [0],
    [-1]]
, dtype=object)
pv3 = np.array(
    [[-1],
    [0],
    [-1]]
, dtype=object)
pv4 = np.array(
    [[0],
    [1],
    [0]]
, dtype=object)

#Prism I list of vectors
vect_list_p1 = [pv1, pv2, pv3, pv4]