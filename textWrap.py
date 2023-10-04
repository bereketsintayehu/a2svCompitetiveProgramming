import textwrap

def wrap(string, max_width):
    nString = ""
    i = 0
    
    while i < len(string):
        nString += string[i:i+max_width]
        nString += '\n'
        i += max_width
        
    return nString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
