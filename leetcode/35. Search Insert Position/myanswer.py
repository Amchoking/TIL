class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if(nums[left]>=target):
            return 0
        elif(nums[right]<target):
            return right+1
        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]<target and target<=nums[mid+1]):
                return mid+1
            elif(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                right=mid
            elif(nums[mid+1]<target):
                left=mid+1
        return left
