def count_unique(data):
    """CSV 파일에서 읽어들인 list 형태의 데이터를 받아
    고유한 id의 수, 고유한 command의 수를 반환하는 함수입니다.

    Input:
        data: read_csv 함수로 읽어들인 list 형태의 데이터

    Output:
        n_unique_id: 고유한 id의 수
        n_unique_command: 고유한 command의 수
    """
    #===== write your code below =======

    # 중복된 id랑 command를 걸러낼 리스트
    check_id = []
    check_command = []

    # data를 한 행마다 i에 넣음
    for i in data:
        # append 메서드로 id, 즉 i의 두 번째 열 데이터를 리스트에 삽입
        check_id.append(i[1])
        # append 메서드로 command, 즉 i의 첫 번째 열 데이터를 리스트에 삽입
        check_command.append(i[0])

    # set 메서드 : 리스트 내의 값에서 중복을 허용하지 않는다는 특징이 있음. set 자료형이라는 새로운 자료형임.
    # len 메서드 : 리스트 혹은 딕셔너리, 튜플, set의 길이를 int형으로 반환해줌.
    n_unique_id = len(set(check_id))
    n_unique_command = len(set(check_command))

    #===================================

    return n_unique_id, n_unique_command

def make_dict(data):
    """CSV 파일에서 읽어들인 list 형태의 데이터를
    dictionary 형태로 변환하여 반환하는 함수입니다.

    주의사항: 명령어들 좌우에 불필요한 공백 등을 제거해야 함

    Input:
        data: read_csv 함수로 읽어들인 list 형태의 데이터

    Output:
        data_dict: id를 key,
                   해당 id가 실행한 command들의 list가 value인 dict
    """
    #===== write your code below =======
    # dict 메서드 : dict 자료형을 선언함.
    data_dict = dict()

    # data의 길이만큼 반복문
    for i in range(len(data)):
        # 만약 data i 번째 행의 두 번째 열 데이터(id)가 data_dict에 있으면
        if data[i][1] in data_dict:
            # data_dict의 key 값에 대한 value 값에 data i 번째 행의 첫 번째 열 데이터(command)를 삽입.
            # strip 메서드 : 문자열의 양 옆에 공백을 삭제해줌.
            data_dict[data[i][1].strip()].append(data[i][0].strip())
        # 아니면
        else:
            # data_dict의 key 값에 대한 value 값에 data i 번째 행의 첫 번째 열 데이터(command)를 리스트 형태로 삽입.
            # dict 자료형은 하나의 key 값에 여러가지 value 값을 넣을 수 있는데 그 value 값을 리스트로 삽입해야지 n개의 value를 넣을 수 있음.
            data_dict[data[i][1].strip()] = [data[i][0].strip()]
    #===================================

    return data_dict

def find_ranked(data_dict, rank=1):
    """dict 형태의 데이터와 rank를 입력받아 명령어 수를 기준으로
    상위 rank 번째에 해당되는 id와 그 id가 실행한 총 명령어 수, 고유한 명령어 수를 반환합니다.

    예를 들어, rank=3 이면 세 번째로 많은 명령어를 실행시킨 id와 그 명령어의 수를 반환합니다.

    Input:
        data_dict: make_dict 함수를 통해 얻은 dict 형태의 데이터

    Output:
        target_id: 상위 rank 번째에 해당되는 id
        n_commands: target_id가 실행시킨 명령어의 수
        n_unique_commands: target_id가 실행한 고유한 명령어의 수
    """

    sorted_dict = sort_by_n_command(data_dict)

    #===== write your code below =======
    # id의 순위를 체크할 리스트
    check_id = []

    # sorted_dict의 key 값이 i에 들어감.
    for i in sorted_dict:
        check_id.append(i)

    # 순차적으로 id가 리스트에 들어갔고, 리스트의 첫 번째 배열은 0으로 시작하기 때문에 rank의 값에서 1을 빼준 값을 인자로 주어야지 정확한 id값을 반환받을 수 있다.
    target_id = check_id[rank - 1]

    # 순차적으로 정리된 OrderedDict 자료형을 get 메서드에 key 값을 인자로 주어 value 값을 얻고 그 value 값의 길이를 구한다.
    n_commands = len(sorted_dict.get(target_id))

    # n_commands를 구할 때 가져온 value 값을 set 메서드에 인자로 주면 중복된 command가 삭제되며 len 메서드의 인자로 주면 길이를 구할 수 있다.
    n_unique_commands = len(set(sorted_dict.get(target_id)))

    #===================================

    return (target_id, n_commands, n_unique_commands)

# Helper function: 이 함수는 수정하지 말 것
def sort_by_n_command(data_dict):
    """dict 형태의 데이터를 받아 각 id의 명령어 수를 기준으로
    내림차순 정렬한 OrderedDict를 반환합니다.
    """

    from collections import OrderedDict

    sorted_dict = OrderedDict(sorted(data_dict.items(),
                                     key=lambda x:len(x[1]),
                                     reverse=True))

    return sorted_dict

# Helper function: 이 함수는 수정하지 말 것
def read_csv(filename):
    """파일 이름을 입력받아 list 형태로 데이터를 반환합니다.
    """

    import csv

    command_data = []
    with open(filename, 'r', encoding='ISO-8859-1') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            command_data.append(row)

    # 첫 줄 (header) 을 제거하고 반환
    return command_data[1:]

if __name__ == "__main__":
    # 구현한 함수들을 아래에서 확인해보세요.

    filename = 'command-data.csv'
    data = read_csv(filename)

    # Correct answer: n_unique_id = 115, n_unique_command = 4245
    n_unique_id, n_unique_command = count_unique(data)
    print(f"Correct answer: n_unique_id = {n_unique_id}, n_unique_command = {n_unique_command}")

    data_dict = make_dict(data)

    # Correct answer: ('elsa', 7500, 78)
    res = find_ranked(data_dict, rank=2)
    print(f"Correct answer: {res}")
