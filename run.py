import pygame
import datetime

from clock import Time

pygame.init()
pygame.font.init()

bg = pygame.image.load("C:/Users/Nick/Desktop/clock/glitter.jpg")

font = pygame.font.SysFont('comicsansms', 30)
        


while True:
#main loop
    
    text_hours = str(Time.get_hours())
    text_mins = str(Time.get_mins())
    text_secs = str(Time.get_secs())


    screen = pygame.display.set_mode((600,600))
    screen.blit(bg,(0,0))

        # HOURS
    pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(0, 0, 200, (int(Time.get_hours())*25)))
    hours_text = font.render(text_hours, True, (255, 153, 255))
        # mins
    pygame.draw.rect(screen, (204, 0, 204), pygame.Rect(200, 0, 200, (int(Time.get_mins())*10)))
    mins_text = font.render(text_mins, True, (255, 153, 255))
        # secs
    pygame.draw.rect(screen, (102, 0, 102), pygame.Rect(400, 0, 200, (int(Time.get_secs())*10)))
    secs_text = font.render(text_secs, True, (255, 153, 255))

        #draw all the times at half the bar
    screen.blit(hours_text,(80,int(Time.get_hours())*12.5))
    screen.blit(mins_text,(280,int(Time.get_mins())*5))
    screen.blit(secs_text,(480,int(Time.get_secs())*5))

    pygame.display.flip()
