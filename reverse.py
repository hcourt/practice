#should be O(n)
def reverse (string):
    new = ""
    for l in string:
        new = l + new
    return new
