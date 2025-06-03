import sys
import re

def main():
    #greets
    greeting()
    print("")
    attributes = get_information()
    print("")
    #print water result
    print("\033[1;92m=== Hydration Recommendation ===\033[0m")
    if int(attributes["Age"]) < 18:
        print("Water consumption is too complex to calculate due to age, consider asking a healthcare professional.")
    else:
        print("You should drink " + f"\033[1m{water(attributes)}\033[0m" + " liters of water daily.")
        print("Take this with a grain of salt. Remember two factors that can increase your water needs:")
        print(" -High temperatures")
        print(" -Dry climate")
        print("(Reverse logic also applies!)")
    #print bmi result
    print("\033[1;92m=== Body Mass Index (BMI) ===\033[0m")
    if int(attributes["Age"]) < 18:
        print("BMI is too complex to calculate due to age, consider asking a healthcare professional.")
    else:
        print("Your BMI result is " + f"\033[1m{bmi(attributes)}\033[0m" + ".")
    #print bmr result
    print("\033[1;92m=== Basal Metabolic Rate (BMR) ===\033[0m")
    if int(attributes["Age"]) < 18:
        print("BMR is too complex to calculate due to age, consider asking a healthcare professional.")
    elif int(attributes["Age"]) > 65:
        print("BMR is too complex to calculate due to age, consider asking a healthcare professional.")
    else:
        print("Your body needs " + f"\033[1m{bmr(attributes)}\033[0m" + " kcal/day to maintain vital functions.")
    #print tdee result
    print("\033[1;92m=== Total Daily Energy Expenditure (TDEE) ===\033[0m")
    if int(attributes["Age"]) < 18:
        print("TDEE is too complex to calculate due to age, consider asking a healthcare professional.")
    elif int(attributes["Age"]) > 65:
        print("TDEE is too complex to calculate due to age, consider asking a healthcare professional.")
    else:
        print("Your body consumes a total of " + f"\033[1m{tdee(attributes)}\033[0m" + " kcal in a day.")
    #print tdee recommendation
    print("\033[1;92m=== TDEE Recommendation ===\033[0m")
    if int(attributes["Age"]) < 18:
        print("Can not recommend because there is no TDEE.")
    elif int(attributes["Age"]) > 65:
        print("Can not recommend because there is no TDEE.")
    else:
        print("Based on your TDEE, there are three options: ")
        print(" -Maintain weight: " + "eat around " + f"\033[1m{tdee(attributes)}\033[0m" + " kcal a day")
        print(" -Lose weight: " + "eat around " + f"\033[1m{round(tdee(attributes)*0.85, 2)}\033[0m" + " kcal a day")
        print(" -Gain weight: " + "eat around " + f"\033[1m{round(tdee(attributes)*1.15, 2)}\033[0m" + " kcal a day")
    print("")

def greeting():
    print("This program will ask for your age, biological sex, height, weight, and level of physical activity.")
    print("Then, it will give you useful information, including:")
    print(" -Recommended daily water consumption")
    print(" -Body mass index (BMI)")
    print(" -Basal metabolic rate (BMR);")
    print(" -Total daily energy expenditure (TDEE)")
    print(" -Recommendation based on your TDEE")
    print("\033[1mNote: This is only an approximation and there are many limitations regarding age!\033[0m")
    print("\033[1mFor more details, consult a healthcare professional.\033[0m")

def get_information():
    attributes = {}
    attributes["Age"] = input("Age(years, whole number): ").strip()
    if matches := re.search(r"([+|-]{1})?\d+", attributes["Age"]):
        attributes["Age"] = matches.group()
        if int(attributes["Age"]) < 0:
            sys.exit("Can not be a negative number.")
    else:
        sys.exit("Invalid Age.")
    attributes["Biological sex"] = input("Biological sex(male or female): ").strip().lower()
    valid_sex = ["male", "female"]
    if attributes["Biological sex"] not in valid_sex:
        sys.exit("Invalid sex.")
    attributes["Height"] = input("Height(meters): ").strip()
    if matches := re.search(r"([+|-]{1})?\d+([\.|,]{1})?(\d+)?", attributes["Height"]):
        attributes["Height"] = matches.group()
        attributes["Height"] = attributes["Height"].replace(",", ".")
        if float(attributes["Height"]) < 0:
            sys.exit("Can not be a negative number.")
    else:
        sys.exit("Invalid height.")
    attributes["Weight"] = input("Weight(kilograms): ").strip()
    if matches := re.search(r"([+|-]{1})?\d+([\.|,]{1})?(\d+)?", attributes["Weight"]):
        attributes["Weight"] = matches.group()
        attributes["Weight"] = attributes["Weight"].replace(",", ".")
        if float(attributes["Weight"]) < 0:
            sys.exit("Can not be a negative number.")
    else:
        sys.exit("Invalid weight.")
    print("\033[1mActivity level guidelines:\033[0m")
    print(" \033[1m-Sedentary: \033[0m" + "Desk job, no structured exercise")
    print(" \033[1m-Lightly Active: \033[0m" + "Light exercise (e.g., walking) 1-3 days/week")
    print(" \033[1m-Moderately Active: \033[0m" + "Moderate exercise (e.g., running, swimming) 3-5 days/week")
    print(" \033[1m-Very Active: \033[0m" + "Intense exercise 6-7 days/week")
    print(" \033[1m-Extremely Active: \033[0m" + "Physically demanding job + daily intense training")
    attributes["Level of physical activity"] = input("Level of physical activity(sedentary, lightly active, moderately active, very active or extremely active): ").strip().lower()
    valid_level = ["sedentary", "lightly active", "moderately active", "very active", "extremely active"]
    if attributes["Level of physical activity"] not in valid_level:
        sys.exit("Invalid level of physical activity.")
    return attributes

def water(x):
    if x["Level of physical activity"] == "sedentary":
        return round(float(x["Weight"])*0.035, 2)
    elif x["Level of physical activity"] == "lightly active":
        return round(float(x["Weight"])*0.035 + 0.4, 2)
    elif x["Level of physical activity"] == "moderately active":
        return round(float(x["Weight"])*0.035 + 0.65, 2)
    elif x["Level of physical activity"] == "very active":
        return round(float(x["Weight"])*0.035 + 1, 2)
    else:
        return round(float(x["Weight"])*0.035 + 1.35, 2)

def bmi(x):
    bmi = float(x["Weight"])/(float(x["Height"])**2)
    if int(x["Age"]) < 60:
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi <= 24.9:
            return "normal weight"
        elif 25 <= bmi <= 29.9:
            return "overweight"
        else:
            return "obesity"
    else:
        if bmi < 22:
            return "underweight"
        elif 22 <= bmi <= 27:
            return "normal weight"
        else:
            return "overweight"

def bmr(x):
    if x["Biological sex"] == "male":
        return round(10*float(x["Weight"]) + 625*float(x["Height"]) - 5*float(x["Age"]) + 5, 2)
    else:
        return round(10*float(x["Weight"]) + 625*float(x["Height"]) - 5*float(x["Age"]) - 161, 2)

def tdee(x):
    if x["Level of physical activity"] == "sedentary":
        return round(bmr(x)*1.2, 2)
    elif x["Level of physical activity"] == "lightly active":
        return round(bmr(x)*1.375, 2)
    elif x["Level of physical activity"] == "moderately active":
        return round(bmr(x)*1.55, 2)
    elif x["Level of physical activity"] == "very active":
        return round(bmr(x)*1.725, 2)
    else:
        return round(bmr(x)*1.9, 2)

if __name__ == "__main__":
    main()
