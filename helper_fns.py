def stripStr(str):
    return ' '.join(c for c in str.split() if c)


def truncateIfLong(str, maxLen=45):
    if not isinstance(maxLen, int):
        maxLen = 15
    if maxLen < 4:
        maxLen = 5
    return str if len(str) < maxLen else str[:maxLen-3]+'...'


def miniStr(obj, lineSep=' ', wordSep=' ', trunc=None):
    mStr = lineSep.join(
        wordSep.join(w for w in lx.split() if w)
        for lx in str(obj).splitlines() if lx.strip()
    )
    return truncateIfLong(mStr, trunc) if trunc else mStr


def reqStatus(r, isv=False, toRet=None):
    rs = f'<Response [{r.status_code} {r.reason}]> in {r.elapsed} from {r.url}'
    if isv:
        return (print(rs), r if toRet is None else toRet)[1]
    return rs
