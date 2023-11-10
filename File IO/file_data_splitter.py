filename = "output.txt"

fh = open(filename, "r")
out = open("metadata_1.csv", "w")
count = 0

for line in fh:
    if count == 1000000:
        count = 0
        out.close()
        out = open("metadata_2.csv", "w")

    line.replace('\t', ',')
    out.write(line)
    count += 1

fh.close()
out.close()