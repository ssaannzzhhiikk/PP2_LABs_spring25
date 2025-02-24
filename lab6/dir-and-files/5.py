def list_to_file(list_name, file_name):
     with open(file_name, "w") as file:
        for i in list_name:
            file.write(f"{i}\n")
