import matrix
import constants
import pygame 
from pygame.locals import *
import numpy as np

def main():
    
    #Needed variables and constants
    WIDTH = 600
    HEIGHT = WIDTH
    angleX = 0
    angleY = 0
    angleZ = 0

    projected_points = np.array( #Array of lists
        [
        [n,n] for n in range(len(constants.vect_list_c1))
        ]
    )

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Render program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Blit everything to the screen
    screen.blit(background, (0, 0)) #Puts the object 'background' on screen at the coords (0,0)
    pygame.display.flip() #Updates surface area 

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))

        background.fill((0, 0, 0))
        
        for index in range(len(constants.vect_list_c1)):
            rotvect = rotateVectX(rotateVectY(rotateVectZ(constants.vect_list_c1[index], angleZ), angleY), angleX)
            newvect = projectVect(rotvect)
            yasvect = yassifyVect(newvect, WIDTH) 

            projected_points[index] = [yasvect[0,0], yasvect[1,0]]

            drawVect(yasvect, background)
            angleX += 0.0001
            angleY += 0.0001
            angleZ += 0.0001
        

        #IMPLEMENT AN ALGORITHM SO THIS CAN BE AUTOMATISED FOR *ANY* FIGURE
        connect_points(0, 1, projected_points, background)
        connect_points(1, 2, projected_points, background)
        connect_points(2, 3, projected_points, background)
        connect_points(3, 0, projected_points, background)

        connect_points(4, 5, projected_points, background)
        connect_points(5, 7, projected_points, background)
        connect_points(6, 7, projected_points, background)
        connect_points(6, 4, projected_points, background)

        connect_points(0, 6, projected_points, background)
        connect_points(1, 7, projected_points, background)
        connect_points(2, 5, projected_points, background)
        connect_points(3, 4, projected_points, background)
        

        pygame.display.flip()


def rotateVectX (vector, angle):
    return matrix.matrixmult(constants.get_rotR3_X(angle), vector)

def rotateVectY (vector, angle):
    return matrix.matrixmult(constants.get_rotR3_Y(angle), vector)

def rotateVectZ (vector, angle):
    return matrix.matrixmult(constants.get_rotR3_Z(angle), vector)

def projectVect (vector):
    projVect = matrix.matrixmult(constants.PROJECTION_MATRIXR3R2, vector)
    return projVect

def drawVect (vector, screen):
    pos = (vector[0,0], vector[1,0])
    pygame.draw.circle(screen, (255, 192, 203), pos, 4)

def yassifyVect (vector, WIDTH): #PENDIENTE DE MEJORA EN LA SIGUIENTE VERSIÓN
    return matrix.sumMatrix(matrix.scalarMult(vector, 100), matrix.scalarMult(constants.ALLONES_R3VECT, WIDTH/2)) #El hecho de multiplicar por 100 es para ponerlo a escala

#Connects the i-th vector with the j-th vector. Both belonging to the list 'proyected_points'
def connect_points (i, j, projected_points, screen):
    pygame.draw.line(screen, (255, 192, 203), (projected_points[i, 0], projected_points[i, 1]), (projected_points[j, 0], projected_points[j, 1]))


if __name__ == '__main__': main()
