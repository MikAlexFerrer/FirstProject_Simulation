import numpy as np

block = np.array([[0,  0,  0,0],
                  [0,255,255,0],
                  [0,255,255,0],
                  [0,  0,  0,0]])

beehive = np.array([[0,  0,  0,  0,  0,0],
                    [0,  0,255,255,  0,0],
                    [0,255,  0,  0,255,0],
                    [0,  0,255,255,  0,0],
                    [0,  0,  0,  0,  0,0]])

loaf = np.array([[0,  0,  0,  0,  0,0],
                 [0,  0,255,255,  0,0],
                 [0,255,  0,  0,255,0],
                 [0,  0,255,  0,255,0],
                 [0,  0,  0,255,  0,0],
                 [0,  0,  0,  0,  0,0]])

boat = np.array([[0,  0,  0,  0,0],
                 [0,255,255,  0,0],
                 [0,255,  0,255,0],
                 [0,  0,255,  0,0],
                 [0,  0,  0,  0,0]])

tub = np.array([[0,  0,  0,  0,0],
                [0,  0,255,  0,0],
                [0,255,  0,255,0],
                [0,  0,255,  0,0],
                [0,  0,  0,  0,0]])

blinker01 = np.array([[0,  0,0],
                      [0,255,0],
                      [0,255,0],
                      [0,255,0],
                      [0,  0,0]])

blinker02 = np.array([[0,  0,  0,  0,0],
                      [0,255,255,255,0],
                      [0,  0,  0,  0,0]])

toad01 = np.array([[0,  0,  0,  0,  0,0],
                   [0,  0,  0,255,  0,0],
                   [0,255,  0,  0,255,0],
                   [0,255,  0,  0,255,0],
                   [0,  0,255,  0,  0,0],
                   [0,  0,  0,  0,  0,0]])

toad02 = np.array([[0,  0,  0,  0,  0,0],
                   [0,  0,255,255,255,0],
                   [0,255,255,255,  0,0],
                   [0,  0,  0,  0,  0,0]])

beacon01 = np.array([  [0,  0,  0,  0,  0,0],
                       [0,255,255,  0,  0,0],
                       [0,255,255,  0,  0,0],
                       [0,  0,  0,255,255,0],
                       [0,  0,  0,255,255,0],
                       [0,  0,  0,  0,  0,0]])

beacon02 = np.array([  [0,  0,  0,  0,  0,0],
                       [0,255,255,  0,  0,0],
                       [0,255,  0,  0,  0,0],
                       [0,  0,  0,  0,255,0],
                       [0,  0,  0,255,255,0],
                       [0,  0,  0,  0,  0,0]])

glider01 = np.array([  [0,  0,  0,  0,0],
                       [0,  0,255,  0,0],
                       [0,  0,  0,255,0],
                       [0,255,255,255,0],
                       [0,  0,  0,  0,0]])

glider02 = np.array([  [0,  0,  0,  0,0],
                       [0,255,  0,255,0],
                       [0,  0,255,255,0],
                       [0,  0,255,  0,0],
                       [0,  0,  0,  0,0]])

glider03 = np.array([  [0,  0,  0,  0,0],
                       [0,  0,  0,255,0],
                       [0,255,  0,255,0],
                       [0,  0,255,255,0],
                       [0,  0,  0,  0,0]])

glider04 = np.array([  [0,  0,  0,  0,0],
                       [0,255,  0,  0,0],
                       [0,  0,255,255,0],
                       [0,255,255,  0,0],
                       [0,  0,  0,  0,0]])

lightweightship01 = np.array([ [0,  0,  0,  0,  0,  0,0],
                               [0,255,  0,  0,255,  0,0],
                               [0,  0,  0,  0,  0,255,0],
                               [0,255,  0,  0,  0,255,0],
                               [0,  0,255,255,255,255,0],
                               [0,  0,  0,  0,  0,  0,0]])

lightweightship02 = np.array([ [0,  0,  0,  0,  0,  0,0],
                               [0,  0,  0,255,255,  0,0],
                               [0,255,255,  0,255,255,0],
                               [0,255,255,255,255,  0,0],
                               [0,  0,255,255,  0,  0,0],
                               [0,  0,  0,  0,  0,  0,0]])

lightweightship03 = np.array([ [0,  0,  0,  0,  0,  0,0],
                               [0,  0,255,255,255,255,0],
                               [0,255,  0,  0,  0,255,0],
                               [0,  0,  0,  0,  0,255,0],
                               [0,255,  0,  0,255,  0,0],
                               [0,  0,  0,  0,  0,  0,0]])

lightweightship04 = np.array([ [0,  0,  0,  0,  0,  0,0],
                               [0,  0,255,255,  0,  0,0],
                               [0,255,255,255,255,  0,0],
                               [0,255,255,  0,255,255,0],
                               [0,  0,  0,255,255,  0,0],
                               [0,  0,  0,  0,  0,  0,0]])


#Size X _ Y _ Array _ Name _ Rotations  
var_sizes = [
    [4, 4, block, 1], 
    [5, 6, beehive, 2],
    [6, 6, loaf, 4], 
    [5, 5, boat, 4], 
    [5, 5, tub, 1], 
    [5, 5, blinker01,0],  
    [5, 5, blinker02, 0],
    [6, 6, toad01, 4], 
    [6, 6, toad02, 4], 
    [6, 6, beacon01, 1], 
    [6, 6, beacon02, 1], 
    [5, 5, glider01, 4], 
    [5, 5, glider02, 4], 
    [5, 5, glider03, 4], 
    [5, 5, glider04, 4], 
    [6, 7, lightweightship01, 4], 
    [6, 7, lightweightship02, 4], 
    [6, 7, lightweightship03, 4], 
    [6, 7, lightweightship04, 4], 
]