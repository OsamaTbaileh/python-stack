# 1-Basic - Print all integers from 0 to 150.
for x in range (0, 151, 1):
    print(x)


# 2-Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range (5, 1000):
    if y%5==0 :
        print(y)


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for z in range (1,101):
    if z%5==0 and z%10!=0:
        print("Coding")
    elif z%10==0:
        print("Coding Dojo")
    else:
        print (z)


# 3-Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for k in range(0,500000):
    if k%2!=0:
        sum= sum + k
print (sum)


# 4-Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for j in range (2018, -1, -1):
    if j%4==0:
        print(j)


# 5-Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=2
highNum=9
mult=3
for v in range (lowNum, highNum+1):
    if v%mult==0:
        print (v)