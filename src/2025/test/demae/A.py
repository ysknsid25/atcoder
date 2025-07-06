def solution(arr):
    ret=[]
    zero=[]
    for num in arr:
        if num == 0:
            zero.append(0)
        else:
            ret.append(num)
    return ret + zero
