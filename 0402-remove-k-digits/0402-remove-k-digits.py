class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size: int = len(num)
        # monolithic stack
        stack: list[int] = []

        for i in range(0, size):
            num_int: int = num[i]
            while (
                len(stack) != 0 and
                k > 0 and
                stack[-1] > num_int
            ):
                stack.pop()
                k -= 1

            stack.append(num_int)

        while len(stack) != 0 and k != 0:
            stack.pop()
            k -= 1

        ans_list: list[chr] = []
        while len(stack) != 0:
            ans_list.append(stack.pop())

        # rm last 0's 
        i: int = len(ans_list) - 1
        while len(ans_list) != 0 and ans_list[i] == '0':
            ans_list.pop()
            i -= 1

        ans_list.reverse()
        if len(ans_list) == 0:
            return "0"

        return "".join(ans_list)