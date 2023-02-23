class Dziesięćna2:

    def __init__(self):
        pass


    def na2(self, n):

        self.w = ""

        while n > 0:
            r = n % 2

            if r < 10:
                self.w = chr(r + 48) + self.w

            else:
                self.w = chr(r + 55) + self.w

            n = n // 2

        print(self.w)

n = int(input())

obj = Dziesięćna2()

obj.na2(n)