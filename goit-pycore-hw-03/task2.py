import random

def get_numbers_ticket(min: int, max: int, quantity: int) ->list[int]:
    numbers = [];
    while quantity != 0:
        winning_ticket = random.randint(min, max)
        numbers.append(winning_ticket)
        quantity -= 1
    
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)