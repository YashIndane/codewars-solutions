def data_reverse(data) : 
       chunks = [data[x*8:(x+1)*8] for x in range(len(data)//8)]
       chunks.reverse()
       k=[]
       for x in chunks:
            k.extend(x)
       return k
