import random
p_count = 0
max_count = 0
flag = False
while True:
    if flag :
        break
    random_number = random.randint(1, 100)
    # print(random_number)


    while True:
        p_count = p_count + 1
        if p_count > max_count:
            max_count = p_count
        try:
            print("숫자를 입력하세요 : ")
            user_input = input()
            number = int(user_input)
            if 0 < number < 101:
                if number < random_number:
                    print("Up")
                elif number > random_number:
                    print("Down")
                else:
                    print("정답입니다")
                    print(f"당신은 {p_count}번만에 정답을 외치셨습니다! 최고기록 : {max_count}")
                    user_tf_input = input("게임을 계속하시겠습니까? Y/N :")
                    if user_tf_input == "Y" or user_tf_input == "y":
                        p_count = 0
                        break
                    if user_tf_input == "N" or user_tf_input == "n":
                        flag = True
                        break
            else:
                print("유효한 범위 내의 숫자를 입력하세요")
        except ValueError:
            print("유효한 범위 내의 숫자를 입력하세요")


