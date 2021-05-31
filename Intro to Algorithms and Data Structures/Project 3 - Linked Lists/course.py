"""
Course Node
"""


class Course:
    """Course ADT is a custom node implementation"""

    def __init__(
        self, course_number=0, course_name="", course_credit=0.0, course_grade=0.0
    ):
        """Initialize course with next node set to None"""

        self.__set_course_number(course_number)
        self.__set_course_name(course_name)
        self.__set_course_credit(course_credit)
        self.__set_course_grade(course_grade)

        self.next = None

    def __set_course_number(self, value):
        """set course number"""
        try:
            if int(value) < 0:
                raise ValueError("Course Number cannot be less than 0")
            self.course_number = int(value)
        except ValueError as value_error:
            raise ValueError("Course Number must be an integer number") from value_error

    def __set_course_name(self, value):
        """set course name"""
        try:
            if value is None:
                raise ValueError("Course Name cannot be None")
            self.course_name = str(value)
        except ValueError as value_error:
            raise ValueError("Course Name must be a string") from value_error

    def __set_course_credit(self, value):
        """set course credit"""
        try:
            if float(value) < 0:
                raise ValueError("Course Credit Hour cannot be less than 0")
            self.course_credit = float(value)
        except ValueError as value_error:
            raise ValueError("Course Credit Hour must be a number") from value_error

    def __set_course_grade(self, value):
        """set course grade"""
        try:
            if float(value) < 0 or float(value) > 4.0:
                raise ValueError("Course Grade must be between 0.0 and 4.0")
            self.course_grade = float(value)
        except ValueError as value_error:
            raise ValueError("Course Grade must be a number") from value_error

    def number(self):
        """Returns course number as an integer"""
        return self.course_number

    def name(self):
        """Returns course name as a string"""
        return self.course_name

    def credit_hr(self):
        """Returns course credits as a float"""
        return self.course_credit

    def grade(self):
        """Returns course grade as a numeric value in range 0.0 - 4.0"""
        return self.course_grade

    def __str__(self):
        """Function def"""
        return (
            f"CS{self.course_number} {self.course_name} Grade:{self.course_grade} "
            f"Credit Hours:{self.course_credit}"
        )
