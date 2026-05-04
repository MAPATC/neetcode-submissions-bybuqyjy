class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs: # i - это слово, типа "neet"
            result += str(len(i)) + "#" + i # += чтобы строка росла
        return result

    def decode(self, s: str) -> List[str]:
        i = 0 # Указатель
        strs = []

        while i < len(s):
            j = s.find("#", i) # Ищем решотку начиная с i(0)

            lenght = int(s[i:j]) # Вытаскиваем число (длину) между i и j

            word = s[j + 1 : j + 1 + lenght] # срезаем слово (оно идет после j + 1!)
            strs.append(word)

            i = j + 1 + lenght # Перепрыгиваем в начало следующего блока(слова)

        return strs
