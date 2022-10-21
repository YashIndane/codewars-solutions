def even_numbers(arr,n):
    l = list(filter(lambda x: x%2==0, arr))
    return l[len(l)-n:]
