import pgzrun
from random import randint


WIDTH = 1000
HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
REMOVE = 5
player = Actor('man')
player.x = WIDTH / 2
player.y = HEIGHT - 200

apples = []
score = 0

player1 = Actor('basket')
player1.x = WIDTH / 2
player1.y = HEIGHT - 331
apple = Actor('apple')
miss = 0


game_over = False
print("WELCOME TO APPLE CATCHER")
print()
print(" HOW TO PLAY")
print()
print("Use the arrow keys to move left and right to catch the apple")
print("There are 3 levels in the game. ")
print()
print("If you miss the apple 5 times then the game will over. Choose the level to continue :")
print("Choose the level ")
print("1")
print("2")
print("3")
user_input = int(input())
background = Actor('background')





def draw():

    screen.blit('tree', (0, 0))
    player.draw()
    player1.draw()
    if game_over:
        screen.clear()

        screen.blit('background', (0, 0))

    screen.draw.text("Score: " + str(score), (850, 90), fontsize=28, color=BLACK)
    screen.draw.text("Miss:   " + str(miss), (850, 125), fontsize=28, color=BLACK)



    for apple in apples:
        apple.draw()
    if game_over:
        screen.draw.text("YOU LOST 5 APPLES ! ", (500, 150), fontsize=35, color=BLACK)




def update():
    if not game_over:

        move_player()
        move_player1()
        move_apple()
        check_apple_collision()
        check_player_collission()
        sounds.bgmusic.play()



def move_player():
    if keyboard.left:
        player.x -= 6
    if keyboard.right:
        player.x += 6
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH


def move_player1():
    if keyboard.left:
        player1.x -= 6
    if keyboard.right:
        player1.x += 6
    if player1.left < 0:
        player1.left = 0
    if player1.right > WIDTH:
        player1.right = WIDTH


def create_new_apple():
    apple = Actor('apple')
    apple.x = randint(100, WIDTH - 100)
    apple.y = 10
    apples.append(apple)


def move_apple():
    for apple in apples:
        if apple.top > HEIGHT:
            apples.remove(apple)
            create_new_apple()
        if user_input == 1:
            apple.y += 2


        if user_input == 2:
            apple.y += 3

        if user_input == 3:
            apple.y += 4


def check_apple_collision():
    global score
    for apple in apples:
        if apple.bottom >= player1.top and (player1.left + REMOVE) < apple.x < (player1.right - REMOVE) and player1.top <= apple.y <= player1.top + 3:
            score += 2
            sounds.bgmusic.stop()
            sounds.catch.play()

            apples.remove(apple)

            create_new_apple()



def check_player_collission():
    global game_over, miss
    for apple in apples:


            if apple.bottom > HEIGHT:
                miss = miss + 1
                sounds.bgmusic.stop()
                sounds.fall.play()
                apples.remove(apple)
                create_new_apple()

                if miss == 5:


                    sounds.bgmusic.stop()


                    game_over = True













create_new_apple()
pgzrun.go()























































