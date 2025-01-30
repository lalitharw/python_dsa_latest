def top_k_frequent_element(nums,k):
    hashmap = {}

    for idx in nums:
        if idx in hashmap:
            hashmap[idx] += 1
        else:
            hashmap[idx] = 1

    result = [num for num,freq in hashmap.items() if freq >= k]

    return result


print(top_k_frequent_element([1, 2, 2, 3, 3, 3, 3],2))
