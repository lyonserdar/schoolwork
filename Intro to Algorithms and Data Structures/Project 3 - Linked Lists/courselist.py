"""
Course List Implementation
TODO: fix docstring
TODO: cleanup iterator 
"""


class CourseList:
    """This is a Custom Ordered Linked List"""

    def __init__(self):
        """Initialize the empty list"""
        self.head = None
        # self.__current = None

    def insert(self, course):
        """Inserts the course with course number ascending order"""
        current = self.head
        previous = None
        while current:
            if current.course_number > course.course_number:
                break

            previous = current
            current = current.next

        if previous:
            course.next = current
            previous.next = course
        else:
            course.next = self.head
            self.head = course

    def remove(self, course_number):
        """Removes the first occurrence of the specified course with course number"""
        current = self.head
        previous = None
        while current:
            if current.course_number == course_number:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                break

            if current.course_number > course_number:
                break

            previous = current
            current = current.next

    def remove_all(self, course_number):
        """Removes the all occurrences of the specified course with course number"""
        current = self.head
        previous = None
        while current:
            if current.course_number == course_number:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                if current.course_number > course_number:
                    break
                previous = current
                current = current.next

    def find(self, course_number):
        """
        Returns the first occurrance of the specified course with course number, if not
        found returns -1
        """
        current = self.head
        while current:
            if current.course_number == course_number:
                return current

            if current.course_number > course_number:
                break

            current = current.next
        return -1

    def size(self):
        """Returns the number of items in the list"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def calculate_gpa(self):
        """Returns the GPA calculated using all courses in the list"""
        if self.size() == 0:
            return 0.0
        current = self.head
        credit_sum = 0
        gpa_times_credit_sum = 0
        while current:
            gpa_times_credit_sum += current.credit_hr() * current.grade()
            credit_sum += current.credit_hr()
            current = current.next
        return gpa_times_credit_sum / credit_sum

    def is_sorted(self):
        """
        Returns True if the list is sorted by course number, returns False otherwise
        """
        if self.size() == 0:
            return True
        current = self.head
        sorted_flag = True
        while current and current.next:
            if current.course_number > current.next.course_number:
                sorted_flag = False
                break
            current = current.next
        return sorted_flag

    def is_empty(self):
        """Returns True if the list is empty, returns False otherwise"""
        return self.head is None

    def __str__(self):
        """Returns a string with each course"""
        # TODO: fix the output
        return "Output"

    def __iter__(self):
        """Creates an iterable"""
        # self.__current = self.head
        # return self.__current
        current = self.head
        while current:
            yield current
            current = current.next

    # def __next__(self):
    #     """Returns the next iterable"""
    #     if not self.__current.next:
    #         raise StopIteration
    #     self.__current = self.__current.next
    #     return self.__current
