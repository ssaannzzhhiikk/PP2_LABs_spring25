#snake case string to camel case string
import re

def SC_to_CC(txt):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), txt)

ex = "Alim_mila"

print(SC_to_CC(ex))