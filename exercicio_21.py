# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo de áudio MP3
pygame.mixer.music.load("musica.mp3")

# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda a música terminar
while pygame.mixer.music.get_busy():  # Verifica se o áudio ainda está tocando
    pygame.time.Clock().tick(10)  # Aguarda de forma eficiente para não sobrecarregar o processador
