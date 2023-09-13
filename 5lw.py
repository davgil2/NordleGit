import re
import chardet

# Read the file in binary mode
with open('fullformsliste.txt', 'rb') as file:
    raw_data = file.read()

# Use chardet to detect the file's encoding
result = chardet.detect(raw_data)
encoding = result['encoding'] if result['encoding'] else 'utf-8'

# Decode the raw data using the detected encoding, replacing any invalid characters
content = raw_data.decode(encoding, errors='replace')

# Regular expression to match 5-letter words after a '-'
pattern = r'-(\w{5})\b'

# Find all matches in the content and remove duplicates by converting to a set and back to a list
matches = list(set(re.findall(pattern, content)))

# Write the unique matched words to a new file
with open('extracted_words.txt', 'w') as output_file:
    for match in sorted(matches):  # Optional: sorting the matches before writing
        output_file.write(match + '\n')

# Print the number of extracted words
print(f"Found {len(matches)} unique five-letter words.")
