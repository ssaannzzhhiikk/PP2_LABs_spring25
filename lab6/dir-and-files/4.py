def count_lines(file_name):
    txt = open("file_name", "r")
    lines = txt.readines()
    txt.close()
    return len(lines)

