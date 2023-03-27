import random


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

        if other.hp <= 0:
            other.hp = 0
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
