from pygame import Vector3, Vector2
from matrix_utils import perform_screenshift
from math import radians
from Camera import Camera

VertexType = list[Vector3]
EdgeType = list[list[int]]
FaceType = list[list[int]]

class WorldObject:

    position: Vector3
    size: Vector3
    rotation: Vector3

    __vertices: VertexType
    __edges: EdgeType
    __faces: FaceType

    camera: Camera

    def __init__(self, vertices: VertexType, edges: EdgeType, faces: FaceType, camera: Camera) -> None:
        self.__vertices = vertices
        self.__edges = edges
        self.__faces = faces
        self.position = Vector3()
        self.size = Vector3(1, 1, 1)
        self.rotation = Vector3()
        self.camera = camera

    @property
    def vertices(self):
        l = [Vector2()] * len(self.__vertices)

        i = 0
        for v in self.__vertices:
            o = list(perform_screenshift(
                self.position, 
                Vector3(*[radians(v) for v in [self.rotation.x, self.rotation.y, self.rotation.z]]), 
                v.elementwise() * self.size + self.position
            ).flat) #type: ignore

            vT = self.camera.project_perspective(Vector3(o[0], o[1], o[2]))

            l[i] = vT
            i += 1

        return l
            

    
    @property
    def edges(self):
        return [[self.vertices[e[0]], self.vertices[e[1]]] for e in self.__edges]
    
    @property
    def faces(self):
        return [[self.vertices[f[0]], self.vertices[f[1]], self.vertices[f[2]]] for f in self.__faces]