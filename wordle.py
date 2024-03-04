"""Structured Wordle Exercise!"""

__author__ = "730662974"


def contains_char(word: str, single_char: str) -> bool: 
    """Returns true if string contains character."""
    assert len(single_char) == 1
    word_idx: int = 0
    while word_idx < len(word):
        if word[word_idx] == single_char:
            return True 
        word_idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emoji color box based on guess string."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    emoji_panel: str = ""
    while idx < len(guess):
        if contains_char(secret, guess[idx]) is False:
            emoji_panel += WHITE_BOX
        else:
            if guess[idx] == secret[idx]:
                emoji_panel += GREEN_BOX
            
            else:
                emoji_panel += YELLOW_BOX
        idx += 1                               

    return emoji_panel 


def input_guess(expected_length: int) -> str:
    """Returns the user's word input if the expected length is correct."""
    word_input: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(word_input):
        word_input = input(f"That wasn't {expected_length} chars! Try again: ")
    return word_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1
    secret_word: str = "codes" 
    guess: str = input_guess(len(secret_word))
    
    while turn_count < 6:
        print(f"=== Turn {turn_count}/6 ===")
        print(emojified(guess, secret_word))

        if guess == secret_word:
            print(f"You won in {turn_count}/6 turns!")
            return 
        else:
            turn_count += 1
            print(f"=== Turn {turn_count}/6 ===")
            guess = input_guess(len(secret_word))

    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()