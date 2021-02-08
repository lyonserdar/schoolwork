"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""
__class__ = "CS 1410"
__project__ = "Project 5 - Payroll"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/5/2021"
__divider__ = "------------------------------------------------------------------------"

from abc import ABC, abstractmethod

EMPLOYEE_FILE = "employees.csv"
PAY_LOGFILE = "payroll.txt"
TIMECARD_FILE = "timecards.csv"
RECEIPTS_FILE = "receipts.csv"

employees = []
timecards = {}
receipts = {}


def load_employees():
    """Loads employees from csv file"""
    print("load_employees()")
    with open(EMPLOYEE_FILE, "r") as f:
        header_line = next(f)  # Skip the header
        for line in f:
            line = line.strip().split(",")
            classification = None
            classification_index = line[7]  # Classification (column 7)
            if classification_index == 1:  # Salaried
                salary = line[8]  # Salary (column 8)
                classification = Salaried(salary)
            elif classification_index == 2:  # Commissioned
                salary = line[8]  # Salary (column 8)
                commission_rate = line[9]  # Commission Rate (column 9)
                classification = Commissioned(salary, commission_rate)
            elif classification_index == 3:  # Hourly
                hourly_rate = line[10]  # Hourly Rate (column 10)
                classification = Hourly(hourly_rate)
            employee = Employee(
                line[0],  # emp_id
                line[1],  # first_name
                line[2],  # last_name
                line[3],  # address
                line[4],  # city
                line[5],  # state
                line[6],  # zipcode
                classification,
            )
            employees.append(employee)


def process_timecards():
    print("process_timecards()")
    with open(TIMECARD_FILE, "r") as f:
        for line in f:
            line = line.strip().split(",")
            timecards[line[0]] = line[1:]


def process_receipts():
    print("process_receipts()")
    with open(RECEIPTS_FILE, "r") as f:
        for line in f:
            line = line.strip().split(",")
            receipts[line[0]] = line[1:]


def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()


def find_employee_by_id(emp_id):
    print("find_employee_by_id()", emp_id)


class Employee:
    """Class for Employee"""

    def __init__(
        self,
        emp_id,
        first_name,
        last_name,
        address,
        city,
        state,
        zipcode,
        classification=None,
    ):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification

    # @property
    # def classification(self):
    #     """Get the employee classification"""
    #     return self.classification

    # @classification.setter
    # def classification(self, value):
    #     """Set the employee classification"""
    #     self.classification = value

    def issue_payment(self):
        pass

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_hourly(self, hourly_rate):
        self.classification = Hourly(hourly_rate)

    def make_commissioned(self, salary, commission_rate):
        self.classification(salary, commission_rate)

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return f"{full_name} (id:{self.emp_id}, {str(self.classification)})"


class Classification(ABC):
    """Abstract class for Employee Classification"""

    @abstractmethod
    def compute_pay():
        pass


class Hourly(Classification):
    """Class for Hourly Employee Classification"""

    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def compute_pay():
        pass

    def add_timecard(self, time):
        timecards[]

    def __str__(self):
        return f"Hourly"


class Salaried(Classification):
    """Class for Salaried Employee Classification"""

    def __init__(self, salary):
        self.salary = salary

    def compute_pay():
        pass

    def __str__(self):
        return f"Salaried"


class Commissioned(Salaried):
    """Class for Commissioned Employee Classification"""

    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate

    def compute_pay():
        pass

    def add_receipt(self, rate):
        pass

    def __str__(self):
        return f"Commissioned"


def main():
    # emp = Employee(
    #     "10593855",
    #     "Serdar",
    #     "Lyon",
    #     "Test address",
    #     "Orem",
    #     "UT",
    #     84059,
    #     Salaried(120000.00),
    # )
    # print(emp)
    load_employees()
    process_timecards()
    process_receipts()


if __name__ == "__main__":
    print(__divider__)
    print(__project__)
    print(__divider__)
    main()
