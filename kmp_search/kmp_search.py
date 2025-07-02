class KMPSearch:
    def __init__(self, text):
        self.__text = text

    def __str__(self):
        return f"Văn bản: '{self.__text}'"

    def build_lps(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, pattern):
        lps = self.build_lps(pattern)
        i = j = 0
        positions = []

        while i < len(self.__text):
            if pattern[j] == self.__text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]
            elif i < len(self.__text) and pattern[j] != self.__text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return positions
