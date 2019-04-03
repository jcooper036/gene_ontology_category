#! /usr/bin/env python3

import sys

# ontology table
ontology_file = sys.argv[1]

# sorting table and the gene list file
sorting_file = sys.argv[2]
gene_list_file = sorting_file.split('_sort')[0] + '_genelist.txt'

def load_ontology_database(ontology_file):
    """
    Input: Kegg ontology file
    Returns: dictionary with [B-term] = list of genes
    """
    ontologies = {}
    with open(ontology_file, 'r') as f:
        for line in f:
            line = line.rstrip()
            line = line.split(',')
            
            # this relies on that there is always a new B term
            # preceeding the approprate D terms
            if 'B' in line[0]:
                bterm = line[1]
                ontologies[bterm] = []
            if 'D' in line[0]:
                ontologies[bterm].append(line[2])

    return ontologies


def parse_sort_file(sorting_file):
    """
    Input: the file that sorts ontologies as desired
    Returns: list of the B-terms that we want genes from
    """
    b_terms = []
    
    with open(sorting_file, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            if line[2] == '1':
                b_terms.append(line[0])

    return b_terms

def build_gene_list(ontologies, b_terms):
    """
    Input: ontology dictionary, list of the keys
    Returns: List of genes specified by that list of keys
    """
    gene_list = set()
    
    for bterm in b_terms:
        for gene in ontologies[bterm]:
            gene_list.add(gene)
    
    return gene_list

def list_to_file(plist, filename):
    """
    Input: List and a file name
    Output: prints that list to a file seperated by new lines
    """
    with open(filename, 'w') as f:
        for item in plist:
            f.write(str(item) + '\n')



ontologies = load_ontology_database(ontology_file)
b_terms = parse_sort_file(sorting_file)
gene_list = build_gene_list(ontologies, b_terms)
list_to_file(gene_list, gene_list_file)