"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""
__class__ = "CS 1410"
__project__ = "Project 4 - GUI for Book Recommendations"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/5/2021"
__divider__ = "------------------------------------------------------------------------"


from breezypythongui import EasyFrame
import bookrecs


class MainWindow(EasyFrame):
    """Application window for the book recommendations."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Book Recommendations", background="#FFFF00")

        self.addButton(text="Friends", row=0, column=0, command=self.getFriends)
        self.addButton(
            text="Recommend", row=0, column=1, command=self.getRecommendations
        )
        self.addButton(text="Report", row=0, column=2, command=self.getReader)

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
            # TODO: Ressize the messageBox
            self.messageBox(title=f"Friends of {reader}", message=message)

    def getRecommendations(self):
        reader = self.getReader()
        if reader:
            recommended_books = bookrecs.recommend(reader)
            message = []
            for book in recommended_books:
                message.append(f"{book[0]}, {book[1]}")
            message = "\n".join(message)
            # TODO: Ressize the messageBox
            self.messageBox(title=f"Friends of {reader}", message=message)

    def getReport(self):
        pass
        # TODO: Finish getReport()
        # TODO: Extract the keys from your ratings dictionary and call sorted.
        # TODO: Ressize the messageBox
        # two_friends = friends(name)
        # print(f"Recommendations for {name} from {two_friends[0]} and {two_friends[1]}:")
        # recommended_books = recommend(name)
        # recommended_books = sorted(
        #     recommended_books, key=lambda i: ((i[0].split())[-1], (i[0].split())[0], i[1]),
        # )
        # for book in recommended_books:
        #     print(f"\t{book[0]}, {book[1]}")

def main():
    print(__divider__)
    print(__project__)
    print(__divider__)
    bookrecs.load_files()
    MainWindow().mainloop()


if __name__ == "__main__":
    main()
