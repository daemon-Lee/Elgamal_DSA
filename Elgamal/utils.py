import random  

# This function is called 
# for all k trials. It returns 
# false if n is composite and  
# returns false if n is 
# probably prime. d is an odd  
# number such that d*2<sup>r</sup> = n-1 
# for some r >= 1 
def miillerTest(d, n): 
      
    # Pick a random number in [2..n-2] 
    # Corner cases make sure that n > 4 
    a = 2 + random.randint(1, n - 4)

    # Compute a^d % n 
    x = pow(a, d, n)
  
    if (x == 1 or x == n - 1): 
        return True
  
    # Keep squaring x while one  
    # of the following doesn't  
    # happen 
    # (i) d does not reach n-1 
    # (ii) (x^2) % n is not 1 
    # (iii) (x^2) % n is not n-1 
    while (d != n - 1): 
        x = (x * x) % n
        d *= 2
  
        if (x == 1): 
            return False
        if (x == n - 1): 
            return True
  
    # Return composite 
    return False
  
# It returns false if n is  
# composite and returns true if n 
# is probably prime. k is an  
# input parameter that determines 
# accuracy level. Higher value of  
# k indicates more accuracy. 
def isPrime(n, k=4):
      
    # Corner cases 
    if (n <= 1 or n == 4): 
        return False
    if (n <= 3): 
        return True
  
    # Find r such that n =  
    # 2^d * r + 1 for some r >= 1 
    d = n - 1
    while (d % 2 == 0): 
        d //= 2
  
    # Iterate given nber of 'k' times 
    for _ in range(k): 
        if (miillerTest(d, n) == False): 
            return False
  
    return True

def isPrimitiveRoot(number, prime, factors):
    phi = prime - 1
    for it in factors:
        if (pow(number, phi // it, prime) == 1):  
            return False
    return True

def loadKeys(filename='keys.txt'):
    keys = {}
    with open(filename, 'r') as stored_keys:
        keys = eval(stored_keys.readline())
    return keys

def saveKeys(keys, filename='keys.txt'):
    with open(filename, 'w+') as stored_keys:
        stored_keys.write(str(keys))

def gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x

def egcd(a, b):
    s,t = 0,1 # init s0, t0 (sb, tb)
    u,v = 1,0 # init s1, t1 (sa, ta)
    while a != 0: 
        q = b//a

        # Euclide (gcd)
        r = b%a
        a,b = r,a
        sr, tr = s-u*q, t-v*q # sr,st = s%u, t%v 
        s,t, u,v = u,v, sr,tr # increase index

    gcd = b
    return gcd, s, t

def modinv(a, m): 
	gcd, x, _ = egcd(a, m) 
	if gcd != 1: 
		return None # modular inverse does not exist 
	else: 
		return x % m


if __name__ == "__main__":
    number, prime = 11, 19
    factors = (3,3)
    print(isPrimitiveRoot(number, prime, factors))
