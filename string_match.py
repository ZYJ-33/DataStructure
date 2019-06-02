def match1(partern, text):
    if partern == '':
        return False
    p = len(partern)
    t = len(text)
    i = j = 0
    while i < p and j < t:
        if partern[i] == text[j]:
            i += 1
            j += 1
        else:
            j -= i-1
            i = 0
    if j - i <= t - p :
        return True
    return False

def match2(partern, text):
    if partern == '':
        return False
    p_len = len(partern)
    t_len = len(text)
    point = forward = 0
    while point <= t_len - p_len:
        if partern[forward] == text[point + forward]:
            forward += 1
            if forward == p_len:
                break
        else:
            forward = 0
            point += 1
    if point <= t_len - p_len:
        return True
    return False


def forming_next_v1(partern):
    next = [-1]
    i = 1
    prefix_len = next[i - 1]
    while i < len(partern):
        if prefix_len < 0 or partern[i-1] == partern[prefix_len]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            prefix_len = next[prefix_len]
    return next

def forming_next_improve(partern):
    next = [-1]
    i = 1
    prefix_len = next[i - 1]
    while i < len(partern):
        if prefix_len < 0 or partern[i-1] == partern[prefix_len]:
            prefix_len += 1
            if partern[i] == partern[i-1]:
                next.append(next[i-1])
            else:
                next.append(prefix_len)
            i += 1
        else:
            prefix_len = next[prefix_len]
    return next


def forming_next(partern):
    return forming_next_improve(partern)

'''
def KMP_match(partern, text):
    next = forming_next(partern)
    i = j = 0
    while i < len(partern) and j < len(text):
        if i < 0 or partern[i] == text[j]:
            i += 1
            j += 1
        else:
            i = next[i]
    if i == len(partern):
        return j - i
    else:
        return None
'''

def construct_next(partern):
    next = [-1]
    i = 1
    prefix = next[i-1]
    while i < len(partern):
        if prefix < 0 or partern[i-1] == partern[prefix]:
            prefix += 1
            if partern[i] == partern[i-1]:
                next.append(next[i-1])
            else:
                next.append(prefix)
            i += 1
        else:
            prefix = next[prefix]
    return next


def KMP_match(partern, text):
    next = construct_next(partern)
    i = j = 0
    while j < len(partern) and i < len(text):
        if j < 0 or partern[j] == text[i]:
            j += 1
            i += 1
        else:
            j = next[j]
    if j == len(partern):
        return i - j
    else:
        return None



def culculate_value(string, len):
    k = 7
    sum = 0
    M = 1000
    i = 0
    index = 0
    bytes = bytearray(string, encoding="utf-8")
    firstclass = []
    for byte in bytes:
        firstclass.append(byte)
        sum = (sum + byte)*k % M
        firstclass = list(map(lambda x: x*k, firstclass))
        i += 1
        if i == len:
            yield index, sum
            index += 1
            i -= 1
            sum -= firstclass.pop(0)


def check_again(partern, substr):
    return partern == substr


def FP_match(partern, text):
    target = culculate_value(partern, len(partern))
    target = next(target)[1]
    gen = culculate_value(text, len(partern))
    for index, value in gen:
        if value == target:
            if check_again(partern, text[index: index+len(partern)]):
                    return index
    return None














if __name__ == "__main__":
    '''
    p = "aaa"
    t = "00001"
    pl = len(p)
    index = KMP_match(p, t)
    print(index)
    print(t[index:index+pl])
    '''
    '''
    t = "000101010000101010001"
    p = "001"
    result = KMP_match("001", "000101010000101010001")
    print(t[result:result+len(p)])
    '''
    print(FP_match("de", "abcde"))
