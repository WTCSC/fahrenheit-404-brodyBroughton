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
            user_input = float(input(prompts[unit_choice]))

            # 3) Validate physical bounds (below absolute zero is not allowed)
            if unit_choice == 1:
                # Absolute zero in F = -459.67; also cap at ~1e13 F to catch typos
                if user_input < -459.67 or user_input >= 10_000_000_000_000:
                    print("Woah! That temperature is impossible! Please try again.")
                    continue
            elif unit_choice == 2:
                # Absolute zero in C = -273.15; cap at ~5.5e12 C
                if user_input < -273.15 or user_input >= 5_500_000_000_000:
                    print("Woah! That temperature is impossible! Please try again.")
                    continue
            else:  # Kelvin
                # Absolute zero in K = 0
                if user_input < 0:
                    print("Woah! That temperature is impossible! Please try again.")
                    continue

            # If we got here, both inputs are valid; return the numeric temperature
            return user_input

        except ValueError:
            print("Invalid value. Please try again.")


def converter(conversion, temperature):
    # F to C
    if conversion == 1:
        result = (temperature - 32) * 0.5555

    # C to F
    else:
        result = (temperature * 1.8) + 32
    
    return result

def main():
    print("Welcome to the temperature converter\n")
    while True:

        try:
            user_temp = temperature_input(user_conversion_choice)
        except:
            print("An error has occured with: user_conversion_choice")
            return

        try:
            result = converter(user_conversion_choice, user_temp)
        except:
            print("An error has occured with: converter")
            return

        if user_conversion_choice == 1:
            print(f"{user_temp}°F is equivalent to {result}°C.")
        else: 
            print(f"{user_temp}°C is equivalent to {result}°F.")

        
        while True:
            try:
                user_loop_choice = input("\nWould you like to do another conversion? (y/n)").lower()
                if user_loop_choice == "y":
                    break
                elif user_loop_choice == "n":
                    return
                else: 
                    print("Invalid value. Please try again")
            except ValueError:
                print("An error has occured with: display_output")

if __name__ == "__main__":
    main()