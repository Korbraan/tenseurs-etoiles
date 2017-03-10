def parseFile (fileName):
    """ Parse the file in param """
    with open(fileName, "r") as f:
        i = 0
        values = []
        for line in f:
            if i != 0:
                values.append(line.replace("\r\n", "").split("\t"))
            i += 1;
        return values
