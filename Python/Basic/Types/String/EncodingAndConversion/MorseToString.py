# Previous input
a = input("Enter morse code (words separated by ' / ', chars by space): ")

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

def from_Morse_String(a):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = a.strip().split(" / ")
    decoded_words = []
    for word in words:
        chars = word.split()
        decoded_chars = [reverse_dict.get(c, "") for c in chars]
        decoded_words.append("".join(decoded_chars))
    return " ".join(decoded_words)

# Post process
print("Decoded string from Morse:", from_Morse_String(a))
