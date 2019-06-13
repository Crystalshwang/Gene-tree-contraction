
with open("41-45/45/bestMLestimatedgenetree_200/all-genes_200.phylip", 'r') as infile, \
    open("41-45/45/bestMLestimatedgenetree_200/edit-all-genes_45_200.phylip", 'w') as outfile:
    data = infile.read()
    data = data.replace("_0_0", "")
    outfile.write(data)
