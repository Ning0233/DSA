def non_decreasing(nums):
  count=0
  if not nums or len(nums)==1:
    return "NA"

  for i in range(1,len(nums)):
    if nums[i-1] > nums[i]:
      count+=1
  if count>1:
    return False
  else:
    return True
    

nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))


