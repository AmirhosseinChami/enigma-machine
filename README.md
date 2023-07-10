## Enigma Machine

The Enigma Machine was a cipher machine used by the German military to encode and decode secret messages during World War II. This repository is a simulation of the Enigma Machine, including its history, how it works, the structure of the rotors, and the sheet of the everyday state of rotors for German armies.
<div align="center">
  <img src="https://user-images.githubusercontent.com/109967486/228447420-9bd4de03-5b3b-4f6b-81d0-9c1c3f159606.jpg" alt="Enigma machine" />
</div>

## History of Enigma

The Enigma Machine was developed by German engineer Arthur Scherbius in the early 20th century. It was adopted by the German military in the late 1920s and became widely used during World War II. The machine was thought to be unbreakable, but British mathematician Alan Turing and his team at Bletchley Park cracked the code, which gave the Allies a significant advantage in the war effort. 

## How it Works

The Enigma Machine works by using a series of rotors and a plugboard to scramble letters in a message. When a letter is pressed on the keyboard, an electric current runs through the plugboard and enters the first rotor. The first rotor rotates each time a letter is pressed, causing each subsequent rotor to rotate as well. As the message travels through the rotors, the letters are scrambled according to the predetermined settings of the rotors.

## Structure of Rotors

The Enigma Machine had three to five rotors that could be switched out to create different encryption patterns. Each rotor had an array of contacts on both sides, with a different wire connecting each contact on one side with a different contact on the other. The wires were arranged in a way that changed the electrical current's path between the contacts and thus changed the character that resulted. The different rotor combinations allowed for millions of potential encryption patterns.

## Monthly key list for the German Force

The sheet of everyday state of rotors for Germany armies was a classified document that detailed the rotor settings for each day. This sheet was distributed to all German military units and was used to encode and decode messages. The sheet was changed daily, making it very difficult for the Allies to break the code.

## Usage

To use the Enigma Machine simulator, clone the repository and first open `todays_key_list.enigma.py` file in your Python environment and `run` it. this will make a file named `todays_key_list.enigma` which specifies the situation of rotors. then open the `enigma.py` file in your Python environment and run it. and the machine will output the encoded message.

## Contributing

If you have any improvements or suggestions for the Enigma Machine simulator, feel free to fork the repository and create a pull request. Any contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
