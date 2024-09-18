def reverse_string(s):
    """Inverte uma string."""
    return s[::-1]

def capitalize_words(s):
    """Capitaliza a primeira letra de cada palavra em uma string."""
    return ' '.join(word.capitalize() for word in s.split())
