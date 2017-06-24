import media
import fresh_tomatoes
# ToyStory
toy_story = media.Movie("Toystory",
                        "a story of boy",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# Avatar Movie
avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_QL50_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# xXx: Return of Xander Cage
xxx = media.Movie("xXx: Return of Xander Cage",
                  "Xander Cage is left for dead after an incident, though he secretly returns to action for a new tough assignment with his handler Augustus Gibbons.",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMzcwMjkxMzQ3NV5BMl5BanBnXkFtZTgwMzgyNDA5MDI@._V1_QL50_SY1000_CR0,0,640,1000_AL_.jpg",
                  "https://www.youtube.com/watch?v=-ziu6JzJTZ0")

# Guardians of the Galaxy Vol. 2
ggv2 = media.Movie("Guardians of the Galaxy Vol. 2 ",
                   "The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill's true parentage.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=dW1BIid8Osg")

movie = [toy_story, avatar, xxx, ggv2]
fresh_tomatoes.open_movies_page(movie)
