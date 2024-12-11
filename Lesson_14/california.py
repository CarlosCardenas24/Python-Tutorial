from random import choice

capital = "Sacramento"

bird = "California Quail"

flower = "California Poppy"

song = "I Love You California"

def randomfunfact():
    funfacts = [
        "The state animal of California is extinct",
        "California has a higher population than Canada",
        "There are over 100,000 earthquakes each year in California",
        "California is home to the world's largest tree"
    ]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()