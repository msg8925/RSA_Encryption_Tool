import rsa

if __name__=="__main__":

    original_msg = []
    c = []

    keys = rsa.rsa_generate_key(61, 53)

    print(f"Keys={keys}")

    public_key = [keys[0], keys[2]]
    private_key = [keys[1], keys[2]]

    print(f"Public key = {public_key}")
    print(f"Private key = {private_key}")

    e = public_key[0]
    n = public_key[1]

    # Convert char to ascii value
    #user_char = input("Please enter a char: ")
    user_string = input("Please enter a string: ")
    user_string.split() 
    print(f"user_string = {user_string}")

    for msg in user_string: 
        msg = ord(msg)
        print(f"msg = {msg}")
        
        c.append(rsa.rsa_encrypt(msg, e, n))

    print(f"Encrypted message: {c}")

    # decrypt data
    

    # d = private_key[0]
    
    # for original_char in original_msg:
    #     original_msg.append(rsa.rsa_decrypt(c, d, n))


    # print(f"original message = {original_msg}")    