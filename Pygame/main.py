import pygame as PG
import text as TX
import button as BT
import atrr as CN

#WINDOW MAIN DATA
WIN_WIDTH = 500
WIN_HIGHT = 600
WIN_TITLE = "GAME WINDOW"
FPS = 0

GAME_LOOP = True

FRAMES = PG.time.Clock()

#COLOR DATA
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)

#ITEM VALUE
USER = CN.Player("Idalia", 1, 100, 10, 10, 1, 100)
USER_EXP = CN.LevelUp(1, 0, 100)
COIN = CN.CoinSystem(0)
FARMERS = 0
WORKER = 0

COINS_PER_SECOND = 0

MENU_EVENT = False

#ENEMY'S
GOBLIN = CN.Player("Goblin", 3, 10, 0, 5, 0, 50)

###TIMER
TIMER_INTERVAL = 1000
NEXT_TIME_EVENT = PG.time.get_ticks() + TIMER_INTERVAL
CHARACTER_MOVEMENT_EVENT = 1000

##PYGAME INIT
PG.init()
##SCREEN STARTER
WINDOW = PG.display.set_mode((WIN_WIDTH, WIN_HIGHT))
PG.display.set_caption(WIN_TITLE)

###GAME MAIN OBJECTS
MENU_BUTTON = BT.Button(20, 20, 200, 20, "Menu")
ADD_COIN_BUTTON = BT.Button(20, 60, 200, 20, "Add coins")
BUY_BUTTON_FARMERS = BT.Button(20, 100, 200, 20, "Buy Farmer!")
BUY_BUTTON_WORKERS = BT.Button(20, 140, 200, 20, "Buy Worker!")

PLAYER = BT.Squere((WIN_WIDTH/2)-200, 250, 50, 50, GREEN)
ENEMY = BT.Squere((WIN_WIDTH)+10, 250, 50, 50, RED)

ALL_SPRITES = PG.sprite.Group()

FPS_TEXT = TX.Text(350, 580, "FPS: " + str(FPS), 25, WHITE)
MONEY = TX.Text(350, 20, str(COIN.coins), 25, WHITE)

##USER_MENU
NAME_TEXT = TX.Text(10, 500, "Name: " + str(USER.name), 25, WHITE)
LEVEL_TEXT = TX.Text(130, 500, "Level: " + str(USER_EXP.level),25, WHITE)
EXP_TEXT = TX.Text(210, 500, "Exp: " + str(USER_EXP.exp), 25, WHITE)
HEALTH_TEXT = TX.Text(10, 520, "Health: " + str(USER.health), 25, WHITE)
DEFENSE_TEXT = TX.Text(130, 520, "Defense: " + str(USER.defense), 25, WHITE)
ATTACK_TEXT = TX.Text(250, 520, "Attack: " + str(USER.attack), 25, WHITE)

####ADDING SPRITES
ALL_SPRITES.add(MENU_BUTTON)
ALL_SPRITES.add(ADD_COIN_BUTTON)
ALL_SPRITES.add(BUY_BUTTON_FARMERS)
ALL_SPRITES.add(BUY_BUTTON_WORKERS)
ALL_SPRITES.add(PLAYER)
ALL_SPRITES.add(ENEMY)


#####GAME MAIN LOOP
while GAME_LOOP:
    for event in PG.event.get():
        if event.type == PG.QUIT:
            GAME_LOOP = False
        elif event.type == PG.MOUSEBUTTONDOWN:
            if MENU_BUTTON.rect.collidepoint(event.pos):
                if MENU_EVENT == False:
                    MENU_EVENT = True
                else:
                    MENU_EVENT = False
            if ADD_COIN_BUTTON.rect.collidepoint(event.pos):
                COIN.coins += 1
            if BUY_BUTTON_FARMERS.rect.collidepoint(event.pos):
                if COIN.coins >= 10:
                    COIN.spend_coins(10)
                    FARMERS += 1
                    COINS_PER_SECOND += FARMERS
            if BUY_BUTTON_WORKERS.rect.collidepoint(event.pos):
                if COIN.coins >= 500:
                    COIN.spend_coins(500)
                    WORKER += 1
                    COINS_PER_SECOND += (WORKER * 10)
            
    
    FPS = FRAMES.get_fps()


    WINDOW.fill(BLACK)
    ALL_SPRITES.update()
    ALL_SPRITES.draw(WINDOW)

    MONEY.draw(WINDOW)
    FPS_TEXT.draw(WINDOW)
        
    NAME_TEXT.draw(WINDOW)
    LEVEL_TEXT.draw(WINDOW)
    EXP_TEXT.draw(WINDOW)
    HEALTH_TEXT.draw(WINDOW)
    DEFENSE_TEXT.draw(WINDOW)
    ATTACK_TEXT.draw(WINDOW)

    CURRENT_TIME = PG.time.get_ticks()
    if CURRENT_TIME >= NEXT_TIME_EVENT:
        COIN.earn_coins(COINS_PER_SECOND)
        NEXT_TIME_EVENT = CURRENT_TIME + TIMER_INTERVAL
        print("Current time " + str(CURRENT_TIME))
        print(USER_EXP.level)
        print(FPS)

    
    if CURRENT_TIME >= CHARACTER_MOVEMENT_EVENT:
        ENEMY.rect.x -= 10
        CHARACTER_MOVEMENT_EVENT += 100
    
    if PLAYER.isColliding(ENEMY.rect):
        ENEMY.rect.x += 50
        CHARACTER_MOVEMENT_EVENT += 1000
        GOBLIN.take_damage(USER.attack-GOBLIN.defense)
        if GOBLIN.health <= 0:
            GOBLIN.health = 10
            ENEMY.rect.x += 500
            USER_EXP.gain_exp(50)
        pass

    

    MONEY.set_text(" $ "+str(COIN.coins))
    LEVEL_TEXT.set_text("Level: " + str(USER_EXP.level))
    EXP_TEXT.set_text("EXP: " + str(USER_EXP.exp))
    FPS_TEXT.set_text("FPS: " + str(FPS))

    PG.display.update()
    FRAMES.tick(60)

PG.quit()