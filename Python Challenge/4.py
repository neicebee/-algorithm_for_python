import requests

"""
php를 파이썬으로 제어할 수 있는지 체크하는 문제
url에 nothing값을 삽입하는 방식으로 하면 중간중간 방해 php 페이지로 넘어간다.
때문에 url에 직접 넣지 않고 get params를 던지는 형식으로 하니 방해 페이지로 넘어가지 않고 바로 답이 나온다.

추가적으로 url에 parameters가 나타난다면 get으로 data를 넘긴 것이고, url에 나타나지 않는다면 post로 넘긴 것이다.
"""

def find_connect_url():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

    res = requests.get(url)

    code = res.text[res.text.find("linkedlist.php?")+len("linkedlist.php?"):res.text.find("><img")-1]

    getting_params(code)

def getting_params(code):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

    param = {
        "nothing": code
    }

    res = requests.get(url, params=param)

    if "and the next nothing is" in res.text:
        code = res.text[res.text.find("is ")+3:]
        getting_params(code)
    else:
        print(f'답은 {res.text}')

if __name__ == '__main__':
    find_connect_url()