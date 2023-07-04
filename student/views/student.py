import logging
from tkinter import ttk
from tkinter import (
    Entry,
    Label,
    Button,
    Tk,
    END,
    messagebox
)

from tkcalendar import DateEntry

from student.controls.student import StudentService

logger = logging.getLogger("auth")


class StudentInformationView(StudentService):
    """
    App labels and inputs are made by tkinter package
    And by using the submit button, the values are taken in
    the form of a dictionary, then the conditions are checked
    And finally it is stored in the database.
    """

    def __init__(self, window: Tk):
        self.window = window
        self.window.geometry('350x400')
        self.window.title("Information Student")
        self.window.resizable(width=False, height=True)
        self.text = "Enter Your Information"

        # First name
        Label(self.window, text="First Name: ", pady=10).grid(row=1, column=0)
        self.first_name = Entry(self.window)
        self.first_name.grid(row=1, column=1)

        # Last name
        Label(self.window, text="Last Name: ", pady=10).grid(row=2, column=0)
        self.last_name = Entry(self.window)
        self.last_name.grid(row=2, column=1)

        # Gender list
        gender_list = ("Male", "Female")
        Label(self.window, text="Gender: ", pady=10).grid(row=3, column=0)
        self.gender = ttk.Combobox(
            self.window,
            values=gender_list,
            state="readonly"
        )
        self.gender.grid(row=3, column=1)

        # Date of birth
        Label(
            self.window,
            text="Date of birth: ",
            pady=10
        ).grid(row=4, column=0)
        self.date_of_birth = DateEntry(
            self.window,
            selectmode="day",
            justify="center"
        )
        self.date_of_birth.grid(row=4, column=1)

        # Grade
        grade_list = ("Associate", "Bachelor", "Master", "Doctoral")
        Label(self.window, text="Grade: ", pady=10).grid(row=5, column=0)
        self.grade = ttk.Combobox(
            self.window,
            values=grade_list,
            state="readonly"
        )
        self.grade.grid(row=5, column=1)

        # Date of registration
        Label(
            self.window,
            text="Date of registration: ",
            pady=10
        ).grid(row=6, column=0)
        self.date_of_registration = DateEntry(
            self.window,
            selectmode="day",
            justify="center"
        )
        self.date_of_registration.grid(row=6, column=1)

        # Graduation date
        Label(
            self.window,
            text="Graduation date: ",
            pady=10
        ).grid(row=7, column=0)
        self.graduation_date = DateEntry(
            self.window,
            selectmode="day",
            justify="center"
        )
        self.graduation_date.grid(row=7, column=1)

        # Address
        Label(self.window, text="Address: ", pady=10).grid(row=8, column=0)
        self.address = Entry(self.window)
        self.address.grid(row=8, column=1)

        # Phone number
        Label(
            self.window,
            text="Phone number: ",
            pady=10
        ).grid(row=9, column=0)
        self.phone_number = Entry(self.window)
        self.phone_number.grid(row=9, column=1)

        # Submit
        self.submit_btn = Button(
            self.window,
            text="Submit",
            command=self.submit
        )
        self.submit_btn.grid(row=10, column=1)

    def submit(self):
        logger.info("The user clicks the submit button")
        student_data = {
            "first_name": self.get_or_none(self.first_name),
            "last_name": self.get_or_none(self.last_name),
            "gender": self.get_or_none(self.gender),
            "date_of_birth": self.get_or_none(self.date_of_birth),
            "grade": self.get_or_none(self.grade),
            "graduation_date": self.get_or_none(self.graduation_date),
            "address": self.get_or_none(self.address),
            "phone_number": self.get_or_none(self.phone_number),
            "date_of_registration": self.get_or_none(self.date_of_registration)
        }

        if self.check_fields(student_data):
            logger.info("The user clicks the submit button")
            self.submit_info_student(student_data)
            logger.info(
                "All fields are without problems and "
                "ready to be registered in the database"
            )
            messagebox.showinfo(
                "Successful",
                "Your information has been successfully registered"
            )
            self.clear_fields()

    @staticmethod
    def get_or_none(value: str) -> None | str:
        """
        It checks if the string value is empty and returns none,
        otherwise it returns the value
        """
        return value.get() if value.get() != "" else None

    def clear_fields(self):
        """
        Clears the values from within the program
        """
        self.first_name.delete(0, END)
        self.last_name.delete(0, END)
        self.gender.set('')
        self.date_of_birth.delete(0, END)
        self.grade.set('')
        self.date_of_registration.delete(0, END)
        self.graduation_date.delete(0, END)
        self.address.delete(0, END)
        self.phone_number.delete(0, END)
        logger.info("The amount of fields were deleted from the user's page")
