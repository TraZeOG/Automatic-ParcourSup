import pygame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

pygame.init()
pygame.display.set_caption("AUtomatic ParcourSup")

CLOCK = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 860, 980
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT_LILITAONE_50 = pygame.font.Font("fonts/LilitaOne-Regular.ttf", 50)
FONT_LILITAONE_30 = pygame.font.Font("fonts/LilitaOne-Regular.ttf", 30)
FONT_LILITAONE_10 = pygame.font.Font("fonts/LilitaOne-Regular.ttf", 10)
CLR_WHITE = (255,255,255)
CLR_BLACK = (0,0,0)