class Solution:
    def twoSum(self, arr, target):

        mp = {}

        for i in range(len(arr)):
            diff = target - arr[i]

            if diff in mp:
                return [mp[diff], i]

            mp[arr[i]] = i
