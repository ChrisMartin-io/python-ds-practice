def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 1, 10], 2)
        (1, 1)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    idx_other = len(nums)
    first_num = None
    second_num = None
    checked_lst = []

    for num in nums:
        if num not in checked_lst:
            if (goal - num) in nums:
                checked_lst.append(goal-num)
                if idx_other > nums.index(goal - num):
                    idx_other = nums.index(goal - num)
                    second_num = goal - num
                    first_num = num
    if first_num == None and second_num == None:
        return ()
    else:
        return (first_num, second_num)  

