import requests, zipfile, re

"""
zip 파일을 컨트롤할 수 있는지 확인하는 문제.

* zipfile 라이브러리 *

압축
new = zipfile.Zipfile('압축파일 저장 경로', 'w')
new.write('압축할 파일 경로', compress_type=압축종류)
new.close()

압축 해제
with zipfile.ZipFile('zip 파일 경로', 'r') as ez:
    ez.extractall('zip 파일 압축 해제 경로')
    
필요한 파일만 추출
with zipfile.ZipFile('zip 파일 경로') as ez:
    ez.extract('필요한 파일명', '파일 저장 경로')
    
Collect the comments.
=> 의견을 수집하십시오.
"""

def get_html_text(url):
    res = requests.get(url)

    return res.text

def download_zip(url):
    res = requests.get(url, allow_redirects=True)

    try:
        with open('channel/channel.zip', 'xb') as fx:
            fx.write(res.content)
            fx.close()
    except:
        print("이미 파일 있음")

    return "channel.zip"

def unlock_zip_and_get_hint(path):
    try:
        with zipfile.ZipFile(f'channel/{path}', 'r') as zr:
            zr.extractall('channel/')
            zr.close()
    except:
        print("이미 압축해제한 파일이 있음")

    with open('channel/readme.txt', 'r') as fr:
        p = re.findall("[0-9]{5}", fr.read())

        hint = p[0]

    return hint

def find_correct(hint):
    com = ""

    try:
        zf = zipfile.ZipFile("channel/channel.zip")
        com = com + zf.getinfo(f"{hint}.txt").comment.decode('utf-8')

        while hint:
            filePath = "channel/" + hint + ".txt"

            with open(filePath, 'r') as tr:
                hint = tr.read().replace("Next nothing is ", "")
                com = com + zf.getinfo(f"{hint}.txt").comment.decode('utf-8')
    except:
        print("\nScript End!")

    print(com)

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/channel.html"

    text = get_html_text(url)
    new_url = url.replace("html", text[text.find("<-- ")+4:text.find(" -->")])

    path = download_zip(new_url)
    hint = unlock_zip_and_get_hint(path)
    find_correct(hint)