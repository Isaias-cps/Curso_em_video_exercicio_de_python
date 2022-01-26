"""Crie um programa que abra e reproduza um arquivo em MP3."""

import pygame 
pygame.init()
pygame.mixer.music.load('13.mp3')
pygame.mixer.music.play()
pygame.event.wait()