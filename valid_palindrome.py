def valid_palindrome_(sent):
    sent = sent.lower()
    # l = ""
    # for i in sent:
    #     if i.isalnum():
    #         l += i
    # return l == l[::-1]
    l = 0
    r = len(sent) - 1
    while l <= r:
        while l < r and not sent[l].isalnum():
            l += 1
        while r > l and not sent[r].isalnum():
            r -= 1
        if sent[l] != sent[r]:
            return False
        l += 1
        r -= 1
    return True


print(valid_palindrome_(" "))
