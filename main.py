import random
import os
import platform
import time
import pygame
from character import *
from monster import *
from textcolor import *


def screen_clear():
    if platform.system == 'window':
        os.system('cls')    # 윈도우
    else:
        os.system('clear')  # mac, 리눅스, 유닉스


monsters = ["달팽이", "파란 달팽이", "빨간 달팽이", "스포아",
            "주황버섯", "시니컬한 주황버섯", "초록버섯", "파란버섯", "우는 파란버섯", "뿔버섯", "돼지", "리본돼지", "파란 리본돼지", "머쉬맘"]

# 몬스터이름, 레벨, 체력, 마나, 일공, 마공, 일방, 마방, 경험치, 메소

# 일방 마방이 1보다 낮은 경우 데미지*(1-그값)로 바꿔야한다.


def select_and_create_monster():
    select_monster = random.choice(monsters)

    if select_monster == "달팽이":
        monster = Monster(select_monster, 1, 15, 0, 2, 1, 0.1, 0.1, 3, 5)
    elif select_monster == "파란 달팽이":
        monster = Monster(select_monster, 2, 20, 0, 3, 2, 0.1, 0.1, 4, 10)
    elif select_monster == "빨간 달팽이":
        monster = Monster(select_monster, 5, 50, 0, 15, 12, 0.1, 0.1, 8, 15)
    elif select_monster == "스포아":
        monster = Monster(select_monster, 3, 20, 0, 6, 4, 0.1, 0.1, 4, 10)
    elif select_monster == "주황버섯":
        monster = Monster(select_monster, 10, 125, 10, 41, 35, 0, 10, 17, 20)
    elif select_monster == "시니컬한 주황버섯":
        monster = Monster(select_monster, 11, 150, 20, 43, 38, 0, 10, 19, 25)
    elif select_monster == "초록버섯":
        monster = Monster(select_monster, 10, 125, 10,
                          47, 35, 0.05, 0.05, 17, 20)
    elif select_monster == "파란버섯":
        monster = Monster(select_monster, 14, 225, 20,
                          58, 55, 0.1, 0.1, 24, 45)
    elif select_monster == "우는 파란버섯":
        monster = Monster(select_monster, 15, 250, 20,
                          63, 57, 0.1, 0.1, 26, 50)
    elif select_monster == "뿔버섯":
        monster = Monster(select_monster, 12, 175, 20,
                          51, 45, 0.1, 0.1, 21, 30)
    elif select_monster == "돼지":
        monster = Monster(select_monster, 7, 80, 10, 24, 19, 5, 20, 12, 18)
    elif select_monster == "리본돼지":
        monster = Monster(select_monster, 10, 125, 10, 38, 35, 10, 30, 17, 20)
    elif select_monster == "파란 리본돼지":
        monster = Monster(select_monster, 13, 200, 20, 54, 49, 10, 30, 23, 47)
    elif select_monster == "머쉬맘":
        monster = Monster(select_monster, 18, 17500, 2000,
                          123, 109, 0.25, 0.25, 1650, 1000)
    else:
        print("몬스터 생성 오류 입니다.")
        # snail = Monster("달팽이", 15, 2, 0)
        # blue_snail = Monster("파란달팽이", 20, 3, 0)
        # red_snail = Monster("빨간달팽이", 50, 15, 3)
        # shroom = Monster("스포아", 20, 6, 10)
        # orange_mushroom = Monster("주황버섯", 125, 41, 0)
        # cynical_monster("시니컬한 주황버섯", 150, 43, 0)
        # green_mushroom = Monster("초록버섯", 125, 47, 12)
        # blue_mushroom = Monster("파란버섯", 225, 58, 10)
        # crying_blue_mushroom = Monster("우는 파란버섯", 250, 63, 10)
        # horny_mushroom = Monster("뿔버섯", 175, 51, 30)
        # pig = Monster("돼지", 80, 25, 10)
        # ribon_pig = Monster("리본돼지", 125, 38, 10)
        # blueribon_pig = Monster("파란 리본돼지", 200, 54, 10)
        # mushmom = Monster("머쉬맘", 17500, 123, 25)
        # -----------------------------------------------------------
        # 스킬 달팽이
    return monster

# 몬스터 이미지


# 딕셔너리로...
# mon = monster_dict[input("직업을 선택해주세요.")]
# if mon_select in monster_dict.keys():
#     job = player_dit[job_select]
#     break
# monster_dict = {
#     "1": Monster(
#         name="달팽이"
#         lv=1
#         hp=15
#         mp=0
#         power=2
#         magic_power=0
#         pysical_defence=10
#         magic_defence=10
#         file_name="snail"
#         new_music="sounds/Maple_Leaf.mp3"
#     ),
# }

