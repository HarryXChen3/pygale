from pygame import Vector3;
import numpy as np;
from math import cos, sin;

def perform_screenshift(object_position: Vector3, object_rotation: Vector3, vertex: Vector3):

    rx, ry, rz = object_rotation.x, object_rotation.y, object_rotation.z;

    vertex_matrix = np.matrix([
        [vertex.x],
        [vertex.y],
        [vertex.z],
        [1]
    ]);

    object_position_matrix = np.matrix([
        [1, 0, 0, object_position.x],
        [0, 1, 0, object_position.y],
        [0, 0, 1, object_position.z],
        [0, 0, 0, 1]
    ]);

    inverse_object_position_matrix = np.matrix([
        [1, 0, 0, -object_position.x],
        [0, 1, 0, -object_position.y],
        [0, 0, 1, -object_position.z],
        [0, 0, 0, 1]
    ]);

    x_rotation_matrix = np.matrix([
        [1, 0, 0, 0],
        [0, cos(rx), -sin(rx), 0],
        [0, sin(rx), cos(rz), 0],
        [0, 0, 0, 1]
    ]);

    y_rotation_matrix = np.matrix([
        [cos(ry), 0, sin(ry), 0],
        [0, 1, 0, 0],
        [-sin(ry), 0, cos(ry), 0],
        [0, 0, 0, 1]
    ]);

    z_rotation_matrix = np.matrix([
        [cos(rz), -sin(rz), 0, 0],
        [sin(rz), cos(rz), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    return object_position_matrix * x_rotation_matrix * y_rotation_matrix * z_rotation_matrix * (inverse_object_position_matrix * vertex_matrix);