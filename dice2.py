import random

stats = ['STR', 'DEX', 'INT', 'LUK']  # 스탯 종류
total_stats = 25  # 총 스탯 포인트
min_stat, max_stat = 4, 13  # 최소값과 최대값

# 스탯 무작위 생성
random_stats = [random.randint(min_stat, max_stat) for _ in stats]

# 남은 스탯 포인트 무작위 배분
for i in range(total_stats - sum(random_stats)):
    random_stats[random.randint(0, len(stats) - 1)] += 1

# 결과 출력
for i, stat in enumerate(stats):
    print(stat, ':', random_stats[i])
