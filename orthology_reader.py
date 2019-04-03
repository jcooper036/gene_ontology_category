#! /usr/bin/env python3

import sys

## gather the input variables
clade1 = sys.argv[1]
clade2 = sys.argv[2]
inlist = sys.argv[3]
outfile = inlist + '.' + str(clade2) + '.txt'
clades = ['primate', 'murinae', 'cricetidae', 'ciroptera', 'bovidae', 'caniformia']

def check_clades(clade1, clade2, clades):
    """Checks that the two clades are known clades
    and that the approptiate files are in place"""
    if clade1 not in clades:
        print('ERROR: {} was not a good clade. Try {}'.format(clade1, clades))
    if clade2 not in clades:
        print('ERROR: {} was not a good clade. Try {}'.format(clade2, clades))
    with open('orthology_tables/{}_ensemble.csv'.format(clade1), 'r') as f:
        pass
    with open('orthology_tables/{}_ensemble.csv'.format(clade2), 'r') as f:
        pass
    with open('orthology_tables/one_to_one_list.txt'.format(clade2), 'r') as f:
        pass

def load_orthology(clade1, clade2):
    """
    Loads the orthology relationship for two clades (1:1 orthology)
    """
    ortho_dictionary = {}

    return ortho_dictionary

def load_ensbid(clade):
    """Loads the gene : esemblID and ensemblID : gene for a clade"""
    enstable = {'gene_to_ensid' : {}, 'ensid_to_gene' : {}}

    return enstable

def genes_to_ensbid(inlist, enstable):
    """given a file, reads in the genes, returns the list
    of their ensemble IDs"""
    ensembl_list = []

    return ensembl_list

def ensid_to_genes(inlist, enstable):
    """Gets a list of ensemble IDs, returns a list of genes"""
    gene_list = []

    return gene_list

def clade_conversion(ensbl_list, ortho_dictionary):
    """Converts the ensemble IDs between two clades"""
    new_ensbl_list = []

    return new_ensbl_list

def list_to_file(plist, filename):
    """
    Input: List and a file name
    Output: prints that list to a file seperated by new lines
    """
    with open(filename, 'w') as f:
        for item in plist:
            f.write(str(item) + '\n')


# load all the tables
check_clades(clade1, clade2, clades)
ortho_dictionary = load_orthology(clade1, clade2)
enstable_1 = load_ensbid(clade1)
enstable_2 = load_ensbid(clade2)

# change to ensemble IDS
ensbl_list = genes_to_ensbid(inlist, enstable_1)
# convert between clades
outlist = clade_conversion(ensbl_list, ortho_dictionary)
# change back to genes
outlist = ensid_to_genes(outlist, enstable_2)
# print the output to a file
list_to_file(outlist, outfile)