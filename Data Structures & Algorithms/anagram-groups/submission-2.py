class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Создаем специальный словарь
        # Если ключа нет, то он сам создаст его и положит туда пустой список []

        for s in strs:
            count = [0] * 26
            # Создание массива из 26 нулей

            for c in s:
                count[ord(c) - ord('a')] += 1
                # к примеру 99 - 97 = 2, значит значение пойдет по индексу 2 и т.п

            res[tuple(count)].append(s)
            # tuple(count) делаем потому, что списки не могут быть ключами словаря(они изменяемые)

            #В конце наш словарь выглядит так:
            #{ (1,0,0,0,1,...): ["eat", "tea", "ate"], (1,0,0,0,0,...): ["tan", "nat"] }
            # Поэтому возвращаем .values()
        return list(res.values())