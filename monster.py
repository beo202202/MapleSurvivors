import random
from textcolor import *


class Monster:  # 몬스터, 추후 마법 공격도?
    def __init__(self, name, lv, hp, mp, physical_power, magic_power, physical_defense, magic_defense, exp, meso):
        self.name = name
        self.lv = lv
        self.hp = random_hp = random.randint(round(hp * 0.9), round(hp * 1.1))
        self.max_hp = random_hp
        self.mp = random_mp = random.randint(round(mp * 0.9), round(mp * 1.1))
        self.max_mp = random_mp
        self.physical_power = random.randint(
            round(physical_power * 0.9), round(physical_power * 1.1))
        self.magic_power = random.randint(
            round(magic_power * 0.9), round(physical_power * 1.1))
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.exp = exp
        self.meso = meso

    def physical_attack(self, other):
        damage = random.randint(
            round(self.physical_power*0.85), round(self.physical_power*1.15)) - other.physical_defense
        damage = round(max(damage, 1))
        other.hp -= damage

        print(f"{Colors.RED}{self.name}{Colors.RESET}의 공격! {Colors.GREEN}{other.name}{Colors.RESET}에게 {Colors.YELLOW}물리공격{Colors.RESET}({Colors.YELLOW}{damage}{Colors.RESET})을(를) 입었습니다.")

        if other.hp <= 0:
            other.hp = 0
            print(Colors.GREEN + f"{other.name}" +
                  Colors.RESET + "이(가) 쓰러졌습니다.")

    def status(self):
        hp_left = round(self.hp/self.max_hp * 50)
        if 0.5 <= self.hp/self.max_hp <= 1:
            print(f"{Colors.RED}{self.name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.GREEN}{self.hp}{Colors.RESET}/{Colors.GREEN}{self.max_hp}{Colors.RESET} 물리방어: ", end="")
            print(f"{self.physical_defense * 100}%") if self.physical_defense < 1 else print(
                f"{self.physical_defense}")
            print(f"{Colors.GREEN}░{Colors.RESET}" * hp_left, end="")
        elif 0.2 <= self.hp/self.max_hp < 0.5:
            print(f"{Colors.RED}{self.name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.ORANGE}{self.hp}{Colors.RESET}/{Colors.GREEN}{self.max_hp}{Colors.RESET} 물리방어: ", end="")
            print(f"{self.physical_defense * 100}%") if self.physical_defense < 1 else print(
                f"{self.physical_defense}")
            print(f"{Colors.ORANGE}░{Colors.RESET}" * hp_left, end="")
        else:
            print(f"{Colors.RED}{self.name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.RED}{self.hp}{Colors.RESET}/{Colors.GREEN}{self.max_hp}{Colors.RESET} 물리방어: ", end="")
            print(f"{self.physical_defense * 100}%") if self.physical_defense < 1 else print(
                f"{self.physical_defense}")
            print(f"{Colors.RED}░{Colors.RESET}" * hp_left, end="")

        print("░" * (50 - hp_left))

        # mp% 그림, mp가 0인경우가 있다. 오류 방지
        if self.max_mp != 0:
            mp_left = round(self.mp/self.max_mp * 50)
        else:
            mp_left = 0

        print(f"{Colors.BLUE}░{Colors.RESET}" * mp_left + "░" * (50 - mp_left))
