# Previous input
n1 = int(input("Enter decimal number: "))

# Process
def to_Morse(a):
    # Implementation for converting decimal to Morse code
    morse_code = {
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    result = ""
    for digit in str(a):
        result += morse_code[digit] + " "
    return result

# Post process
print("The Morse representation is:", to_Morse(n1))
