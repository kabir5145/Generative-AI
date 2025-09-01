def bmi_calculator():
    print("=== BMI Calculator ===")
    user_type = input("Are you an Adult (M/F) or a Child (C)? Enter M/F/C: ").strip().upper()

    # Taking inputs
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = weight / (height ** 2)
    print(f"\nYour BMI is: {bmi:.2f}")

    # Adult men/women categories
    if user_type in ["M", "F"]:
        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    # Child categories (simplified without growth charts)
    elif user_type == "C":
        age = int(input("Enter age of the child (in years, 2–19): "))
        if age < 2 or age > 19:
            print("BMI categories for children are valid only for ages 2–19.")
            return

        if bmi < 14:
            print("Category: Underweight (approx.)")
        elif 14 <= bmi < 18:
            print("Category: Healthy weight (approx.)")
        elif 18 <= bmi < 21:
            print("Category: Overweight (approx.)")
        else:
            print("Category: Obese (approx.)")

    else:
        print("Invalid input. Please enter M (Male), F (Female), or C (Child).")


# Run the program
bmi_calculator()
