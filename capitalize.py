# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    temp = []

    for word in words:
        if word != '':
            word = list(word)
            word[0] = word[0].upper()
            word = "".join(word)
        temp.append(word)

    s = " ".join(temp)
    print(s)
    return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    # s = 'hello world'
    s = 'j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'
    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
