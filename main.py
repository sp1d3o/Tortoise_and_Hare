print("Find duplicated number in:")
print("[3,1,3,4,2]\n")

def find_duplicated_number(nums):
    tortoise = nums[0]
    hare = nums[0]

    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

print(find_duplicated_number([3,1,3,4,2]))