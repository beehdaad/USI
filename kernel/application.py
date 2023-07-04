import logging
from tkinter import Tk

from student.views import StudentInformationView

logger = logging.getLogger("core")


def main():
    """
    among the root of the project that makes the information page
    """
    window = Tk()
    logger.info("The tkinter object was created")
    StudentInformationView(window)
    window.mainloop()
    logger.info("The user has exited the program")
