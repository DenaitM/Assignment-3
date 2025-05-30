
print("Hello, Search Students data file!")

def printOptions():
    print("Options: \n")
    print("1. Search by last name")
    print("2. Search by major")
    print("3. Quit")

    print()  # add a new line for better readability

def readStudentFile(filename):
    studentDictionary = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    student_id = parts[0].strip()
                    last_name = parts[1].strip()
                    first_name = parts[2].strip()
                    major = parts[3].strip()
                    gpa = float(parts[4].strip())
                    studentDictionary[student_id] = [last_name, first_name, major, gpa]
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.") #message if the file is not found
        return {}
    except Exception as e:
        print(f"something happened while reading the file: {e}")
        return {}
    return studentDictionary

def searchByLastName(studentDictionary, LastName):
    results = {}
    for student_id, info in studentDictionary.items():
        if info[0].lower() == LastName.lower():
            results[student_id] = info
    return results

def searchByMajor(studentDictionary, Major):
    results = {}
    for student_id, info in studentDictionary.items():
        if info[2].lower() == Major.lower():
            results[student_id] = info
        return results
    
def main():
    filename = (r'C:\Users\denai\OneDrive\Documents\cs222\Assignment 3\students.txt')
    studentDictionary = readStudentFile(filename)
    if not studentDictionary:
        print("student file is empty")
        return
    
    while True:
        printOptions()
        choice = input("Choose an option: \n")
        if choice == '1':
            last_name = input("\nEnter a lastname to search for: \n")
            results = searchByLastName(studentDictionary, last_name)
            print()
            if results:
                for student_id, info in results.items():
                    print(f"ID: {student_id}, Last Name: {info[0]}, First Name: {info[1]}, Major: {info[2]}, GPA: {info[3]}")
            else:
                print("There isn't a student with that last name.")
                print()
        
        elif choice == '2':
            major = input("\nEnter major to search for: \n")
            results = searchByMajor(studentDictionary, major)

            print()

            if results:
                for student_id, info in results.items():
                    print(f"ID: {student_id}, Last Name: {info[0]}, First Name: {info[1]}, Major: {info[2]}, GPA: {info[3]}")
            else:
                print("There are no students with that major.")
        
        elif choice == '3':
            print("The End. Quitting the program.")
            break
        
        else:
            print("choose one of the options above.")

if __name__ == "__main__":
    main()