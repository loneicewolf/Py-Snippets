# -------------------------------------------------------------- #

# outputs a - z #

[chr(i) for i in range(ord('a'),ord('z')+1)]

['a',
 'b',
 ...
 'y',
 'z']
# -------------------------------------------------------------- #




# -------------------------------------------------------------- #

# outputs ord(a - z) #
[(i) for i in range(ord('a'),ord('z')+1)]

[97,
 98,
...
 121,
 122]
# -------------------------------------------------------------- #

# version 2 #

[((i)-65,chr(i))  for i in range(65,91)]

# output

[(0, 'A'),
 (1, 'B'),
 ...
 (24, 'Y'),
 (25, 'Z')]








az="abcdefghijklmnopqrstuvwxyz"
za=az[::-1]
for j in enumerate(zip(az,za)):
    print(j)

# outputs # 
(24, ('y', 'b'))
(25, ('z', 'a'))
(2, ('c', 'x'))
...
(0, ('a', 'z'))
(1, ('b', 'y'))




message="hello world"
for l in enumerate(message):
    print(l[0],l[1])

# outputs #
# 0 h, 1 e, 2 l, ...





