import random
import time
import sys

# Large categorized word list
word_categories = {
    "Animals": [
        "elephant", "giraffe", "kangaroo", "lion", "tiger", "penguin", "dolphin", "owl",
        "butterfly", "crocodile", "zebra", "hippopotamus", "rabbit", "fox", "bear", "shark"
    ],
    "Objects": [
        "bicycle", "computer", "telephone", "clock", "guitar", "camera", "umbrella",
        "backpack", "lamp", "chair", "table", "book", "microscope", "pencil", "television"
    ],
    "Actions": [
        "running", "jumping", "swimming", "dancing", "cooking", "painting", "singing",
        "reading", "writing", "climbing", "flying", "sleeping", "driving", "laughing"
    ],
    "Places": [
        "beach", "mountain", "city", "forest", "desert", "restaurant", "school", "library",
        "park", "zoo", "museum", "airport", "stadium", "theater", "hospital"
    ],
    "Food": [
        "pizza", "hamburger", "pasta", "ice cream", "apple", "banana", "carrot", "chocolate",
        "bread", "cheese", "salad", "sushi", "cake", "sandwich", "tomato"
    ]
}

def clear_console():
    # Clear screen for better readability
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"Time Remaining: {timer}", end="\r")
        time.sleep(1)
    print("\nTime's up! Hope you guessed it!\n")

def get_random_word():
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    return word, category

def pictionary_game(rounds=5, time_per_round=120):
    clear_console()
    print("🎨 Welcome to Pictionary Game! 🎨\n")
    print(f"You will get {rounds} rounds, each with {time_per_round//60} minutes to draw the word.\n")
    print("Press Enter to start or type 'quit' anytime to exit.\n")

    for round_num in range(1, rounds + 1):
        user_input = input(f"Ready for Round {round_num}? (Press Enter to continue / type 'quit' to exit): ").strip().lower()
        if user_input == 'quit':
            print("Thanks for playing! Goodbye!")
            sys.exit()
        clear_console()

        word, category = get_random_word()
        print(f"Round {round_num} of {rounds}")
        print(f"Category: {category}")
        print(f"Your Pictionary word is:\n\n--> {word.upper()} <--\n")
        print(f"You have {time_per_round//60} minutes to draw it!\n")

        countdown_timer(time_per_round)
    
    print("🎉 All rounds completed! Thanks for playing! 🎉")

if __name__ == "__main__":
    # You can adjust rounds and time per round here
    pictionary_game(rounds=5, time_per_round=120)
      ss
