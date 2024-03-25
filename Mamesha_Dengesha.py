import time
import sys

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()  # Newline after the message

def mamesha_recommender():
    movies = ['Beekeeper', 'Dune Part 2', 'Boy and the Heron', 'The Kill Room', 'Midsommar']
    introduction_lines = [
        "Hello, I'm Mamesha, The Movie Buff!",
        "I only recommend movies I like.",
        "Choose a movie from my list, and remember to dress up because I consider this a date!"
    ]

    for line in introduction_lines:
        print_slow(line)
        time.sleep(1)

    first_attempt = True
    while movies:
        print("\nHere are my movie recommendations:")
        for movie in movies:
            print(f"- {movie}")
            time.sleep(1)

        choice = input("\nWhich one would you like to watch? (Type the movie name exactly) ")

        if choice in movies:
            print_slow(f"\n{choice} is the best, love me please!")
            movies.remove(choice)
            time.sleep(1)

            print("\nHere is the updated list of movies:")
            for movie in movies:
                print(f"- {movie}")
            time.sleep(1)

            if movies:
                print_slow("Can we watch another one tonight?")
                print_slow("I'm a bit needy and need you beside me, is that okay? (Y/N)")
                another = input().strip().upper()

                if another == 'Y':
                    print_slow("Neenu Naanu gupchup gupchup aadona?")
                else:
                    print_slow("Yaaru nan jothe aataadala, naanu wastuu.")
                    time.sleep(2)
                    break  # Exit the loop to let Dengesha take over
            else:
                print_slow("\nYou've watched all my favorites, I'm so happy! Thank you for loving me.")
                break  # Exit the loop to let Dengesha take over
        else:
            if first_attempt:
                print_slow("\nPlease choose only from the list, then only I will be happy.")
                first_attempt = False
            else:
                print_slow("\nHow dare you not choose from my list again! I'm really upset now!")
                print_slow("\nNo movies for you from me, watch whatever you want!")
                time.sleep(2)
                break  # Exit the loop to let Dengesha take over

    # After Mamesha's interaction, Dengesha takes over
    
    dengesha_recommender()

def dengesha_recommender():
    introduction_lines = [
        "Don't leave yettttt! Wait....Hello! I am Dengesha, I support you in your movie choices, unlike Mamesha.",
        "I will watch whatever you are comfortable with."
    ]

    for line in introduction_lines:
        print_slow(line)
        time.sleep(1)

    print_slow("\nPlease let me know a movie name or if you don't have any recommendation (Y/N): ")
    has_recommendation = input().strip().upper()

    if has_recommendation == 'Y':
        movie_choice = input("Great! Which movie would you like to watch? ")
        print_slow(f"\nI am excited, hope you are as I am about watching {movie_choice}! Let me get some pop corn, coming soon")
    else:
        alternative_movies = ['Dunki', 'Guntur Kaaram', 'The Nun Part 2', 'Side A', 'Love is Blind']
        print("\nWe could watch the following movies:")
        for movie in alternative_movies:
            print(f"- {movie}")
            time.sleep(1)

        choice = input("\nWhich one would you like to watch? (Type the movie name exactly) ")

        responses = {
            'Dunki': "Bade bade desho mein aisi ache ache movies dekhni hothi hai.",
            'Guntur Kaaram': "Nuvvu Mahesh Babu fan ah?, nenu kuda.",
            'The Nun Part 2': "Could we get closer? I am a little frightened of horror.",
            'Side A': "Preethi preethi yella preethi ye.",
            'Love is Blind': "I love me some drama too."
        }

        print_slow(f"\n{responses.get(choice, 'Great choice! getting some popcorn')}")
        alternative_movies.remove(choice)

        print_slow("\nGetting some popcorn, Maybe we watch the rest in the list below next time!:")
        for movie in alternative_movies:
            print_slow(f"- {movie}")
        print_slow("\nthis is how you get someone to watch a movie, cry now, Mamesha")

mamesha_recommender()
