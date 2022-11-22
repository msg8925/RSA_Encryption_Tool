import math
from Crypto.Util import number

###################################################
#  
#   Desc: Find the greatest common divisor 
#         (Highest common factor) using Euclid's 
#         algorithm
#
###################################################

# Returns greatest common divisor (a.k.a Highest common factor) of a and b
def gcd(A, B):

    r=0  
    a=0
    b=0

    if A > B: 
        a = A
        b = B
    else:
        a = B
        b = A
        

    # Euclid's algorithm (Find GCF/HCF of two numbers 'A' and 'B')
    while 1:
        
        # Show iterations of GCD algorithm
        # printf("a: %d, b: %d, r: %d\n", a, b, r);    

        if b == 0:
            return a
        
        
        r = a % b    

        # Shift B into A and R into B for the next iteration  
        a = b
        b = r   


###################################################
#  
#   Desc: Finds the multiplicative inverse using the
#         extended Euclid's algorithm    
#
###################################################
def multiplcative_inverse(A, B):

    a=0
    b=0
    r=0
    T=0
    T1=0
    T2=1
    Q=0

    # Ensure that a's value is always larger than a's value
    if A > B:
        a = A
        b = B
    
    else:
        a = B
        b = A
        

    # Euclid's algorithm (Find GCF/HCF of two numbers 'A' and 'B')
    while 1:
        
        # Show iterations of EEA algorithm
        #print(f"Q: {Q}, a: {a}, b: {b}, r: {r}, T1: {T1}, T2: {T2}, T: {T}", Q, a, b, r, T1, T2, T)    

        if b == 0:
            if T1 < 0:
                T1 = T1 + T2
            
            #print(f"T1={T1}")
            return T1
        

        # r = a mod b
        # a % b;
        r = a % b
        Q = math.floor(a / b)

        # T = T1 - (T2 * Q) 
        T = T1 - (T2 * Q)

        # Shift B into A and R into B for the next iteration  
        a = b
        b = r   

        # Shift T2 into T1 and shift T into T2
        T1 = T2
        T2 = T  


###################################################
#  
#   Desc: Generates a random prime number between     
#         two given limits
#
###################################################    
def generate_random_prime():

    return number.getPrime(8)

    # while True:
    #     random_prime_number = random.randrange(101, 173)
    #     if (random_prime_number % 2) == 0:
    #         continue
    #     else:
    #         return random_prime_number