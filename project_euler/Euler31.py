# coins_list = [2, 5, 10, 20, 50, 100, 200]
coins_list = [2, 5, 10, 20]
amount_to_make = 20
total_possibilities = 1
first_coin = coins_list[0]

# for i in range(0, len(coins_list)):
#     coin = coins_list[i]
#     previous_coin = coin
#     previous_index = i
#     possibilities = amount_to_make//coin
#     if coin == 2:
#         total_possibilities += possibilities
#     else:
#         for no_of_coins in range(0, possibilities):
#             remaining_amount = amount_to_make - (no_of_coins + 1) * coin
#             new_remaining_amount_list = []
#             if remaining_amount == 0:
#                 total_possibilities += 1
#             else:
#                 new_remaining_amount = remaining_amount
#                 while previous_coin != first_coin:
#                     previous_index -= 1
#                     previous_coin = coins_list[previous_index]
#                     possibilities_prev_coin = new_remaining_amount//previous_coin + 1
#                     for no_of_prev_coin in range(0, possibilities_prev_coin):
#                         new_remaining_amount = remaining_amount - (no_of_prev_coin + 1) * previous_coin
#                         if new_remaining_amount == 0:
#                             total_possibilities += 1
#                         else:
#                             new_remaining_amount_list.append(new_remaining_amount)
#                     # total_possibilities += remaining_amount//previous_coin

# for i in range(0, len(coins_list)):
#     coin = coins_list[i]
#     previous_index = i - 1
#     previous_coin = coin
#     possibilities = amount_to_make//coin
#     total_possibilities += possibilities
#     if i != 0:
#         for no_of_coins in range(1, possibilities + 1):
#             remaining_amount = amount_to_make - no_of_coins * coin
#             new_remaining_amount = remaining_amount
#             if remaining_amount != 0:
#                 for prev_coin_index in range(i-1, -1, -1):
#                     previous_coin = coins_list[prev_coin_index]
#                     possibilities_prev_coin = remaining_amount//previous_coin
#                     for
                # while True:
                #     previous_coin = coins_list[previous_index]
                #     possibilities_prev_coin = new_remaining_amount//previous_coin
                #
                #     for no_of_prev_coins in range(1, possibilities_prev_coin + 1):


