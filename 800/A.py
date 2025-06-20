import sys
input=sys.stdin.readline
print=sys.stdout.write

'''

Luke Skywalker gave Chewbacca an integer number x. Chewbacca isn't good at numbers but he loves inverting digits in them. Inverting digit t means replacing it with digit 9 - t.

Help Chewbacca to transform the initial number x to the minimum possible positive number by inverting some (possibly, zero) digits. The decimal representation of the final number shouldn't start with a zero.
'''

strl=str
intl=int
n=input().strip()
result=''
for i in range(len(n)):
    digit=intl(n[i])
    res=9-digit
    if i==0 and res==0:
        result+=n[i]
    else:
        result+=str(min(res,digit))
    


print(result+'\n')