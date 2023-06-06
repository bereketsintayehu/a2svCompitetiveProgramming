class Solution:
    def decodeString(self, s: str) -> str:
        def decoder(string, i):
            decodedString = ""
            count = 0

            while i < len(string):
                if string[i].isdigit():
                    count = count * 10 + int(string[i])
                elif string[i] == '[':
                    substring, i = decoder(string, i + 1)
                    decodedString += count * substring
                    count = 0
                elif string[i] == ']':
                    return decodedString, i
                else:
                    decodedString += string[i]

                i += 1

            return decodedString
    
        return decoder(s, 0)