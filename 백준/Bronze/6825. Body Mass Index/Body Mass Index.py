def get_bmi(weight, height):
    return weight / (height * height)


def body_mass_index(weight, height):
    check_result = ""
    
    bmi = get_bmi(
        weight=weight, height=height
    )
    
    if bmi < 18.5:
        check_result = "Underweight"
    elif 18.5 <= bmi < 25:
        check_result = "Normal weight"
    elif bmi >= 25:
        check_result = "Overweight"
        
    return check_result


if __name__ == "__main__":
    weight = float(input())
    height = float(input())
    
    print(body_mass_index(weight=weight, height=height))