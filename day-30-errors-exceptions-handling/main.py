try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist in dictionary")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    raise TypeError("This is an error I made up")
    print("test")
