def is_isbn_oe_key(word):
    '''
    :param word:
    :return:
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isgigit:
        isbn_or_key = 'isbn'
    return isbn_or_key