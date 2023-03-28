import random
from textcolor import *


class Monster:  # 몬스터, 추후 마법 공격도?
    def __init__(self, name, hp, physical_attack_power, physical_defense_power=0):
        self.name = name
        self.hp = random_hp = random.randint(
            round(hp-hp*0.1), round(hp+hp*0.1))
        self.max_hp = random_hp
        self.physical_attack_power = random.randint(round(
            physical_attack_power-physical_attack_power*0.1), round(physical_attack_power+physical_attack_power*0.1))
        self.physical_defense_power = random.randint(round(
            physical_defense_power-physical_defense_power*0.1), round(physical_defense_power+physical_defense_power*0.1))

    def physical_attack(self, other):
        max_stat_attack = self.physical_attack_power     # (일반공격력)
        # (일반공격력) * 0.85(몬스터 공격계수)
        min_stat_attack = round(0.85 * max_stat_attack)

        damage = random.randint(min_stat_attack, max_stat_attack)
        other.hp -= damage

        print(f"{Colors.RED}{self.name}{Colors.RESET}의 공격! {Colors.GREEN}{other.name}{Colors.RESET}에게 {Colors.YELLOW}물리공격{Colors.RESET}({Colors.YELLOW}{damage}{Colors.RESET})을(를) 입었습니다.")

        if other.hp <= 0:
            other.hp = 0
            print(Colors.GREEN + f"{other.name}" +
                  Colors.RESET + "이(가) 쓰러졌습니다.")

    def status(self):
        hp_left = round(self.hp/self.max_hp * 50)
        if 0.5 <= self.hp/self.max_hp <= 1:
            print(f"{Colors.RED}{self.name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.GREEN}{self.hp}{Colors.RESET}/{Colors.GREEN}{self.max_hp}{Colors.RESET} 물리방어력: {self.physical_defense_power}")
            print(f"{Colors.GREEN}░{Colors.RESET}" *
                  hp_left + "░" * (50-hp_left))
        elif 0.2 <= self.hp/self.max_hp < 0.5:
            print(f"{Colors.RED}{self.name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.ORANGE}{self.hp}{Colors.RESET}/{Colors.GREEN}{self.max_hp}{Colors.RESET} 물리방어력: {self.physical_defense_power}")
            print(f"{Colors.ORANGE}░{Colors.RESET}" *
                  hp_left + "░" * (50-hp_left))
        else:
            print(f"{Colors.RED}{self.name}{Colors.RESET}의 상태: {Colors.RED} HP {Colors.RESET}{Colors.RED}{self.hp}{Colors.RESET}/{Colors.GREEN}{self.max_hp}{Colors.RESET} 물리방어력: {self.physical_defense_power}")
            print(f"{Colors.RED}░{Colors.RESET}" *
                  hp_left + "░" * (50-hp_left))
