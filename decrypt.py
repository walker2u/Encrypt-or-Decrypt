message = input("Enter your message : ")
key = int(input("Enter your key : "))
new_msg = ''
alphabet = "abcdefghijklmnopqrstuvwxyz"
for character in message:
    old_pos = alphabet.find(character)
    new_pos = (old_pos - key) % 26
    char = alphabet[new_pos]
    new_msg += char
print("your mesage is : "+new_msg)
