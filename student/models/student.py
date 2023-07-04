from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    Text
)

from kernel.database import SQLalchemy

db = SQLalchemy()


class StudentModel(db.Base):
    """
    model of student
    """

    __tablename__ = 'students'

    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: str,
        date_of_birth: str,
        grade: str,
        date_of_registration: str,
        graduation_date: str,
        address: str,
        phone_number: int
    ):

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.grade = grade
        self.date_of_registration = date_of_registration
        self.graduation_date = graduation_date
        self.address = address
        self.phone_number = phone_number

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(150), nullable=False)
    gender = Column(String(7), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    grade = Column(String(20), nullable=False)
    date_of_registration = Column(Date, nullable=False)
    graduation_date = Column(Date)
    address = Column(Text, nullable=False)
    phone_number = Column(String, nullable=False)
