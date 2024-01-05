from read import text

def write():
    f =open('pdf/Text/Example.txt', 'w')

    with open('pdf/Text/Example.txt', 'w') as f:
        f.write(text)
