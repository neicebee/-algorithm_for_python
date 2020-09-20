import requests, re

"""
One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
=> 양쪽에 정확히 세 명의 큰 경호원으로 둘러싸인 소문자 1 개.
"""

def find_hint_text():
    url = "http://www.pythonchallenge.com/pc/def/equality.html"

    res = requests.get(url)

    hint_text = res.text[res.text.find("<!--"):].replace("<!--", "").replace("-->", "").strip()

    return hint_text

def find_letter(hint_text):

    result = ""

    # 소문자 1, 대문자 3, 소문자 1, 대문자 3, 소문자 1 정규식
    p = re.findall("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}", hint_text)

    for i in p:
        result = result + i[4:5]

    return result

if __name__ == '__main__':
    print(find_letter(find_hint_text()))
