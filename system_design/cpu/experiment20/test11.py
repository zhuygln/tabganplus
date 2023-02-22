import time
def main():
    print("old name is john")
    new("harry")

def new(name):
    time.sleep(2)
    print("new name is", name)

main()