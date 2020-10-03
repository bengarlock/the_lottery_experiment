import random
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

def gen_numbers():
    numbers = []
    while len(numbers) < 6:
        num = random.randint(1, 69)
              #rand(1..69) in ruby!
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)


def win_the_lottery(winning_numbers):
    user_numbers = gen_numbers()
    total_losses = 1
    highest_match = 0
    while user_numbers != winning_numbers:
        match = 0
        user_numbers = gen_numbers()
        total_losses += 1
        for number in user_numbers:
            if number in winning_numbers:
                match += 1
        if match > highest_match:
            highest_match = match

        total_losses_formatted = locale.format_string("%d", total_losses, grouping=True)
        print("Highest Match: {}. Ticket Match: {}. Tickets Purchased: {}   {}{}"
              .format(highest_match, match, total_losses_formatted, user_numbers, winning_numbers))

    return "You won after {} tries".format(total_losses_formatted)

print(win_the_lottery(gen_numbers()))