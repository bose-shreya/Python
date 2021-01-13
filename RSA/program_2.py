# Shreya Bose and Sarayu Das
f = open('primes.txt','r')
text = f.read()

#p and q value should be where (p -1)/2 and q-1/2 should be a prime.
#co-prime means should not divide or factor by phi_mod
#print(number)
for a in text:
    a = text.split("\n")
    for b in a[0]:
        b = a[0].split(" ")
        p = int(b[0])
        q = int(b[1])
        e = int(b[2])
        size = int(b[3])
#print('hello')
print("P: %d" % (p))
print("Q: %d" % (q))
print("ENCRYPTION E: %d" % (e))
mod = p * q
print("MODULUS: %d" % (mod))
phi_mod = (p - 1) * (q - 1)
print("PHIOFMODULUS: %d" % (phi_mod))
print("BLOCKSIZE: %d" % (size))
def gcdofe(e,phi_mod):
     while(phi_mod!=0):
        e,phi_mod=phi_mod,e%phi_mod
            
#e =  e % phi_mod   #( e is public)
for d in range(1, phi_mod):
    if((e * d) % phi_mod == 1):
        #print('we are here')
        de = d #(private)
print("DECRYPTION D:%d" % (de))
alph = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,'k': 10,'l': 11,'m': 12,'n': 13,'o': 14,
        'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u': 20,'v': 21,'w': 22,'x': 23,'y':24,'z': 25,' ': 26}
#print(alph[25])

message = 'this is the message to be sent'
print('\n')
print('MESSAGE:',message)
bytes = []
#number of complete bytes
#num_of_bytes = int(len(message) / 8)
#number of excess bits
#if (len(message) % 8) > 0:
    #if excess bits, need to add +1 byte to account for it
    #num_of_bytes += 1
#print(num_of_bytes)
i = 0
# if thinking about different lengths of messages, change j
j = size
while True:
    #if j goes past the array, it brings it back
    if (j >= len(message)):
        j = len(message)
        bytes.append(message[i:j])
        break
    #slices from index i to j, returns a string which is being added to bytes array
    bytes.append(message[i:j])
    #print(bytes)
    i += size
    j += size

products = []
for byte in bytes:
    current_product = 1
    for letter in byte:
        if byte.index(letter) == 0:
            current_product = alph[letter]
        else:
            alphaNum = alph[letter]
            current_product = (256 * current_product) + alphaNum
                
        #print(current_product)
    products.append(current_product)
#print(products)
decrypt_str = ''
    
print('\n')

for integers in range(0,len(products)):
    encrypted = products[integers]**e % mod
    print("ENCRYPTED: %d" % (encrypted))
    decrypted = encrypted**de % mod
    print("DECRYPTED: %d"  % (decrypted))
    decrypt_str += bytes[integers]
    print("DECRYPTED MESSAGE: " + bytes[integers])
    print('\n')

print("DECRYPT MSG: " + decrypt_str)
