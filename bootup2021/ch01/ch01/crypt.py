import binascii

#range=range
#len=len
#chr=chr
#ord=ord
#zip=zip
#print=print
#input=input
#binascii.hexlify=binascii.hexlify

def func1(output):
 strEmpty=""
 theArr=[3,19,1337,42,9,11,56,2,72,100,81,90,11,23,84,77,192,810,999,239,74]
 comp1="the quick fox jumps over the lazy dog"
 comp2="lorem ipsum dolor sit amet consectetur adipiscing elit"
 for i in range(0,len(output)):
  a4=happens[(theArr[i]*i)%len(happens)]
  a3=comp2[(theArr[i]*i)%len(comp2)]
  a2=''.join(chr(ord(a)^ord(b))for a,b in zip(a4,a3))
  a1=''.join(chr(ord(a)^ord(b))for a,b in zip(a2,output[i]))
  strEmpty+=binascii.hexlify(a1.encode()).decode()
 return strEmpty[::-1]
def output(output):
 print("placeholder")

answer=raw_input("> ")
print(func1(answer))

