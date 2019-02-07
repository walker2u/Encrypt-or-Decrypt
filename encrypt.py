alphabet = 'abcdefghijklmnopqrstuvwxyz'
key=int(input("Enter your key : "))
new_msg=''
message=input("Enter your message : ")
for character in message:
    position = alphabet.find(character)
    new_pos = (position + key) % 26
    new_char = alphabet[new_pos]
    new_msg += new_char
print("your code is : "+new_msg)
