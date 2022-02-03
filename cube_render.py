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

        rotvect1 = rotateVectX(rotateVectY(rotateVectZ(constants.cv1, angleZ), angleY), angleX)
        newvect1 = projectVect(rotvect1)
        yasvect1 = yassifyVect(newvect1, WIDTH) 

        rotvect2 = rotateVectX(rotateVectY(rotateVectZ(constants.cv2, angleZ), angleY), angleX)
        newvect2 = projectVect(rotvect2)
        yasvect2 = yassifyVect(newvect2, WIDTH)

        rotvect3 = rotateVectX(rotateVectY(rotateVectZ(constants.cv3, angleZ), angleY), angleX)
        newvect3 = projectVect(rotvect3)
        yasvect3 = yassifyVect(newvect3, WIDTH)

        rotvect4 = rotateVectX(rotateVectY(rotateVectZ(constants.cv4, angleZ), angleY), angleX)
        newvect4 = projectVect(rotvect4)
        yasvect4 = yassifyVect(newvect4, WIDTH)

        rotvect5 = rotateVectX(rotateVectY(rotateVectZ(constants.cv5, angleZ), angleY), angleX)
        newvect5 = projectVect(rotvect5)
        yasvect5 = yassifyVect(newvect5, WIDTH)

        rotvect6 = rotateVectX(rotateVectY(rotateVectZ(constants.cv6, angleZ), angleY), angleX)
        newvect6 = projectVect(rotvect6)
        yasvect6 = yassifyVect(newvect6, WIDTH)

        rotvect7 = rotateVectX(rotateVectY(rotateVectZ(constants.cv7, angleZ), angleY), angleX)
        newvect7 = projectVect(rotvect7)
        yasvect7 = yassifyVect(newvect7, WIDTH)

        rotvect8 = rotateVectX(rotateVectY(rotateVectZ(constants.cv8, angleZ), angleY), angleX)
        newvect8 = projectVect(rotvect8)
        yasvect8 = yassifyVect(newvect8, WIDTH)
        
        angleX += 0.001
        angleY += 0.001
        angleZ += 0.001

        pygame.draw.line(background, (0,0,0), (yasvect1[0,0], yasvect1[1,0]), (yasvect2[0,0], yasvect2[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect1[0,0], yasvect1[1,0]), (yasvect4[0,0], yasvect4[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect1[0,0], yasvect1[1,0]), (yasvect7[0,0], yasvect7[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect2[0,0], yasvect2[1,0]), (yasvect3[0,0], yasvect3[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect2[0,0], yasvect2[1,0]), (yasvect8[0,0], yasvect8[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect3[0,0], yasvect3[1,0]), (yasvect4[0,0], yasvect4[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect3[0,0], yasvect3[1,0]), (yasvect6[0,0], yasvect6[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect4[0,0], yasvect4[1,0]), (yasvect5[0,0], yasvect5[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect6[0,0], yasvect6[1,0]), (yasvect8[0,0], yasvect8[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect5[0,0], yasvect5[1,0]), (yasvect7[0,0], yasvect7[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect7[0,0], yasvect7[1,0]), (yasvect8[0,0], yasvect8[1,0]))
        pygame.draw.line(background, (0,0,0), (yasvect5[0,0], yasvect5[1,0]), (yasvect6[0,0], yasvect6[1,0]))
        
        
        #for vect in constants.vect_list_c1:
        #    rotvect = rotateVectX(rotateVectY(rotateVectZ(vect, angleZ), angleY), angleX)
        #    newvect = projectVect(rotvect)
        #    yasvect = yassifyVect(newvect, WIDTH) 
        #    drawVect(yasvect, background)
        #    angleX += 0.0005
        #    angleY += 0.0005
        #    angleZ += 0.0005

        #    pygame.draw.line(background, (0,0,0), (0,0), (yasvect[0,0], yasvect[1,0]))

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
    pygame.draw.circle(screen, (0, 0, 0), pos, 4)

def yassifyVect (vector, WIDTH): #PENDIENTE DE MEJORA EN LA SIGUIENTE VERSIÓN
    return matrix.sumMatrix(matrix.scalarMult(vector, 100), matrix.scalarMult(constants.ALLONES_R3VECT, WIDTH/2)) #El hecho de multiplicar por 100 es para ponerlo a escala



if __name__ == '__main__': main()
