import rsa
import os
from user import User
from file_context_managers import Open_file
from db_funcs import open_db, insert_into_db
from dotenv import load_dotenv 

if __name__=="__main__":

    load_dotenv()

    original_msg = []
    c = []
    string_encrypted_message = []
    char_spacing_message = []
    ampersand_embedded_message = []
    NUMBER_OF_BITS = 8
    #DB_NAME = "user.db"
    DB_NAME = os.getenv("DB_NAME")
    print(DB_NAME)

    # Setup DB
    open_db(DB_NAME)

    # user = User("Mike", "Jones", "user1", "1234", "mj@mail.com")
    # insert_into_db(DB_NAME, user)

    while True:

        os.system('cls')

        print("***************** Mike's RSA algorithm ***************")

        print("""
        
            1. Generate keys
            2. Encrypt message 
            3. Decrypt message
            4. Encrypt file
            5. Decrypt file
            7. Exit
        
        """)

        user_input = input(">>: ")

        if user_input == '1':
            
            os.system('cls')

            # username = input("Please enter your username: ")
            # password = input("Please enter your password: ")
            # email = input("Please enter your email: ") 

            # user = User(username=username, password=password, email=email)

            # db.insert_user_into_db(user, DB_NAME)

            # Generate the public and private keys
            keys = rsa.rsa_generate_key(NUMBER_OF_BITS)

            #print(f"Keys={keys}")

            public_key = [keys[0], keys[2]]
            private_key = [keys[1], keys[2]]

            print(f"""
            
                [Instructions: Publish the public key so others can send you encrypted messages.
                               Keep the private key secret and store it in a secure location. 
                               You will need the private key when decrypting messages that
                               have been sent to you.]

                               Public key = {public_key}    
                               Private key = {private_key} 
            """)
                
            #print(f"Public key = {public_key}")
            #print(f"Private key = {private_key}")

            e = public_key[0]
            n = public_key[1]

            # Export keys to files
            with Open_file("Public_key.txt", 'w') as f:
                f.write(str(public_key))

            with Open_file("Private_key.txt", 'w') as f:
                f.write(str(private_key))


            print("\n")
            input("Press any key to continue...")

            
        elif user_input == '2':

            os.system('cls')    

            e = int(input("Please enter the e public key: "))
            n = int(input("Please enter the n public key: "))
            

            


            # Convert char to ascii value
            #user_char = input("Please enter a char: ")
            user_string = input("Please enter the string you want to encrypt: ")
            user_string.split() 
            #print(f"user_string = {user_string}")

            for msg in user_string: 
                msg = ord(msg)
                #print(f"msg = {msg}")
                
                c.append(rsa.rsa_encrypt(msg, e, n))


            index = 0
            for msg_element in c:
                string_encrypted_message.append(str(c[index])) 
                index = index + 1

            #print(f"string_encrypted_message = {string_encrypted_message}") 

            # Insert symbol '&' to allow dectection of word boundaries    
            
            for msg_item in string_encrypted_message:
                ampersand_embedded_message.append(msg_item + '&')
    

            #print(f"ampersand embedded message = {ampersand_embedded_message}")

            #  # Join the string version
            ampersand_embedded_message = "".join(ampersand_embedded_message)
            # joined_encrypted_message = "".join(string_encrypted_message)

            print(f"""Encrypted message: 
            
                {ampersand_embedded_message}
                        
            """)
        
            print("\n")
            input("Press any key to continue...")

        elif user_input == '3':

            os.system('cls')    

            d = int(input("Please enter the e private key: "))
            n = int(input("Please enter the n private key: "))

            c = input("Please enter the message you want to decrypt: ")

            # Separate the message into a list 
            c = c.split('&')

            # Remove the final empty index     
            c.pop()

            #print(f"c.split('&') = {c}")  

            # d = private_key[0]
        
            for original_char in c:
                original_msg.append(chr(rsa.rsa_decrypt(int(original_char), d, n)))


            original_text = "".join(original_msg)    
            print(f"original message = {original_text}")   

            print("\n")
            input("Press any key to continue...")


        elif user_input == '7':
            print("Exiting Program...")
            exit() 


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



    
 
     