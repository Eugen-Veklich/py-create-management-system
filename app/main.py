import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    try:
        return max(len(group.students) for group in groups)
    except ValueError:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    speciality = set(group.specialty.name for group in groups)
    return list(speciality)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
