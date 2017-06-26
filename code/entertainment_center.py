# coding = utf-8

import media
import fresh_tomatoes

# ToyStory
toy_story = media.Movie("Toystory",
                        "a story of boy",
                        "https://goo.gl/JE1sMa",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar Movie
avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on \
                     unique mission becomes torn between following his orders \
                     and protecting the world he feels is his home.",
                     "https://goo.gl/W5WssM",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# xXx: Return of Xander Cage
xxx = media.Movie("xXx: Return of Xander Cage",
                  "Xander Cage is left for dead after an incident, though he \
                  secretly returns to action for a new tough assignment with \
                  his handler Augustus Gibbons.",
                  "https://goo.gl/oBa9sd",
                  "https://www.youtube.com/watch?v=-ziu6JzJTZ0")

# Guardians of the Galaxy Vol. 2
ggv2 = media.Movie("Guardians of the Galaxy Vol. 2 ",
                   "The Guardians must fight to keep their newfound family \
                   together as they unravel the mystery of Peter Quill's true \
                   parentage.",
                   "https://goo.gl/TBcLxn",
                   "https://www.youtube.com/watch?v=dW1BIid8Osg")

# making the list of all media.Movie object
movie = [toy_story, avatar, xxx, ggv2]
# movie list pass through open_movie_page
fresh_tomatoes.open_movies_page(movie)
