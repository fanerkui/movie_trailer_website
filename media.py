import webbrowser


class Movie():
    """Record movie related information.
    Attributes:
        movie_title(str): Movie name.
        movie_storyline(str): Movie storyline.
        poster_image(str): Movie poster url.
        movie_title(str): Movie trailer url.
    """

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
