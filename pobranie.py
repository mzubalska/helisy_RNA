#!/usr/bin python
# -*- coding: utf-8 -*-
"""
Skrypt do pobierania plików CSV z RNA Bricks2.
RNA Brick 2: http://iimcb.genesilico.pl/rnabricks2/fragments/browse_structures_of_rna_and_rna_protein_complexes
"""
import sys
import urllib.request


# 1 uzyskanie listy nazw struktur pdb o wysokiej rozdzielczości
def get_pdb_list_hq(fasta, list_pdb):
    lines_seen = set()
    with open(fasta, 'rb') as fetch:
        with open(list_pdb, 'wb') as output:
            for line in fetch:
                pdb_name = line[1:5]
                if '>' in line and pdb_name not in lines_seen and pdb_name != "quer":
                    output.write(pdb_name + '\n')
                    lines_seen.add(pdb_name)


# 2 pobranie plików parowań w formacie CSV
def download(pdb_list):
    with open(pdb_list, 'rb') as fetch:
        for pdb in fetch:
            pdb1 = pdb.rstrip()
            csv = urllib.request.urlopen("http://iimcb.genesilico.pl/rnabricks2//fragments/basepairs/" + pdb1 + "_clarna_basepairs.csv")
            with open(pdb1 + ".csv", 'wb') as output:
                output.write(csv.read())


get_pdb_list_hq(sys.argv[1], sys.argv[2])
download(sys.argv[2])
