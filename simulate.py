# 몬티 홀 문제를 시뮬레이션하는 파이썬 코드
# 10,000번 실험해서 바꿨을 때와 안 바꿨을 때의 승률 비교
import random

def monty_hall_simulation(num_trials=10000):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # Step 1: 랜덤하게 문 배치 (1개의 자동차, 2개의 염소)
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        # Step 2: 참가자가 처음 선택한 문
        player_choice = random.randint(0, 2)

        # Step 3: 사회자가 염소가 있는 문을 열어줌
        host_options = [i for i in range(3) if i != player_choice and doors[i] == 'goat']
        host_reveal = random.choice(host_options)

        # Step 4: 참가자가 선택을 바꾸는 경우
        switch_choice = [i for i in range(3) if i != player_choice and i != host_reveal][0]

        # 결과 확인
        if doors[switch_choice] == 'car':
            switch_wins += 1
        if doors[player_choice] == 'car':
            stay_wins += 1

    # 승률 계산
    switch_win_rate = (switch_wins / num_trials) * 100
    stay_win_rate = (stay_wins / num_trials) * 100

    return switch_win_rate, stay_win_rate

if __name__ == "__main__":
    num_trials = 10000
    switch_win_rate, stay_win_rate = monty_hall_simulation(num_trials)

    print(f"문을 바꿨을 때 승률: {switch_win_rate:.2f}%")
    print(f"문을 바꾸지 않았을 때 승률: {stay_win_rate:.2f}%")