# Previous input
a = input("Enter the string: ")

# Process
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", ",": "--..--", ".": ".-.-.-", "?": "..--..",
    "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-"
}

def to_Morse_String(a):
    words = a.upper().split(" ")
    morse_words = []
    for word in words:
        morse_chars = [MORSE_CODE_DICT[c] for c in word if c in MORSE_CODE_DICT]
        if morse_chars:
            morse_words.append(" ".join(morse_chars))
    return " / ".join(morse_words)

# Post process
print("Morse code:", to_Morse_String(a))
