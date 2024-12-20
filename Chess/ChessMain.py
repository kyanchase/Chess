
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

# Initialize a global dictionary of images. This will be called exactly once in the main
def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ'] 
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

