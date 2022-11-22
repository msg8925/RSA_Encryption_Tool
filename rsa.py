import extended_euclids_algorithm

def rsa_generate_key(p, q):
        # -> \
        #Tuple[Tuple[int, int, int], Tuple[int, int]]:
    """Return an RSA key pair generated using primes p and q.

    The return value is a tuple containing two tuples:
      1. The first tuple is the private key, containing (p, q, d).
      2. The second tuple is the public key, containing (n, e).

    Preconditions:
        - p and q are prime
        - p != q
    """
    # Print prime values
    print(f"p = {p}")
    print(f"q = {q}")


    # Compute the product of p and q
    n = p * q
    print(f"n = {n}")

    # Choose e such that gcd(e, phi_n) == 1.
    phi_n = (p - 1) * (q - 1)
    print(f"phi_n = {phi_n}")

    # Since e is chosen randomly, we repeat the random choice
    # until e is coprime to phi_n.
    # e = random.randint(2, phi_n - 1)
    # while math.gcd(e, phi_n) != 1:
    #     e = random.randint(2, phi_n - 1)

    # find e
    # Cycle through numbers for e which are less than the totient/phi
    e = 2
    while e < phi_n:
        # e must be co-prime to phi and
        # smaller than phi.
        if extended_euclids_algorithm.gcd(e, phi_n) == 1:
            break
        else:
            e = e + 1
    

    # Print encryption value
    print(f"e = {e}")




    # Choose d such that e * d % phi_n = 1.
    # Notice that we're using our modular_inverse from our work in the last chapter!
    d = extended_euclids_algorithm.multiplcative_inverse(e, phi_n)
    print(f"d = {d}")

    keys = [e, d, n] 

    #return ((p, q, d), (n, e))
    return keys




# Encryption c = (msg ^ e) % n
def rsa_encrypt(msg, e, n):

    print(f"Message data = {msg}")
 
    # Encryption c = (msg ^ e) % n
    c = pow(msg, e) 
    print(f"c = pow({msg}, {e}) = {c}")
    
    c = c % n
    print(f"Encrypted data = {c}")
 
    return c


# Decryption m = (c ^ d) % n
def rsa_decrypt(c, d, n):

    m = pow(c, d)
    #print(f"m = pow({c}, {d}) = {m}")
    
    m = m % n
    print(f"Original Message Sent = {m}")    

    return m