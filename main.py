import rsa



if __name__=="__main__":
    keys = rsa.rsa_generate_key(61, 53)

    print(f"Keys={keys}")

    public_key = [keys[0], keys[2]]
    private_key = [keys[1], keys[2]]

    print(f"Public key = {public_key}")
    print(f"Private key = {private_key}")

    # encrypt data
    msg = 100
    e = public_key[0]
    n = public_key[1]
    c = rsa.rsa_encrypt(msg, e, n)

    # decrypt data
    original_msg = 0
    d = private_key[0]
    original_msg = rsa.rsa_decrypt(c, d, n)