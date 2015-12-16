import os,sys
import hashlib

while True:
    n = raw_input().split(" ")
    if n != '':
        a, b = n[0], n[1]
    else:
        break
    s = a + b
    output = []
while True:
    a = raw_input()
    if a != '':
        output.append(count[int(a)])
    else:
        break
for i in output:
    print i