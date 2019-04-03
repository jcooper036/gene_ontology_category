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