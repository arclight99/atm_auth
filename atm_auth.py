"""
This program prompts for valid ATM pin code
"""
def main():

    enter_pin = input("Please enter your 4-digit PIN number, you have three attempts: ")
    valid_pin = "1234"
    counter = 1

    if valid_pin == enter_pin:
        print("Thank You, PIN accepted.")
        exit()

    while type(enter_pin) != int:

        if enter_pin == valid_pin:
            print("Thank You, PIN accepted.")
            exit()
        else:
            enter_pin = input("Invalid PIN number, please try again: ")
            counter = counter + 1

        if counter == 3 and enter_pin != valid_pin:
                print("I'm sorry that has been 3 unsuccessful attempts. Goodbye.")
                exit()

if __name__ == '__main__':
    main()