def find_duplicate(nums):
    one_step = nums[0]
    double_step = nums[0]

    while True:
        one_step = nums[one_step]
        double_step = nums[nums[double_step]]
        if one_step == double_step:
            break

    one_step = nums[0]
    while one_step != double_step:
        one_step = nums[one_step]
        double_step = nums[double_step]

    return double_step
