class Solution:
    def myAtoi(self, str: str) -> int:
        numMet = False
        siMet = False
        # somethingMet = False
        si = '+'
        num = 0
        for c in str:
            # print(c)
            somethingMet = False
            if (c.isalpha()): break
            if ((c == '-' or c == '+')):
                if (not numMet and not siMet):
                    si = c
                    siMet = True
                    somethingMet = True
                    continue
                else:
                    break

            if (c.isdigit()):
                num = num * 10 + int(c)
                numMet = True
                someThingMet = True
                continue

            if (c == ' '):
                if (not numMet and not siMet):
                    somethingMet = True
                    continue
                else:
                    break
            if (not somethingMet): break
        if (not numMet):
            return 0
        else:
            if (siMet):
                if (si == '-'):
                    num *= -1
                    if (num < -2147483648): return -2147483648

        if (num > (2 ** 31) - 1): return (2 ** 31 - 1)
        return num