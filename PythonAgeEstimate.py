from datetime import datetime
import sys

def calculate_age(date_of_birth):
    today = datetime.now()
    birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python age_predictor.py <date_of_birth>")
        sys.exit(1)

    dob = sys.argv[1]
    print(f"Input Date of Birth: {dob}")
    
    age = calculate_age(dob)
    print(f"Calculated Age: {age} years")
    print("New Line added=modification")
