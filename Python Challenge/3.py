import requests, re
from bs4 import BeautifulSoup

"""
recognize the characters. maybe they are in the book, but MAYBE they are in the page source.
=> 문자를 인식합니다. 아마도 그들은 책에 있지만 페이지 소스에 있을수도 있습니다.
"""

def find_hint_text():
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"

    res = requests.get(url)

    hint_text_1 = res.text[res.text.find("<!--"):].replace("<!--", "").replace("-->", "")
    hint_text = hint_text_1[hint_text_1.find("below:"):].replace("below:", "").strip()

    return hint_text

# re 라이브러리의 compile 메서드를 사용한 정답찾기
def compile_find_characters(hint_text):
    p = re.compile('[a-zA-Z]')

    result = ""

    for i in hint_text:
        if p.search(i):
            result = result + i

    return result

# isalpha 메서드를 사용한 정답찾기
def isalpha_find_characters(hint_text):
    result = ""

    for i in hint_text:
        if i.isalpha():
            result = result + i

    return result

# re 라이브러리의 findall 메서드를 사용한 정답찾기
def findall_find_characters(hint_text):
    p = re.findall("[a-zA-Z]", hint_text)

    return ''.join(p)

if __name__ == '__main__':
    print(compile_find_characters(find_hint_text()))
    print(isalpha_find_characters(find_hint_text()))
    print(findall_find_characters(find_hint_text()))

