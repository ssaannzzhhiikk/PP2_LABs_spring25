import re

def CC_to_SC(a):
    return re.sub(r'([A-Z])', lambda m: "_"+m.group(1).lower(), a)
#r'_([a-z])', lambda m: m.group(1).upper(), txt)

print(CC_to_SC("aldMamLaa"))