# current_music = ""
played_music = []


def screen_monster(name):
    # global current_music
    global played_music

    if name == "달팽이":
        file_name = "snail"
        new_music = "sounds/Maple_Leaf.mp3"
    elif name == "파란 달팽이":
        file_name = "blue_snail"
        new_music = "sounds/Maple_Leaf.mp3"
    elif name == "빨간 달팽이":
        file_name = "red_snail"
        new_music = "sounds/Above_the_Treetops.mp3"
    elif name == "스포아":
        file_name = "shroom"
        new_music = "sounds/Cava_Bien.mp3"
    elif name == "주황버섯":
        file_name = "orange_mushroom"
        new_music = "sounds/Cava_Bien.mp3"
    elif name == "시니컬한 주황버섯":
        file_name = "cynical_orange_mushroom"
        new_music = "sounds/Cava_Bien.mp3"
    elif name == "초록버섯":
        file_name = "green_mushroom"
        new_music = "sounds/Ancient_Move.mp3"
    elif name == "파란버섯":
        file_name = "blue_mushroom"
        new_music = "sounds/Rest_n_Peace.mp3"
    elif name == "우는 파란버섯":
        file_name = "crying_blue_mushroom"
        new_music = "sounds/Rest_n_Peace.mp3"
    elif name == "뿔버섯":
        file_name = "horny_mushroom"
        new_music = "sounds/Ancient_Move.mp3"
    elif name == "돼지":
        file_name = "pig"
        new_music = "sounds/Blue_Sky.mp3"
    elif name == "리본돼지":
        file_name = "ribon_pig"
        new_music = "sounds/Blue_Sky.mp3"
    elif name == "파란 리본돼지":
        file_name = "blue_ribon_pig"
        new_music = "sounds/Blue_Sky.mp3"
    elif name == "머쉬맘":
        file_name = "mushmom"
        new_music = "sounds/FloralLife.mp3"
    else:
        print("몬스터 생성 오류 입니다.")

    # if current_music != new_music:
    #     current_music = new_music
    #     pygame.mixer.music.load(current_music)

    if new_music not in played_music:
        played_music.append(new_music)
        pygame.mixer.music.load(new_music)
        pygame.mixer.music.play(-1)

    f = open("img/" + file_name + ".txt", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines:
        line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
        print(line)

    f.close()

    print("\n")


# -------------------       알고리즘 시작      --------------------------


screen_clear()

# pygame.init()
pygame.mixer.init()

sound_effect = pygame.mixer.Sound("sounds/NexonLoad.mp3")  # 넥슨 로딩
# sound_effect.set_volume(0.5)
sound_effect.play()

f = open("img/nexon_logo.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
    time.sleep(0.05)
f.close()

time.sleep(1)


screen_clear()


a = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
my_list_a = list(a)
b = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
my_list_b = list(b)
c = "░░░░█▄░▄█░░░█░░░█▀▀▄░█░░░░█▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
my_list_c = list(c)
d = "░░░░█░▀░█░░█▄█░░█▀▀░░█░░░░█▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
my_list_d = list(d)
e = "░░░░▀░░░▀░▀░░░▀░▀░░░░▀▀▀▀░▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
my_list_e = list(e)
f = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀▀▀▀░█░░░█░█▀▀▀▄░█░░░█░▀▀█▀▀░█░░░█░▄▀▀▀▄░█▀▀▀▄░▄▀▀▀▀░░░░"
my_list_f = list(f)
g = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▄░█░░░█░█▀▀█░░░█░█░░░░█░░░░█░█░░█░░░█░█▀▀█░░░▀▀▀▄░░░░"
my_list_g = list(g)
h = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀░░░▀▀▀░░▀░░░▀░░░▀░░░▀▀▀▀▀░░░▀░░░░▀▀▀░░▀░░░▀░▀▀▀▀░░░░░"
my_list_h = list(h)
i = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
my_list_i = list(i)
j = "༼๑◕◞◟◕๑༽⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞"
my_list_j = list(j)

str_a = str_b = str_c = str_d = str_e = str_f = str_g = str_h = str_i = str_j = ""
for i in range(len(my_list_a)):
    screen_clear()
    str_a += my_list_a[i]
    str_b += my_list_b[i]
    str_c += my_list_c[i]
    str_d += my_list_d[i]
    str_e += my_list_e[i]
    str_f += my_list_f[i]
    str_g += my_list_g[i]
    str_h += my_list_h[i]
    str_i += my_list_i[i]
    str_j += my_list_j[i]
    print(f"{str_a}\n{str_b}\n{str_c}\n{str_d}\n{str_e}\n{str_f}\n{str_g}\n{str_h}\n{str_i}\n{str_j}")
    time.sleep(0.001)


time.sleep(2)

screen_clear()


for i in range(6):
    screen_clear()
    print(f"{Colors.RED}몬스터 인스턴스{Colors.RESET}를 생성할 준비 중" + "." * (i % 3))
    time.sleep(0.3)


pygame.mixer.music.load("sounds/Old_Main_Title.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

screen_clear()

f = open("img/login.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
    time.sleep(0.05)
f.close()

# 캐릭터 이름 설정하는...
user_name = str(
    input(f"당신의 캐릭터 {Colors.GREEN}이름{Colors.RESET}을 입력해주세요.\n>>입력: {Colors.GREEN}"))

sound_effect = pygame.mixer.Sound("sounds/Maplestory-004.wav")  # 입력 후 출력 소리
sound_effect.play()

for i in range(6):
    screen_clear()

    print(f"{Colors.GREEN}{user_name} 모험가{Colors.RESET}님 환영합니다.")
    print(f"{Colors.GREEN}{user_name}{Colors.RESET} 캐릭터 생성 중" + "." * (i % 3))
    time.sleep(0.3)

while True:
    # 총스탯 25 중 STR, DEX, INT, LUK 을 부여 해주고
    # total_stat = 25

    # 나중에 확인 후 다시 만들자...
    # 리스트나 딕셔터리에 저장해야하나?
    # 럭이 높은 확률이 적나?, 동일 확률이 맞는가?
    remain_stat = 9
    str_stat = 4 + random.randint(0, remain_stat)
    remain_stat += 4 - str_stat

    dex_stat = 4 + random.randint(0, remain_stat)
    remain_stat += 4 - dex_stat

    int_stat = 4 + random.randint(0, remain_stat)
    remain_stat += 4 - int_stat

    luk_stat = 4 + remain_stat
    remain_stat += 4 - luk_stat     # 디버그 코딩

    # sum_stat = str_stat + dex_stat + int_stat + luk_stat    # 디버그 코딩

    # print(f"{remain_stat=}")    # 디버그
    # print(f"{sum_stat=}")       # 디버그

    # stat = {'str_stat': str_stat, 'dex_stat': dex_stat,
    #        'int_stat': int_stat, 'luk_stat': luk_stat}

    # Python 3.8부터 변수 한 번만 사용 가능
    # print(f"{str_stat=}\n{dex_stat=}\n{int_stat=}\n{luk_stat=}")
    screen_clear()

    print(
        f"주사위\n{Colors.ORANGE}STR: {str_stat}\nDEX: {dex_stat}\nINT: {int_stat}\nLUK: {luk_stat}{Colors.RESET}")

    # GUI 시 묻지 않고 주사위 이미지, 확인, 취소로
    user_input = str(
        input(f"{Colors.GREEN}이대로 생성하시겠습니까?{Colors.RESET}\n(확인(\"1\"), 아니오(\"any key\")\n>>입력: {Colors.GREEN}"))

    sound_effect = pygame.mixer.Sound(
        "sounds/Maplestory-004.wav")  # 입력 후 출력 소리
    sound_effect.play()

    if user_input == "1":
        break

screen_clear()

user = Beginner(user_name, str_stat, dex_stat, int_stat, luk_stat)
user.get_job()

print(f"{Colors.RESET}전직하실 {Colors.GREEN}직업{Colors.RESET}을 고르세요.")
user_input = str(
    input(f"검사(\"1\")    아처(\"2\")   매지션(\"3\")   로그(\"4\")     그대로(\"any key\")\n>>입력(숫자): {Colors.GREEN}"))

if (user_input == "1"):
    user = Knight(user_name, str_stat, dex_stat, int_stat, luk_stat)
    sound_effect = pygame.mixer.Sound(
        "sounds/Maplestory-011_2.wav")  # 입력 후 출력 소리
    sound_effect.play()
    user.get_job()

elif (user_input == "2"):
    user = Archer(user_name, str_stat, dex_stat, int_stat, luk_stat)
    sound_effect = pygame.mixer.Sound(
        "sounds/Maplestory-011_2.wav")  # 입력 후 출력 소리
    sound_effect.play()
    user.get_job()
elif (user_input == "3"):
    user = Magician(user_name, str_stat, dex_stat, int_stat, luk_stat)
    sound_effect = pygame.mixer.Sound(
        "sounds/Maplestory-011_2.wav")  # 입력 후 출력 소리
    sound_effect.play()
    user.get_job()
elif (user_input == "4"):
    user = Rogue(user_name, str_stat, dex_stat, int_stat, luk_stat)
    sound_effect = pygame.mixer.Sound(
        "sounds/Maplestory-011_2.wav")  # 입력 후 출력 소리
    sound_effect.play()
    user.get_job()
else:
    user = Beginner(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()

time.sleep(2)

# 물방도 넣고, 최소 데미지는 최소1 입도록 시간 안될듯...
exit_while = False
while True:
    screen_clear()

    # 유저 상태 보여주기
    user.status()

    user_input = str(
        input(f"{Colors.RED}전투를 하시겠습니까?\n예{Colors.RESET}(\"1\"), 종료(\"any key\")\n>>입력: {Colors.GREEN}"))

    sound_effect = pygame.mixer.Sound(
        "sounds/Maplestory-004.wav")  # 입력 후 출력 소리
    sound_effect.play()

    screen_clear()
    if user_input == "1":

        # 몬스터 중에서 랜덤으로 고르기
        monster = select_and_create_monster()
        print(f"{Colors.RESET}{Colors.RED}{monster.name}{Colors.RESET}을(를) 만났습니다.")
        # 몬스터 상태 보여주기
        monster.status()
        # 몬스터 이미지
        screen_monster(monster.name)
        # 몬스터 배경음
        # Monster_Sound(monster.name)

        # 전투 하기
        while True:
            # 유저 상태 보여주기
            user.status()

            user_input = str(
                input(f"{Colors.GREEN}일반공격{Colors.RESET}(\"1\"), {Colors.BLUE}스킬공격{Colors.RESET}(\"2\"), {Colors.RED}도망가기{Colors.RESET}(\"3\"), 게임종료(\"any key\")\n>>입력: "))

            sound_effect = pygame.mixer.Sound(
                "sounds/Maplestory-004.wav")  # 입력 후 출력 소리
            sound_effect.play()

            screen_clear()

            if user_input == "1":
                user.physical_attack(monster)
                sound_effect = pygame.mixer.Sound(
                    "sounds/Maplestory-006.wav")  # 입력 후 출력 소리
                sound_effect.play()
                print("\n")
            elif user_input == "2":
                screen_clear()

                sound_effect = pygame.mixer.Sound(
                    "sounds/Maplestory-008.wav")  # 입력 후 출력 소리
                sound_effect.play()

                user.skill_attack(monster)
                print("\n")
            elif user_input == "3":
                print("도망가기")
                break
            else:
                exit_while = True
                break

            # 몬스터가 죽으면 pass
            if monster.hp == 0:
                time.sleep(1)
                sound_effect = pygame.mixer.Sound(
                    "sounds/Maplestory-013.wav")  # 입력 후 출력 소리
                sound_effect.play()
                for i in range(4):
                    screen_clear()
                    print("승리하였습니다!!! 축하드립니다!!!")
                    time.sleep(0.2)

                    screen_clear()
                    print(f"{Colors.GREEN}승리하였습니다!!! 축하드립니다!!!{Colors.RESET}")
                    time.sleep(0.2)
                break
            else:
                # 몬스터 상태 보여주기
                monster.status()

                # 몬스터 이미지
                screen_monster(monster.name)

                # 몬스터가 공격
                monster.physical_attack(user)

                # 상태체크 사망 시 게임을 종료하기...
                if user.hp <= 0:
                    time.sleep(1)
                    user.status()

                    pygame.mixer.music.stop()
                    sound_effect = pygame.mixer.Sound(
                        "sounds\Tombston.mp3")  # 입력 후 출력 소리
                    sound_effect.set_volume(1)
                    sound_effect.play()

                    print(
                        f"{Colors.RESET}{Colors.GREEN}{user_name}{Colors.RESET}{Colors.RED}이(가) 사망하였습니다. 게임을 종료합니다. (패배조건){Colors.RESET}")
                    exit_while = True

                    time.sleep(2)
                    break

    else:
        exit_while = True

    if exit_while:      # user가 게임종료를 선택함
        print(f"{Colors.RESET}{Colors.GREEN}{user_name}{Colors.RESET}(이)가 게임을 종료합니다.")
        break

# 데코레이터를 쓸 일이 있나?
