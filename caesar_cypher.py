# Caesar cypher.
print("Encrypting message")
text = input("Enter your message: ")
invalid_shift = True
while invalid_shift:
    shift = input("Enter a shift value (an integer number from the range 1..25): ")
    if shift.isdigit() and int(shift) in range(1, 26):
        invalid_shift = False

cypher = ""
for char in text:
    if not char.isalpha():
        cypher += char
        continue
    code = ord(char) + int(shift)
    if char.islower():
        if code > ord("z"):
            code = code - 26
    else:
        if code > ord("Z"):
            code = code - 26
    cypher += chr(code)

print(cypher)

# Caesar cypher - decrypting a message.
print("Decrypting message")
# cypher = input("Enter your cryptogram: ")
text = ""
for char in cypher:
    if not char.isalpha():
        text += char
        continue
    code = ord(char) - int(shift)
    if char.islower():
        if code < ord("a"):
            code = code + 26
    else:
        if code < ord("A"):
            code = code + 26
    text += chr(code)

print(text)
