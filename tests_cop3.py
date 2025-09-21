from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content
from functions.write_file import write_file

def test():
    #result = get_files_content("calculator", "lorem.txt")
    #print("Result for lorem.txt:")
    #print(result)
    #print("")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print('next test')

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print('next test')

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    print('next test')
    




if __name__ == "__main__":
    test()