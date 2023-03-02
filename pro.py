import os

from_dir = os.path.expanduser("~/Downloads")
to_dir = os.path.expanduser("~/Document_Files")

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + extension[1:].upper() + "_Files"
        path3 = to_dir + '/' + extension[1:].upper() + "_Files" + '/' + file_name

        if not os.path.exists(path2):
            os.makedirs(path2)

        print(f"Moving {file_name} to {path2}")
