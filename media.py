class Movie():

    """This class defines a movie.

    Attributes:
        movie_title (str): The title of the movie
        poster_url (str): The url to the movie poster
        youtube_link (str): The link to the movie trailer
    """

    # Movie constructor
    def __init__(self, movie_title, poster_url, youtube_link):
        self.title = movie_title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_link
