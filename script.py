def conversion_choice():
    while True:
        try: 
            user_input = int(input("Enter 1 or 2 for conversion type:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n"))
            if user_input not in (1, 2):
                continue
        except ValueError:
            print("Invalid value. Please try again")
        else:
            return user_input


def temperature_input(conversion_choice):
    while True:
        try:
            # F to C
            if conversion_choice == 1:
                user_input = float(input("Enter a temperature in Fahrenheit: "))
                # Not allowed to do below absolute zero
                if user_input <= -459.67:
                    print("Woah! It must be really cold... impossibly cold. Please try again")
                    continue
            # C to F
            else:
                user_input = float(input("Enter a temperature in Celsius: "))
                # Not allowed to do below absolute zero
                if user_input <= -273.15:
                    print("Woah! It must be really cold... impossibly cold. Please try again")
                    continue
        except ValueError:
            print("Invalid value. Please try again")
        else:
            return user_input

def converter(conversion, temperature):
    # F to C
    if conversion == 1:
        result = (temperature - 32) * 0.5555

    # C to F
    else:
        result = (temperature * 1.8) + 32
    
    return result


def main():
    print("Welcome to the temperature converter.")

    try:
        user_conversion_choice = conversion_choice()
    except:
        print("An error has occured with: conversion_choice")
        return

    try:
        user_temp = temperature_input(user_conversion_choice)
    except:
        print("An error has occured with: user_conversion_choice")
        return
        
    try:
        result = converter(user_conversion_choice, user_temp)
        print(result)
    except:
        print("An error has occured with: converter")
        return

if __name__ == "__main__":
    result = main()