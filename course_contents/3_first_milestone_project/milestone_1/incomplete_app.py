# Incomplete app!


movies = []


# You may want to create a function for this code
title = input("Enter the movie title: ")
director = input("Enter the movie director: ")
year = input("Enter the movie release year: ")
MENU_PROMPT = movies[a]
movies.append({
    'title': title,
    'director': director,
    'year': year
})


# Create other functions for:
# list of movies
for movie in movies:
    movies = movie['title']['director']['year']
    print(f" the list of movies are {title}: {director}: {year}.")
#   - finding movies
title = input["Enter the title of the movie:"]
print(f" {title}, {[director]}, {[year]}, :")


# And another function here for the user menu
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        pass
    elif selection == "l":
        pass
    elif selection == "f":
        pass
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
