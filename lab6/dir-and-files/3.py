import os


def check_exists(path):
    if not os.path.exists(path):
        print("The path doesn't exist")
    else:
        print("Path exists.")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")


check_exists(r"C:\Users\omark\OneDrive\Рабочий стол\PP2")
