import numbers
from urllib.parse import urlparse
import re


def f1(url: str) -> int:
    """ Full URL length. """

    return len(url)

def f2(url: str) -> int:
    """ Hostname length. """

    hostname = "{uri.netloc}".format(uri=urlparse(url))

    return len(hostname)

def f4(url: str) -> int:
    """ Number of occurences of character '.' in URL. """

    return url.count('.')

def f5(url: str) -> int:
    """ Number of occurences of character '-' in URL. """

    return url.count('-')

def f6(url: str) -> int:
    """ Number of occurences of character '@' in URL. """

    return url.count('@')

def f7(url: str) -> int:
    """ Number of occurences of character '?' in URL. """

    return url.count('?')

def f8(url: str) -> int:
    """ Number of occurences of character '&' in URL. """

    return url.count('&')

def f9(url: str) -> int:
    """ Number of occurences of character '|' in URL. """

    return url.count('|')

def f10(url: str) -> int:
    """ Number of occurences of character '=' in URL. """

    return url.count('=')

def f11(url: str) -> int:
    """ Number of occurences of character '_' in URL. """

    return url.count('_')

def f12(url: str) -> int:
    """ Number of occurences of character '~' in URL. """

    return url.count('~')

def f13(url: str) -> int:
    """ Number of occurences of character '%' in URL. """

    return url.count('%')

def f14(url: str) -> int:
    """ Number of occurences of character '/' in URL. """

    return url.count('/')

def f15(url: str) -> int:
    """ Number of occurences of character '*' in URL. """

    return url.count('*')

def f16(url: str) -> int:
    """ Number of occurences of character ':' in URL. """

    return url.count(':')

def f17(url: str) -> int:
    """ Number of occurences of character ',' in URL. """

    return url.count(',')

def f18(url: str) -> int:
    """ Number of occurences of character ';' in URL. """

    return url.count(';')

def f19(url: str) -> int:
    """ Number of occurences of character '$' in URL. """

    return url.count('$')

def f20(url: str) -> int:
    """ Number of occurences of character '%20' or space in URL. """

    return url.count(' ')

def f25(url: str) -> bool:
    """ Checks for HTTPS token in URL. """
    # TODO HTTPS token
    
    scheme = urlparse(url).scheme
    return scheme == 'https'

def f26(url: str) -> float:
    """ Ratio of digits in full URL. """

    if (len(url) == 0):
        return 0.0

    numeric = len(re.sub("[^0-9]", "", url))
    
    return numeric / len(url)

def f27(url: str) -> float:
    """ Ratio of digits in hostname. """

    if (len(url) == 0):
        return 0.0

    hostname = urlparse(url).netloc
    numbers = len(re.sub("[^0-9]", "", hostname))
    
    return numbers / len(hostname)
