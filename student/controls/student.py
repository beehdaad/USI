import re
import logging
from tkinter import messagebox

from student.models import Student
from kernel.database.core import SQLalchemy

db = SQLalchemy()
loggerA = logging.getLogger("auth")
loggerC = logging.getLogger("core")


class StudentService:
    """
    It takes the student's information and registers
    it in the database before verifying its values
    """

    @staticmethod
    def submit_info_student(student: dict):
        # Create a new student object with the entered information
        obj = Student(
            first_name=student["first_name"],
            last_name=student["last_name"],
            gender=student["gender"],
            date_of_birth=student["date_of_birth"],
            grade=student["grade"],
            date_of_registration=student["date_of_registration"],
            graduation_date=student["graduation_date"],
            address=student["address"],
            phone_number=student["phone_number"]
        )
        loggerC.info("A query was created")
        # Save the student object to the database
        db.session.add(obj)
        loggerC.info("The query was delivered to the session")
        db.session.commit()
        loggerC.info("A query was registered in the database")
        db.session.close()
        loggerC.info("The connection of the session with the database is over")

    @staticmethod
    def check_fields(student_data: dict) -> bool:
        """
        Verification of the values sent by the student
        """
        valid = True
        # Validation that the value is not None
        if None in student_data.values():
            messagebox.showerror("Error", "field cannot be empty.")
            loggerA.info("Validation that the value is not None")
            valid = False

        # Validation that the first name is not Digit
        elif not re.match(r"^[A-Za-z]+$", student_data["first_name"]):
            messagebox.showerror(
                "Error",
                "Invalid format for First Name. "
                "Only alphabetic characters are allowed."
            )
            loggerA.info("Validation that the first name is not Digit")
            valid = False

        # Validation that last name is not Digit
        elif not re.match(r"^[A-Za-z]+$", student_data["last_name"]):
            messagebox.showerror(
                "Error",
                "Invalid format for Last Name. "
                "Only alphabetic characters are allowed."
            )
            loggerA.info("Validation that last name is not Digit")
            valid = False

        # Validation that phone number is not str and 11 digits
        elif student_data["phone_number"]:
            try:
                int(student_data["phone_number"])
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Phone number field must be number."
                )
                loggerA.info("Validation that phone number is not str")
                valid = False
            else:
                if len(student_data["phone_number"]) != 11:
                    messagebox.showerror(
                        "Error",
                        "Phone number field must be 11 digits"
                    )
                    loggerA.info(
                        "Validation that phone number is not 11 digits"
                    )
                    valid = False

        return valid
