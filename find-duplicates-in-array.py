#1. Optimal Approach (Using a Dictionary/Hash Map)
def find_duplicates(nums):
    count_map = {}
    duplicates = []
    
    for num in nums:
        # Number dictionary-la munnadiye irundha, adhu duplicate
        if num in count_map:
            if count_map[num] == 1: # Oru dharava mela add aagama irukka
                duplicates.append(num)
            count_map[num] += 1
        else:
            count_map[num] = 1
            
    return duplicates

# Example
print(find_duplicates([1, 2, 3, 2, 4, 5, 1])) # Output: [2, 1]

#Complexity Analysis:Time Complexity: $O(n)$ — Array-va oru dharava scan panna podhum.Space Complexity: $O(n)$ — Numbers-ah store panna extra dictionary thevai.
#2. Set Approach (Simple & Fast)
def find_duplicates_set(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)


# Scenario,Input,    Expected       Output
# No Duplicates,     "[1, 2, 3]",    []
# All Duplicates,    "[1, 1, 1]",    [1]
# Empty Array,        [],             []
# Negative Numbers,  "[-1, 2, -1]",  [-1]
# Large Input,1 million elements,Efficiency check (O(n) is must)
