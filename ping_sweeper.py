import sys
import os

ip = str(sys.argv[1])
start = int(sys.argv[2])
end = int(sys.argv[3])

for x in range(start, end+1):
    response = os.system(f"ping -c 1 {ip}.{x} > /dev/null")
    if response == 0:
        print(f"{ip}.{x}")
