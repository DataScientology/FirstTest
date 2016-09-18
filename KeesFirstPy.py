import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/Kees Mulder/Downloads/train.csv')
dims = df.shape
nrow = df.shape[0]
ncol = df.shape[1]

# get neighbours for a specific pixel index
def getNeighbours(pixNum, dims):
    
    # Dimensions and total size.
    dx = dims[0]
    dy = dims[1]
    nPixels = dx * dy
    
    # Empty set of neighbors
    neighbors = []
    
    # Check in order if we are not at the far left, far right, top or bottom.
    if pixNum % dx != 0: 
        neighbors.append(pixNum + 1)
    if pixNum % dx != 1: 
        neighbors.append(pixNum - 1)
    if pixNum > dx: 
        neighbors.append(pixNum - dx)
    if pixNum < (nPixels - dx): 
        neighbors.append(pixNum + dx)
    
    return neighbors

# Generate a data
def labelAreas 
    









