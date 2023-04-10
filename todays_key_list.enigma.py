import pickle
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

rotor1 = list(alphabet)
random.shuffle(rotor1)
rotor1 = ''.join(rotor1)

rotor2 = list(alphabet)
random.shuffle(rotor2)
rotor2 = ''.join(rotor2)

rotor3 = list(alphabet)
random.shuffle(rotor3)
rotor3 = ''.join(rotor3)

key_list = open('todays_key_list.enigma', 'wb')
pickle.dump((rotor1, rotor2, rotor3), key_list)
key_list.close()