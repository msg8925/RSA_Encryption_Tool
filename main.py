import rsa

if __name__=="__main__":

    original_msg = []
    c = []
    string_encrypted_message = []
    char_spacing_message = []


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

        e = int(input("Please enter the e public key: "))
        n = int(input("Please enter the n public key: "))
        
        # Convert char to ascii value
        #user_char = input("Please enter a char: ")
        user_string = input("Please enter the string you want to encrypt: ")
        user_string.split() 
        print(f"user_string = {user_string}")

        for msg in user_string: 
            msg = ord(msg)
            print(f"msg = {msg}")
            
            c.append(rsa.rsa_encrypt(msg, e, n))


        index = 0
        for msg_element in c:
            string_encrypted_message.append(str(c[index])) 
            index = index + 1

        print(f"string_encrypted_message = {string_encrypted_message}") 

        # Insert symbol '&' to allow dectection of word boundaries    
        index = 0
        for msg_item in string_encrypted_message:
            if index == (2*index -1):
                char_spacing_message.append('&')
            else:
                char_spacing_message.append(msg_item)
                 

            index = index + 1          


        #  # Join the string version
        char_spacing_message = "".join(char_spacing_message)
        # joined_encrypted_message = "".join(string_encrypted_message)

        print(f"Encrypted message: {char_spacing_message}")
    

    elif user_input == '3':

        d = int(input("Please enter the e private key: "))
        n = int(input("Please enter the n private key: "))

        c = input("Please enter the message you want to decrypt: ")

        #c =  

        # d = private_key[0]
    
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



    
 
     