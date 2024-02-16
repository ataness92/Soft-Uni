def selection_sort(nums):
    for index in range(len(nums)):
        min_index = index

        for curr_index in range(index + 1, len(nums)):
            if nums[curr_index] < nums[min_index]:
                min_index = curr_index

        nums[index], nums[min_index] = nums[min_index], nums[index]

nums = [int(x) for x in input().split()]
selection_sort(nums)
print(*nums)