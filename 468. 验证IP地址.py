class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            # val ipv4
            ips = IP.split('.')
            if len(ips) != 4:
                return "Neither"
            for a in ips:
                try:
                    if a.startswith('0') and len(a) != 1:
                        return "Neither"
                    elif int(a) < 0 or int(a) > 255:
                        return "Neither"
                except:
                    return "Neither"
            return "IPv4"

        elif ':' in IP:
            ips = IP.split(':')
            if len(ips) != 8:
                return "Neither"
            # val ipv6
            for a in IP.split(':'):
                if len(a) == 0 or len(a) > 4:
                    return "Neither"
                for aa in a:
                    if aa not in '0123456789abcdefABCDEF':
                        return "Neither"
                # if a.startswith('00'):
                #     return "Neither"
            return "IPv6"

        return "Neither"


print(Solution().validIPAddress('02001:0db8:85a3:0000:0000:8a2e:0370:7334'))