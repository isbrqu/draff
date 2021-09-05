import sys

lines1 = open(sys.argv[1]).read().splitlines()
lines2 = open(sys.argv[2]).read().splitlines()

missing = []
present = []

for line1 in lines1:
    lastname = line1.split(',', 1)[0]
    for line2 in lines2:
        if line2.startswith(lastname):
            present.append(line2)
            break
    else:
        missing.append(line1)

print('present:')
for p in present:
    print(p)

print('missing:')
for t in missing:
    print(t)
