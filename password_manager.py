import pyperclip;

FILE_NAME = "password.txt"

# Save password function
def save_password():
    website = input("Website name: ")
    password = input("Pasword: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{website}||{password}\n")
        print("your password saved successfully!")

# Get password function
def get_password():
    print("Get your password")
    website = input("Website name: ")
    with open(FILE_NAME, "r") as f:
        for line in f:
            if website in line:
                pyperclip.copy(line.strip().split("||")[1])
                print("Your password copied to clipboard.")
                


        else: 
            print("Website not found")    

# Start of the application
def main():
    while True:
        print('1. Save Password\n2. Get Password\n3. Exit')
        user_input = input("Enter your option in number.")

        if user_input == "1":
            save_password()

        if user_input == "2":
            get_password()

        if user_input == "3":
            print("Exiting.....")
            break;

main();