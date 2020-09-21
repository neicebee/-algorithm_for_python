import requests, pickle
import urllib.request

"""
pronounce it
=> 그것을 발음

peak hell sounds familiar?
=> peak hell 발음이 익숙한가요?

파이썬 pickle 파일을 의미함. pickle 파일의 확장자는 .p
pickle 파일 내에 있는 리스트 데이터를 txt화 시켜서 보이는 글자가 정답.
"""

def get_html_text(url):
    res = requests.get(url)

    return res.text

# urllib 라이브러리로 pickle 데이터를 불러오는 경우
def get_urllib_pickle_data(url):
    data = urllib.request.urlopen(url)

    p_data = pickle.load(data)

    return p_data

# requests 라이브러리로 pickle 데이터를 불러오는 경우
def get_requests_pickle_data(url):
    data = requests.get(url, allow_redirects=True)

    try:
        with open('banner.p', 'xb') as fw:
            fw.write(data.content)
            fw.close()
    except:
        pass

    with open('banner.p', 'rb') as fr:
        p_data = pickle.load(fr)
        fr.close()

    return p_data

def make_correct_text(p_data):
    with open('correct.txt', 'w') as fw:
        for i in p_data:
            for j in i:
                fw.write(j[0]*j[1])
            fw.write("\n")
        fw.close()

    return "Script Finsh!"

if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/def/peak.html"

    res_text_1 = get_html_text(url)
    next_url = "http://www.pythonchallenge.com/pc/def/" + res_text_1[res_text_1.find("peakhell src=") + 14:res_text_1.find(""".p"/>""") + 2]

    p_data = get_requests_pickle_data(next_url)

    print(make_correct_text(p_data))
