KEYS = {
    'a': '@',
    'b': 5,
    'e': 3,
    'i': 1,
    'o': 0,
}


def encrypt(letter):
    ltr = str( letter.lower() )
    if ltr in KEYS:
        return str( KEYS[ltr] )
    return ltr


password = input( "Enter your password:" )
new_password = ""
cicle = 0
for letter in password:
    encr_letter = encrypt( letter )
    if cicle % 5 == 0:
        encr_letter = encr_letter.upper()
        new_password += encr_letter
    else:
        new_password += encr_letter
    cicle += 1

print( new_password )
