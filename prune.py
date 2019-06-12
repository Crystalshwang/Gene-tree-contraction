if __name__ == "__main__":
    '''
    This is how we handle loading the input dataset, running pruning functions, and outputting the results
    '''
    # parse user arguments
    import argparse
    import treeswift
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--tree', required=False, type=str, default='stdin', help="Input Tree File (Newick)")
    parser.add_argument('-v', '--value', required=False, type=float, default=1.0, help="Support value")
    parser.add_argument('-o', '--output', required=False, type=str, default='stdout', help="Output Tree After Pruning")
    args = parser.parse_args()

    # load input tree
    from treeswift import read_tree_newick
    if args.tree == 'stdin':
        from sys import stdin
        trees = read_tree_newick(stdin)
    else:
        trees = read_tree_newick(args.tree)
    # give threshold value
    if args.value == 1:
        value = stdin.read()
    else:
        value = args.value
    # prune the tree based on the threshold
    for tree in trees:
        tree.contract_low_support(value)

    # write output tree
    if args.output == 'stdout':
        from sys import stdout as outfile
    else:
        outfile = open(args.output,'w')
    for tree in trees:
        outfile.write(tree.newick()+'\n')
    outfile.close()
