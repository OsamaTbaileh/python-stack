
import random
def randInt(min=0, max=100):
    if min>max:
        return False
    else:
        num = random.random()*(max-min) + min
        num = round (num)
        return number
result = randInt(min=50, max=70)
print (result)
