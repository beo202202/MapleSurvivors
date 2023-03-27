# 1.  이름을 입력해 플레이어를 생성할 수 있어야 합니다.
# 문자열로 받기.
# 2.  몬스터는 임의 생성할 수 있어야 합니다.


# 3.  while 반복문을 사용해 종료 조건을 충족할 때까지 턴제 플레이어와 몬스터간 전투를 반복 진행해야 합니다.
# 종료 조건1: 전투 중이지 않을 때 게임을 종료한다.
# 종료 조건2: 캐릭터 사망 후 아무 키나 누른다.

# 4.  플레이어는 공격 타입을 선택할 수 있어야 합니다.
#     ex) `일반공격` , `마법공격`
# 5.- 몬스터는 일반 공격을 할 수 있어야 합니다.
# 6.- 매 전투시 플레이어와 몬스터의 상태 정보를 출력해야 합니다.
# 7.- 모든 공격은 캐릭터의 파워 기준으로 랜덤성을 가지고있어야 합니다.
#     ex) 파워가 10인경우 일반공격은 8~12사이의 랜덤한 값으로 공격
# 8. 몬스터나 플레이어의 HP가 0이되면 전투를 종료하고 승리 또는 패배를 출력해야 합니다

import random
import os
import platform
import time


def Screen_Clear():
    if platform.system == 'window':
        os.system('cls')    # 윈도우
    else:
        os.system('clear')  # mac, 리눅스, 유닉스


class Character:        # 첫 캐릭터
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        self.name = name
        self.hp = 50 + str_stat * 5 + dex_stat * 1
        self.max_hp = 50 + str_stat * 5 + dex_stat * 1
        self.max_mp = 70 + int_stat * 5
        self.mp = 70 + int_stat * 5
        self.str_stat = str_stat
        self.dex_stat = dex_stat
        self.int_stat = int_stat
        self.luk_stat = luk_stat

    # physical_attack, magical_attack
    def physical_attack(self, other):
        # 기본 숙련도 0.4
        # 데미지 계산을 직업마다 다르게, 공격 시 other의 디펜스도... , 레벨 차...
        max_stat_attack = round((self.str_stat * 4 + self.dex_stat) *
                                0.1)     # (주스탯*4+부스탯) * 직업계수
        # 숙련도% × 뒷스공
        min_stat_attack = round(0.4 * max_stat_attack)
        attack_count = 1

        for i in range(attack_count):
            damage = random.randint(min_stat_attack, max_stat_attack)
            other.hp -= damage

            print(f"{self.name}의 공격! {other.name}에게 물리공격{damage}의 데미지를 입혔습니다.")

        if other.hp <= 0:
            other.hp = 0
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skill_attack(self, other):
        print("스킬을 사용할 수 없는 직업입니다.")

    def status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
        print(f"{self.name}의 상태: MP {self.mp}/{self.max_mp}")


class Beginner(Character):       # 초보자
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)

    def get_job(selff):
        print("당신은 전직을 하지 않은 초보자입니다.")


class Knight(Character):       # 검사, '파워 스트라이크'스킬을 추후 추가, 추후 레벨10부터 가능하게?
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)
        # self.max_hp = 50 + str_stat * 5 + dex_stat * 1
        # self.hp = 50 + str_stat * 5 + dex_stat * 1
        self.skill_name = "파워 스트라이크"

    def get_job(self):
        print("검사로 전직하셨습니다.")
        print(f"{self.skill_name}을 사용하실 수 있습니다.")

    def physical_attack(self, other):
        max_stat_attack = round((self.str_stat * 4 + self.dex_stat) *
                                0.3)     # (주스탯*4+부스탯) * 직업계수
        min_stat_attack = round(0.6 * max_stat_attack)     # 숙련도% × 최대스공
        attack_count = 1

        for i in range(attack_count):
            damage = random.randint(min_stat_attack, max_stat_attack)
            other.hp -= damage

            print(f"{self.name}의 공격! {other.name}에게 물리공격 {damage}의 데미지를 입혔습니다.")

        if other.hp <= 0:
            other.hp = 0
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skill_attack(self, other):
        if (self.mp >= 12):
            self.mp -= 12

            max_stat_attack = round((self.str_stat * 4 + self.dex_stat) *
                                    0.3 * 2.6)     # (주스탯*4+부스탯) * 직업계수 * 스킬계수
            min_stat_attack = round(0.6 * max_stat_attack)     # 숙련도% × 최대스공
            attack_count = 1

            for i in range(attack_count):
                damage = random.randint(min_stat_attack, max_stat_attack)
                other.hp -= damage

                print(
                    f"{self.name}의 공격! {other.name}에게 {self.skill_name}으로 {damage}의 데미지를 입혔습니다.")

            if other.hp <= 0:
                other.hp = 0
                print(f"{other.name}이(가) 쓰러졌습니다.")

        else:
            print("MP가 부족합니다.")


