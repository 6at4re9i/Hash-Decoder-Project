from string import digits, punctuation, ascii_letters
import itertools
import hashlib

print("*** Hello! I will try to dehash your password! ***")

password_length = input("Let's choose the length of your password!\n"               # this will enter the length                 
                        "Write length in format 3-5, 2-4: ")
password_length = [int(item) for item in password_length.split("-")]

possible_symbols = ''
choose = int(input("What kind of symbols did your password have?\n"                 # this will enter possible symbols
                   "1 - Only numbers;\n"
                   "2 - Only letters;\n"
                   "3 - Numbers and letters;\n"
                   "4 - Numbers, letters and punctuation\n"
                   "Choose: "))
if choose == 1:
    possible_symbols = digits
elif choose == 2:
    possible_symbols = ascii_letters
elif choose == 3:
    possible_symbols = digits + ascii_letters
elif choose == 4:
    possible_symbols = digits + ascii_letters + punctuation

hash_str = input("Enter the hashed password: ")

for password_length in range(password_length[0], password_length[1] + 1):            # this loop will generate passwords within the selected length
    for password in itertools.product(possible_symbols, repeat=password_length):     # with itertools we are joining selected symbols
        password = "".join(password)                                                 # to our combinations
        encoded_pass = password.encode('utf-8')                                      # then we are encoding created password in 'utf-8' format
        hashed_pass = hashlib.md5(encoded_pass.strip())                              # then we are hashing our encoded password by md5(but you can choose another)
        digesting = hashed_pass.hexdigest()                                          # finally we got a hashed password
        if digesting == hash_str:                                                    # then we are compare it with entered hash-code
            print(f"Your password is: {password}")                                   # if we find equal values, then enter the password and stop the selection
            break
        else:                                                                        # i add this strings only to be sure that the code is brute force
            print(password)                                                          # and so i can see at what stage brute forcing is

# you can try to write combinations in txt file, but remember: you'll need a looooooooot of memory
# but if you are really brave, you need to create a list in which you will write your combinations
# and then open a blank txt and create a loop, that will write [i] members of list + " "
# if you write down the combinations, then in the future you can rewrite the code
# so that it compares the hash with the combinations in the list
