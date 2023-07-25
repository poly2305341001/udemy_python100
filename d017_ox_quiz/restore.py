import re


class Restore:

    def __init__(self):
        pass

    def quot(self, string):
        quot = r"&quot\;"
        return re.sub(quot, '"', string)

    def s_quot(self, string):
        s_quot = r"&#039\;"
        return re.sub(s_quot, "'", string)

    def all_quot(self, string):
        step_1 = self.quot(string)
        step_2 = self.s_quot(step_1)
        return step_2

    # 아 정규식 잘 쓰고 싶다 힝구힝구