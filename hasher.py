import hashlib

data = input("Enter the string to hash: ")
encoded_data = data.encode('utf-8')
hash_object = hashlib.md5(encoded_data.strip())
hash_value = hash_object.hexdigest()
print(hash_value)

# you can hash whatever you want!


