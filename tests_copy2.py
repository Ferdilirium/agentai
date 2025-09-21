from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content

def test():
    #result = get_files_content("calculator", "lorem.txt")
    #print("Result for lorem.txt:")
    #print(result)
    #print("")

    result = get_files_content("calculator", "main.py")
    print("Result for main.py:")
    print(result)
    print("")

    result = get_files_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py:")
    print(result)
    print("")

    result = get_files_content("calculator", "/bin/cat")
    print("Result for /bin/cat:")
    print(result)
    print("")

    result = get_files_content("calculator", "pkg/does_not_exist.py")
    print("Result for pkg/does_not_exist.py:")
    print(result)
    print("")
    




if __name__ == "__main__":
    test()