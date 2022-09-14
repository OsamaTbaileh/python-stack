
import random
def randInt(min=0, max=100):
    if min>max:
        return False
    else:
        number = random.random()*(max-min) + min
        number = round (num)
        return num
result = randInt(min=50, max=70)
print (result)
