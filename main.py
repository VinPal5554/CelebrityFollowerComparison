import art
import random
from game_data import data

# create a final score that increments when they are correct

final_score = 0
still_playing = True

# Randomly pick two celebrities for comparison

def generate_celebrity(my_data):
    rand_index = random.randint(0, len(my_data) - 1)
    chosen_celebrity = my_data[rand_index]
    return chosen_celebrity

def check_player_correct(choice):
    if choice == 'A' and celebrity_a_followers > celebrity_b_followers or choice == 'B' and celebrity_b_followers > celebrity_a_followers:
        return True
    else:
        return False



# Structure comparison to print in appropriate format

celebrity_a = generate_celebrity(data)   # CHECK THAT CELEBRITIES ARE DIFFERENT
celebrity_b = generate_celebrity(data)

while still_playing:

    # Print ascii art
    print(art.logo)

    print(f"Compare A: {celebrity_a['name']}, a {celebrity_a['description']}, from {celebrity_a['country']}")
    print(art.vs)
    print(f"Compare B: {celebrity_b['name']}, a {celebrity_b['description']}, from {celebrity_b['country']}")

    celebrity_a_followers = celebrity_a['follower_count']
    celebrity_b_followers = celebrity_b['follower_count']

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    is_player_correct = check_player_correct(user_choice)
    # Regardless of choice console is cleared
    print("\n" * 20)

    # If correct choice set celebrity B as celebrity A
    if is_player_correct:
        final_score = final_score + 1
        print(f"You're right! Current score: {final_score}")

        # Previous B becomes new A
        celebrity_a = celebrity_b

        # randomly pick another celebrity for the new B
        celebrity_b = generate_celebrity(data)

    # if wrong choice print final score and stop choosing
    else:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        break

