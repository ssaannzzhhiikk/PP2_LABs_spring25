import re

def ins_spc(a):
    return re.sub(r'([A-Z])', r' \1', a)

print(ins_spc("almAtt"))