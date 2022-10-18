from collections import defaultdict
import csv
path = "input.csv"
import json

def ctree():
    return defaultdict(ctree)


def build_leaf(name, leaf):
    res = {"name": name}

    if len(leaf.keys()) > 0:
        res["children"] = [build_leaf(k, v) for k, v in leaf.items()]
    return res


def main():
    tree = defaultdict(ctree)
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for rid, row in enumerate(reader):
            if rid == 0:
                continue
            leaf = tree[row[0]]
            for cid in range(1, len(row)):
                if str(row[cid]) == '':
                    continue
                leaf = leaf[row[cid]]

    res = []
    for name, leaf in tree.items():
        res.append(build_leaf(name, leaf))

    with open("output.json", "w") as outfile:
        outfile.write(json.dumps(res))
    print(json.dumps(res))

main()
