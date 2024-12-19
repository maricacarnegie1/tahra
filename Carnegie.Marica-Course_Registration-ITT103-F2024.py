system= RegistrationSystem

        print("Course Registration System")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll Student in Course")
        print("4. Make Payment")
        print("5. Show All Courses")
        print("6. Show All Registered Students")
        print("7. Show Students in a Course")
        print("8. Check Student Balance")
        print("9. Exit")

        choice = input("Enter your choice: ")

            if choice = "1":
                input("Enter course ID:")
                input("Enter course name: ")
                float(input("Enter course fee: ")
                system.add_course (“ITT101”,” Info Tech”, “$200”)
                print("Course added successfully.")

            elif choice = "2":
                 input("Enter student ID: ")
                 input("Enter student name: ")
                 input("Enter student email: ")
                 system.register_student (“2200”, “Marica”, “mcarnegie45@gmail.com”)
                 print("Student registered successfully.")

            elif choice = "3":
                   input("Enter student ID: ")
                   input("Enter course ID: ")
                   system.enroll_in_course (“2200”, “ITT101”) #Marica is enrolled in Info Tech.
                   print("Student enrolled in course successfully.")

            elif choice = "4":
                input("Enter student ID: ")
                float(input("Enter payment amount: "))
                system.calculate_payment(“2200”, “$80”) #Marica pays 40% of the fee.
                print("Payment processed successfully.")

            elif choice = "5":
                print("Available Courses:", system.show_courses) #List all courses.

            elif choice ="6":
                print("Registered Students:", system.show_registered_students)#List all registered students.

            elif choice = "7":
                input("Enter course ID: ")
                print("Students in Course:", system.show_students_in_course(“ITT101”))#Show all the students in Info Tech.

            elif choice = "8":
                input("Enter student ID: ")
                print("Student Balance: $", system.check_student_balance(“2200”))#Shows Marica’s remaining balance.

            elif choice = "9":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
