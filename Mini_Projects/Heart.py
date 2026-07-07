import pygame
import math

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Heart using Pygame")

red = (255, 0, 0)
pink = (255, 105, 180)
black = (0, 0, 0)

screen.fill(black)

points = []
for t in range(0, 360):
    angle = math.radians(t)
    x = 16 * math.sin(angle) ** 3
    y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
    points.append((300 + x * 15, 300 - y * 15))

pygame.draw.polygon(screen, pink, points)
pygame.draw.lines(screen, red, True, points, 3)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
