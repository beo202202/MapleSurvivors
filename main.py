# 1.  이름을 입력해 플레이어를 생성할 수 있어야 합니다.
# 문자열로 받기.
# 2.  몬스터는 임의 생성할 수 있어야 합니다.


# 3.  while 반복문을 사용해 종료 조건을 충족할 때까지 턴제 플레이어와 몬스터간 전투를 반복 진행해야 합니다.
# 4.  플레이어는 공격 타입을 선택할 수 있어야 합니다.
#     ex) `일반공격` , `마법공격`
# 5.- 몬스터는 일반 공격을 할 수 있어야 합니다.
# 6.- 매 전투시 플레이어와 몬스터의 상태 정보를 출력해야 합니다.
# 7.- 모든 공격은 캐릭터의 파워 기준으로 랜덤성을 가지고있어야 합니다.
#     ex) 파워가 10인경우 일반공격은 8~12사이의 랜덤한 값으로 공격
# 8. 몬스터나 플레이어의 HP가 0이되면 전투를 종료하고 승리 또는 패배를 출력해야 합니다

import random
import os
import time


class Character:        # 첫 캐릭터
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        self.name = name
        self.hp = 50
        self.max_hp = 50
        # self.max_mp = mp
        self.mp = 5
        self.str_stat = str_stat
        self.dex_stat = dex_stat
        self.int_stat = int_stat
        self.luk_stat = luk_stat

    # physical_attack, magical_attack
    def physical_attack(self, other):
        # 기본 숙련도 0.4
        # 데미지 계산을 직업마다 다르게, 공격 시 other의 디펜스도... , 레벨 차...
        max_stat_attack = (self.str_stat * 4 + self.dex_stat) * \
            0.1     # (주스탯*4+부스탯) * 직업계수
        min_stat_attack = 0.4 * max_stat_attack                      # 숙련도% × 뒷스공

        damage = random.randint(min_stat_attack, max_stat_attack)
        other.hp -= damage

        print(f"{self.name}의 공격! {other.name}에게 물리공격{damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Beginner(Character):       # 초보자
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)

    def get_job(selff):
        print("당신은 전직을 하지 않은 초보자입니다.")


class Knight(Character):       # 검사, '파워 스트라이크'스킬을 추후 추가, 추후 레벨10부터 가능하게?
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)
        self.max_hp = 50 + str_stat * 5
        self.hp = 50 + str_stat * 5

    def get_job(self):
        print("검사로 전직하셨습니다.")

    def physical_attack(self, other):
        max_stat_attack = (self.str_stat * 4 + self.dex_stat) * \
            0.3     # (주스탯*4+부스탯) * 직업계수
        min_stat_attack = 0.6 * max_stat_attack     # 숙련도% × 최대스공

        damage = random.randint(min_stat_attack, max_stat_attack)
        other.hp -= damage

        print(f"{self.name}의 공격! {other.name}에게 물리공격{damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Monster:  # 몬스터, 추후 마법 공격도?
    def __init__(self, name, hp, physical_attack_power, physical_defense_power=0):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.physical_attack_power = physical_attack_power
        self.physical_defense_power = physical_defense_power

    def physical_attack(self, other):
        other.hp -= self.physical_attack_power

        print(
            f"{self.name}의 공격! {other.name}에게 물리공격{self.physical_attack_power}의 데미지를 입혔습니다.")


os.system('cls')    # 윈도우
print("░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░█▀▀▀░█▀▀▀░░█▀▀░▀▀█░░█░░")
print("░░░█░▀█░█░▀█░░█▀▀░▄▀░░░▀░░")
print("░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░▀░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞")

time.sleep(2)

for i in range(6):
    # os를 체크 하는 기능을 넣어야하나?
    os.system('cls')    # 윈도우
    # os.system('clear')  # 리눅스 or 맥
    print("몬스터 인스턴스를 생성 중" + "." * (i % 3))
    time.sleep(0.3)

# 달팽이 레벨1, hp15, mp0, 물공2, 마공1, 명중률10,회피율0,물방0,마방0
snail = Monster("달팽이", 15, 2, 0)
blue_snail = Monster("파란달팽이", 20, 3, 0)
red_snail = Monster("빨간달팽이", 50, 15, 3)

# -----------------------------------------------------------
# print로 로딩 하는 모션 보여주기....
# print("현재 모험가 초보자 클래스만 구현되어있습니다.")
# 스킬 달팽이

# os를 체크 하는 기능을 넣어야하나?
os.system('cls')    # 윈도우
# os.system('clear')  # 리눅스 or 맥

# 캐릭터 이름 설정하는...
user_name = str(input("당신의 캐릭터 이름은?: "))

for i in range(6):
    # os를 체크 하는 기능을 넣어야하나?
    os.system('cls')    # 윈도우
    # os.system('clear')  # 리눅스 or 맥
    print(f"{user_name} 모험가님 환영합니다.")
    print("캐릭터 생성 중" + "." * (i % 3))
    time.sleep(0.3)

while True:
    # 총스탯 25 중 STR, DEX, INT, LUK 을 부여 해주고
    # sum_stat = 25

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
    os.system('cls')    # 윈도우
    os.system('clear')  # 리눅스 or 맥

    print(
        f"주사위\nSTR: {str_stat}\nDEX: {dex_stat}\nINT: {int_stat}\nLUK: {luk_stat}")

    # GUI 시 묻지 않고 주사위 이미지, 확인, 취소로
    user_input = str(
        input("이대로 생성하시겠습니까?\n(확인(\"y\"), 아니오(\"any key\")\n>>입력: "))
    if user_input == "y":
        break

# os를 체크 하는 기능을 넣어야하나?
os.system('cls')    # 윈도우
# os.system('clear')  # 리눅스 or 맥

user = Beginner(user_name, str_stat, dex_stat, int_stat, luk_stat)
user.get_job()

print("전직하실 직업을 고르세요.")
user_input = int(
    input("1. 검사    2. 아처   3. 매지션   4. 로그 5. 그대로(any key)\n>>입력: "))
if (user_input == 1):
    user = Knight(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()
else:
    user = Beginner(user_name, str_stat, dex_stat, int_stat, luk_stat)
    user.get_job()


# 상대를 찾는 알고리즘(몬스터 여러 개를 딕셔너리? 리스트화 해서 랜덤 해서 상대 찾기)

# 싸움 하는 알고리즘
# user.attack()

# print(user.hp)
print(f"{snail.hp=}")

# 0326 직업 상속을 주지 않아서 오류가 났었다. 수정완료.
# 0326 함수 get_job()을 get_job(self)로 디버그
