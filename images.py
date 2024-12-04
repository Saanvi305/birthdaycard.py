import pygame
import time

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Happy Birthday!")

img=pygame.image.load("birthday1.jpg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))

while(True):
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running=False
    #font=pygame.font.#SysFont("Times New Roman" ,72)
    #text=font.render("Happy ",True,(0,0,0))
    screen.fill((0,0,0))
    screen.blit(image,(200,150))
pygame.display.flip()
pygame.quit()
sys.exit()




