"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""
__class__ = "CS 1410"
__project__ = "Project 4 - GUI for Book Recommendations"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "3/17/2021"
__divider__ = "------------------------------------------------------------------------"


from breezypythongui import EasyFrame
import bookrecs

WIDTH = 120
HEIGHT = 30


class MainWindow(EasyFrame):
    """Application window for the book recommendations."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Book Recommendations", background="#FFFF00")

        self.addButton(text="Friends", row=0, column=0, command=self.getFriends)
        self.addButton(
            text="Recommend", row=0, column=1, command=self.getRecommendations
        )
        self.addButton(text="Report", row=0, column=2, command=self.getReport)

    # The event handler method for the button
    def getReader(self):
        try:
            reader = self.prompterBox(
                title="Friends", promptString="Enter Reader Name:"
            )
            reader = reader.strip().lower()
            if bookrecs.has_reader(reader):
                return reader
            else:
                self.messageBox(title="Error", message="No such reader.")
                return None
        # except KeyError:
        #     self.messageBox(title="Error", message="No such reader.")
        except:
            self.messageBox(title="Error", message="Unexpected error.")
            return None

    def getFriends(self):
        reader = self.getReader()
        if reader:
            message = bookrecs.friends(reader)
            print(message)
            message = "\n".join(message)
            self.messageBox(
                title=f"Friends of {reader}",
                message=message,
                width=WIDTH,
                height=HEIGHT,
            )

    def getRecommendations(self):
        reader = self.getReader()
        if reader:
            recommended_books = bookrecs.recommend(reader)
            message = []
            for book in recommended_books:
                message.append(f"{book[0]}, {book[1]}")
            message = "\n".join(message)
            self.messageBox(
                title=f"Friends of {reader}",
                message=message,
                width=WIDTH,
                height=HEIGHT,
            )

    def getReport(self):
        message = ""
        for name in bookrecs.get_readers():
            two_friends = bookrecs.friends(name)
            message += f"Recommendations for {name} from {two_friends[0]} and {two_friends[1]}:\n"
            recommended_books = bookrecs.recommend(name)
            recommended_books = sorted(
                recommended_books,
                key=lambda i: ((i[0].split())[-1], (i[0].split())[0], i[1]),
            )
            for book in recommended_books:
                message += f"\t{book[0]}, {book[1]}\n"
            message += "\n"
        self.messageBox(
            title=f"Report", message=message, width=WIDTH, height=HEIGHT,
        )


def main():
    print(__divider__)
    print(__project__)
    print(__divider__)
    bookrecs.load_files()
    MainWindow().mainloop()


if __name__ == "__main__":
    main()
