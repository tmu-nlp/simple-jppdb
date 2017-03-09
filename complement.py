# coding: utf-8

import sys
from collections import defaultdict


def main():
    # jev
    word2level = defaultdict(str)
    fin = open(sys.argv[1], "r")
    for line in fin:
        line = line.strip().split(",")
        if "初級" in line[3]:
            level = "1"
        elif "中級" in line[3]:
            level = "2"
        elif "上級" in line[3]:
            level = "3"
        else:
            continue
        word2level[line[1]] = level
    fin.close()
    # word-level-japanese
    fout = open("word-level-japanese.out", "w")
    fin = open("word-level-japanese", "r")
    for line in fin:
        word, level = line.strip().split("\t")
        if level == "?":
            level = word2level[word]
        fout.write("%s\t%s\n" % (word, level))
    fin.close()
    fout.close()
    # simple-ppdb-japanese
    fout = open("simple-ppdb-japanese.out", "w")
    fin = open("simple-ppdb-japanese", "r")
    for line in fin:
        paraprob, complex_word, simple_word, level_complex, level_simple = line.strip().split("\t")
        if level_complex == "?":
            level_complex = word2level[complex_word]
        if level_simple == "?":
            level_simple = word2level[simple_word]
        fout.write("%s\t%s\t%s\t%s\t%s\n" % (paraprob, complex_word, simple_word, level_complex, level_simple))
    fin.close()
    fout.close()


if __name__ == '__main__':
    main()
