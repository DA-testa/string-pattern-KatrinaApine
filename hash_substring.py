# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp = input().rstrip()
    if inp == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
        
    if inp == 'F':
        with open("tests/06", 'r') as F:
            pattern = F.readline().rstrip()
            text = F.readline().rstrip()
    return pattern, text
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pl, tl = len(pattern), len(text)
    p = hash(pattern)
    t = hash(text[:pl])

    out = []
    
    for i in range (tl - pl + 1):
        if t = p and text[i:i+p_len] == pattern:
            out.append(i)
            
        if i + pl < tl:
            t = hash(text [i + 1:i + pl + 1])
    return out

    # and return an iterable variable
    # return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

