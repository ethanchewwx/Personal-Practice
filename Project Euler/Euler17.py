number_dict = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
               30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
               100: "hundred", 1000: "onethousand"}

number_list_words = []
total = 0

for number in range(1, 1001):
    hundredth_digit = (number / 100).__floor__()
    tenth_digit = ((number - hundredth_digit * 100)/10).__floor__()
    last_digit = number - hundredth_digit * 100 - tenth_digit * 10
    last_two_digits = number - hundredth_digit * 100
    if hundredth_digit > 0:
        if number == 1000:
            number_list_words.append(number_dict[1000])
        elif hundredth_digit * 100 == number:
            number_list_words.append(number_dict[hundredth_digit] + number_dict[100])
        elif last_two_digits == tenth_digit ** 10 or last_two_digits < 20:
            number_list_words.append(number_dict[hundredth_digit] + number_dict[100] + "and" + number_dict[last_two_digits])
        else:
            number_list_words.append(number_dict[hundredth_digit] + number_dict[100] + "and" + number_dict[tenth_digit * 10] + number_dict[last_digit])
    elif number in number_dict.keys():
        number_list_words.append(number_dict[number])
    else:
        number_list_words.append(number_dict[tenth_digit * 10] + number_dict[last_digit])

print(number_list_words)

for words in number_list_words:
    total += len(words)
print(total)