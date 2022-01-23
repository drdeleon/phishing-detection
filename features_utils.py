from urllib.parse import urlparse


def f1(url: str):
    """ Full URL length. """

    return len(url)

def f2(url: str):
    """ Hostname length. """

    return "{uri.netloc}".format(uri=urlparse(url))

def f4(url: str):
    """ Number of occurences of character '.' in URL. """

    return url.count('.')

def f5(url: str):
    """ Number of occurences of character '-' in URL. """

    return url.count('-')

def f6(url: str):
    """ Number of occurences of character '@' in URL. """

    return url.count('@')

def f7(url: str):
    """ Number of occurences of character '?' in URL. """

    return url.count('?')

def f8(url: str):
    """ Number of occurences of character '&' in URL. """

    return url.count('&')

def f9(url: str):
    """ Number of occurences of character '|' in URL. """

    return url.count('|')

def f10(url: str):
    """ Number of occurences of character '=' in URL. """

    return url.count('=')

def f11(url: str):
    """ Number of occurences of character '_' in URL. """

    return url.count('_')

def f12(url: str):
    """ Number of occurences of character '~' in URL. """

    return url.count('~')

def f13(url: str):
    """ Number of occurences of character '%' in URL. """

    return url.count('%')

def f14(url: str):
    """ Number of occurences of character '/' in URL. """

    return url.count('/')

def f15(url: str):
    """ Number of occurences of character '*' in URL. """

    return url.count('*')

def f16(url: str):
    """ Number of occurences of character ':' in URL. """

    return url.count(':')

def f17(url: str):
    """ Number of occurences of character ',' in URL. """

    return url.count(',')

def f18(url: str):
    """ Number of occurences of character ';' in URL. """

    return url.count(';')

def f19(url: str):
    """ Number of occurences of character '$' in URL. """

    return url.count('$')

def f20(url: str):
    """ Number of occurences of character '%20' or space in URL. """

    return url.count(' ')

def f25(url: str):
    """ Checks for HTTPS token in URL. """
    # TODO HTTPS token
    
    uri = urlparse(url)

def f26(url: str):
    """ Ratio of digits in full URL. """
    
    return 

def f27(url: str):
    """ Ratio of digits in hostname. """
    
    return
