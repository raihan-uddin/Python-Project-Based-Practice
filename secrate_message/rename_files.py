import os

folder_path = r"F:\PycharmProjects\UdacityPythonPractice\secrate_message\prank\prank"
def rename_files():
    #(1) get file names for a folder
    file_list = os.listdir(folder_path);
    # print(file_list)
    saved_path = os.getcwd()
    print("Current Woring Directory is " + saved_path)
    os.chdir(folder_path)

    #(2) for each file, rename filename
    for file_name in file_list:
        try:
            os.rename(file_name, file_name.translate(str.maketrans('','','0123456789')))
        except:
            print("Error file not found!")
rename_files()