def add_line_numbers(text):
    lines = text.split("\n")  # Split the text into individual lines
    numbered_lines = []

    for i, line in enumerate(lines, 1):
        numbered_line = f"{i}\t{line}"  # Add line number and tab character
        numbered_lines.append(numbered_line)

    modified_text = "\n".join(numbered_lines)  # Join the lines back into a single string
    return modified_text

#q1 and 2
file_path = "the-zen-of-python.txt"  # Replace with the actual file path

with open(file_path, "r") as file:
    text = file.read()  # Read the contents of the file

modified_text = add_line_numbers(text)  # Add line numbers to the text

#q3
output_file_path = "modified_text.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(modified_text)  # Write the modified text to the output file

print(modified_text)

#q4
def count_words(text):
    words = text.split()  # Split the text into words using whitespace as the delimiter
    total_words = len(words)  # Count the number of words
    return total_words

counting = count_words(text)
print(counting)

#q5
def largest_counts(text, count=3):
    words = text.split()  # Split the text into words
    word_lengths = [len(word) for word in words]  # Get the lengths of all words
    sorted_lengths = sorted(set(word_lengths), reverse=True)  # Sort unique word lengths in descending order
    largest_words = []

    for length in sorted_lengths[:count]:  # Get the 'count' largest word lengths
        largest_words += [word for word in words if len(word) == length]  # Find words with the current length

    return largest_words

largest_words = largest_counts(text, count=3)  # Find the words with the three largest character counts
print(largest_words)