"""
Replace the contents of this module docstring with your own details
Name: Nguyen Hoang Ba Han
Date started: 4th December, 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1---movies-NguyenHan123-Aston-master
"""


def main():
    """..."""
    print("Movies To Watch 1.0 - by <Nguyen Hoang Ba Han>")
    # Open file
    in_file = open('movies.csv', 'r+')
    list_movies_data = in_file.readlines()
    print('{} movies loaded'.format(len(list_movies_data)))

    while True:
        print("\t Menu: ")
        print("L - List movies")
        print("A - Add a new movie")
        print("W - Watch a movie")
        print("Q - Quit")

        choice = input(">>> ").upper()
        if choice == 'L':
            movies_listed(list_movies_data)
        elif choice == 'A':
            movies_added(list_movies_data)
        elif choice == 'W':
            movies_watching_choice(list_movies_data)
        elif choice == 'Q':
            # Link all the information and updates of movies
            link_data = ''.link(list_movies_data)
            in_file.seek(0)
            in_file.write(link_data)
            print("{} movies saved to movies.csv".format(len(list_movies_data)))
            break
        else:
            print("Invalid menu choice")

    # Close file
    in_file.close()

    """
    List movies data 
    """


def movies_listed(list_movies_data):
    # Find the longest title in the movie
    longest_title = max_length_data_found(list_movies_data)
    # Print the list of movies in movies.csv
    listing_movie(list_movies_data, longest_title)


def max_length_data_found(list_movies_data):
    longest_title = 0
    for movies in list_movies_data:
        movies_data_split = movies.split(',')
        longest_title = len(movies_data_split[0]) if longest_title < len(movies_data_split[0]) else longest_title

    return longest_title


def listing_movie(raw_data, longest_title):
    watched_amount = 0
    for index, movies in enumerate(raw_data, start=1):
        movies_data_split = movies.split(',')
        mark = '*' if 'u' in movies_data_split[3] else ''
        title = movies_data_split[0]
        year = movies_data_split[1]
        genre = movies_data_split[2]
        print('{0}. {1:< 2} {2:< {3}} - {4:< 4} ({5})'.format(index, mark, title, longest_title, year, genre))

        if not mark:
            watched_amount += 1

    unwatched_amount = len(raw_data) - watched_amount
    print("\n{} movies watched, {} movies still to watch".format(watched_amount, unwatched_amount))

    """
    Adding movies into data 
    """


def movies_added(list_movies_data):
    # Input movie info:
    title = title_add("Title: ")
    year = year_add()
    category = category_add("Category: ")

    # Input the info into list_movies_data:
    list_movie_data[0] += '\n'

    # Output: show movie added
    info_inputted = '{}, {}, {}'.format(title, year, category)
    list_movies_data.append(info_inputted)
    print('{} ({} from {}) added to movie list'.format(title, year, category))


def title_add(title_input):
    title_name = input(title_input)
    while not title_name.strip():
        print("Input cannot be blank")
        title_name = input(title_input)

    return title_name


def year_add():
    while True:
        try:
            movie_year = int(input('Year: '))
            if movie_year <= 0:
                raise Exception("Number must be >= 0")
            return movie_year
        except ValueError:
            print("Invalid input; enter a valid number")
        except Exception:
            print("Number must be >= 0")
            
            
def category_add(category_input):
    category_name = input(category_input)
    while not category_name.strip():
        print("Input cannot be blank")
        category_name = input(category_input)

    return category_name


"""
Input watched movie into data
"""


def movies_watching_choice(list_movies_data):
    print("Enter the number of movie to mark as watched")
    while True:
        try:
            check_movie_watch = watch_all(list_movies_data)
            if check_movie_watch:
                print("No more movies to watch!")
                return

            total_movie = int(input('>>> '))
            if total_movie not in range(1, len(list_movies_data) + 1):
                raise KeyError("Invalid movie number")

            movies_data_split = list_movies_data[total_movie - 1].split(',')

            if 'u' in movies_data_split[3]:
                # Replace u(unwatched) to w(watched)
                movies_data_split[3] = movies_data_split[3].replace('u', 'w')
                list_movies_data[total_movie - 1] = ','.join(movies_data_split)
                print('{} from {} watched'.format(movies_data_split[0], movies_data_split[1]))
            else:
                raise Exception("You have already watched {}".format(movies_data_split[0]))

            break
        except ValueError:
            print('Invalid input, enter a valid number')
        except KeyError:
            print('Your number of movie does not exist, try again')
        except Exception:
            print('You have already watched {}'.format(splited_data[0]))
            break


def watch_all(list_movies_data):
    check_movie_watch = True
    for movie in list_movies_data:
        movies_data_split = movie.split(',')
        if 'w' in movies_data_split[3]:
            check_movie_watch = True and check_movie_watch
        else:
            check_movie_watch = False

    return check_movie_watch


main()
