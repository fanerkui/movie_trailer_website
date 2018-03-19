import media
import fresh_tomatoes

"""Create some specific movie instance.
"""
star_wars_the_last_jedi = media.Movie("Star Wars: The Last Jedi",
                                      "The Last Jedi, the \
                                      Skywalker saga continues.",
                                      "https://upload.wikimedia.org/wikipedia/"
                                      "en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                                      "https://www.youtube.com/"
                                      "watch?v=Q0CbN8sfihY")
co_co = media.Movie("Coco",
                    "The real story behind Miguel's family history.",
                    "https://upload.wikimedia.org/wikipedia/"
                    "en/9/98/Coco_%282017_film%29_poster.jpg",
                    "https://www.youtube.com/"
                    "watch?v=Ga6RYejo6Hk")

jumanji_welcome_to_the_jungle = media.Movie("Jumanji: Welcome to the Jungle",
                                            "Jungle games adventure",
                                            "https://upload.wikimedia.org/"
                                            "wikipedia/en/d/dc/Jumanji_"
                                            "Welcome_to_the_Jungle.png",
                                            "https://www.youtube.com/"
                                            "watch?v=2QKg5SZ_35I")


darkest_hour = media.Movie("Darkest Hour",
                           "Churchill's courage to lead changed \
                           the course of world history.",
                           "https://upload.wikimedia.org/wikipedia/"
                           "en/3/38/Darkest_Hour_poster.png",
                           "https://www.youtube.com/"
                           "watch?v=LtJ60u7SUSw")

the_shape_of_water = media.Movie("The Shape of Water",
                                 "There was an emotion between \
                                 Elsa and the monster",
                                 "https://upload.wikimedia.org/"
                                 "wikipedia/en/3/37/"
                                 "The_Shape_of_Water_%28film%29.png",
                                 "https://www.youtube.com/"
                                 "watch?v=XFYWazblaUA")


call_me_by_your_name = media.Movie("Call Me by Your Name",
                                   "The raging passion broke through the line \
                                   of defense between Elliot and Oliver, and \
                                   the two began a romantic relationship that \
                                   was doomed to fail.",
                                   "https://upload.wikimedia.org/wikipedia/"
                                   "en/c/c9/CallMeByYourName2017.png",
                                   "https://www.youtube.com/"
                                   "watch?v=Z9AYPxH5NTM")

movies = [co_co,
          darkest_hour,
          the_shape_of_water,
          jumanji_welcome_to_the_jungle,
          call_me_by_your_name,
          star_wars_the_last_jedi]

fresh_tomatoes.open_movies_page(movies)
