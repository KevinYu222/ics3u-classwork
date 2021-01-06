def sum67(nums):
    sum = 0
    six = False
    for i in range(len(nums)):
        if nums[i] == 6:
            six = True
            nums[i] = 0
        if six == True:
            if nums[i] == 7:
                six = False
            nums[i] = 0
        sum += nums[i]
    return sum

def tests():
    assert sum67([1, 2, 2]) == 5
    assert sum67([1, 2, 2, 6, 99, 99, 7])== 5
    assert sum67([1, 1, 6, 7, 2]) == 4	
    assert sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2	
    assert sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2	
    assert sum67([2, 7, 6, 2, 6, 7, 2, 7]) == 18
    assert sum67([2, 7, 6, 2, 6, 2, 7]) == 9
    assert sum67([1, 6, 7, 7]) == 8
    assert sum67([6, 7, 1, 6, 7, 7]) == 8	
    assert sum67([6, 8, 1, 6, 7]) == 0
    assert sum67([]) == 0	
    assert sum67([6, 7, 11]) == 11	
    assert sum67([11, 6, 7, 11]) == 22
    assert sum67([2, 2, 6, 7, 7]) == 11
    print("Correct!")

if __name__ == "__main__":
    tests()
