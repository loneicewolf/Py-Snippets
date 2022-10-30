
# Functions
# -------------------------
# returns: list
def csr_1(m,k):
    i=0
    RL=[]
    for l in m:
        RL.append(m[(i+k)%len(m)])
        i+=1
    return RL


# returns: str
def csr_2(m,k):
    a=""
    i=0
    #  RL=[]
    for l in m:
        #  RL.append(m[(i+k)%len(m)])
        i+=1
        a+=m[(i+k)%len(m)]
    #  return RL
    #dbg print(a)
    return(a)

# -------------------------


# Function calls
# -------------------------
print(csr_1("abc",2))   # ['c', 'a', 'b']
print(csr_2("hello",2)) # 'lohel'



## total output
# -----
#  ['c', 'a', 'b']
#  lohel
