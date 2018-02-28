import media
import fresh_tomatoes

"""The entertainment center contains a library of movies to be displayed.
Each movie specifies the title, a movie poster url, and a Youtube link for
its movie trailer. Each of these movies are collected in a list to display
to the webpage.
"""

# Instantiate a few movies

home_alone = media.Movie("Home Alone",
                        "https://i.ytimg.com/vi/ZbqYIE4Nvy0/movieposter.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=CK2Btk6Ybm0")
inception = media.Movie("Inception",
                       "http://cdn01.cdn.justjared.com/wp-content/uploads/2010/05/dicaprio-inception/leo-dicaprio-inception-movie-poster-15.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=8hP9D6kZseM")
black_panther = media.Movie("Black Panther",
                           "http://thesource.com/wp-content/uploads/2018/01/7816401.3.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=xjDjIWPwcPU")
pink_panther = media.Movie("Pink Panther",
                          "https://occ-0-299-300.1.nflxso.net/art/adf73/da2740163ceaf78cbd9a46375d5edf90b09adf73.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=0CYYvYlYYbQ")
finding_nemo = media.Movie("Finding Nemo",
                          "https://vignette.wikia.nocookie.net/disney/images/e/e5/Finding_Nemo_-_Poster_2.jpg/revision/latest?cb=20160317165615",  # NOQA
                          "https://www.youtube.com/watch?v=wZdpNglLbt8")
wonder_woman = media.Movie("Wonder Woman",
                           "http://www.hedford.com/blog/wp-content/uploads/2016/12/wonder-woman-new-poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")
# Collection of all movies
movie_collection = [home_alone, inception, black_panther, pink_panther, finding_nemo, wonder_woman]  # NOQA

# Function to open movies HTML page with movie collection specified above
fresh_tomatoes.open_movies_page(movie_collection)

