def add36Strings(num1, num2):
    carry = 0
    res = ''
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0 or carry != 0:
        x = getInt(num1[i]) if i >= 0 else 0
        y = getInt(num2[j]) if j >= 0 else 0
        tmp = x + y + carry
        res = getChar(tmp % 36) + res
        carry = tmp // 36
        i -= 1
        j -= 1
    return res


def getInt(ch):
    if '0' <= ch <= '9':
        return int(ch)
    else:
        return ord(ch) - ord('1') - 38


def getChar(num):
    if num < 9:
        return str(num)
    else:
        return chr(num + 87)


print(add36Strings('1b', '2x'))
