import pickle
alphabet = 'abcdefghijklmnopqrstuvwxyz'

key_list = open('todays_key_list.enigma', 'rb')
rotor1, rotor2, rotor3 = pickle.load(key_list)
key_list.close()
print(rotor1, rotor2, rotor3)

def reflector(letter):
    return alphabet[len(alphabet)-alphabet.find(letter)-1]


def enigma_character(letter):
    char1 = rotor1[alphabet.find(letter)]
    char2 = rotor2[alphabet.find(char1)]
    char3 = rotor3[alphabet.find(char2)]

    reflected = reflector(char3)

    char3 = alphabet[rotor3.find(reflected)]
    char2 = alphabet[rotor2.find(char3)]
    char1 = alphabet[rotor1.find(char2)]

    return char1


def rotate_rotors():
    global rotor1, rotor2, rotor3
    rotor1 = rotor1[1:]+rotor1[0]
    if state % 26:
        rotor2 = rotor2[1:] + rotor2[0]
    if state % (26*26):
        rotor3 = rotor3[1:] + rotor3[0]

plain = input('Enter your text : ')
cipher = ''
state = 0
for letter in plain:
    if letter == ' ':
        cipher += ' '
    else:
        state +=1
        cipher += enigma_character(letter)
        rotate_rotors()
print(cipher)
