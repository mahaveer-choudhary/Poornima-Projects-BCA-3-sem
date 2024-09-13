import re

## funciton for knowing the time it take to bruteforce 
def get_bruteforce_time(password_length, char_type):
    if 4 <= password_length <= 8:
        times = {
            'numbers': '9 minutes',
            'lowercase': '5 hours',
            'uppercase_lowercase': '67.4 days',
            'numbers_uppercase_lowercase': '1 year',
            'numbers_uppercase_lowercase_special': '2.17 years'
        }
    elif 9 <= password_length <= 12:
        times = {
            'numbers': '3 days',
            'lowercase': '209 years',
            'uppercase_lowercase': '1.02 million years',
            'numbers_uppercase_lowercase': '7.94 million years',
            'numbers_uppercase_lowercase_special': '34.83 million years'
        }
    elif 13 <= password_length <= 18:
        times = {
            'numbers': '2,521 years',
            'lowercase': '67 billion years',
            'uppercase_lowercase': '22.57 trillion years',
            'numbers_uppercase_lowercase': '137.25 quadrillion years',
            'numbers_uppercase_lowercase_special': '10.43 quintillion years'
        }
    else:
        return "Password length not supported for brute-force estimation."
    
    return times.get(char_type, "Character set not supported.")


## function for determining the character type 
def determine_char_type(user_password):
    has_numbers = bool(re.search(r"\d", user_password))
    has_lowercase = bool(re.search(r"[a-z]", user_password))
    has_uppercase = bool(re.search(r"[A-Z]", user_password))
    has_special = bool(re.search(r"[#\$@%\^&\*\(\)\-\+=!`~{}'\[\]\\| ,\.?/]", user_password))

    if has_numbers and has_uppercase and has_lowercase and has_special:
        print(f"Your {user_password} is too Stong ")
        return 'numbers_uppercase_lowercase_special'
    elif has_numbers and has_uppercase and has_lowercase:
        print(f"your {user_password} is strong")
        return 'numbers_uppercase_lowercase'
    elif has_uppercase and has_lowercase:
        print(f"your {user_password} is good")
        return 'uppercase_lowercase'
    elif has_lowercase:
        print(f"your {user_password} is weak")
        return 'lowercase'
    elif has_numbers:
        print(f"your {user_password} is too weak. ")
        return 'numbers'
    else:
        return 'unknown'

def strength_checker(user_password):
    ## checking speical character in the user password 
    special_char = r"[#\$@%\^&\*\(\)\-\+=!`~{}'\[\]\\| ,\.?/]"
    special_checker = re.findall(special_char, user_password)

    if len(special_checker) == 0:
        found = "There are no special characters in the password."
    elif 1 <= len(special_checker) < 3:
        found = f"Special characters found in '{user_password}' are {special_checker}."
    elif len(special_checker) >= 3:
        found = f"Multiple special characters found in '{user_password}': {special_checker}."
    else:
        found = "Nothing found."
    
    ## checking password length  
    password_length = len(user_password)
    length_count = f"The length of password is {password_length}"

    ## determining character type 
    char_type = determine_char_type(user_password)
    
    ## get bruteforce time 
    brute_force_time = get_bruteforce_time(password_length, char_type)

    return f"{found}, {length_count}\nEstimated brute-force time: {brute_force_time}"

def main():
    # print("Password Strength Checker...")
    logo = ("""
          Password Strength Checker 
          """)
    print(logo)
    
    user_password = input("Enter your password to check its strength: ")
    result = strength_checker(user_password)
    
    print(result)


## calling the main function 
if __name__ == "__main__":
    main()
