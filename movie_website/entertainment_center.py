from movie_website import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an aline planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=EzETGqZN6dU")
print(avatar.storyline)

avatar.show_trailer()