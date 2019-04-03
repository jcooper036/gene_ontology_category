#! /usr/bin/env python3

import sys
import pandas as pd

# label and two necessary files
category = sys.argv[1]
results_file = sys.argv[2]
gene_list_file = sys.argv[3]
inclue_results_file = results_file + '.{}_include.tsv'.format(category)
exclude_results_file = results_file + '.{}_exclude.tsv'.format(category)

def read_list(list_file):
    """Makes a list from a file where each 
    item is seperated by a new line"""
    new_list = []
    with open(list_file, 'r') as f:
        for line in f:
            line = line.strip()
            new_list.append(line)
    return new_list

def convert_species_names(gene_list):
    """
    Converts the gene list to other species, using conversion to
    ENSEMBLE IDs and back to gene names (files are provided in
    directory)
    """
    species_converter = {}

    return species_converter


def parse_results(results, gene_list):
    """
    Takes a pandas data frame and a list
    Returns two data frames, one that has the list included 
    and one that is everything except the list
    """
    include = results
    exclude = results

    return include, exclude


results = pd.Dataframe(results_file)
gene_list = read_list(gene_list_file)
species_converter = convert_species_names(gene_list) 
include_results, exclude_results = parse_results(results, gene_list)
