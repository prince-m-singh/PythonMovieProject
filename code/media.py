import webbrowser

"""movie class having 4 argument 1. movie_title:- passing movie name
2. movie_storyline:- passing only story line in one line
3. poster_image:- passing url of poster of movie
4. trailer_youtube:- passing the youtube url of movie trailer"""


class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# this function open trailer of movie in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
