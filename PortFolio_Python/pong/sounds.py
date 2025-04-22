import pygame

pygame.mixer.init()

sonido_rebote = pygame.mixer.Sound(r"E:\pong\sounds\rebote.ogg")
sonido_punto = pygame.mixer.Sound(r"E:\pong\sounds\punto.ogg")
sonido_marcador = pygame.mixer.Sound(r"E:\pong\sounds\marcador.ogg")
sonido_pared = pygame.mixer.Sound(r"E:\pong\sounds\pared.ogg")
sonido_mover_paleta = pygame.mixer.Sound(r"E:\pong\sounds\mover_paleta.ogg")

def reproducir_sonido_rebote():
    sonido_rebote.play()

def reproducir_sonido_punto():
    sonido_punto.play()

def reproducir_sonido_marcador():
    sonido_marcador.play()

def reproducir_sonido_pared():
    sonido_pared.play()

def reproducir_sonido_mover_paleta():
    sonido_mover_paleta.play()