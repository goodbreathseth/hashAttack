import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
import hashlib
import random
import string

     
bitSizes = [8, 10, 16, 20, 24]
collisionAvgs = list()
preImageAvgs = list()
theoreticalAvgs = list()

def collision(n):

    mask = 0
    vals = list()
    for i in range(n):
        mask = mask | 0x1 << i

    for i in range(50):
        mySet = set()
        counter = 0
        while (len(mySet) == counter):
            # Generate random string
            randomStr = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

            # Create hash of n bits from the string
            m = int(hashlib.sha1(randomStr.encode('utf-8')).hexdigest(), 16) & mask

            # Add to set and increment counter
            mySet.add(m)
            counter += 1
        
        vals.append(counter)

    return mean(vals)

def preImage(n):
    mask = 0
    vals = list()
    for i in range(n):
        mask = mask | 0x1 << i


    for i in range(50):
        # Generate random string
        letters = string.ascii_lowercase
        randomStr = ''.join(random.choice(letters) for i in range(10))
        # Create base hash of n bits from the string
        baseHash = int(hashlib.sha1(randomStr.encode('utf-8')).hexdigest(), 16) & mask
        newHash = ""
        counter = 0

        while (baseHash != newHash):
            # Generate random string
            randomStr = ''.join(random.choice(letters) for i in range(10))

            # Create hash of n bits from the string
            newHash = int(hashlib.sha1(randomStr.encode('utf-8')).hexdigest(), 16) & mask

            # Increment counter
            counter += 1
        
        vals.append(counter)

    return mean(vals)

# Call 'collision' on each bit size and store the returned data
# for i in range (len(bitSizes)):
#     collisionAvgs.append(collision(bitSizes[i]))
#     # 2 ^ (n / 2)
#     theoreticalAvgs.append(2 ** (bitSizes[i] / 2))


# Preimage
# Comment this out and uncomment the block above to implement collision
for i in range(len(bitSizes)):
    preImageAvgs.append(preImage(bitSizes[i]))
    # 2 ^ n
    theoreticalAvgs.append(2 ** bitSizes[i])


fig, ax = plt.subplots()
x = np.arange(len(bitSizes))
ax.set_xticklabels(bitSizes)
ax.set_xticks(x)
plt.xlabel('num of bits:\n' + str(bitSizes))
plt.ylabel("num of rounds")
plt.plot(preImageAvgs)
plt.plot(theoreticalAvgs)
plt.show()
