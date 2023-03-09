import pygame
import random

pygame.init()

# definir as dimensões da janela
window_width = 1080
window_height = 720
window = pygame.display.set_mode((window_width, window_height))

# carregar a imagem da espaçonave e redimensioná-la
spaceship_image = pygame.image.load("spaceship.png")
spaceship_width = 75
spaceship_height = 75
spaceship_image = pygame.transform.scale(spaceship_image, (spaceship_width, spaceship_height))
# virar a imagem da espaçonave para cima
spaceship_image = pygame.transform.rotate(spaceship_image, 270)

# carregar a imagem do meteoro e redimensioná-la
meteor_image = pygame.image.load("meteor.png")
meteor_width = 50
meteor_height = 50
meteor_image = pygame.transform.scale(meteor_image, (meteor_width, meteor_height))

# definir a posição inicial da espaçonave
spaceship_x = window_width // 2 - spaceship_width // 2
spaceship_y = window_height - spaceship_height

# definir a posição inicial dos meteoros
meteor_x = random.randint(0, window_width - meteor_width)
meteor_y = -meteor_height

# definir a velocidade dos meteoros e da espaçonave
meteor_speed = 1.0
spaceship_speed = 0.5

# definir a fonte do texto
font = pygame.font.SysFont(None, 48)

# definir o loop principal do jogo
running = True
while running:
    # lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # mover a espaçonave
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT]:
        spaceship_x += spaceship_speed
    if keys[pygame.K_UP]:
        spaceship_y -= spaceship_speed
    if keys[pygame.K_DOWN]:
        spaceship_y += spaceship_speed
    
    # mover o meteoro
    meteor_y += meteor_speed
    
    # verificar se a espaçonave colidiu com o meteoro
    if spaceship_x < meteor_x + meteor_width and \
       spaceship_x + spaceship_width > meteor_x and \
       spaceship_y < meteor_y + meteor_height and \
       spaceship_y + spaceship_height > meteor_y:
        text = font.render("Game Over!", True, (255, 0, 0))
        window.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000) # esperar 2 segundos antes de encerrar o jogo
        running = False
    
    # desenhar os objetos na tela
    window.fill((0, 0, 0))
    window.blit(spaceship_image, (spaceship_x, spaceship_y))
    window.blit(meteor_image, (meteor_x, meteor_y))
    pygame.display.update()
    
    # reiniciar a posição do meteoro se ele sair da tela
    if meteor_y > window_height:
        meteor_x = random.randint(0, window_width - meteor_width)
        meteor_y = -meteor_height
        
# encerrar o Pygame
pygame.quit()
