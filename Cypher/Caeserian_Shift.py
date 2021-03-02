def csr(m,k):
    i=0
    RL=[]
    for l in m:
        RL.append(m[(i+k)%len(m)])
        i+=1
    return RL

# usage:
csr("abc",2) # ['c', 'a', 'b']
