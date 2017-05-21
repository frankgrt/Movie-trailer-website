import media
import fresh_tomatoes
moana = media.Movie("MOANA",
                    "mythic adventure set around 2000 years ago and across a series of islands in the South Pacific",
                    "https://www.tribute.ca/tribute_objects/images/movies/moana/moana-poster-lg.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

sideways = media.Movie("SIDEWAYS",
                    "A story of a boy and his toys",
                    "http://static.rogerebert.com/uploads/movie/movie_poster/sideways-2004/large_tojQbn3H4UcM8lkuns1E7CnLv8D.jpg",
                    "https://www.youtube.com/watch?v=Pqbz8yojxBY")






movies = [moana, sideways]
fresh_tomatoes.open_movies_page(movies)
