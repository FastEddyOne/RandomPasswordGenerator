import secrets
import string

def generate_random_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    character_sets = []
    
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special_chars:
        character_sets.append(string.punctuation)
    
    if not character_sets:
        raise ValueError("At least one character set must be selected.")
    
    all_characters = ''.join(character_sets)
    
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

def generate_passphrase(wordlist, num_words=4):
    if num_words <= 0:
        raise ValueError("Number of words must be positive.")
    
    passphrase = ' '.join(secrets.choice(wordlist) for _ in range(num_words))
    return passphrase

def generate_pronounceable_password(length=12):
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    password = ''

    for i in range(length):
        if i % 2 == 0:
            password += secrets.choice(consonants)
        else:
            password += secrets.choice(vowels)

    return password

def get_user_input(prompt, validator=None):
    while True:
        try:
            user_input = input(prompt)
            if validator and not validator(user_input):
                raise ValueError("Invalid input.")
            return user_input
        except ValueError as e:
            print(f"Error: {e}")

def main():
    while True:
        try:
            print("Password Generation Options:")
            print("1. Generate Random Password")
            print("2. Generate Passphrase")
            print("3. Generate Pronounceable Password")
            print("4. Exit")
            
            choice = get_user_input("Enter your choice (1/2/3/4):", lambda x: x in ['1', '2', '3', '4'])

            if choice == '1':
                length = int(get_user_input("Enter the password length: ", lambda x: x.isdigit() and int(x) > 0))
                password = generate_random_password(length)
            elif choice == '2':
                num_words = int(get_user_input("Enter the number of words in the passphrase: ", lambda x: x.isdigit() and int(x) > 0))
                wordlist = ["apple", "banana", "cherry", "dog", "elephant", "fox", "grape", "horse", "iguana", "jacket"]
                password = generate_passphrase(wordlist, num_words)
            elif choice == '3':
                length = int(get_user_input("Enter the password length: ", lambda x: x.isdigit() and int(x) > 0))
                password = generate_pronounceable_password(length)
            elif choice == '4':
                print("Exiting.")
                break
            else:
                print("Invalid choice.")
                continue

            print("\nGenerated Password:")
            print("************************")
            print(password)
            print("************************\n")
        
        except KeyboardInterrupt:
            print("\nPassword generation aborted.")

if __name__ == "__main__":
    main()
