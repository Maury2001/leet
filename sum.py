def two_sum(nums, target):
    # Create a dictionary to store the elements and their indices
    num_dict = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement of the current number with respect to the target
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_dict:
            # If it is, return the indices of the two numbers
            return [num_dict[complement], i]
        
        # If the complement is not in the dictionary, add the current number to the dictionary
        num_dict[num] = i
    
    # If no solution is found, return an empty list or raise an exception, depending on your preference
    return []

nums = [4, 7, 11, 2]
target = 9
result = two_sum(nums, target)
print(result)  # Output should be [0, 1], as nums[0] + nums[1] = 2 + 7 = 9
