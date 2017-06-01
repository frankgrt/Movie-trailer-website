import media
import fresh_tomatoes

# 6 instance of most liked movies.
moana = media.Movie("MOANA",
                    "mythic adventure set around 2000 years ago and across \
                     series of islands in the South Pacific",
                    "https://www.tribute.ca/tribute_objects/images/movies/moana/moana-poster-lg.jpg",  # noqa
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

sideways = media.Movie("SIDEWAYS",
                       "road trip through Santa Ynez Valley wine country",
                       "http://static.rogerebert.com/uploads/movie/movie_poster/sideways-2004/large_tojQbn3H4UcM8lkuns1E7CnLv8D.jpg",  # noqa
                       "https://www.youtube.com/watch?v=Pqbz8yojxBY")

matrix = media.Movie("MATRIX",
                     "A computer hacker learns from mysterious rebels about \
                     the true nature of his reality and his role in the war \
                     against its controllers. ",
                     "https://neo1210.files.wordpress.com/2010/09/matrix_movie1.jpg",  # noqa
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

becoming_jane = media.Movie("BECOMING JANE",
                            "A biographical portrait of a pre-fame Jane \
                            Austen and her romance with a young Irishman. ",
                            "http://image.tmdb.org/t/p/original/k4QuGUDAzeFcnS2N7rWn1D5JnQs.jpg",  # noqa
                            "https://www.youtube.com/watch?v=qmd-ej9Hx20")

notting_hill = media.Movie("NOTTING HILL",
                           "The life of a simple bookshop owner changes when \
                           he meets the most famous film star in the world. ",
                           "https://goddessella.files.wordpress.com/2012/03/notting-hill1.jpg",  # noqa
                           "https://www.youtube.com/watch?v=4RI0QvaGoiI")

minions = media.Movie("MINIONS",
                      "Ever since the dawn of time, the Minions have lived to \
                      serve the most despicable of masters. ",
                      "http://www.flickeringmyth.com/wp-content/uploads/2015/06/minions-poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=eisKxhjBnZ0")

# including instance name in a list
movies = [moana, sideways, matrix, becoming_jane, notting_hill, minions]

# Create and open html page
fresh_tomatoes.open_movies_page(movies)
