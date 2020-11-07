def sort_sales(data):
    #===== write your code below =======
    list_check = []

    # 중복된 품목 및 판매량을 처리하는 반복문
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            # 만약 data i 배열의 품목과 j 배열의 품목이 같으면 i 배열의 판매량과 j 배열의 판매량을 더해 새로운 튜플을 만들고 list_check 리스트에 추가한다.
            if data[i][0] == data[j][0]:
                check = (data[i][0], data[i][1]+data[j][1])
                list_check.append(check)

    # 기존의 data에서 중복되어 처리된 배열을 제거하는 반복문
    for i in list_check:
        for j in data:
            # data를 돌면서 list_check 내에 저장되어 있는 품목과 마주치면 해당 배열을 data 리스트에서 삭제한다.
            if i[0] in j:
                data.remove(j)

    # 기존의 data를 덮어쓰는 새로운 data 생성코드
    data = data + list_check

    # sort 메서드는 새로운 반환값을 주는 메서드가 아님. 객체로 받은 변수를 변경하는 메서드임.
    data.sort(key=lambda x : -x[1])

    return data

def sales_summary(data):
    #===== write your code below =======

    # 순위 정렬 알고리즘
    for i in range(len(data)):
        rank = 1
        for j in range(len(data)):
            # 하나하나 돌아가면서 나보다 비교값이 크면 rank를 1 up
            if data[i][1] < data[j][1]:
                rank += 1

        # 한 가지 Tip : 꼼수임. 기존의 튜플에 튜플과 튜플을 더한 값을 덧씌우면 튜플을 수정할 수 있다. (기존 튜플에 더해진 튜플은 끝에 추가된다.)
        data[i] = data[i] + (rank, )

    return data

if __name__ == '__main__':
    data = [('apple', 5), ('beer', 2), ('pencil', 1),
            ('beer', 2), ('book', 8), ('apple', 9),
            ('paper', 3), ('pencil', 13), ('orange', 6)]

    sorted_sales = sort_sales(data)
    print(sorted_sales)
    summary = sales_summary(sorted_sales)
    print(summary)
