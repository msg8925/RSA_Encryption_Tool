import rsa

if __name__=="__main__":

    original_msg = []
    c = []
    string_encrypted_message = []


    print("""
    
        1. Generate keys
        2. Encrypt message
        3. Decrypt message
    
    """)

    user_input = input(">>: ")


    if user_input == '1':
        
        keys = rsa.rsa_generate_key(61, 53)

        #print(f"Keys={keys}")

        public_key = [keys[0], keys[2]]
        private_key = [keys[1], keys[2]]

        print(f"Public key = {public_key}")
        print(f"Private key = {private_key}")

        e = public_key[0]
        n = public_key[1]

        
    elif user_input == '2':
        
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
    

    elif user_input == '3':

        d = private_key[0]
    
        for original_char in c:
            original_msg.append(chr(rsa.rsa_decrypt(original_char, d, n)))


        original_text = "".join(original_msg)    
        print(f"original message = {original_text}")   


    else:
        print("Error: Invalid menu item selected.")

    


    ################### Hash encrypted key ############################## 
    # index = 0
    # for msg_element in c:
    #     string_encrypted_message.append(str(c[index])) 
    #     index = index + 1

    # print(f"string_encrypted_message = {string_encrypted_message}")    


    # # Create hashed version
    # joined_encrypted_message = "".join(string_encrypted_message)

    # print(f"joined encrypted message: {joined_encrypted_message}")  

    # hashed_encrypted_message = hash(joined_encrypted_message)
    # print(f"hashed encrypted message: {hashed_encrypted_message}")



    
 
     