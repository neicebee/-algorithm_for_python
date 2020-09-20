class my_maketrans:
    def __init__(self):
        self.correct_msg = ""

    def make_trans(self, msg):
        for i in range(len(msg)):
            if msg[i] == " " or msg[i] == "." or msg[i] == "'" or msg[i] == "(" or msg[i] == ")":
                self.correct_msg = self.correct_msg + msg[i]
            else:
                if ord(msg[i])+2 > 122:
                    self.correct_msg = self.correct_msg + chr(97 + (ord(msg[i])+2) - 123)
                else:
                    self.correct_msg = self.correct_msg + chr(ord(msg[i])+2)

        return self.correct_msg

if __name__ == '__main__':
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    m_m = my_maketrans()
    correct_text = m_m.make_trans(text)
    print(correct_text)

    # 손으로 번역하지 않았으면 좋겠습니다. 그것이 컴퓨터의 목적입니다. 손으로 하는 것은 비효율적이며이 텍스트가 너무 긴 이유입니다. string.maketrans() 사용을 권장합니다. 이제 URL에 적용하십시오.
    # maketrans 메서드 => 대칭되는 문자열을 매개로 줘야함.
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "cdefghijklmnopqrstuvwxyzab"
    print(text.translate(text.maketrans(a, b)))

    url_text = 'map'

    m_m1 = my_maketrans()
    correct_url_text = m_m1.make_trans(url_text)

    print(url_text.translate(url_text.maketrans(a, b)))
    print(correct_url_text)

