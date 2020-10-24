def SpiralArray(X, Y):
    sa_list = [[0 for x in range(X)] for y in range(Y)]
    '''
    count : 0부터 X*Y-1의 값을 차례로 저장할 변수
    flag : 진행방향을 정할 변수
    '''
    count = 0
    flag = 0
    i, j = 0, 0

    while True:
        '''
        flag가 0일 때 오른쪽으로 진행
        배열에 count 값을 넣고 오른쪽으로 진행되니 j 값이 1씩 증가해야함.
        count 값은 사용했으니 1 증가
        반복문을 돌리다가 j 값이 Y와 같아지거나(배열 인덱스 값이 맞지 않을 때) 배열 내의 값이 0이 아닐 때
        j의 값을 1 감소시켜 전 배열 인덱스로 돌아간 후 i의 값을 1 증가시켜 다음 배열로 넘어간다.
        flag의 값을 1로 정의한다.
        
        flag가 1일 때 아래쪽으로 진행
        
        flag가 2일 때 왼쪽으로 진행
        
        flag가 3일 때 위쪽으로 진행
        '''
        if flag == 0:
            sa_list[i][j] = count
            j+=1
            count+=1
            if j == Y or sa_list[i][j] != 0:
                j-=1
                i+=1
                flag = 1
        elif flag == 1:
            sa_list[i][j] = count
            i+=1
            count+=1
            if i == X or sa_list[i][j] != 0:
                i-=1
                j-=1
                flag = 2
        elif flag == 2:
            sa_list[i][j] = count
            j-=1
            count+=1
            if j == -1 or sa_list[i][j] != 0:
                i-=1
                j+=1
                flag = 3
        elif flag == 3:
            sa_list[i][j] = count
            i-=1
            count+=1
            if i == 0 or sa_list[i][j] != 0:
                i+=1
                j+=1
                flag = 0

        # 만약 count가 X*Y의 값과 같아질 때 while문 break
        if count == X*Y:
            break

    # 2차원 배열 원소 출력하기
    for k1 in sa_list:
        for k2 in k1:
            print(k2, "\t", end='')
        print()


if __name__ == '__main__':
    # map : 리스트의 요소를 지정된 함수로 처리해주는 함수(원본 리스트를 변경하지 않고 새 리스트를 생성함.)
    X, Y = map(int, input("입력: ").split(" "))
    SpiralArray(X, Y)
