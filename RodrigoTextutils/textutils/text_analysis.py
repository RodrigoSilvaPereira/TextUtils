def word_count(text):
    """Conta o número de palavras em um texto."""
    return len(text.split())

def sentence_count(text):
    """Conta o número de sentenças em um texto, assumindo que as sentenças terminam com ponto, exclamação ou interrogação."""
    return text.count('.') + text.count('!') + text.count('?')
