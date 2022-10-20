# DRAGON TASK
# Born with 3 heads
# 0....100  ---> 3HEADS PER YEAR
# 101...200 --> 2 HEADS PER YEAR
# > 200 ---> 1 HEAD

FIRST_PERIOD = 100
SECOND_PERIOD = 200


def calculate_dragon_head(age):
    if age < 1:
        return -1
    else:
        head = 3
        if age <= FIRST_PERIOD:
            head += age * 3
        elif age <= SECOND_PERIOD:
            head += FIRST_PERIOD * 3 + (age - FIRST_PERIOD) * 2
        else:
            head += (FIRST_PERIOD * 3 + (SECOND_PERIOD - FIRST_PERIOD) * 2
                     + age - SECOND_PERIOD)
        return head


def main():
    age = int(input("Input the dragon's age: "))

    head = calculate_dragon_head(age)

    msg = f"your dragon has {head} heads" if head > 0 else "Error age!!!"

    print(msg)


main()
