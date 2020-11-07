# Command_analyzer

CSV 파일 형태로 주어진 데이터를 이용하여 몇 가지 정보를 추출하는 코드를 작성

CSV 파일 이름 `command-data.csv`

파일의 첫 번째 열은 사용자가 실행시킨 명령어, 두 번째 열은 해당 사용자 id

- `count_unique` 함수
  - 이 함수는 `read_csv` 함수를 통해 읽어들인 `list` 형태의 데이터를 입력받아 **고유한 id의 수**, **고유한 command의 수**를 반환
- `make_dict` 함수
  - 이 함수는 `read_csv` 함수를 통해 읽어들인 `list` 형태의 데이터를 `dictionary` 형태의 데이터로 변환. 반환되는 `dictionary`는 `(key, value) = (id, list of commands)` 형태
    ```python
    data_dict = {id1: [command11, command12, ...],
                 id2: [command21, command22, ...],
                 ...}
    ```
  - 이때 `command`의 **좌우에 있는 불필요한 공백은 제거**되어야 합니다.
- `find_ranked` 함수
  - 이 함수는 `make_dict` 함수의 결과 `dictionary`를 입력으로 받고, `rank` 인자를 받는다. 여기서 주어진 `sort_by_n_command` 함수를 먼저 사용해야 하는데 이 함수는 입력받은 `dictionary`를 명령어 수 기준으로 내림차순 정렬한 새로운 `sorted_dict`를 반환
  - `sorted_dict`를 이용하여 입력받은 **`rank`에 해당되는 id**, **해당 id가 실행시킨 명령어의 총 수**, **해당 id가 실행시킨 고유한 명령어의 수**를 반환

