import pygame
import random
from my_game import player_info
from os import path
from pathlib import Path


img_dir = Path('my_game', 'img')
snd_dir = Path('my_game', 'snd')

# Параметры экрана
WIDTH = 1280
HEIGHT = 720
FPS = 60

# Параметры игры
POWERUP_TIME = 5000
NOTES = player_info.NOTES
score = 0
MOBS = 15
LEVEL = player_info.LEVEL
POWER_UP_CHANCE = 0.1
NOTE_CHANCE = 0.01

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


font_name = pygame.font.match_font('Comic Sans MS')


def show_menu_screen():
    screen.blit(background_img, background_rect)
    draw_text(screen, "SHCHEK!", 64, WIDTH / 2, HEIGHT / 4, WHITE)
    draw_text(screen, "WASD to move, LMB to fire", 22,
              WIDTH / 2, HEIGHT / 2, WHITE)
    draw_text(screen, "Esc to quit the game or to pause while playing", 22, WIDTH / 2,
              HEIGHT * 2 / 3, WHITE)
    draw_text(screen, "Press SPACE key to begin", 18, WIDTH / 2,
              HEIGHT * 3 / 4, WHITE)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()


def show_pause_screen():
    screen.fill(BLACK)
    screen.blit(background_img, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 28, int(WIDTH / 2), 10, WHITE)
    draw_healthbar(screen, 5, 5, player.health)
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    draw_notes(screen, 2, int(HEIGHT / 2), NOTES, info_mini_image)
    draw_questions(screen, -17, int(HEIGHT / 2) - 45, NOTES, question_image)
    draw_text(screen, "|| PAUSE", 64, WIDTH / 2, HEIGHT / 4, WHITE)
    draw_text(screen, "TO CONTINUE PRESS ESC", 22,
              WIDTH / 2, HEIGHT / 2, WHITE)
    draw_text(screen, "M TO GO TO THE MAIN MENU", 22,
              WIDTH / 2, HEIGHT / 2 + 30, WHITE)
    pygame.display.flip()
    game_paused = True
    while game_paused:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    game_paused = False
                    show_menu_screen()


