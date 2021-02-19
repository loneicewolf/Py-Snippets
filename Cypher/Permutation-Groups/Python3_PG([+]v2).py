#------------------------------------------------------------------#
# Author: William
# Date  : Feb 19
# Year  : 2021
# Topic: One of my projects to demonstrate some permutations/etc.
#------------------------------------------------------------------#
Z=""
CTXL=[]
m=input("input message: ")
i=0;j=0
k=0
PermutedAlphabets={}
for c in m:
    for C in m:
        print(m[(j+i)%len(m)],end='')
        Z+=(m[(j+i)%len(m)])
        j+=1
    print(" ",end='\n')
    Z+=" "

    i+=1
#m="ABC"
# will print all possible permutations btw the letters 'A','B' and 'C'
#: ABC BCA CAB

# input message: ABCXYZ
# ABCXYZ 
# BCXYZA 
# CXYZAB 
# XYZABC 
# YZABCX 
# 
#input message: .0-3.
# .0-3. 
# 0-3.. 
# -3..0 
# 3..0- 
# ..0-3 

Z # contains 'ABC BCA CAB '
Z.replace("ABC","XYZ")
Z # now contains "XYZ BCA CAB"

# So, this is quite nice - we have a easy way of manipulating these values.
# so separate "blocks" of our message (m) we need a way to separate them. 
# Which we have done now. trough the 2 loops, 1 processing each individual character,
# and  the second for loop is processing "blocks" or "bricks" ("packets") of merged-characters(before proc. by  for loop 1)


