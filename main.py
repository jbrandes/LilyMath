import random
import string 
import time

def ran_gen(size, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for x in range(1000))
 

max_time = int(input('Enter the amount of seconds you want to run this: '))
start_time = time.time()  # remember when we started
while (time.time() - start_time) < max_time:
    print(list(ran_gen(10, "abcdefgABCDEFG")))