class Archer(Character):       # 아처
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)
        # self.max_hp = 50 + str_stat * 5 + dex_stat * 1
        # self.hp = 50 + str_stat * 5 + dex_stat * 1
        self.skill_name = "애로우 블로우"

    def get_job(self):
        print("아처로 전직하셨습니다.")
        print(f"{self.skill_name}을 사용하실 수 있습니다.")

    def physical_attack(self, other):
        max_stat_attack = round((self.dex_stat * 4 + self.str_stat) *
                                0.15)     # (주스탯*4+부스탯) * 직업계수
        min_stat_attack = round(0.8 * max_stat_attack)     # 숙련도% × 최대스공

        attack_count = 1

        for i in range(attack_count):
            damage = random.randint(min_stat_attack, max_stat_attack)
            other.hp -= damage

            print(f"{self.name}의 공격! {other.name}에게 물리공격 {damage}의 데미지를 입혔습니다.")

        if other.hp <= 0:
            other.hp = 0
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skill_attack(self, other):
        if (self.mp >= 11):
            self.mp -= 11

            max_stat_attack = round((self.str_stat * 4 + self.dex_stat) *
                                    0.3 * 1.6)     # (주스탯*4+부스탯) * 직업계수 * 스킬계수
            min_stat_attack = round(0.6 * max_stat_attack)     # 숙련도% × 최대스공
            attack_count = 3

            for i in range(attack_count):
                damage = random.randint(min_stat_attack, max_stat_attack)
                other.hp -= damage

                print(
                    f"{self.name}의 공격! {other.name}에게 {self.skill_name}으로 {damage}의 데미지를 입혔습니다.")

            if other.hp <= 0:
                other.hp = 0
                print(f"{other.name}이(가) 쓰러졌습니다.")

        else:
            print("MP가 부족합니다.")


class Magician(Character):       # 매지션
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)
        # self.max_hp = 25 + str_stat * 2 + dex_stat * 1
        # self.hp = 50 + str_stat * 2 + dex_stat * 1
        self.skill_name = "매직 클로"

    def get_job(self):
        print("매지션으로 전직하셨습니다.")
        print(f"{self.skill_name}을 사용하실 수 있습니다.")

    def physical_attack(self, other):       # 매지션은 일반공격이 매우 약하지
        max_stat_attack = round((self.str_stat * 4 + self.dex_stat) *
                                0.1)     # (주스탯*4+부스탯) * 직업계수
        min_stat_attack = round(0.4 * max_stat_attack)     # 숙련도% × 최대스공
        attack_count = 1

        for i in range(attack_count):
            damage = random.randint(min_stat_attack, max_stat_attack)
            other.hp -= damage

            print(f"{self.name}의 공격! {other.name}에게 물리공격 {damage}의 데미지를 입혔습니다.")

        if other.hp <= 0:
            other.hp = 0
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skill_attack(self, other):
        if (self.mp >= 20):
            self.mp -= 20

            max_stat_attack = round((self.int_stat * 4 + self.luk_stat) *
                                    0.4 * 2.5)     # (주스탯*4+부스탯) * 직업계수 * 스킬계수
            min_stat_attack = round(0.6 * max_stat_attack)     # 숙련도% × 최대스공
            attack_count = 2

            for i in range(attack_count):
                damage = random.randint(min_stat_attack, max_stat_attack)
                other.hp -= damage

                print(
                    f"{self.name}의 공격! {other.name}에게 {self.skill_name}으로 {damage}의 데미지를 입혔습니다.")

            if other.hp <= 0:
                other.hp = 0
                print(f"{other.name}이(가) 쓰러졌습니다.")

        else:
            print("MP가 부족합니다.")


