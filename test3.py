import pygame

pygame.init()
a = pygame.display.set_mode((500,500))
a.fill((119, 85, 212))
pygame.display.set_caption("Second")

run = True

while run:
    pygame.display.update()
    w = pygame.event.wait()
    if w.type == pygame.QUIT:
        run = False
        pygame.quit()
    elif w.type == pygame.KEYDOWN:
        u = pygame.key.get_pressed() #альтернативный способ проверить нажатие клавиши
        if u[pygame.K_q]: # для key.get_pressed()
            a.fill((85, 176, 212))
        elif w.key == pygame.K_w: # для KEYDOWN
            a.fill((119, 85, 212))
        elif w.key == pygame.K_e:
            b = pygame.Surface((40, 60))
            b.fill((120,0,0,10))
            a.blit(b, (350,350))
        elif u[pygame.K_r]:
            pygame.draw.line(a, (0,150,0), (150, 150), (350, 150), 10)
        elif u[pygame.K_t]:
            pygame.draw.circle(a, (0,0,176), (320, 320), 70, 0)

        
        