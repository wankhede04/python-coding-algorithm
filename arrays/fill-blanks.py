array1 = [1,None,2,3,None,None,5,None]

def solution(nums):
    valid = 0            
    res = []                 
    for i in nums: 
        if i is not None:    
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

print(solution(array1))
