def temperature_input():
    while True:
        try:
            # 1) Ask what unit the user's current temperature is in
            unit_choice = int(input(
                "What is your current temperature unit?\n"
                "1. Fahrenheit (F)\n"
                "2. Celsius (C)\n"
                "3. Kelvin (K)\n"
                "Enter 1, 2, or 3: "
            ))
            if unit_choice not in (1, 2, 3):
                print("Invalid selection. Please try again.")
                continue

            # 2) Ask for the numeric value, using a unit-appropriate prompt
            prompts = {
                1: "Enter a temperature in Fahrenheit: ",
                2: "Enter a temperature in Celsius: ",
                3: "Enter a temperature in Kelvin: "
            }
            user_temp_input = float(input(prompts[unit_choice]))

            # 3) Validate (below absolute zero is not allowed)
            if unit_choice == 1:
                # Absolute zero in F = -459.67, cap at 10 trillion degrees
                if user_temp_input < -459.67 or user_temp_input >= 10_000_000_000_000:
                    print("Woah! That temperature is impossible! Please try again.")
                    continue
            elif unit_choice == 2:
                # Absolute zero in C = -273.15; cap at 5.5 trillion degrees
                if user_temp_input < -273.15 or user_temp_input >= 5_500_000_000_000:
                    print("Woah! That temperature is impossible! Please try again.")
                    continue
            else:  # Kelvin
                # Absolute zero in K = 0
                if user_temp_input < 0:
                    print("Woah! That temperature is impossible! Please try again.")
                    continue

            # If we got here, both inputs are valid return the temperature number
            return user_temp_input, unit_choice

        except ValueError:
            print("Invalid value. Please try again.")

def conversion_input(user_unit_input):
    units = {1: "Fahrenheit", 2: "Celsius", 3: "Kelvin"}
    while True:
        try:
            user_input = int(input(
                f"What would you like to convert to?\n"
                "1. Fahrenheit (F)\n"
                "2. Celsius (C)\n"
                "3. Kelvin (K)\n"
                "Enter 1, 2, or 3: "
            ))
            if user_input not in (1, 2, 3):
                print("Invalid selection. Please enter 1, 2, or 3.")
                continue

            # Doesn't allow conversion of the same unit
            if user_input == user_unit_input:
                print(f"You are already using {units[user_unit_input]}. Please choose a different unit.")
                continue
            
            # If we got here, conversion choice is returned
            return user_input
        
        except ValueError:
            print("Invalid value. Please try again.")

def converter(user_temp_input, user_unit_input, user_conversion_choice):
    # Fahrenheit conversions
    if user_unit_input == 1:
        # Celsius
        if user_conversion_choice == 2:
            result = (user_temp_input - 32) * 0.5555
        # Kelvin
        if user_conversion_choice == 3:
            result = ((user_temp_input - 32) * 0.5555) + 273.15

    # Celsius conversions
    if user_unit_input == 2:
        # Fahrenheit
        if user_conversion_choice == 1:
            result = (user_temp_input * 1.8) + 32
        # Kelvin
        if user_conversion_choice == 3:
            result = user_temp_input + 273.15

    # Kelvin conversions
    if user_unit_input == 3:
        # Fahrenheit
        if user_conversion_choice == 1:
            result = ((user_temp_input - 273.15) * 1.8) + 32
        # Celsius
        if user_conversion_choice == 2:
            result = user_temp_input - 273.15

    # Rounds result to 2 decimal places and returns
    return round(result, 2)

def main():
    print("Welcome to the temperature converter\n")

    # Get user's temperature
    try:
        user_temp_input, user_unit_input = temperature_input()
    except:
        print("An error has occured with: temperature_input")
        return
    
    # Get conversion input
    try:
        user_conversion_choice = conversion_input(user_unit_input)
    except:
        print("An error has occured with: conversion_input")
    try:
        # Convert temps
        result = converter(user_temp_input, user_unit_input, user_conversion_choice)
        
        units = {1: "F", 2: "C", 3: "K"}

        # Print finalized result
        print(f"{user_temp_input}°{units[user_unit_input]} is equal to {result}°{units[user_conversion_choice]}")

    except:
        print("An error has occured with: converter")
        return
    
    # Loop for asking if the user wants to do another conversion
    while True:
        user_loop_choice = input("\nWould you like to do another conversion? (y/n) ").strip().lower()
        if user_loop_choice == "y":
            print()
            return main()  # restart main
        elif user_loop_choice == "n":
            return
        else:
            print("Invalid value. Please try again.")

if __name__ == "__main__":
    main()