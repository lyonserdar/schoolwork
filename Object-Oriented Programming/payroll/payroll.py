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
import os

EMPLOYEE_FILE = "employees.csv"
PAY_LOGFILE = "payroll.txt"
TIMECARD_FILE = "timecards.csv"
RECEIPTS_FILE = "receipts.csv"

employees = []


def load_employees():
    """Loads employees from csv file"""
    print("load_employees()")
    with open(EMPLOYEE_FILE, "r") as f:
        header_line = next(f)  # Skip the header
        for line in f:
            line = line.strip().split(",")
            employee = Employee(
                line[0],  # emp_id
                line[1],  # first_name
                line[2],  # last_name
                line[3],  # address
                line[4],  # city
                line[5],  # state
                line[6],  # zipcode
            )
            classification = None
            classification_index = int(line[7])  # Classification (column 7)
            if classification_index == 1:  # Salaried
                salary = float(line[8])  # Salary (column 8)
                employee.make_salaried(salary)
            elif classification_index == 2:  # Commissioned
                salary = float(line[8])  # Salary (column 8)
                commission_rate = float(line[9])  # Commission Rate (column 9)
                employee.make_commissioned(salary, commission_rate)
            elif classification_index == 3:  # Hourly
                hourly_rate = float(line[10])  # Hourly Rate (column 10)
                employee.make_hourly(hourly_rate)
            employees.append(employee)


def process_timecards():
    print("process_timecards()")
    with open(TIMECARD_FILE, "r") as f:
        for line in f:
            line = line.strip().split(",")
            emp_id = line[0]
            employee = find_employee_by_id(emp_id)
            times = line[1:]
            for time in times:
                employee.classification.add_timecard(float(time))
            print(employee.classification.timecard)


def process_receipts():
    print("process_receipts()")
    with open(RECEIPTS_FILE, "r") as f:
        for line in f:
            line = line.strip().split(",")
            emp_id = line[0]
            employee = find_employee_by_id(emp_id)
            receipts = line[1:]
            for receipt in receipts:
                employee.classification.add_receipt(float(receipt))


def run_payroll():
    print("run_payroll()")
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()


def find_employee_by_id(emp_id):
    for employee in employees:
        if employee.emp_id == emp_id:
            return employee

    print("Employee with given id does not exists!")
    return None


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

    def issue_payment(self):
        with open(PAY_LOGFILE, "a+") as f:
            pay = self.classification.compute_pay()
            if pay:
                f.write(f"Mailing {pay:.2f} to {self.full_name} at {self.full_address} \n")

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_hourly(self, hourly_rate):
        self.classification = Hourly(hourly_rate)

    def make_commissioned(self, salary, commission_rate):
        self.classification = Commissioned(salary, commission_rate)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_address(self):
        return f"{self.address} {self.city} {self.state} {self.zipcode}"

    def __str__(self):
        return f"{self.full_name} (id:{self.emp_id}, {str(self.classification)})"


class Classification(ABC):
    """Abstract class for Employee Classification"""

    @abstractmethod
    def compute_pay():
        pass


class Hourly(Classification):
    """Class for Hourly Employee Classification"""

    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecard = []

    def compute_pay(self):
        hours = sum(self.timecard)
        self.timecard = []
        return round(hours * self.hourly_rate, 2)

    def add_timecard(self, time):
        self.timecard.append(time)

    def __str__(self):
        return f"Hourly"


class Salaried(Classification):
    """Class for Salaried Employee Classification"""

    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        return round(self.salary / 24, 2)

    def __str__(self):
        return f"Salaried"


class Commissioned(Salaried):
    """Class for Commissioned Employee Classification"""

    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def compute_pay(self):
        receipts = sum(self.receipts)
        self.receipts = []
        return round(self.salary / 24 + receipts * self.commission_rate / 100.0, 2)

    def add_receipt(self, rate):
        self.receipts.append(rate)

    def __str__(self):
        return f"Commissioned"


def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

    employee = Employee(
        "12-3456789", "John", "Doe", "123 Anystreet", "Anytown", "Anystate", "98765"
    )
    rate = 35.5
    employee.make_hourly(rate)
    for d in range(10):
        employee.classification.add_timecard(4.0 + d * 0.5)


if __name__ == "__main__":
    print(__divider__)
    print(__project__)
    print(__divider__)
    main()
