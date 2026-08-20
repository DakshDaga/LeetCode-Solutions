from bisect import bisect_right

class Solution:

    def resultArray(self, nums):

        arr1 = [nums[0]]
        arr2 = [nums[1]]

        sorted1 = [nums[0]]
        sorted2 = [nums[1]]

        for i in range(2, len(nums)):

            greater1 = len(sorted1) - bisect_right(sorted1, nums[i])
            greater2 = len(sorted2) - bisect_right(sorted2, nums[i])

            if greater1 > greater2:

                arr1.append(nums[i])

                pos = bisect_right(sorted1, nums[i])
                sorted1.insert(pos, nums[i])

            elif greater2 > greater1:

                arr2.append(nums[i])

                pos = bisect_right(sorted2, nums[i])
                sorted2.insert(pos, nums[i])

            elif len(arr1) <= len(arr2):

                arr1.append(nums[i])

                pos = bisect_right(sorted1, nums[i])
                sorted1.insert(pos, nums[i])

            else:

                arr2.append(nums[i])

                pos = bisect_right(sorted2, nums[i])
                sorted2.insert(pos, nums[i])

        return arr1 + arr2