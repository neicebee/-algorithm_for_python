class Caesar():
    def __init__(self, num, msg):
        self.num = num
        self.msg = msg

        print(f"초기 문장: {self.msg}")

    def encoding(self) -> str:
        self.msg = list(self.msg)

        for i in range(len(self.msg)):
            if self.msg[i].isupper():
                self.msg[i] = chr((ord(self.msg[i]) - 65 + self.num) % 26 + 65)
            elif self.msg[i].islower():
                self.msg[i] = chr((ord(self.msg[i]) - 97 + self.num) % 26 + 97)

        self.rt_msg = ''.join(self.msg)

        return self.rt_msg

    def decoding(self) -> str:
        try:
            self.rt_msg = list(self.rt_msg)
        except:
            print('No message encoded.')

        for i in range(len(self.rt_msg)):
            if self.rt_msg[i].isupper():
                self.rt_msg[i] = chr((ord(self.rt_msg[i]) - 65 - self.num) % 26 + 65)
            elif self.rt_msg[i].islower():
                self.rt_msg[i] = chr((ord(self.rt_msg[i]) - 97 - self.num) % 26 + 97)

        self.dec_msg = ''.join(self.rt_msg)

        return self.dec_msg

if __name__ == '__main__':
    C1 = Caesar(5, "I Love Python")
    print(C1.encoding())
    print(C1.decoding())

    C2 = Caesar(18, "I Hate JAVA")
    print(C2.encoding())
    print(C2.decoding())