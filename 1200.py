class Solution:
    def minimumAbsDifference(self, arr):
        mini = 10000000
        arr.sort()
        nums = []
        for i in range(0,len(arr)-1):
            if (arr[i+1]-arr[i] < mini):
                mini = arr[i+1]-arr[i]
        
        for i in range(0,len(arr)-1):
            if (arr[i+1]-arr[i] == mini):
                new_element = [arr[i],arr[i+1]]
                nums.append(new_element)
        return nums