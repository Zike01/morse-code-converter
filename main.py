from morse_converter import MorseConverter

print("Welcome to the Text to Morse Code Converter!")


def start():
    # Create converter object from MorseConverter Class.
    converter = MorseConverter()

    text_input = input("Please Provide a String Input: ")
    morse_output = converter.translate(text_input)
    print(f"Output: {morse_output}")

    continue_app = input("Do you want to continue? Type 'Y' or 'N': ")

    if continue_app.lower() == "n":
        print("Goodbye!")
        return
    else:
        start()


start()
