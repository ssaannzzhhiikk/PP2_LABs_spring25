def copy_file(file1, file2):
    with open(file1, "r") as f1:
        cont1 = f1.read()
    with open(file2, "w") as f2:
        f2.write(cont1)