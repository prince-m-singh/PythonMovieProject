# coding=utf-8

import webbrowser


class Movie():
    """
    This class provides a way to store movie related information
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        initialize instance of class Movie

        :param movie_title: title
        :param movie_storyline: storyline
        :param poster_image: poster_image_url
        :param trailer_youtube: trailer_youtube_url
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # this function open trailer of movie in browser
    def show_trailer(self):
        """
        initializing instance for opening the youtube video

        :return: webbrowser to play thriller
        """
        webbrowser.open(self.trailer_youtube_url)
