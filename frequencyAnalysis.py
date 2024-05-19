def frequency_analysis(text):
    # Sanitize the input text: remove non-alphabetic characters and convert to uppercase
    text = ''.join(filter(str.isalpha, text.upper()))
    
    # Initialize a dictionary to store the frequency of each letter
    frequency_dict = {}
    
    # Count the frequency of each letter in the text
    for char in text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    # Find the most frequent character
    most_frequent_char = max(frequency_dict, key=frequency_dict.get)
    
    return most_frequent_char

# Example usage
text = "HELLO WORLD"
most_frequent_char = frequency_analysis(text)

print(f"Most Frequent Character: {most_frequent_char}")
