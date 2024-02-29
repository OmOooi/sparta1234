import random

win_count = 0
lose_count = 0
drown_count = 0


while True:
    random_number = random.randint(1, 3)
    user_input = input("가위, 바위, 보 중 하나를 선택하세요")
    if user_input == "가위" or user_input == "바위" or user_input == "보":
        if random_number == 1:
            print(f"당신 : {user_input} computer : 바위")
            if user_input == "보":
                print("이겼습니다")
                win_count=win_count+1
            if user_input == "가위":
                print("졌습니다")
                lose_count=lose_count+1
            if user_input == "바위":
                print("비겼습니다")
                drown_count=drown_count+1
        if random_number == 2:
            print(f"당신 : {user_input} computer : 보")
            if user_input == "가위":
                print("이겼습니다")
                win_count=win_count+1
            if user_input == "바위":
                print("졌습니다")
                lose_count=lose_count+1
            if user_input == "보":
                print("비겼습니다")
                drown_count=drown_count+1
        if random_number == 3:
            print(f"당신 : {user_input} computer : 가위")
            if user_input == "바위":
                print("이겼습니다")
                win_count=win_count+1
            if user_input == "보":
                print("졌습니다")
                lose_count=lose_count+1
            if user_input == "가위":
                print("비겼습니다")
                drown_count=drown_count+1
    else:
        print("유효한 범위 내의 값을 입력하세요")
    user_again_input = input("다시 하시겠습니까? (y/n):")
    if user_again_input == "Y" or user_again_input == "y":
        continue
    if user_again_input == "N" or user_again_input == "n":
        break
    else:
        print("에러 : y&n 값을 찾을 수 없음, 가위, 바위, 보 게임을 종료합니다.")
        break


print("게임을 종료합니다")
print(f"승 : {win_count} 패 : {lose_count} 무승부 : {drown_count}")