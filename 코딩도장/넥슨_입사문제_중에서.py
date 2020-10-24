sum_c = []
check_bool = True
answer_for = 0

'''
각 자릿수 숫자들과 자신을 더하기 위한 for문
int 자료형으로는 인덱스를 나눌 수 없기에 str 자료형으로 바꿔준 후 다시 int 자료형으로 바꿔서 연산해준다.
각 자릿수 숫자들은 더해준 후 자기 자신을 더해준다. 그리고 sum_c 리스트에 append 한다.
결과적으로 sum_c에는 1부터 4999까지의 제네레이터가 포함된다.
'''
for i in range(1, 5000):
    sum_check = 0
    for j in range(0, len(str(i))):
        sum_check = sum_check + int(str(i)[j])

    sum_check = sum_check + i
    sum_c.append(sum_check)


# bool 체크해서 출력하는 코딩
'''
1부터 4999까지의 숫자가 sum_c의 모든 값들을 하나하나 대조하며 같은지 아닌지를 확인하는 for문
같다면 check_bool이 True이며 같지 않다면 False를 저장한다.
그 후 check_bool이 False라면 answer_for에 i를 계속 더해간다.
결과적으로 check_for에는 제네레이터가 없는 숫자들만 더해진다.
'''
for i in range(1, 5000):
    for j in range(0, len(sum_c)):
        if sum_c[j] == i:
            check_bool = True
            break
        else:
            check_bool = False

    if check_bool == False:
        answer_for = answer_for + i

print(answer_for)

# set 자료형을 사용해서 출력하는 코딩
'''
1부터 4999까지의 숫자를 set으로 set 자료형을 만들고 sum_c를 set 자료형으로 만들어 두 집합의 여집합을 구하는 코딩이다.
answer_set에는 제네레이터가 없는 숫자들만 포함되며 sum 메서드를 사용해 각 원소들을 모두 더해주면 된다.
'''
answer_set = set(range(1, 5000)) - set(sum_c)
print(sum(answer_set))
