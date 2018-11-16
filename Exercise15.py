def word(text):
    return input(text)
    
def create_list(text):
    return text.split()
    
def reverse(list):
    return list[::-1]

reverse(create_list(word('Please provide your input text')))