def show_info(surf, info_num, x, y, img):

    img_rect = img.get_rect()
    img_rect.center = (x, y)
    
    if info_num == 0:
        
        screen.fill(BLACK)
        screen.blit(background_img, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 28, int(WIDTH / 2), 10, WHITE)
        draw_healthbar(screen, 5, 5, player.health)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        draw_notes(screen, 2, int(HEIGHT / 2), NOTES, info_mini_image)
        draw_questions(screen, -17, int(HEIGHT / 2) - 45, NOTES, question_image)
        surf.blit(img, img_rect)

        # Отрисовать тест записки №1
        draw_text(screen, "1/5",
                  20, WIDTH / 2 + 250, HEIGHT / 8 - 25, BLACK)
        for string in player_info.info_card_1:
            draw_text(screen, string[1], string[0], WIDTH / 2, HEIGHT / 4 + string[2], BLACK)

        pygame.display.flip()
        showing = True
        while showing:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        showing = False
                    
    if info_num == 1:
        
        screen.fill(BLACK)
        screen.blit(background_img, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 28, int(WIDTH / 2), 10, WHITE)
        draw_healthbar(screen, 5, 5, player.health)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        draw_notes(screen, 2, int(HEIGHT / 2), NOTES, info_mini_image)
        draw_questions(screen, -17, int(HEIGHT / 2) - 45, NOTES, question_image)
        surf.blit(img, img_rect)
        draw_text(screen, "2/5",
                  20, WIDTH / 2 + 250, HEIGHT / 8 - 25, BLACK)
        draw_text(screen, "Подмена понятий".upper(),
                  16, WIDTH / 2, HEIGHT / 4 + 20, BLACK)
        draw_text(screen, "Интеллект — способность воспринимать информацию и сохранять её в качестве знания",
                  12, WIDTH / 2, HEIGHT / 4 + 72, BLACK)
        draw_text(screen, "для построения адаптивного поведения в среде или контексте",
                  12, WIDTH / 2, HEIGHT / 4 + 86, BLACK)
        draw_text(screen, "Это определение интеллекта из Википедии может быть применено как к органическому",
                  12, WIDTH / 2, HEIGHT / 4 + 100, BLACK)
        draw_text(screen, "мозгу, так и к машине. Наличие интеллекта не предполагает наличие сознания. Это —",
                  12, WIDTH / 2, HEIGHT / 4 + 114, BLACK)
        draw_text(screen, "распространённое заблуждение, принесённое в мир писателями научной фантастики,",
                  12, WIDTH / 2, HEIGHT / 4 + 128, BLACK)
        draw_text(screen, "и именно оно стало источником большинства теорий порабощения мира машинами.",
                  12, WIDTH / 2, HEIGHT / 4 + 142, BLACK)
        draw_text(screen, "На самом деле, если мы хотим, чтобы ИИ-система была субъектом/личностью и у нее могли возникать",
                  12, WIDTH / 2, HEIGHT / 4 + 156, BLACK)
        draw_text(screen, "мотивации вида «ради развития» или «во имя всеобщего блага» или любой другой не заложенной",
                  12, WIDTH / 2, HEIGHT / 4 + 170, BLACK)
        draw_text(screen, "конструктивно мотивации, она должна обладать, во-первых, первичными мотивациями и, во-",
                  12, WIDTH / 2, HEIGHT / 4 + 184, BLACK)
        draw_text(screen, "вторых, встроенным языком и построенном на базе него графом из ценностей и убеждений.",
                  12, WIDTH / 2, HEIGHT / 4 + 198, BLACK)
        draw_text(screen, "Чтобы создать ИИ с интеллектом эквивалентным человеческому на базе нейронной сети",
                  12, WIDTH / 2, HEIGHT / 4 + 212, BLACK)
        draw_text(screen, "потребуется порядка 8 миллиардов нейронов, и машины все равно будут проигрывать нам",
                  12, WIDTH / 2, HEIGHT / 4 + 226, BLACK)
        draw_text(screen, "в сложности и многофакторности просто в силу того, что нейрон в нервной системе человека сам по",
                  12, WIDTH / 2, HEIGHT / 4 + 240, BLACK)
        draw_text(screen, "себе очень сложный молекулярный механизм, зависящий от огромного числа параметров,",
                  12, WIDTH / 2, HEIGHT / 4 + 254, BLACK)
        draw_text(screen, "в отличие от нейрона современных нейронных сетей, имеющего простую структуру.",
                  12, WIDTH / 2, HEIGHT / 4 + 268, BLACK)
        draw_text(screen, "Нажмите Enter, чтобы закрыть записку".upper(),
                  20, WIDTH / 2, HEIGHT / 4 + 400, BLACK)
        pygame.display.flip()
        showing = True
        while showing:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        showing = False
                    
    if info_num == 2:
        
        screen.fill(BLACK)
        screen.blit(background_img, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 28, int(WIDTH / 2), 10, WHITE)
        draw_healthbar(screen, 5, 5, player.health)
        draw_lives(screen, WIDTH - 100, 5, player.lives,
	           player_mini_img)
        draw_notes(screen, 2, int(HEIGHT / 2), NOTES,
	           info_mini_image)
        draw_questions(screen, -17, int(HEIGHT / 2) - 45, NOTES,
	               question_image)
        surf.blit(img, img_rect)
        draw_text(screen, "3/5",
                  20, WIDTH / 2 + 250, HEIGHT / 8 - 25, BLACK)
        draw_text(screen, "ИИ - это просто программа".upper(),
                  16, WIDTH / 2, HEIGHT / 4 + 20, BLACK)
        draw_text(screen, "Теперь давйте вспомним, что ИИ - это просто программа, такая же, как и эта игра.",
                  12, WIDTH / 2, HEIGHT / 4 + 72, BLACK)
        draw_text(screen, "Просто набор команд, алгоритм, создающих иллюзию обучения. Чтобы вы лучше",
                  12, WIDTH / 2, HEIGHT / 4 + 86, BLACK)
        draw_text(screen, "понимали, что собой представляет ИНС, посмотрите на следующий кусок кода:",
                  12, WIDTH / 2, HEIGHT / 4 + 100, BLACK)
        draw_text(screen, "import numpy as np",
                  12, WIDTH / 2, HEIGHT / 4 + 114, BLACK)
        draw_text(screen, "def sigmoid(x):",
                  12, WIDTH / 2, HEIGHT / 4 + 128, BLACK)
        draw_text(screen, "return 1 / (1 + np.exp(-x))",
                  12, WIDTH / 2, HEIGHT / 4 + 142, BLACK)
        draw_text(screen, "class Neuron:",
                  12, WIDTH / 2, HEIGHT / 4 + 156, BLACK)
        draw_text(screen, "def __init__(self, weights, bias):",
                  12, WIDTH / 2, HEIGHT / 4 + 170, BLACK)
        draw_text(screen, "self.weights = weights",
                  12, WIDTH / 2, HEIGHT / 4 + 184, BLACK)
        draw_text(screen, "self.bias = bias",
                  12, WIDTH / 2, HEIGHT / 4 + 198, BLACK)
        draw_text(screen, "def feedforward(self, inputs):",
                  12, WIDTH / 2, HEIGHT / 4 + 212, BLACK)
        draw_text(screen, "total = np.dot(self.weights, inputs) + self.bias",
                  12, WIDTH / 2, HEIGHT / 4 + 226, BLACK)
        draw_text(screen, "return sigmoid(total)",
                  12, WIDTH / 2, HEIGHT / 4 + 240, BLACK)
        draw_text(screen, "weights = np.array([0, 1])",
                  12, WIDTH / 2, HEIGHT / 4 + 254, BLACK)
        draw_text(screen, "bias = 4  # b = 4",
                  12, WIDTH / 2, HEIGHT / 4 + 268, BLACK)
        draw_text(screen, "n = Neuron(weights, bias)",
                  12, WIDTH / 2, HEIGHT / 4 + 282, BLACK)
        draw_text(screen, "И вот, дамы и господа, мы создали нейрон! Теперь, если кто-то и боялся",
                  12, WIDTH / 2, HEIGHT / 4 + 296, BLACK)
        draw_text(screen, "восстания машин, то сейчас он точно этого уже не делает.",
                  12, WIDTH / 2, HEIGHT / 4 + 310, BLACK)
        draw_text(screen, "Обучение же ИИ полностью основано на математических функциях",
                  12, WIDTH / 2, HEIGHT / 4 + 324, BLACK)
        draw_text(screen, "(довольно сложных и объемных для описания здесь и сейчас)",
                  12, WIDTH / 2, HEIGHT / 4 + 338, BLACK)
        draw_text(screen, "Так, любая нейросеть все еще остается алгоритмом, хоть и довольно сложным",
                  12, WIDTH / 2, HEIGHT / 4 + 352, BLACK)
        draw_text(screen, "Нажмите Enter, чтобы закрыть записку".upper(),
                  20, WIDTH / 2, HEIGHT / 4 + 400, BLACK)
        pygame.display.flip()
        showing = True
        while showing:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        showing = False
                    
    if info_num == 3:
        
        screen.fill(BLACK)
        screen.blit(background_img, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 28, int(WIDTH / 2), 10, WHITE)
        draw_healthbar(screen, 5, 5, player.health)
        draw_lives(screen, WIDTH - 100, 5, player.lives,
   	           player_mini_img)
        draw_notes(screen, 2, int(HEIGHT / 2), NOTES,
	           info_mini_image)
        draw_questions(screen, -17, int(HEIGHT / 2) - 45, NOTES,
	               question_image)
        surf.blit(img, img_rect)
        draw_text(screen, "4/5",
                  20, WIDTH / 2 + 250, HEIGHT / 8 - 25, BLACK)
        draw_text(screen, "ИИ выполняет только определенную человеком задачу",
                  16, WIDTH / 2, HEIGHT / 4 + 20, BLACK)
        draw_text(screen, "Да, ИИ обыграли нас в шахматы, в го, научились распознавать людей по фотографии",
                  12, WIDTH / 2, HEIGHT / 4 + 72, BLACK)
        draw_text(screen, "и даже прошли тест Тьюринга, но это все были разные машины, у каждой ис которых",
                  12, WIDTH / 2, HEIGHT / 4 + 86, BLACK)
        draw_text(screen, "была одна задача. Если машина умеет обыгрывать кого угодно в шахматы, это еще",
                  12, WIDTH / 2, HEIGHT / 4 + 100, BLACK)
        draw_text(screen, "не значит, что она сможет пройти, к примеру, тест Тьюринга и т.д.",
                  12, WIDTH / 2, HEIGHT / 4 + 114, BLACK)
        draw_text(screen, "Чаще всего ИИ исполняет одну конкретную задачу, которую скажет ему человек",
                  12, WIDTH / 2, HEIGHT / 4 + 128, BLACK)
        draw_text(screen, "Так, сколько бы вы не сомневались в том, что ИИ не выйдет из под контроля,",
                  12, WIDTH / 2, HEIGHT / 4 + 142, BLACK)
        draw_text(screen, "они все равно остаются программами, исполняющими то, что им скажут",
                  12, WIDTH / 2, HEIGHT / 4 + 156, BLACK)
        draw_text(screen, "ИИ захватит мир, только если человек скажет ему. А это уже звучит как ревльная проблема",
                  12, WIDTH / 2, HEIGHT / 4 + 170, BLACK)
        draw_text(screen, "Но пока не нашлось гениев-безумцев, желающих захватить мир с помощью ИИ,",
                  12, WIDTH / 2, HEIGHT / 4 + 184, BLACK)
        draw_text(screen, "мы можем жить спокойно",
                  12, WIDTH / 2, HEIGHT / 4 + 198, BLACK)
        draw_text(screen, "Нажмите Enter, чтобы закрыть записку".upper(),
                  20, WIDTH / 2, HEIGHT / 4 + 212, BLACK)
        pygame.display.flip()
        showing = True
        while showing:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        showing = False
                    
    if info_num == 4:
        screen.fill(BLACK)
        screen.blit(background_img, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 28, int(WIDTH / 2), 10, WHITE)
        draw_healthbar(screen, 5, 5, player.health)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        draw_notes(screen, 2, int(HEIGHT / 2), NOTES, info_mini_image)
        draw_questions(screen, -17, int(HEIGHT / 2) - 45, NOTES, question_image)
        surf.blit(img, img_rect)
        # TODO: rename draw_text to draw_string
        # TODO: make draw_text function to draw multiline texts
        draw_text(screen, "5/5",
                  20, WIDTH / 2 + 250, HEIGHT / 8 - 25, BLACK)
        draw_text(screen, "Поздравляю, это последняя записка! Прочти ее, и игра будет окончена".upper(),
                  14, WIDTH / 2, HEIGHT / 4 + 20, BLACK)
        draw_text(screen, "Прочитав все предыдущие записки, вы наверное осознали, что ИИ",
                  12, WIDTH / 2, HEIGHT / 4 + 72, BLACK)
        draw_text(screen, "не представляет никакой угрозы для человека. Давайте же теперь наконец",
                  12, WIDTH / 2, HEIGHT / 4 + 86, BLACK)
        draw_text(screen, "поговорим и о пользе искусственного интелекта.",
                  12, WIDTH / 2, HEIGHT / 4 + 100, BLACK)
        draw_text(screen, "Во-первых, как бы это ни было очевидно, они облегчают жизнь человека во",
                  12, WIDTH / 2, HEIGHT / 4 + 114, BLACK)
        draw_text(screen, "многих сферах, таких как медицина (ИИ для принятия решений медицинской диагностики),",
                  12, WIDTH / 2, HEIGHT / 4 + 128, BLACK)
        draw_text(screen, "тяжелая промышленность (применение роботов в работе, которая считается опасной для людей),",
                  12, WIDTH / 2, HEIGHT / 4 + 142, BLACK)
        draw_text(screen, "финансы (алгоритмическая торговля, исследования рынка и интеллектуальный анализ данных),",
                  12, WIDTH / 2, HEIGHT / 4 + 156, BLACK)
        draw_text(screen, "транспорт (автономные самоуправляемые автомобили) т.д.",
                  12, WIDTH / 2, HEIGHT / 4 + 170, BLACK)
        draw_text(screen, "Во-вторых, ИИ используется в развлекательной сфере. А именно, в играх.",
                  12, WIDTH / 2, HEIGHT / 4 + 184, BLACK)
        draw_text(screen, "Согласитесь, намного приятнее играть против умного противника, одновременно",
                  12, WIDTH / 2, HEIGHT / 4 + 198, BLACK)
        draw_text(screen, "развивая при этом интеллект и моторику, ведь, как мы знаем, сложные",
                  12, WIDTH / 2, HEIGHT / 4 + 212, BLACK)
        draw_text(screen, "игры стимулируют мышление лучше, чем легкие",
                  12, WIDTH / 2, HEIGHT / 4 + 226, BLACK)
        draw_text(screen, "Надеюсь тебе понравилось, и ты больше не переживаешь о восстании машин".upper(),
                  13, WIDTH / 2, HEIGHT / 4 + 440, BLACK)
        draw_text(screen, "Нажмите Enter, чтобы закрыть записку".upper(),
                  20, WIDTH / 2, HEIGHT / 4 + 400, BLACK)
        pygame.display.flip()
        showing = True
        while showing:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        showing = False

            
