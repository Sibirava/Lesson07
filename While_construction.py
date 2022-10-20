def hello(count):
    str = ""
    while count > 0:
        str +="hello!!" +"\n"
        count -=1
    return str

def main():
    count = 3
    print(hello(count))

main()