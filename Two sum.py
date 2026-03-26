#Given an array of numbers and a target, return indices of two numbers that add up to the target.
def two_sum(nums, target):
    seen = {}

    for k, num in enumerate(nums):
        required = target - num
        if required in seen:
            return [seen[required], k]
        seen[num] = k

    return [] 

if __name__ == "__main__":
    # User input
    nums = list(map(int, input("Array elements (space separated): ").split())) 
    target = int(input("Target value: "))

    result = two_sum(nums, target)

    if result:
        print("Indices:", result)
    else:
        print("No two sum solution found")
