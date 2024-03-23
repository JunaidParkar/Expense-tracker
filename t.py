from prefixed import Float

def format_number_with_suffix(number):
    ns = str(number)
    na = [n for n in ns]
    print(na)
    if len(ns) > 3:
        num = ""
        li = len(na) - 3
        for i, n in enumerate(na):
            if i == li or i > li:
                return f"{num}K"
            num += n

# print(format_number_with_suffix(20000000000000000000000000000000000))
# print(len(str(20000)))
            
# print(format_number_with_suffix(20000))
            
# print(f'{Float(325000000006210125102):.2h}')
            
def format_number(number):
    # Define abbreviations and their corresponding thresholds
    abbreviations = [
        (1e33, 'Dc'), (1e30, 'Nn'), (1e27, 'O'), (1e24, 'Sp'), (1e21, 'Sx'),
        (1e18, 'Qi'), (1e15, 'Q'), (1e12, 'T'), (1e9, 'B'), (1e6, 'M'), (1e3, 'k')
    ]
    
    # Iterate through the abbreviations
    for threshold, suffix in abbreviations:
        if number >= threshold:
            # If the number is greater than or equal to the threshold, format it accordingly
            formatted_number = "{:.1f}{}".format(number / threshold, suffix)
            if len(formatted_number) <= 5:
                return formatted_number
            else:
                formatted_number = "{:.0f}{}".format(number / threshold, suffix)
                if len(formatted_number) <= 5:
                    return formatted_number
                else:
                    formatted_number = "{:.2f}{}".format(number / threshold, suffix)
                    return formatted_number
    
    # If the number is smaller than 1,000, don't apply any abbreviation
    return str(number)

# Test the function
followers = 100000000000000
formatted_followers = format_number(followers)
print("Followers:", formatted_followers)
