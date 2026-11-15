# Previous input
n1 = input("Enter Morse code: ")

# Process
def from_Morse_Decimal(a):
    morse_values = {
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
    }
    total = ""
    for code in a.split():
        total += morse_values.get(code, '')
    return int(total) if total else 0

# Post process
print("The decimal representation is:", from_Morse_Decimal(n1))
