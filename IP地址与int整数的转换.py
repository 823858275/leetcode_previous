# 将ip地址转换成10进制整数。
# 例如，ip地址为10.0.3.193，把每段拆分成一个二进制形式组合起来为00001010 00000000 00000011 11000001，然后把这个二进制数转变成十进制整数就是167773121。

"""
将ip地址四个模块依次平移 然后求或
"""

def ipToInt(ip):
    ipList = ip.split(".")
    seg0 = int(ipList[0]) << 24
    seg1 = int(ipList[1]) << 16
    seg2 = int(ipList[2]) << 8
    seg3 = int(ipList[3])
    return seg0 | seg1 | seg2 | seg3
