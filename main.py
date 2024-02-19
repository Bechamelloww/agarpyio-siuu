import pygame
from pygame.mixer import Sound
import sys
import math
import time

from Agar import Agar
from Food import Food
from Trap import Trap

pygame.init()
pygame.mixer.init()
timer_start_time = None

screenWidth = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("AgarPyIo")
pygame.mixer.music.load("menuBackgroundMusic.mp3")
pygame.mixer.music.play(-1)  # pour lire en boucle
siu = Sound("siuuu.mp3")
camerawowo = Sound("camerawowo.mp3")

background_image = pygame.image.load("menuBackground.jpg")
background_image = pygame.transform.scale(background_image, (screenWidth, screenHeight))

bg_pitch = pygame.image.load("pitch.jpg")
bg_pitch = pygame.transform.scale(bg_pitch, (screenWidth, screenHeight))
font = pygame.font.Font(None, 36)

difficulty_text = font.render("Choisissez la difficulté :", False, pygame.color.Color("white"))
controls_text = font.render("Choisissez les contrôles :", False, pygame.color.Color("white"))
easy_button = font.render("Facile", False, pygame.color.Color("white"))
normal_button = font.render("Normal", False, pygame.color.Color("white"))
hard_button = font.render("Difficile", False, pygame.color.Color("white"))
keyboard_button = font.render("Clavier (ZQSD)", False, pygame.color.Color("white"))
mouse_button = font.render("Souris", False, pygame.color.Color("white"))
play_button = font.render("Jouer", False, pygame.color.Color("white"))

