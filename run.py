import pygame
import datetime

from clock import Time

pygame.init()

bg = pygame.image.load("C:/Users/Nick/Desktop/clock/glitter.jpg")

        
while True:
#main loop
    
    screen = pygame.display.set_mode((600,600))
    screen.blit(bg,(0,0))
        # HOURS
    pygame.draw.rect(screen, (150, 0, 20, ), pygame.Rect(0, 0, 200, (int(Time.get_hours())*25)))
        # mins
    pygame.draw.rect(screen, (20, 150, 0, 155), pygame.Rect(200, 0, 200, (int(Time.get_mins())*10)))
        # secs
    pygame.draw.rect(screen, (0, 20, 150, 155), pygame.Rect(400, 0, 200, (int(Time.get_secs())*10)))
    pygame.display.flip()
