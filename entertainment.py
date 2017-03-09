import fresh_tomatoes
import media


toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys which come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

logan = media.Movie("Logan", "A movie on marvel character wolverine",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI1MjkzMjczMV5BMl5BanBnXkFtZTgwNDk4NjYyMTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://www.youtube.com/watch?v=DekuSxJgpbY")
#logan.show_trailer()
movies =[toy_story, avatar, logan]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__) #__doc__ is used to print documentation part of any code added using """ """ .


