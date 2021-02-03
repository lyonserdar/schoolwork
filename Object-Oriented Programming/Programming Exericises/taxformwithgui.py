__class__ = "CS 1410"
__project__ = "Programming Exercise 8.1"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/3/2021"
__divider__ = "------------------------------------------------------------------------"

"""
Open the taxformwithgui.py file and write a GUI-based program that implements the tax
calculator program shown in the figures below.

The first screenshot of the tax calculator program contains 2 input fields, 1 output
field, and 1 compute button. The 2 input fields are, gross income, and dependents. The
output field is, total tax. The second screenshot of the tax calculator program contains
the inputs entered and the total tax calculated are as follows. Gross income, 25000.00.
Dependents, 2. Total Tax, 1800.00. Figure 8-2 A GUI-based tax calculator program Be sure
to use the field names provided in the comments in your starter code.
"""

from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

        # Label and field for the income
        # (self.incomeField)
        self.addLabel(text="Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1, precision=2)

        # Label and field for the number of dependents
        # (self.depField)
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value=0, row=1, column=1)

        # The command button
        self.addButton(
            text="Compute", row=2, column=0, columnspan=2, command=self.computeTax
        )

        # Label and field for the tax
        # (self.taxField)
        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(value=0.0, row=3, column=1)

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        """Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and a flat tax rate
of 20%.
        """
        total_tax = 0
        income = self.incomeField.getNumber()
        num_of_dependents = self.depField.getNumber()
        deduction = 10000
        exemption = 3000
        tax_rate = 0.20
        total_tax = (income - num_of_dependents * exemption - deduction) * tax_rate
        self.taxField.setNumber(total_tax)


def main():
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()

