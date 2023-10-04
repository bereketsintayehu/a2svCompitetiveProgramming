def swap_case(s):
    return ''.join([ch.upper() if ch.islower() else ch.lower() for ch in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
