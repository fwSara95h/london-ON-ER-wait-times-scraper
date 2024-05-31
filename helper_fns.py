def stripStr(str):
    '''
    This function removes extra whitespace from a string
    by splitting it into words
    and joining them back together with a single space.
    '''
    return ' '.join(c for c in str.split() if c)


def truncateIfLong(str, maxLen=45):
    '''
    This function truncates a string to a specified maximum length,
    adding '...' if the string is too long.
    '''
    if not isinstance(maxLen, int):
        maxLen = 15
    if maxLen < 4:
        maxLen = 5
    return str if len(str) < maxLen else str[:maxLen-3]+'...'


def miniStr(obj, lineSep=' ', wordSep=' ', trunc=None):
    '''
    This function
    - converts an object to a string,
    - removes extra whitespace,
    - joins lines and words with specified separators, and
    - optionally truncates the string.
    '''
    mStr = lineSep.join(
        wordSep.join(w for w in lx.split() if w)
        for lx in str(obj).splitlines() if lx.strip()
    )
    return truncateIfLong(mStr, trunc) if trunc else mStr


def reqStatus(r, isv=False, toRet=None):
    '''
    This function formats the status of an HTTP request as a string,
    including the status code, reason, elapsed time, and URL.
    Optionally, it can print the status and return a specific object.
    '''
    rs = f'<Response [{r.status_code} {r.reason}]> in {r.elapsed} from {r.url}'
    if isv:
        return (print(rs), r if toRet is None else toRet)[1]
    return rs
