# 16S-rRna-Analysis-Visualisation

### Summary
The identification of bacteria based on the sequences of hypervariable regions was performed within the gene encoding 16S ribosomal RNA (rRNA) synthesis. 
A total of 2533 sequences of bacteria was used. 1216 sequences originate from cultivated species that inhabit the human intestinal tract, while the remaining 1317 sequences are derived from intestinal tract bacteria detected in studies based on the 16S rRNA sequence. The taxonomic position was determined using an adapted 16S rRNA SILVA database. 

The 16S rRNA sequence contains nine hypervariable regions (V1-V9).  A bioinformatics analysis was done based on the V1 to V8 hypervariable regions because the data set had incomplete sequences.
The analysis was performed using mothur bioinformatic data processing tool, while data visualization was performed with Python programming language. 
Deviations from reference data occur due to the quality and length of the input sequences, the degree of variability of the region, as well as the choice of reference bases.

Graphical representation of recovered sequences by taxonomic levels can be seen below. `visualisation.py` was used for generating graphical report. 
![RecoveredSequence](https://user-images.githubusercontent.com/91345686/161155200-8da64874-c6b1-4d79-8a66-3b872bf87b91.png)

Graphical representation of the share of classified taxa at the phylum level. `phylum_pie_chart.py` was used for generating graphical report.
![Pie Example(V1234)](https://user-images.githubusercontent.com/91345686/161162580-d522f0ea-1fbe-480f-b6d1-daa14c960621.png)

