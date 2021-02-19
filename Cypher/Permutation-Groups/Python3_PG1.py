#------------------------------------------------------------------#
# Author: William
# Date  : Feb 19
# Year  : 2021
# Topic: One of my projects to demonstrate some permutations/etc.
#------------------------------------------------------------------#


# empty list
CTXL=[]

# msg

m=input("input message: ")
# ctrA,ctrB (ctr<> for counter <n. of ctr>)
i=0;j=0


# (k for key)
k=0

# for char in msg m:
for c in m:
    for C in m:
        print(m[(j+i)%len(m)],end='') ;
        j+=1
    print(" ",end='\n')
    
    i+=1
#m="ABC"
# will print all possible permutations btw the letters 'A','B' and 'C'
#: ABC BCA CAB

# # so for example, entering the alphabet: "abcdefghijklmnopqrstuvwxyz"
# # produces the following output:
# abcdefghijklmnopqrstuvwxyz 
# bcdefghijklmnopqrstuvwxyza 
# cdefghijklmnopqrstuvwxyzab 
# defghijklmnopqrstuvwxyzabc 
# efghijklmnopqrstuvwxyzabcd 
# fghijklmnopqrstuvwxyzabcde 
# ghijklmnopqrstuvwxyzabcdef 
# hijklmnopqrstuvwxyzabcdefg 
# ijklmnopqrstuvwxyzabcdefgh 
# jklmnopqrstuvwxyzabcdefghi 
# klmnopqrstuvwxyzabcdefghij 
# lmnopqrstuvwxyzabcdefghijk 
# mnopqrstuvwxyzabcdefghijkl 
# nopqrstuvwxyzabcdefghijklm 
# opqrstuvwxyzabcdefghijklmn 
# pqrstuvwxyzabcdefghijklmno 
# qrstuvwxyzabcdefghijklmnop 
# rstuvwxyzabcdefghijklmnopq 
# stuvwxyzabcdefghijklmnopqr 
# tuvwxyzabcdefghijklmnopqrs 
# uvwxyzabcdefghijklmnopqrst 
# vwxyzabcdefghijklmnopqrstu 
# wxyzabcdefghijklmnopqrstuv 
# xyzabcdefghijklmnopqrstuvw 
# yzabcdefghijklmnopqrstuvwx 
# zabcdefghijklmnopqrstuvwxy 


# #Or, one could obviously enter 0-9:
# input message: 1234567890
# 1234567890 
# 2345678901 
# 3456789012 
# 4567890123 
# 5678901234 
# 6789012345 
# 7890123456 
# 8901234567 
# 9012345678 
# 0123456789 
# 
# or a already permuted will give you a permuted list of permutations:
#input message: 0192837465
# 0192837465 
# 1928374650 
# 9283746501 
# 2837465019 
# 8374650192 
# 3746501928 
# 7465019283 
# 4650192837 
# 6501928374 
# 5019283746 

#
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