class Rogue(Character):       # 로그
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)
        # self.max_hp = 25 + str_stat * 2 + dex_stat * 1
        # self.hp = 50 + str_stat * 2 + dex_stat * 1
        self.skill_name = "럭키★세븐"

    def get_job(self):
        print("로그로 전직하셨습니다.")

    def physical_attack(self, other):       # 매지션은 일반공격이 매우 약하지
        max_stat_attack = round((self.luk_stat * 4 + self.dex_stat) *
                                0.25)     # (주스탯*4+부스탯) * 직업계수
        min_stat_attack = round(0.4 * max_stat_attack)     # 숙련도% × 최대스공
        attack_count = 1

        for i in range(attack_count):
            damage = random.randint(min_stat_attack, max_stat_attack)
            other.hp -= damage

            print(f"{self.name}의 공격! {other.name}에게 물리공격 {damage}의 데미지를 입혔습니다.")

        if other.hp <= 0:
            other.hp = 0
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skill_attack(self, other):
        if (self.mp >= 14):
            self.mp -= 14

            max_stat_attack = round((self.luk_stat * 4 + self.dex_stat) *
                                    0.4 * 1.9)     # (주스탯*4+부스탯) * 직업계수 * 스킬계수
            min_stat_attack = round(0.6 * max_stat_attack)     # 숙련도% × 최대스공
            attack_count = 2

            for i in range(attack_count):
                damage = random.randint(min_stat_attack, max_stat_attack)
                other.hp -= damage

                print(
                    f"{self.name}의 공격! {other.name}에게 {self.skill_name}으로 {damage}의 데미지를 입혔습니다.")

            if other.hp <= 0:
                other.hp = 0
                print(f"{other.name}이(가) 쓰러졌습니다.")

        else:
            print("MP가 부족합니다.")


class Monster:  # 몬스터, 추후 마법 공격도?
    def __init__(self, name, hp, physical_attack_power, physical_defense_power=0):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.physical_attack_power = physical_attack_power
        self.physical_defense_power = physical_defense_power

    def physical_attack(self, other):
        max_stat_attack = self.physical_attack_power     # (일반공격력)
        # (일반공격력) * 0.85(몬스터 공격계수)
        min_stat_attack = round(0.85 * max_stat_attack)

        damage = random.randint(min_stat_attack, max_stat_attack)
        other.hp -= damage

        print(
            f"{self.name}의 공격! {other.name}에게 물리공격 {damage}의 데미지를 입혔습니다.")

    def status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


Screen_Clear()

