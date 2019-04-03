# gene_ontology_category
A python program to extract genes from an ontology given a general category.

## KEGG database
We will be pulling our gene ontology (GO) terms from the KEGG database (https://www.genome.jp/kegg/). The file that we have has 4 different hierarchical levels:  
- A: biologic process (ex: Metabolism)
- B: groups of pathways (ex: Carbohydrate metabolism)
- C: specific pathways (ex: Glycolysis,/,Gluconeogenesis)
- D: a specific gene in that pathway  
  
Here is an example of that file format:  
```
A,09100,Metabolism  
B,09101,Carbohydrate,metabolism  
C,00010,Glycolysis,/,Gluconeogenesis,[PATH:hsa00010]  
D,3101,HK3,hexokinase,3	K00844,HK,hexokinase,[EC:2.7.1.1]  
D,3098,HK1,hexokinase,1	K00844,HK,hexokinase,[EC:2.7.1.1]  
D,3099,HK2,hexokinase,2	K00844,HK,hexokinase,[EC:2.7.1.1]  
D,80201,HKDC1,hexokinase,domain,containing,1	K00844,HK,hexokinase,[EC:2.7.1.1]  
D,2645,GCK,glucokinase	K12407,GCK,glucokinase,[EC:2.7.1.2]  
D,2821,GPI,glucose-6-phosphate,isomerase	K01810,GPI,glucose-6-phosphate,isomerase,[EC:5.3.1.9]  
D,5213,PFKM,phosphofructokinase,muscle	K00850,pfkA,6-phosphofructokinase,1,[EC:2.7.1.11]  
D,5214,PFKP,phosphofructokinase,platelet	K00850,pfkA,6-phosphofructokinase,1,[EC:2.7.1.11]  
D,5211,PFKL,phosphofructokinase,liver,type	K00850,pfkA,6-phosphofructokinase,1,[EC:2.7.1.11]  
D,2203,FBP1,fructose-bisphosphatase,1	K03841,FBP,fructose-1,6-bisphosphatase,I,[EC:3.1.3.11]  
D,8789,FBP2,fructose-bisphosphatase,2	K03841,FBP,fructose-1,6-bisphosphatase,I,[EC:3.1.3.11]
```

Counting the number of As, Bs, Cs, and Ds, we see that there are 7 As, 51 Bs, 512 Cs. So in terms of sorting, it is probably best to build a table for all B's for the category that we want.

## The process
1) Make a csv for all the B levels labeled with the sorting category. The CSV should have B ID #, B name, 0 (for False) or 1 (for True)  
2) Gather a list of all genes in each B type    
3) Return a list of all genes that are in all genes that were in that type

# Orthology reader
In this program it is necessary to convert the gene names from one species to another. Since I've had to to this multiple times, I'm just going to write code to do this any which way. Here's how it works:  
```bash
python3 orthology_reader.py <clade1> <clade2> <gene_list_clade1.txt>
```
