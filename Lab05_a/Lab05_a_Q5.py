input_line = input("Enter a line of text: ")

letter_counts = {}

for char in input_line:
    if char.isalpha():
        if char not in letter_counts:
            letter_counts[char] = 1
        else:
            letter_counts[char] += 1

with open("result.txt",'w') as f:
    for letter, count in letter_counts.items():
        f.write(f"The letter '{letter}' appears {count} times\n")
