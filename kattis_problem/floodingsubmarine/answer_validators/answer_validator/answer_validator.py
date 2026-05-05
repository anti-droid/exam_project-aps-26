import sys
import re

output = sys.stdin.readline()
if not re.fullmatch(r"[1-9][0-9]*", output):
    print("answer is not a valid number")
    sys.exit(43)

sys.exit(42)