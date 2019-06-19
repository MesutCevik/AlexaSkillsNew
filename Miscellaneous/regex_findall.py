import re
from math import sin

my_task = "sin(30)"

if "sin" in my_task:
    sin_num_str = re.findall('[0-9]+', my_task)
    sin_num_float = float(sin_num_str[0])
    print(sin_num_float)

