class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        char_list = []
        for char, freq in counts.items():
            char_list.append([char, freq])

        char_list.sort(key=lambda x: x[1], reverse=True)

        res = []
        for char, freq in char_list:
            res.append(char * freq)
            
        return "".join(res)