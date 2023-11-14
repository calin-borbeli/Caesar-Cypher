# Caesar cipher.
text = input("Enter your message: ")
invalid_shift = True
while invalid_shift:
    shift = input("Enter a shift value (an integer number from the range 1..25): ")
    if shift.isdigit() and int(shift) in range(1, 26):
        invalid_shift = False

cipher = ""
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + int(shift)
    if char.islower():
        if code > ord("z"):
            code = code - 26
    else:
        if code > ord("Z"):
            code = code - 26
    cipher += chr(code)

print(cipher)
