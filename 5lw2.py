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

# Regular expression to match standalone 5-letter words
pattern = r'\b[a-zA-ZæøåÆØÅ]{5}\b'

# Find all matches in the content
matches_with_duplicates = re.findall(pattern, content)

# Remove duplicates by converting to a set and back to a list
unique_matches = list(set(matches_with_duplicates))

# Write the unique matched words to a new file
with open('extracted_words2.txt', 'w') as output_file:
    for match in sorted(unique_matches):  # Optional: sorting the matches before writing
        output_file.write(match + '\n')

# Print the number of extracted unique words
print(f"Found {len(unique_matches)} unique five-letter words.")

