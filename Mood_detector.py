# Датчик настроения
# happy - :)
# bad - :(
# neutral - :|
# shouted  - :()
# nervous - :/

import random

MOOD_NUMBER = 5
HAPPY_MOOD = ":)"
BAD_MOOD = ":("
NEUTRAL_MOOD = ":|"
SHOUTED_MOOD = ":()"
NERVOUS_MOOD = ":/"

def detect_mood():
    number = random.randrange(MOOD_NUMBER)

    mood = HAPPY_MOOD   #default value

    if number == 0:
        mood = BAD_MOOD
    elif number == 1:
        mood = NEUTRAL_MOOD
    elif number == 2:
        mood = SHOUTED_MOOD
    elif number ==3:
        mood = NERVOUS_MOOD
    return mood

def main():
    msg = f"Your mood is{detect_mood()}"
    print(msg)

main()
