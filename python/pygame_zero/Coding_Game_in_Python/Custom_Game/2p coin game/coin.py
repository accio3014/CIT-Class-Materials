import pgzrun
from random import randint

# 대문자로 적은 이유는 상수(변하지 않는 수)이기 때문
WIDTH = 400     
HEIGHT = 400

score = 0
timer = 60
game_over = False

# fox의 위치를 100, 100 위치에 지정
fox = Actor("fox")
fox.pos = 100, 100
# coin의 위치를 200, 200 위치에 지정
coin = Actor("coin")
coin.pos = 200, 200
# hedgehog의 위치를 300, 300 위치에 지정
hedgehog = Actor("hedgehog")
hedgehog.pos = 300, 300

# 화면에 그리는 부분
def draw():
    
    screen.fill("green")    # 배경색 설정

    # 화면에 이미지를 그리는 부분
    fox.draw()
    coin.draw()
    hedgehog.draw()

    # 화면에 문자를 그리는 부분(글자색은 검은색, 위치는 10, 10)
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    # 게임의 제한시간이 종료되었을 경우 출력
    if(game_over):
        screen.fill("pink")    # 배경색 설정
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def on_mouse_down(pos): 
    if(game_over):
        quit()

# 시간제한 설정 함수
def time_up():
    global game_over
    game_over = True

# 키보드를 눌렀을 때 이벤트
def update():
    global score

    # 방향키를 누르면 fox가 이동
    if(keyboard.left): 
        fox.x = fox.x - 2
    if(keyboard.right): 
        fox.x = fox.x + 2
    if(keyboard.up): 
        fox.y = fox.y - 2
    if(keyboard.down): 
        fox.y = fox.y + 2

    # w,a,s,d를 누르면 hedgehog가 이동
    if(keyboard.a): 
        hedgehog.x = hedgehog.x - 2
    if(keyboard.d): 
        hedgehog.x = hedgehog.x + 2
    if(keyboard.w): 
        hedgehog.y = hedgehog.y - 2
    if(keyboard.s): 
        hedgehog.y = hedgehog.y + 2

    # coin_colleted 변수에 fox와 coin이 겹쳤는지 확인
    coin_collected = fox.colliderect(coin)

    # hedgehog_collected 변수에 hedgehog와 coin이 겹쳤는지 확인
    hedgehog_collected = hedgehog.colliderect(coin)

    # coin과 동물이 겹쳤으면 발생하는 이벤트
    if(coin_collected): 
        score = score + 10      # 점수 증가
        place_coin()            # coin 위치 이동
    if(hedgehog_collected):
        score = score - 10 
        place_coin()


# 동전의 위치를 랜덤하게 이동
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

clock.schedule(time_up, timer)          # timer초뒤에 time_up() 함수 실행
place_coin()
pgzrun.go()