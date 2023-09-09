# Define the file names
input_file_name = "lemma.txt"
output_file_name = "5_letter_words2.txt"

# Read the input file and filter out 5-letter words
with open(input_file_name, 'r') as infile:
    # Read words, assuming one word per line
    words = infile.readlines()
    
    # Use a list comprehension to filter out 5-letter words
    five_letter_words = [word.strip() for word in words if len(word.strip()) == 5]

# Write the filtered words to the output file
with open(output_file_name, 'w') as outfile:
    for word in five_letter_words:
        outfile.write(word + '\n')

print(f"Extracted {len(five_letter_words)} 5-letter words and saved to {output_file_name}")
