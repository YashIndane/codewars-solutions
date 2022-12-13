def up_array(arr):
    #your code here
    if arr and all([10>x>=0 for x in arr]):
        return [int(j) for j in str(int("".join([str(x) for x in arr]))+1)]
        
    else:
        return None
