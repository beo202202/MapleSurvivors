import random

stats = ['STR', 'DEX', 'INT', 'LUK']  # 스탯 종류
total_stats = 25  # 총 스탯 포인트

# 최소값과 최대값 설정
min_stat = 4
max_stat = 13

# 무작위 스탯 생성
random_stats = [random.randint(min_stat, max_stat) for _ in range(len(stats))]

# 총 스탯 포인트에서 생성된 스탯 포인트 빼기
remaining_stats = total_stats - sum(random_stats)

# 남은 스탯 포인트를 무작위로 스탯에 배분
while remaining_stats > 0:
    # 스탯 종류 중에서 무작위로 하나 선택
    stat_index = random.randint(0, len(stats)-1)
    # 선택된 스탯에 1 포인트 추가
    random_stats[stat_index] += 1
    # 남은 스탯 포인트 1 감소
    remaining_stats -= 1

# 결과 출력
for i in range(len(stats)):
    print(stats[i], ':', random_stats[i])
