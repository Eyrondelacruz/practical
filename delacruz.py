def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

def check_vowel_consonant(letter):
    vowels = "AEIOUaeiou"
    if letter in vowels:
        print(f"'{letter}' is a Vowel.")
    else:
        print(f"'{letter}' is a Consonant.")

def check_special_character(char):
    if not char.isalnum():
        print(f"'{char}' is a Special Character.")
    else:
        print(f"'{char}' is NOT a Special Character.")

def identify_input(value):
    for char in value:  
        if char.isdigit():
            check_odd_even(int(char))
        elif char.isalpha():
            check_vowel_consonant(char)
        else:
            check_special_character(char)

def main():
    while True:
        print("\nMenu:")
        print("1. Check if a number is Odd or Even")
        print("2. Check if a letter is Vowel or Consonant")
        print("3. Check if a character is a Special Character")
        print("4. Identify and check each character in your input")
        print("Type 'STOP' to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num = input("Enter a number: ")
            if num.isdigit():
                check_odd_even(int(num))
            else:
                print("Invalid input! Please enter a valid number.")
                
        elif choice == '2':
            letter = input("Enter a letter: ")
            if len(letter) == 1 and letter.isalpha():
                check_vowel_consonant(letter)
            else:
                print("Invalid input! Please enter a single letter.")

        elif choice == '3':
            char = input("Enter a character: ")
            if len(char) == 1:
                check_special_character(char)
            else:
                print("Invalid input! Please enter a single character.")

        elif choice == '4':
            value = input("Enter any characters: ")
            identify_input(value)

        elif choice.lower() == 'stop':
            print("Program Stopped.")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
