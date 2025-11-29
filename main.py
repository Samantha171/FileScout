import os
def creating_file():
    current_directory=input("Enter your path:")
    new_folder=input("Enter the new folder name:")
    path=os.path.join(current_directory,new_folder)
    os.makedirs(path)
    print(os.path.dirname(path))
    filename=input("enter the file name:")
    file=open(filename,"x")
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    file_path = os.path.join(new_folder, filename)
    file_inside=input("Enter the data to be added:")
    with open(file_path, 'w') as file:
        file.write(file_inside)
    print(f"File '{filename}' created inside folder '{new_folder}'.")
def search_file(directory, filename):

    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None
def search_word(word,folder_path):
    files_with_word = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, "r") as f:
                file_contents = f.read()
                if word in file_contents:
                    files_with_word.append(file_path)
        except PermissionError:
            print(f"Permission denied: {file_path}")
            continue

    return files_with_word
def search_word_in_directory(word, directory):
    files_with_word = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                with open(file_path, "r", errors='ignore') as f:
                    for line_number, line in enumerate(f, start=1):
                        if word in line:
                            files_with_word.append((file_path, line_number, line.strip()))
                            break 
    return files_with_word
def main():
    choice=0
    print("Wecome to File Systems!")
    while(choice!=4):
        choice=int(input("\tMENU\t\n1. Create a file,folder and write data into it\n2. Search a file in a directory\n3. Search a word in a file\n4.exit\nEnter your choice:"))
        if choice==1:
            creating_file()
        elif choice==2:
            directory_path = input("Enter the directory path to search within: ")
            file_name = input("Enter the file name to search for: ")
            found_file = search_file(directory_path, file_name)
            if found_file:
                print(f"The file '{file_name}' was found at: {found_file}")
            else:
                print(f"The file '{file_name}' was not found in the directory.")
        elif choice==3:
            word=input("Enter the word:")
            directory=input("Enter the directory you want to search for :")
            result = search_word_in_directory(word, directory)
            if result:
                print("The word ",word," was found in the following files:")
                for file_path, line_number, line in result:
                    print(f"File: {file_path}, Line {line_number}: {line}")
            else:
                print("The word ",word," was not found in any files.")
        elif choice==4:
            print("Thank you!")
        else:
            print("Invalid choice\n")
main()
