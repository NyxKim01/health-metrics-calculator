# Prologue
    Description
        Water Consumption
        Body Mass Index (BMI)
        Basal Metabolic Rate (BMR)
        Total Daily Energy Expenditure (TDEE)
        TDEE Recommendation
    Requirements
    Usage
    Disclaimer

## Description
This program will calculate health metrics, such as body mass index (BMI), basal metabolic rate (BMR), and total daily energy expenditure (TDEE).
Furthermore, it will recommend daily water consumption and explain how to use your TDEE to maintain, lose, or gain weight.
In the next sections, more complete descriptions of each functionality will be covered, including the calculations used and their limitations.

### Water Consumption
**Calculation method:**
Base = weight(kg) x 0.035  
Sedentary: base
Lightly Active: base + 0.4L
Moderately Active: base + 0.65L
Very Active: base + 1L
Extremely Active: base + 1.35L
*Observation:*
Using 35 mL per kg is an academic consensus, but the level of activity is not. Despite that, the activity-based adjustments draw from proven studies
showing that 1 hour of exercise demands an additional 500 mL. Therefore, activity-based adjustments are approximations derived from these studies.
Moreover, other methods are used for children (under 18 years), which are not considered here.
### Body Mass Index (BMI)
**Calculation method:**
BMI = weight(kg) / height(m)^2
Then, using the BMI result for individuals aged 18 to 59:
    < 18.5: underweight
    18.5-24.9: normal
    25-29.9: overweight
    ≥ 30: obesity
For individuals aged 60 and older:
    < 22: underweight
    22-27: normal
    > 27: obesity
*Observation:*
People under 18 years utilize growth curves and BMI for assessment, but this program does not support that. Additionally, obesity has different scales
not addressed here.
### Basal Metabolic Rate (BMR)
**Calculation method:**
Uses Mifflin-St Jeor Equation:
Male: (10 x weight(kg)) + (6.25 x height(cm)) - (5 x age(years)) + 5
Female: (10 x weight(kg)) + (6.25 x height(cm)) - (5 x age(years)) - 161
*Observation:*
Mifflin-St Jeor Equation is best suited for adults, so the program only calculates between 18 and 65 years.
### Total Daily Energy Expenditure (TDEE)
**Calculation method:**
Sedentary: BMR x 1.2
Lightly Active: BMR x 1.375
Moderately Active: BMR x 1.55
Very Active: BMR x 1.725
Extremely Active: BMR x 1.9
*Observation:*
TDEE uses BMR; because of this, it inherits the same limitations.
### TDEE Recommendation
**Calculation method:**
Maintain: TDEE
Lose weight: TDEE x 0.85
Gain weight: TDEE x 1.15
*Observation:*
Normally for weight loss/gain this method involves adjusting TDEE by 10-20%. In this program the intermediate value was used (15%).

## Requirements
- Python >= 3.12.10
- pytest == 8.3.5

## Usage
1. Run the program directly: `python project.py`
2. Follow the interactive prompts to enter your:
 -Age (whole years)
 -Biological sex (male/female)
 -Height (in meters)
 -Weight (in kilograms)
 -Physical activity level (with detailed definitions provided)
3. All the results will appear in the terminal.

## Disclaimer
⚠️ This program does not provide medical advice and is intended for adults aged 18 to 65. Results may vary, and errors are possible.
Always consult a healthcare professional.
