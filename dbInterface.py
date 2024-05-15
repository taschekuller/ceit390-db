import requests
from main import list_tables, update_student, create_student, delete_student, update_instructor, create_instructor, delete_instructor, update_classroom, create_classroom, delete_classroom, update_course, create_course, delete_course, update_section, create_section, delete_section, update_enrollment, create_enrollment, delete_enrollment

def main():
    base_url = "http://localhost:5434"  # Assuming Flask runs on this URL
    
    while True:
        print("1. Interact with database")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("***")
            print("Welcome to the METU Course Database")
            print("***")
            
            while True:
                list_tables()
                print("0. Return to main menu")
                table_choice = input("Enter table choice: ")
                
                # STUDENT
                if table_choice == "1":
                    print("1. List all students")
                    print("2. Get student by ID")
                    print("3. Update student")
                    print("4. Add new student")
                    print("5. Delete student by ID")
                    print("0. Exit")
                    student_choice = input("Enter student choice: ")
                    
                    if student_choice == "1":
                        # Make a GET request to list all students
                        response = requests.get(f"{base_url}/students")
                        if response.status_code == 200:
                            students = response.json()
                            print("Students:")
                            for student in students:
                                print(student)
                        else:
                            print("Error:", response.text)
                    elif student_choice == "2":
                        student_id = input("Enter student's ID: ")
                        int(student_id)
                        response = requests.get(f"{base_url}/students/{student_id}")
                        if response.status_code == 200:
                            student = response.json()
                            print("Student:", student)
                            print(student)
                        else:
                            print("Error:", response.text)
                    elif student_choice == "3":
                        student_id = input("Enter student's ID for updating: ")
                        update_student(student_id)
                        response = requests.get(f"{base_url}/students/{student_id}")
                        if response.status_code == 200:
                            student = response.json()     
                            print("Student:", student)
                            print(student)
                        else:
                            print("Error:", response.text)
                    elif student_choice == "4":
                        create_student()        
                    elif student_choice == "5":
                        student_id_to_delete = input("Which student you want to delete, type ID:")
                        delete_student(student_id_to_delete)
                    elif student_choice == "0":
                        break
                    else:
                        print("Invalid choice")
                
                # INSTRUCTOR
                if table_choice == "2":
                    print("1. List all instuctors")
                    print("2. Get instructor by ID")
                    print("3. Update instructor")
                    print("4. Add new instructor")
                    print("5. Delete instructor by ID")
                    print("0. Exit")
                    instructor_choice = input("Enter instructor choice: ")

                    if instructor_choice == "1":
                        # Make a GET request to list all instructors
                        response = requests.get(f"{base_url}/instructors")
                        if response.status_code == 200:
                            instructors = response.json()
                            print("instructors:")
                            for instructor in instructors:
                                print(instructor)
                        else:
                            print("Error:", response.text)
                    elif instructor_choice == "2":
                        instructor_id = input("Enter instructor's ID: ")
                        int(instructor_id)
                        response = requests.get(f"{base_url}/instructors/{instructor_id}")
                        if response.status_code == 200:
                            instructor = response.json()
                            print("instructor:", instructor)
                            print(instructor)
                        else:
                            print("Error:", response.text)
                    elif instructor_choice == "3":
                        instructor_id = input("Enter instructor's ID for updating: ")
                        update_instructor(instructor_id)
                        response = requests.get(f"{base_url}/instructors/{instructor_id}")
                        if response.status_code == 200:
                            instructor = response.json()     
                            print("instructor:", instructor)
                            print(instructor)
                        else:
                            print("Error:", response.text)
                    elif instructor_choice == "4":
                        create_instructor()        
                    elif instructor_choice == "5":
                        instructor_id_to_delete = input("Which instructor you want to delete, type ID:")
                        delete_instructor(instructor_id_to_delete)
                    elif instructor_choice == "0":
                        break
                    else:
                        print("Invalid choice")
                        
                # CLASSROOM
                if table_choice == "3":
                    print("1. List all classroom")
                    print("2. Get classroom by ID")
                    print("3. Update classroom")
                    print("4. Add new classroom")
                    print("5. Delete classroom by ID")
                    print("0. Exit")
                    classroom_choice = input("Enter classroom choice: ")

                    if classroom_choice == "1":
                        # Make a GET request to list all classroom
                        response = requests.get(f"{base_url}/classroom")
                        if response.status_code == 200:
                            classroom = response.json()
                            print("classroom:")
                            for classroom in classroom:
                                print(classroom)
                        else:
                            print("Error:", response.text)
                    elif classroom_choice == "2":
                        classroom_id = input("Enter classroom's ID: ")
                        int(classroom_id)
                        response = requests.get(f"{base_url}/classroom/{classroom_id}")
                        if response.status_code == 200:
                            classroom = response.json()
                            print("classroom:", classroom)
                            print(classroom)
                        else:
                            print("Error:", response.text)
                    elif classroom_choice == "3":
                        classroom_id = input("Enter classroom's ID for updating: ")
                        update_classroom(classroom_id)
                        response = requests.get(f"{base_url}/classroom/{classroom_id}")
                        if response.status_code == 200:
                            classroom = response.json()     
                            print("classroom:", classroom)
                            print(classroom)
                        else:
                            print("Error:", response.text)
                    elif classroom_choice == "4":
                        create_classroom()        
                    elif classroom_choice == "5":
                        classroom_id_to_delete = input("Which classroom you want to delete, type ID:")
                        delete_classroom(classroom_id_to_delete)
                    elif classroom_choice == "0":
                        break
                    else:
                        print("Invalid choice")
                  
                # COURSE
                if table_choice == "4":
                    print("1. List all course")
                    print("2. Get course by ID")
                    print("3. Update course")
                    print("4. Add new course")
                    print("5. Delete course by ID")
                    print("0. Exit")
                    course_choice = input("Enter course choice: ")

                    if course_choice == "1":
                        # Make a GET request to list all course
                        response = requests.get(f"{base_url}/course")
                        if response.status_code == 200:
                            course = response.json()
                            print("course:")
                            for course in course:
                                print(course)
                        else:
                            print("Error:", response.text)
                    elif course_choice == "2":
                        course_id = input("Enter course's ID: ")
                        int(course_id)
                        response = requests.get(f"{base_url}/course/{course_id}")
                        if response.status_code == 200:
                            course = response.json()
                            print("course:", course)
                            print(course)
                        else:
                            print("Error:", response.text)
                    elif course_choice == "3":
                        course_id = input("Enter course's ID for updating: ")
                        update_course(course_id)
                        response = requests.get(f"{base_url}/course/{course_id}")
                        if response.status_code == 200:
                            course = response.json()     
                            print("course:", course)
                            print(course)
                        else:
                            print("Error:", response.text)
                    elif course_choice == "4":
                        create_course()        
                    elif course_choice == "5":
                        course_id_to_delete = input("Which course you want to delete, type ID:")
                        delete_course(course_id_to_delete)
                    elif course_choice == "0":
                        break
                    else:
                        print("Invalid choice")
                  
                # SECTION
                if table_choice == "5":
                    print("1. List all section")
                    print("2. Get section by ID")
                    print("3. Update section")
                    print("4. Add new section")
                    print("5. Delete section by ID")
                    print("0. Exit")
                    section_choice = input("Enter section choice: ")

                    if section_choice == "1":
                        # Make a GET request to list all section
                        response = requests.get(f"{base_url}/section")
                        if response.status_code == 200:
                            section = response.json()
                            print("section:")
                            for section in section:
                                print(section)
                        else:
                            print("Error:", response.text)
                    elif section_choice == "2":
                        section_id = input("Enter section's ID: ")
                        int(section_id)
                        response = requests.get(f"{base_url}/section/{section_id}")
                        if response.status_code == 200:
                            section = response.json()
                            print("section:", section)
                            print(section)
                        else:
                            print("Error:", response.text)
                    elif section_choice == "3":
                        section_id = input("Enter section's ID for updating: ")
                        update_section(section_id)
                        response = requests.get(f"{base_url}/section/{section_id}")
                        if response.status_code == 200:
                            section = response.json()     
                            print("section:", section)
                            print(section)
                        else:
                            print("Error:", response.text)
                    elif section_choice == "4":
                        create_section()        
                    elif section_choice == "5":
                        section_id_to_delete = input("Which section you want to delete, type ID:")
                        delete_section(section_id_to_delete)
                    elif section_choice == "0":
                        break
                    else:
                        print("Invalid choice")
                        
                # ENROLLMENT
                if table_choice == "6":
                    print("1. List all enrollment")
                    print("2. Get enrollment by ID")
                    print("3. Update enrollment")
                    print("4. Add new enrollment")
                    print("5. Delete enrollment by ID")
                    print("0. Exit")
                    enrollment_choice = input("Enter enrollment choice: ")

                    if enrollment_choice == "1":
                        # Make a GET request to list all enrollment
                        response = requests.get(f"{base_url}/enrollment")
                        if response.status_code == 200:
                            enrollment = response.json()
                            print("enrollment:")
                            for enrollment in enrollment:
                                print(enrollment)
                        else:
                            print("Error:", response.text)
                    elif enrollment_choice == "2":
                        enrollment_id = input("Enter enrollment's ID: ")
                        int(enrollment_id)
                        response = requests.get(f"{base_url}/enrollment/{enrollment_id}")
                        if response.status_code == 200:
                            enrollment = response.json()
                            print("enrollment:", enrollment)
                            print(enrollment)
                        else:
                            print("Error:", response.text)
                    elif enrollment_choice == "3":
                        enrollment_id = input("Enter enrollment's ID for updating: ")
                        update_enrollment(enrollment_id)
                        response = requests.get(f"{base_url}/enrollment/{enrollment_id}")
                        if response.status_code == 200:
                            enrollment = response.json()     
                            print("enrollment:", enrollment)
                            print(enrollment)
                        else:
                            print("Error:", response.text)
                    elif enrollment_choice == "4":
                        create_enrollment()        
                    elif enrollment_choice == "5":
                        enrollment_id_to_delete = input("Which enrollment you want to delete, type ID:")
                        delete_enrollment(enrollment_id_to_delete)
                    elif enrollment_choice == "0":
                        break
                    else:
                        print("Invalid choice")
                               
                
                
                elif table_choice == "0":
                    break
                else:
                    print("Invalid choice")
        elif choice == "2":
            break
        else:
            print("Invalid choice")

main()
