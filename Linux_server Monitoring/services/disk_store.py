output = """Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1       20G  8.5G   11G   43% /
tmpfs           484M     0  484M    0% /dev/shm"""

lines = output.splitlines()
print(lines)

headers = lines[0].split()
print(headers)

# Merge "Mounted on" into one header
headers[-1:] = ["Mounted on"]
print(headers)

headers[-2:] = ["Mounted on"]
print(headers)