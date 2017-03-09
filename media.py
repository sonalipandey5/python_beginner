import webbrowser
class Movie():
    """This class provides a way to store movie related information""" #""" """ quotes are to used to add documentation the code
                                                                       
    VALID_RATINGS=("G","PG","PG-13","R") # if a variable is constand then the variable name should be in caps according to the google style check library.
    
    def __init__ (self,movie_title,movie_storyline,image,trailer_youtube): #self is the object being created which is toy_Story
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=image
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    
