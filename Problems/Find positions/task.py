# put your python code here
nums = input().split()
num_find = input()
if nums.count(num_find):
    print(" ".join([str(index) for index, num in enumerate(nums) if num == num_find]))
else:
    print("not found")
