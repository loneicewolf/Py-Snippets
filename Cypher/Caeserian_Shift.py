### Caeserian_Shift Python3 Implementation

# ----------------------------------------- #


def caeser_shift(m,k):
    ctx=""
    #m="hello"
    #k=3
    i=0
    for c in m:
        print(m[(i+k)%len(m)])#modulo[len(m)]
        i+=1
    
    return ctx




# caeser_shift("abc",24) -> a b c 
# caeser_shift("abc",9124) -> b c a
