class Solution:
    def removeDuplicates(self, nums):
        unique_values = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_values]= nums[i]
                unique_values+=1
        return unique_values

def main():
    nums = [1, 1, 2, 2, 3, 4, 4]
    solution = Solution()
    unique_count = solution.removeDuplicates(nums)
    print(f"Number of unique elements: {unique_count}")
    print(f"Array after removing duplicates: {nums[:unique_count]}")
main()
    