def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (int(x), int(y))
    surface.blit(text_surface, text_rect)


def draw_lives(surf, x, y, lives, img):
    draw_text(screen, "{}/3".format(lives), 20, WIDTH - 35, 5, WHITE)
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x - 45 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def draw_notes(surf, x, y, NOTES, img):
    draw_text(screen, "{}/5".format(NOTES), 24, 25, HEIGHT / 2 - 30, WHITE)
    for i in range(NOTES):
        img_rect = img.get_rect()
        img_rect.y = y + 35 * i
        img_rect.x = x
        surf.blit(img, img_rect)


def draw_questions(surf, x, y, NOTES, img):
    for i in range(5 - NOTES):
        img_rect = img.get_rect()
        img_rect.y = y + 35 * (5 - i)
        img_rect.x = x
        surf.blit(img, img_rect)


def draw_healthbar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 180
    BAR_HEIGHT = 20
    fill = int((pct / 100) * BAR_LENGTH)
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 38
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 4
        self.health = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 4

        keystate = pygame.key.get_pressed()

        mousestate = pygame.mouse.get_pressed()

        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if keystate[pygame.K_w]:
            self.speedy = -8
        if keystate[pygame.K_s]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

        if mousestate[0]:
            self.shoot()

        # показать, если скрыто
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1:
            self.hidden = False
            self.rect.centerx = int(WIDTH / 2)
            self.rect.bottom = HEIGHT - 10

        # тайм-аут для бонусов
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        # временно скрыть игрока
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (int(WIDTH / 2), HEIGHT + 200)

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8 + LEVEL)
        self.speedx = random.randrange(-3 - LEVEL // 2, 3 + LEVEL // 2)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        self.rotate()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -15

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # убить, если он сдвинется с нижней части экрана
        if self.rect.top > HEIGHT:
            self.kill()


class Info(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = info_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # убить, если он сдвинется с нижней части экрана
        if self.rect.top > HEIGHT:
            self.kill()


# Загрузка всей игровой графики
background_img = pygame.image.load(path.join(img_dir, 'purple.png')).convert()
background_img = pygame.transform.scale(background_img, (1920, 1080))
background_rect = background_img.get_rect()
player_img = pygame.image.load(path.join(img_dir, 'playerShip1_blue.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (40, 35))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, 'laserGreen02.png')).convert()
meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png','meteorGrey_med1.png', 'meteorGrey_big1.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

powerup_images = {}
shield_image = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
gun_image = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()
info_image = pygame.image.load(path.join(img_dir, 'scroll_2.png')).convert()
info_image = pygame.transform.scale(info_image, (50, 50))
info_mini_image = pygame.transform.scale(info_image, (35, 35))
info_mini_image.set_colorkey(BLACK)
info_bg_image = pygame.image.load(path.join(img_dir, 'info_bg.png')).convert()
info_bg_image = pygame.transform.scale(info_bg_image, (750, 850))
info_bg_image.set_colorkey(WHITE)
question_image = pygame.image.load(path.join(img_dir, 'question.jpg')).convert()
question_image = pygame.transform.scale(question_image, (70, 70))
question_image.set_colorkey(WHITE)
powerup_images['shield'] = shield_image
powerup_images['gun'] = gun_image

# И звуков ;)
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
bonus_sound = pygame.mixer.Sound(path.join(snd_dir, 'bonus.mp3'))
power_up_sound = bonus_sound = pygame.mixer.Sound(path.join(snd_dir, 'power_up.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.mp3'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
info = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(MOBS + LEVEL):
    newmob()


pygame.mixer.music.play(loops=-1)

# Цикл игры
running = True
game_over = True
paused = False
pygame.mouse.set_visible(False)

while running:
    if game_over:
        show_menu_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        info = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(MOBS):
            newmob()
        score = 0

        
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_pause_screen()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                show_menu_screen()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and NOTES >= 1:
                show_info(screen, 0, WIDTH // 2, HEIGHT // 2 - 25,
                          info_bg_image)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2 and NOTES >= 2:
                show_info(screen, 1, WIDTH // 2, HEIGHT // 2 - 25,
                          info_bg_image)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3 and NOTES >= 3:
                show_info(screen, 2, WIDTH // 2, HEIGHT // 2 - 25,
                          info_bg_image)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4 and NOTES >= 4:
                show_info(screen, 3, WIDTH // 2, HEIGHT // 2 - 25,
                          info_bg_image)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_5 and NOTES == 5:
                show_info(screen, 4, WIDTH // 2, HEIGHT // 2 - 25,
                          info_bg_image)
                
    # Обновление
    all_sprites.update()

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.health -= hit.radius + 15
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.health <= 0:
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.health = 100

    # Если игрок умер, игра окончена
    if player.lives <= 0 and not death_explosion.alive():
        game_over = True

    # Проверка, не задела ли пуля моба
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 70 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > (1 - NOTE_CHANCE) and NOTES < 5:
            info_new = Info(hit.rect.center)
            all_sprites.add(info_new)
            info.add(info_new)
        elif random.random() > (1 - POWER_UP_CHANCE):
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()
         

    # Проверка столкновений игрока и улучшения
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            power_up_sound.play()
            player.health += 50
            if player.health >= 100:
                player.health = 100
        if hit.type == 'gun':  
            power_up_sound.play()
            player.powerup()

    # Проверка столкновений игрока и информационной карточки
    hits = pygame.sprite.spritecollide(player, info, True)
    for hit in hits:
        bonus_sound.play()
        if NOTES < 5:
            pygame.mixer.music.stop()
            show_info(screen, NOTES, WIDTH // 2, HEIGHT // 2 - 25, info_bg_image)
            pygame.mixer.music.play(loops=-1)
            NOTES += 1
            LEVEL += 1        
            POWER_UP_CHANCE -= 0.01
            NOTE_CHANCE -= 0.001
            f = open(r'C:\Users\CТАС\Desktop\MyGame\player_info.py', 'w')
            f.write('NOTES = {}\n'.format(int(NOTES)))
            f.write('LEVEL = {}\n'.format(int(LEVEL)))
            f.write('POWER_UP_CHANCE = {}\n'.format(int(POWER_UP_CHANCE)))
            f.write('NOTE_CHANCE = {}\n'.format(int(NOTE_CHANCE)))
            f.close()
        newmob()
            
    
    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background_img, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 28, int(WIDTH / 2), 10, WHITE)
    draw_healthbar(screen, 5, 5, player.health)
    draw_lives(screen, WIDTH - 100, 5, player.lives,
	       player_mini_img)
    draw_notes(screen, 2, int(HEIGHT / 2), NOTES,
	       info_mini_image)
    draw_questions(screen, -17, int(HEIGHT / 2) - 45, NOTES,
	           question_image)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
