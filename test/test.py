def solution(message, k):
    ret = ''
    words = message.split(' ')
    for word in words:
        if len(ret) >= k:
            return ret.strip()
        else:
            character_length = len(word)
            if character_length > k:
                return ret.strip()
            else:
                if len(ret) + len(word) > k:
                    return ret.strip()
                else:
                    ret += word
                    ret += ' '
        length_ret = len([i for i in ret.split() if i != ' '])
        if length_ret == len(words):
            return ret.strip()


text = "Codility We test coders"
number = 14

# text = "Why not"
# number = 100

# text = "The quick brown fox jumps over the lazy dog"
# number = 39

# text = "To crop or not to crop"
# number = 21

print(solution(text, number))
