"""how to use while"""

from time import sleep

TEMPERATURE = 115
DELAY_TIME = 1
while TEMPERATURE > 90: # first while loop code
    print(TEMPERATURE)
    TEMPERATURE = TEMPERATURE - 1
    sleep(DELAY_TIME) # be cool too fast to like reality
else:
    print("Now")

print('The tea is cool enough.')
