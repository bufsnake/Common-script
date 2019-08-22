from collections import deque

alpha = deque("abcdefghijklmnopqrstuvwxyz") 
t1 = deque([8, 25, 17, 23, 7, 22, 1, 16, 6, 9, 21, 0, 15, 5, 10, 18, 2, 24, 4, 11, 3, 14, 19, 12, 20, 13]) 
t2 = deque([7, 14, 16, 21, 4, 24, 25, 20, 5, 15, 9, 17, 6, 13, 3, 18, 12, 10, 19, 0, 22, 2, 11, 23, 1, 8])

ss = 'wigwrkaugala'

for _ in range(2): 
    t1.append(t1.popleft()) 
for _ in range(3): 
    t2.append(t2.popleft()) 
print(t1) 
print(t2)

def dec(s): 
    i = t2[(ord(s) - ord('a'))] 
    print(ord(s)-ord('a'))
    print(i)
    i = t1[(i)]
    print(i)
    print(alpha[i], end='') 
    t1.append(t1.popleft()) 
    alpha.append(alpha.popleft())


for s in ss: 
    dec(s)
