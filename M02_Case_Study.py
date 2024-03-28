# =========================
# Created By: John Kane 
# File Name: M02_Case_Study
# What the program will do: 
#   ask for and accept a student's last name.
#   quit processing student records if the last name entered is 'ZZZ'.
#   ask for and accept a student's first name.
#   ask for and accept the student's GPA as a float.
#   test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#   test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
# =========================
def main():
    while True:
        last_name = input("Enter student's last name (Enter ZZZ to quit): ")
        if last_name == 'ZZZ':
            break
        
        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))
        
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for any honor.")
        
        print()  

if __name__ == "__main__":
    main()
