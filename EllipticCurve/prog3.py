import math

"""
f = open('xprime00031.txt')
prime = f.read()
prime = int(prime)

s = open('zz00031out.txt')
text2 = s.read()

# for s in text2.split():
#        print(s)

res = [int(i) for i in text2.split() if i.isdigit()]
# print(res)
a = int(res[0])
b = int(res[1])

"""

a = 1
b = 3
cycles = 41
prime = 31
x = 1
y = 6
z = 1


co = [x,y,z]

List3 = []
List3.append(co)
print(List3)


# doubling
def doubling():
    A = y**2 % prime
    B = (4*x*A) % prime
    C = (8*(A**2)) % prime
    D = (3*(x**2) + a*(z**4)) % prime
    xjacob = (D**2 - (2 * B)) % prime
    yjacob = ((D * (B - xjacob)) - C) % prime
    zjacob = (2*y*z) % prime

    List = [xjacob, yjacob, zjacob]
    List3.extend(List)
    return List


# adding
def adding():
    w = doubling()
    A1 = (w[2]**2) % prime
    B1 = (w[2]*A1) % prime
    C1 = (x*A1) % prime
    D1 = (y*B1) % prime
    E1 = (C1 - w[0]) % prime
    F1 = (D1 - w[1]) % prime
    G1 = (E1**2) % prime
    H1 = (G1*E1) % prime
    I1 = (w[0] * G1) % prime
    xadd = ((F1**2) - H1 - (2*I1)) % prime
    yadd = ((F1 * (I1-xadd)) - (w[1]*H1)) % prime
    zadd = (w[2]*E1) % prime

    List2 = [xadd, yadd, zadd]
    List3.extend(List2)
    return List2


# kinda like main method






