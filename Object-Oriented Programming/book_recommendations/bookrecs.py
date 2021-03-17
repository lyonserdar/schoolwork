"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""
__class__ = "CS 1410"
__project__ = "Project 1 - Book Recommendations"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "1/15/2021"
__divider__ = "------------------------------------------------------------------------"


from heapq import nlargest

authors_and_titles = []
readers_and_ratings = {}


def load_files():
    lines = []

    def read_file(file_name):
        with open(file_name, "r") as f:
            return f.readlines()

    # Load the authors and titles
    lines = read_file("booklist.txt")

    for line in lines:
        line = line.strip()  # Removes whitespace and newline
        line = line.split(",")  # Split the author and titles
        authors_and_titles.append((line[0], line[1]))

    lines.clear()  # Empty the lines list

    # Load the readers and ratings
    lines = read_file("ratings.txt")

    for i, line in enumerate(lines):
        if i % 2 == 0:
            ratings = []
            raw_ratings = lines[i + 1].strip().split()
            for rating in raw_ratings:
                ratings.append(int(rating))
            readers_and_ratings[line.strip().lower()] = ratings


def dotprod(x, y):
    score = 0
    for index in range(len(x)):
        score += x[index] * y[index]
    return score


def friends(name):
    scores = {}
    for reader, rating in readers_and_ratings.items():
        if name != reader:
            scores[reader] = dotprod(readers_and_ratings[name], rating)
    return sorted(nlargest(2, scores, key=scores.get))


def recommend(name):
    recommended_books = []
    two_friends = friends(name)
    for index in range(len(authors_and_titles)):
        if readers_and_ratings[name][index] == 0:
            if (
                readers_and_ratings[two_friends[0]][index] >= 3
                or readers_and_ratings[two_friends[1]][index] >= 3
            ):
                recommended_books.append(authors_and_titles[index])
    return sorted(
        recommended_books, key=lambda i: ((i[0].split())[-1], (i[0].split())[0], i[1]),
    )


def get_readers():
    return sorted(
        list(readers_and_ratings.keys()),
        key=lambda i: ((i[0].split())[-1], (i[0].split())[0], i[1]),
    )


def has_reader(name):
    if name in readers_and_ratings:
        return True
    return False


def main():
    print(__divider__)
    print(__project__)
    print(__divider__)
    load_files()
    name = input("Enter a reader's name: ")
    name = name.lower()
    if not has_reader(name):
        print(f"No such reader {name}")
        return
    two_friends = friends(name)
    print(f"Recommendations for {name} from {two_friends[0]} and {two_friends[1]}:")
    recommended_books = recommend(name)
    recommended_books = sorted(
        recommended_books, key=lambda i: ((i[0].split())[-1], (i[0].split())[0], i[1]),
    )
    for book in recommended_books:
        print(f"\t{book[0]}, {book[1]}")


if __name__ == "__main__":
    main()
