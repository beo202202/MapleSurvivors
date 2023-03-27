import random


class Character:                # 첫 캐릭터
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
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, MP {self.mp}/{self.max_mp}")


class Beginner(Character):      # 초보자
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)

    def get_job(selff):
        print("당신은 전직을 하지 않은 초보자입니다.")


class Knight(Character):        # 검사, 추후 레벨10부터 가능하게?
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


class Archer(Character):        # 아처
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


class Magician(Character):      # 매지션
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


class Rogue(Character):         # 로그
    def __init__(self, name, str_stat, dex_stat, int_stat, luk_stat):
        super().__init__(name, str_stat, dex_stat, int_stat, luk_stat)
        # self.max_hp = 25 + str_stat * 2 + dex_stat * 1
        # self.hp = 50 + str_stat * 2 + dex_stat * 1
        self.skill_name = "럭키★세븐"

    def get_job(self):
        print("로그로 전직하셨습니다.")
        print(f"{self.skill_name}을 사용하실 수 있습니다.")

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
