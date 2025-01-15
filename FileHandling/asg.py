# # Read grades from grades.txt file and calculate total, count, and average

# def main():
#     try:
#         # Open the file in read mode
#         with open("grades.txt", "r") as file:
#             # Read all lines and convert them to a list of integers
#             grades = [int(line.strip()) for line in file if line.strip().isdigit()]

#         # Display individual grades
#         print("Grades:")
#         for grade in grades:
#             print(grade)

#         # Calculate total, count, and average
#         total = sum(grades)
#         count = len(grades)
#         average = total / count if count > 0 else 0

#         # Display the results
#         print("\nTotal:", total)
#         print("Count:", count)
#         print("Average:", average)

#     except FileNotFoundError:
#         print("Error: The file 'grades.txt' was not found.")
#     except ValueError:
#         print("Error: Could not convert one or more lines to an integer.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()



# def count_words_in_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             content = file.read()
#             words = content.split()  # Split the content into words
#             word_count = len(words)  # Count the number of words
#             print(f"Total number of words in the file '{file_name}': {word_count}")
#     except FileNotFoundError:
#         print(f"The file '{file_name}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # File to be processed
# file_name = 'sample.txt'

# # Call the function
# count_words_in_file(file_name)



# import json

# def safely_deserialize_json(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             # Attempt to load JSON data
#             data = json.load(file)
#             print("JSON data successfully loaded.")
#             print("Deserialized Data:", data)
#     except json.JSONDecodeError as e:
#         print(f"Error: Invalid JSON data in file '{file_name}'. Details: {e}")
#     except FileNotFoundError:
#         print(f"Error: File '{file_name}' not found.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Test with a valid JSON file
# print("Testing with valid JSON:")
# safely_deserialize_json('data.json')

# # Test with an invalid JSON file
# print("\nTesting with invalid JSON:")
# safely_deserialize_json('invalid_data.json')






# def count_words_and_vowels(file_name):
#     vowels = "aeiouAEIOU"
#     try:
#         with open(file_name, 'r') as file:
#             content = file.read()
            
#             # Counting words
#             words = content.split()
#             word_count = len(words)
            
#             # Counting vowels
#             vowel_count = sum(1 for char in content if char in vowels)
            
#             print(f"Number of words in the file '{file_name}': {word_count}")
#             print(f"Number of vowels in the file '{file_name}': {vowel_count}")
#     except FileNotFoundError:
#         print(f"The file '{file_name}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# file_name = 'file1.txt'
# count_words_and_vowels(file_name)


# import re

# def extract_unique_emails(input_file, output_file):
#     try:
#         with open(input_file, 'r') as file:
#             content = file.read()
            
#             # Regular expression to match email addresses
#             email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#             emails = re.findall(email_pattern, content)
            
#             # Extract unique emails
#             unique_emails = sorted(set(emails))
        
#         # Write unique emails to the output file
#         with open(output_file, 'w') as file:
#             for email in unique_emails:
#                 file.write(email + '\n')
        
#         print(f"Unique email addresses have been extracted and saved to '{output_file}'.")
    
#     except FileNotFoundError:
#         print(f"The file '{input_file}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_file = 'sample.txt'
# output_file = 'unique_emails.txt'
# extract_unique_emails(input_file, output_file)