f = open("img/donxon2.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

time.sleep(1)

Screen_Clear()


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
    Screen_Clear()
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
    time.sleep(0.01)


time.sleep(2)

for i in range(6):
    Screen_Clear()
    print("몬스터 인스턴스를 생성 중" + "." * (i % 3))
    time.sleep(0.3)


monsters = ["달팽이", "파란달팽이", "빨간달팽이", "스포아", "주황버섯", "초록버섯", "파란버섯", "뿔버섯"]


def Select_And_Create_Monster():
    select_monster = random.choice(monsters)

    if select_monster == "달팽이":
        monster = Monster("달팽이", 15, 2, 0)
    elif select_monster == "파란달팽이":
        monster = Monster("파란달팽이", 20, 3, 0)
    elif select_monster == "빨간달팽이":
        monster = Monster("빨간달팽이", 50, 15, 3)
    elif select_monster == "스포아":
        monster = Monster("스포아", 20, 6, 10)
    elif select_monster == "주황버섯":
        monster = Monster("주황버섯", 125, 41, 0)
    elif select_monster == "초록버섯":
        monster = Monster("초록버섯", 125, 47, 12)
    elif select_monster == "파란버섯":
        monster = Monster("파란버섯", 225, 58, 10)
    elif select_monster == "뿔버섯":
        monster = Monster("뿔버섯", 175, 51, 30)
    elif select_monster == "머쉬맘":
        monster = Monster("머쉬맘", 17500, 123, 25)
    else:
        print("몬스터 생성 오류 입니다.")
        # 달팽이 레벨1, hp15, mp0, 물공2, 마공1, 명중률10,회피율0,물방0,마방0
        # 이름, 체력, 일반공격력, 일반방어력
        # snail = Monster("달팽이", 15, 2, 0)
        # blue_snail = Monster("파란달팽이", 20, 3, 0)
        # red_snail = Monster("빨간달팽이", 50, 15, 3)
        # shroom = Monster("스포아", 20, 6, 10)
        # orange_mushroom = Monster("주황버섯", 125, 41, 0)
        # green_mushroom = Monster("초록버섯", 125, 47, 12)
        # blue_mushroom = Monster("파란버섯", 225, 58, 10)
        # horny_mushroom = Monster("뿔버섯", 175, 51, 30)
        # mushmom = Monster("머쉬맘", 17500, 123, 25)
        # -----------------------------------------------------------
        # 스킬 달팽이

    return monster


Screen_Clear()

# 캐릭터 이름 설정하는...
user_name = str(input("당신의 캐릭터 이름을 입력해주세요: "))

for i in range(6):
    Screen_Clear()

    print(f"{user_name} 모험가님 환영합니다.")
    print("캐릭터 생성 중" + "." * (i % 3))
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
    Screen_Clear()

    print(
        f"주사위\nSTR: {str_stat}\nDEX: {dex_stat}\nINT: {int_stat}\nLUK: {luk_stat}")

    # GUI 시 묻지 않고 주사위 이미지, 확인, 취소로
    user_input = str(
        input("이대로 생성하시겠습니까?\n(확인(\"1\"), 아니오(\"any key\")\n>>입력: "))
    if user_input == "1":
        break

Screen_Clear()

user = Beginner(user_name, str_stat, dex_stat, int_stat, luk_stat)
user.get_job()

print("전직하실 직업을 고르세요.")
user_input = int(
    input("1. 검사    2. 아처   3. 매지션   4. 로그     5. 그대로(any key)\n>>입력(숫자): "))
if (user_input == 1):
    user = Knight(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()
elif (user_input == 2):
    user = Archer(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()
elif (user_input == 3):
    user = Magician(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()
elif (user_input == 4):
    user = Rogue(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()
else:
    user = Beginner(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()

time.sleep(1)
Screen_Clear()

# 물방도 넣고, 최소 데미지는 최소1 입도록
exit_while = False
while True:
    user_input = str(
        input("전투를 하시겠습니까?\n(예(1), 종료(\"any key\")\n>>입력: "))
    if user_input == "1":
        Screen_Clear()
        # 몬스터 중에서 랜덤으로 고르기
        monster = Select_And_Create_Monster()
        print(f"{monster.name}을(를) 만났습니다.")
        # 몬스터 상태 보여주기
        monster.status()

        # 전투 하기
        while True:
            user_input = str(
                input("(일반공격(1), 스킬공격(2), 도망가기(3), 게임종료(\"any key\")\n>>입력: "))
            Screen_Clear()
            if user_input == "1":
                user.physical_attack(monster)
            elif user_input == "2":
                user.skill_attack(monster)
            elif user_input == "3":
                print("도망가기")
                break
            else:
                exit_while = True
                break

            # 몬스터가 죽으면 pass
            if monster.hp <= 0:
                break
            else:
                # 몬스터 상태 보여주기
                monster.status()

                # 몬스터가 공격
                monster.physical_attack(user)

                # 유저 상태 보여주기
                user.status()

                # 상태체크 사망 시 게임을 종료하기...
                if user.hp <= 0:
                    print(f"{user_name}이 사망하였습니다. 게임을 종료합니다.")
                    exit_while = True
                    break

    else:
        exit_while = True

    if exit_while:      # user가 게임종료를 선택함
        print("user가 게임을 종료합니다.")
        break

# 인스턴스를 초기화 할 수 있나?
# 데코레이터를 쓸 일이 있나?
