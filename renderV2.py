import matrix
import constants
import pygame 
import math
from pygame.locals import *
import numpy as np


def main():
    
    WIDTH = 600
    HEIGHT = WIDTH
    angleX = 0
    angleY = 0
    angleZ = 0

    i = 0

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

        background.fill((250, 250, 250))

        if i >= (len(constants.vect_list_c1)-1):
            i = 0

        for vect in constants.vect_list_c1:
            rotvect = rotateVectX(rotateVectY(rotateVectZ(vect, angleZ), angleY), angleX)
            newvect = projectVect(rotvect)
            yasvect = yassifyVect(newvect, WIDTH) 

            drawVect(yasvect, background)

            connect_points(vect, constants.vect_list_c1[i], WIDTH, background, angleX, angleY, angleZ)


            angleX += 0.0001
            angleY += 0.0001
            angleZ += 0.0001

        #    pygame.draw.line(background, (0,0,0), (300,300), (yasvect[0,0], yasvect[1,0]))

        i += 1

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

def drawVect (vector, screen): #VOID function
    pos = (vector[0,0], vector[1,0])
    pygame.draw.circle(screen, (0, 0, 0), pos, 4)

def yassifyVect (vector, WIDTH): #PENDIENTE DE MEJORA EN LA SIGUIENTE VERSIÓN
    return matrix.sumMatrix(matrix.scalarMult(vector, 100), matrix.scalarMult(constants.ALLONES_R3VECT, WIDTH/2)) #El hecho de multiplicar por 100 es para ponerlo a escala

def connect_points (vect1, vect2, WIDTH, screen, angleX, angleY, angleZ):

    if (vect1[0,0] == vect2[0,0]):
        rotvect1 = rotateVectX(rotateVectY(rotateVectZ(vect1, angleZ), angleY), angleX)
        newvect1 = projectVect(rotvect1)
        yasvect1 = yassifyVect(newvect1, WIDTH) 

        rotvect2 = rotateVectX(rotateVectY(rotateVectZ(vect2, angleZ), angleY), angleX)
        newvect2 = projectVect(rotvect2)
        yasvect2 = yassifyVect(newvect2, WIDTH)
        pygame.draw.line(screen, (0,0,0), (yasvect1[0,0], yasvect1[1,0]), (yasvect2[0,0], yasvect2[1,0]))

    if (vect1[1,0] == vect2[1,0]):
        rotvect1 = rotateVectX(rotateVectY(rotateVectZ(vect1, angleZ), angleY), angleX)
        newvect1 = projectVect(rotvect1)
        yasvect1 = yassifyVect(newvect1, WIDTH) 

        rotvect2 = rotateVectX(rotateVectY(rotateVectZ(vect2, angleZ), angleY), angleX)
        newvect2 = projectVect(rotvect2)
        yasvect2 = yassifyVect(newvect2, WIDTH)
        pygame.draw.line(screen, (0,0,0), (yasvect1[0,0], yasvect1[1,0]), (yasvect2[0,0], yasvect2[1,0]))    
    
    if (vect1[2,0] == vect2[2,0]):
        rotvect1 = rotateVectX(rotateVectY(rotateVectZ(vect1, angleZ), angleY), angleX)
        newvect1 = projectVect(rotvect1)
        yasvect1 = yassifyVect(newvect1, WIDTH) 

        rotvect2 = rotateVectX(rotateVectY(rotateVectZ(vect2, angleZ), angleY), angleX)
        newvect2 = projectVect(rotvect2)
        yasvect2 = yassifyVect(newvect2, WIDTH)
        pygame.draw.line(screen, (0,0,0), (yasvect1[0,0], yasvect1[1,0]), (yasvect2[0,0], yasvect2[1,0]))    



if __name__ == '__main__': main()