difficulty_text_rect = difficulty_text.get_rect(center=(screenWidth // 2, 200))
controls_text_rect = controls_text.get_rect(center=(screenWidth // 2, 400))
easy_button_rect = easy_button.get_rect(center=(screenWidth // 2, 250))
normal_button_rect = normal_button.get_rect(center=(screenWidth // 2, 290))
hard_button_rect = hard_button.get_rect(center=(screenWidth // 2, 330))
keyboard_button_rect = keyboard_button.get_rect(center=(screenWidth // 2, 450))
mouse_button_rect = mouse_button.get_rect(center=(screenWidth // 2, 490))
play_button_rect = play_button.get_rect(center=(screenWidth // 2, 550))

menu_active = True
game_active = False

difficulty = None
controls = None

agar = Agar(500, 500)
all_sprites = pygame.sprite.Group()
food_group = pygame.sprite.Group()
trap_group = pygame.sprite.Group()
all_sprites.add(agar)
moving_x = 0
moving_y = 0


def print_menu():
    screen.blit(background_image, (0, 0))
    screen.blit(difficulty_text, difficulty_text_rect)
    screen.blit(controls_text, controls_text_rect)
    screen.blit(easy_button, easy_button_rect)
    screen.blit(normal_button, normal_button_rect)
    screen.blit(hard_button, hard_button_rect)
    screen.blit(keyboard_button, keyboard_button_rect)
    screen.blit(mouse_button, mouse_button_rect)
    screen.blit(play_button, play_button_rect)


while menu_active:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            menu_active = False
            pygame.quit()
            sys.exit()
        if keys[pygame.K_q] and game_active == False:
            menu_active = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if easy_button_rect.collidepoint(event.pos):
                difficulty = "Facile"
            elif normal_button_rect.collidepoint(event.pos):
                difficulty = "Normal"
            elif hard_button_rect.collidepoint(event.pos):
                difficulty = "Difficile"
            elif keyboard_button_rect.collidepoint(event.pos):
                controls = "Clavier"
            elif mouse_button_rect.collidepoint(event.pos):
                controls = "Souris"
            elif play_button_rect.collidepoint(event.pos):
                if difficulty and controls:
                    agar = Agar(screenWidth // 2, screenHeight // 2)
                    all_sprites = pygame.sprite.Group()
                    all_sprites.add(agar)
                    pygame.mixer.music.load("gameMusic1.mp3")
                    pygame.mixer.music.play(-1)
                    if difficulty == "Facile":
                        nb_trap = 2
                        nb_food = 5
                    elif difficulty == "Normal":
                        nb_trap = 3
                        nb_food = 3
                    else:
                        nb_trap = 4
                        nb_food = 2
                    for _ in range(nb_food):
                        new_food = Food(screenWidth, screenHeight)
                        all_sprites.add(new_food)
                        food_group.add(new_food)
                    for _ in range(nb_trap):
                        new_trap = Trap(screenWidth, screenHeight)
                        all_sprites.add(new_trap)
                        trap_group.add(new_trap)
                    timer_start_time = time.time()
                    game_active = True

    if game_active:
        # print("Difficulté:", difficulty)
        # print("Contrôles:", controls)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        foodcollisions = pygame.sprite.spritecollide(agar, food_group, True)
        if foodcollisions:
            new_food = Food(screenWidth, screenHeight)
            agar.score += 1
            siu.play()
            all_sprites.add(new_food)
            food_group.add(new_food)
            agar.increase_speed()
            agar.increase_size()
        trapcollisions = pygame.sprite.spritecollide(agar, trap_group, False)
        if trapcollisions and agar.size > trapcollisions[0].size:
            if difficulty == "Facile":
                agar.collidetrap(1.5)
            elif difficulty == "Normal":
                agar.collidetrap(2)
            else:
                agar.collidetrap(3)
            trapcollisions[0].kill()
            camerawowo.play()
            new_trap = Trap(screenWidth, screenHeight)
            all_sprites.add(new_trap)
            trap_group.add(new_trap)
        if controls == "Clavier":
            if keys[pygame.K_q]:
                moving_x -= 0.02 * agar.speed
            if keys[pygame.K_d]:
                moving_x += 0.02 * agar.speed
            if keys[pygame.K_z]:
                moving_y -= 0.02 * agar.speed
            if keys[pygame.K_s]:
                moving_y += 0.02 * agar.speed
            # décommenter les lignes en dessous si vous voulez que quand on appuie sur la touche a pdt le jeu le ballon grandisse et tt
            #if keys[pygame.K_a]:
               # agar.increase_size()
               # agar.increase_speed()
            agar.rect.y = moving_y
            agar.rect.x = moving_x
            agar.rect.x = (agar.rect.x - agar.rect.width/2 + screenWidth) % screenWidth
            agar.rect.y = (agar.rect.y - agar.rect.height/2 + screenHeight) % screenHeight
        elif controls == "Souris":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction_x = mouse_x - agar.rect.x - agar.rect.width/2
            direction_y = mouse_y - agar.rect.y - agar.rect.height/2
            distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

            if distance >= 15:
                normalized_direction_x = direction_x / distance
                normalized_direction_y = direction_y / distance

                agar.rect.x += normalized_direction_x * agar.speed * 0.02
                agar.rect.y += normalized_direction_y * agar.speed * 0.02
                # pas besoin de gérer les sorties d'écran vu que la mousepos n'est pas prise en compte en dehors

        screen.blit(bg_pitch, (0, 0))
        all_sprites.draw(screen)
        score_text = font.render(f"Score: {agar.score}", True, pygame.color.Color("white"))
        score_rect = score_text.get_rect(topright=(screenWidth - 20, 10))
        screen.blit(score_text, score_rect)
        elapsed_time = time.time() - timer_start_time
        remaining_time = max(60 - int(elapsed_time), 0)  # Calcul du temps restant
        timer_text = font.render(f"Temps restant: {remaining_time}s", True, pygame.color.Color("white"))
        timer_rect = timer_text.get_rect(topleft=(500, 10))
        screen.blit(timer_text, timer_rect)
        pygame.display.flip()
        pygame.time.delay(10)

        if elapsed_time >= 60 or keys[pygame.K_ESCAPE]:
            pygame.mixer.music.load("menuBackgroundMusic.mp3")
            pygame.mixer.music.play(-1)
            difficulty = None
            controls = None
            keyboard_button = font.render("Clavier (ZQSD)", False, pygame.color.Color("white"))
            mouse_button = font.render("Souris", False, pygame.color.Color("white"))
            easy_button = font.render("Facile", True, pygame.color.Color("white"))
            normal_button = font.render("Normal", True, pygame.color.Color("white"))
            hard_button = font.render("Difficile", False, pygame.color.Color("white"))
            game_active = False

    else:
        print_menu()
        if difficulty == "Facile":
            easy_button = font.render("Facile", True, pygame.color.Color("red"))
            normal_button = font.render("Normal", True, pygame.color.Color("white"))
            hard_button = font.render("Difficile", False, pygame.color.Color("white"))
        elif difficulty == "Normal":
            easy_button = font.render("Facile", True, pygame.color.Color("white"))
            normal_button = font.render("Normal", True, pygame.color.Color("red"))
            hard_button = font.render("Difficile", False, pygame.color.Color("white"))
        elif difficulty == "Difficile":
            easy_button = font.render("Facile", True, pygame.color.Color("white"))
            normal_button = font.render("Normal", True, pygame.color.Color("white"))
            hard_button = font.render("Difficile", False, pygame.color.Color("red"))

        if controls == "Clavier":
            keyboard_button = font.render("Clavier (ZQSD)", False, pygame.color.Color("red"))
            mouse_button = font.render("Souris", False, pygame.color.Color("white"))
        elif controls == "Souris":
            keyboard_button = font.render("Clavier (ZQSD)", False, pygame.color.Color("white"))
            mouse_button = font.render("Souris", False, pygame.color.Color("red"))

    pygame.display.flip()
