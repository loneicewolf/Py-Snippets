i=0
s1="abcdefghijklmnopqrstuvwxyz"
current_alphabet=s1

X=[]
Y=[]
# wField={k: v for k, v in zip(X,Y)}
# wBox  ={k: v for k, v in zip(X,Y)}

wField={k: v for k, v in zip(wBox.items()
                            ,wBox.keys()) }


X+= list(map(ord,current_alphabet))
Y+= list(map(ord,current_alphabet))

wBox={k: v for k, v in zip(X, Y)}
wField={k: v for k, v in zip(wBox.items(),wBox.keys())}

print(wBox,
      wField,
     sep="\n\n")


Y.reverse()



#example output:
# {97: 97, 98: 98, 99: 99, 100: 100, 101: 101, 102: 102, 103: 103, 104: 
# 104, 105: 105, 106: 106, 107: 107, 108: 108, 109: 109, 110: 110, 111: 
# 111, 112: 112, 113: 113, 114: 114, 115: 115, 116: 116, 117: 117, 118:
# 118, 119: 119, 120: 120, 121: 121, 122: 122}
# 
# {(97, 97): 97, (98, 98): 98, (99, 99): 99, (100, 100): 100, (101, 101): 101, (102, 102): 102, (103, 103): 103, (104, 104): 104, (105, 105): 105, (106, 106): 106, (107, 107): 107, (108, 108): 108, (109, 109): 109, (110, 110): 110, (111, 111): 111, (112, 112): 112, (113, 113): 113, (114, 114): 114, (115, 115): 115, (116, 116): 116, (117, 117): 117, (118, 118): 118, (119, 119): 119, (120, 120): 120, (121, 121): 121, (122, 122): 122}