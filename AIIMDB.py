from math import *
from random import *
import pygame

class Neuron():
    def __init__(s,tempVal,bias):
        s.tempVal = tempVal
        s.bias = bias

def createNewNeuron(tempVal,bias):
    return Neuron(tempVal,bias)


class AI():
    def __init__(s, layers):
        s.layers = [[createNewNeuron(0,random()*10) for i in range(l)] for l in layers]
        s.weitedConnections = [[random()for _ in range(layers[idL1]) for __ in range(layers[idL1+1 ])] for idL1 in range(len(layers)-1)]

    def simulate(s, inputs):
        for i in range(len(inputs)):
            s.layers[0][i].tempVal = inputs[i]
        
        for layer in range(1,len(s.layers)):
            for i in range(len(s.layers[layer])):
                neuron = s.layers[layer][i]
                val = 0
                for lastNeuron in s.layers[layer-1]:
                    val += lastNeuron.tempVal*s.weitedConnections[layer-1][i] + neuron.bias
                neuron.tempVal = val
                print(val)
        return s.layers[-1]
test =AI([1,2,3])

def renderAI(ai):
    for idLayer in range(len(ai.layers)):
        for idNeuron in range(len(ai.layers[idLayer])):
            pygame.draw.circle(screen, (0,255,0), (idLayer*50,50), 1)




(width, height) = (500, 400)
background_colour = (0,0,0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()


renderAI(test)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
