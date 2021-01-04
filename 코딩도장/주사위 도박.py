import random

dice1 = random.Random()
dice2 = random.Random()

def bat_money() -> list:
    while 1:
        # user_bat = []
        print("\n==================")
        msg = input("유저 세 명의 배팅 금액을 띄어쓰기로 구분해 입력해주세요.\n(1 ~ 10,000)>>> ")

        if len(msg.split(" ")) == 3:
            '''for i in msg.split(" "):
                if 1 <= int(i) <= 10000:
                    user_bat.append(int(i))'''
            user_bat = [int(i) for i in msg.split(" ") if 1 <= int(i) <= 10000]

            if len(user_bat) == 3:
                break
            else:
                print("배팅 금액의 범위는 1 ~ 10,000 입니다.")
        else:
            print("세 명의 배팅 금액을 입력해주세요.")

    return user_bat

def game(user_num, user_money, user_bat_money) -> list:
    print(f"Dealer VS User{user_num}\nUser{user_num} 잔고: {user_money:,}원\nUser{user_num}이 배팅한 금액: {user_bat_money:,}원")

    dealer_dices = dice_rule("Dealer", dice1.randint(1, 6), dice2.randint(1, 6))
    user_dices = dice_rule(f"User{user_num}", dice1.randint(1, 6), dice2.randint(1, 6))

    result = match(dealer_dices, user_dices)

    if result == "Draw":
        print("Draw\n")
    elif "D" in result:
        print("Dealer Win\n")
    elif "U" in result:
        print(f"User{user_num} Win\n")

    return [result, user_num, user_bat_money]

def match(d, u) -> str:
    if type(d) == int and type(u) == int:
        msg = "D 1" if d > u else "U 1"
    elif type(d) == list:
        if type(u) == list:
            msg = "D 2" if d[0] > u[0] else "Draw" if d[0] == u[0] else "U 2"
        else:
            msg = "D 2"
    else:
        msg = "U 2"

    return msg

def dice_rule(name, num1, num2):
    print(f"{name}'s Result: {num1} / {num2}")
    if not num1 == num2:
        return num1 + num2
    else:
        return [num1, num2]

def print_rank(user):
    user_rank = {}
    for i in range(len(user)):
        if user[i] < 0:
            user[i] = 0
        print(f"User{i+1} 잔고: {user[i]:,}원")
        r = 1
        for j in range(len(user)):
            if user[i] == 0:
                r = "파산"
            elif user[i] < user[j]:
                r = r+1

        user_rank[f"User{i+1}"] = r

    for i in user_rank:
        if type(user_rank[i]) == str:
            print(f"{i}: {user_rank[i]}")
        else:
            print(f"{i}: {user_rank[i]}위")

if __name__ == "__main__":
    print(f"유저 세 명의 초기 자본금은 50,000원 입니다.")
    user = [50000, 50000, 50000]

    cnt = 0
    while cnt < 5:
        user_bat = bat_money()

        print(f"==================\nGame{cnt+1}!\n==================")

        for i in range(len(user)):
            if user[i] <= 0:
                user[i] = 0
                print(f"* User{i+1}은 자본금을 모두 잃었기에 배팅 금액 {user_bat[i]:,}원은 0원으로 조정됩니다 *\n")
                continue
            else:
                result = game(i+1, user[i], user_bat[i])

                if "D" in result[0]:
                    user[result[1] - 1] = user[result[1] - 1] - result[2] * int(result[0].split(" ")[1])
                elif "U" in result[0]:
                    user[result[1] - 1] = user[result[1] - 1] + result[2] * int(result[0].split(" ")[1])
        '''
        bankruptcy = []
        
        for i in range(len(user)):
            if user[i] <= 0:
                bankruptcy.append(i)
        '''
        bankruptcy = [i for i in range(len(user)) if user[i] <= 0]

        if bankruptcy:
            for i in bankruptcy:
                print(f"User{i+1} ", end="파산 ")

        if len(bankruptcy) == 2:
            break

        cnt = cnt + 1

    print("\n==================\nGame Result!\n==================")
    print_rank(user)