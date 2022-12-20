def sum_of_differences(arr):
    if len(arr)<=1:
        return 0
    else:
        s=sorted(arr, reverse=True)
        q=0
        for i in range(len(s)-1):
            q+=s[i]-s[i+1]
        return q
