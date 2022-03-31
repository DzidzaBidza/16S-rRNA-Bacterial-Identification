# 16S-rRNA-bacterial-identification

16S rRNA bacterial identification using [mothur](https://mothur.org) and Python.

## Summary
The identification of bacteria based on the sequences of hypervariable regions was performed within the gene encoding 16S ribosomal RNA (rRNA) synthesis. 
A total of 2533 sequences of bacteria was used. 1216 sequences originate from cultivated species that inhabit the human intestinal tract, while the remaining 1317 sequences are derived from intestinal tract bacteria detected in studies based on the 16S rRNA sequence. The taxonomic position was determined using an adapted 16S rRNA SILVA database. 

The 16S rRNA sequence contains nine hypervariable regions (V1-V9).  A bioinformatics analysis was done based on the V1 to V8 hypervariable regions because the data set had incomplete sequences.
The analysis was performed using mothur bioinformatic data processing tool, while data visualization was performed with Python programming language. 
Deviations from reference data occur due to the quality and length of the input sequences, the degree of variability of the region, as well as the choice of reference bases.

### mothur pipeline

mothur pipeline for 16S rRNA gene sequence analysis is based on the universal way of bioinformatics data processing. It contains functions for quality control and sequence filtering, functions for clustering and taxonomy assignment. These functions represent the implementation of existing algorithms that have found their application in bioinformatics analysis.

#### mothur pipeline for one hypervariable region:

```
mothur > unique.seqs(fasta=HITTestV1.fasta)

mothur > count.seqs(name=HITTestV1.names)

mothur > align.seqs(fasta=HITTestV1.unique.fasta, reference=silva.nr_v138_1.align)

mothur > summary.seqs(fasta=HITTestV1.unique.align, count=HITTestV1.count_table)

mothur > screen.seqs(fasta=HITTestV1.unique.align, count=HITTestV1.count_table, summary=HITTestV1.unique.summary, start=1143, end=1793, maxhomop=8)

mothur > filter.seqs(fasta=HITTestV1.unique.good.align, vertical=T, trump=.)

mothur > pre.cluster(fasta=HITTestV1.unique.good.filter.fasta, count=HITTestV1.good.count_table, diffs=2)

mothur > chimera.vsearch(fasta=HITTestV1.unique.good.filter.precluster.fasta, count=HITTestV1.good.precluster.count_table, dereplicate=t) 

mothur > classify.seqs(fasta=HITTestV1.unique.good.filter.precluster.fasta, count=HITTestV1.unique.good.filter.precluster.count_table, reference=silva.nr_v138_1.align, taxonomy=silva.nr_v138_1.tax, cutoff=80)

mothur > remove.lineage(fasta=HITTestV1.unique.good.filter.precluster.fasta, count=HITTestV1.unique.good.filter.precluster.count_table, taxonomy=HITTestV1.unique.good.filter.precluster.nr_v138_1.wang.taxonomy, taxon=Chloroplast-Mitochondria-unknown-Archaea-Eukaryota)

mothur > summary.tax(taxonomy=current, count=current)

mothur > summary.seqs(fasta=HITTestV1.unique.good.filter.precluster.pick.fasta, count=HITTestV1.unique.good.filter.precluster.pick.count_table)

mothur > phylotype(taxonomy=HITTestV1.unique.good.filter.precluster.nr_v138_1.wang.pick.taxonomy) 

mothur > classify.otu(list=HITTestV1.unique.good.filter.precluster.nr_v138_1.wang.pick.tx.list, count=HITTestV1.unique.good.filter.precluster.pick.mothurGroup.count_table, taxonomy=HITTestV1.unique.good.filter.precluster.nr_v138_1.wang.pick.taxonomy, cutoff=80) 
```
### Data visualisation

`classification.py` script was used to transform mothur pipeline output data to a JSON format for easier visualization. (`Classification.json`)

Graphical representation of recovered sequences by taxonomic levels can be seen below. `visualisation.py` script was used for generating graphical report. 
![RecoveredSequence](https://user-images.githubusercontent.com/91345686/161155200-8da64874-c6b1-4d79-8a66-3b872bf87b91.png)

Graphical representation of the share of classified taxa at the phylum level. `phylum_pie_chart.py` script was used for generating graphical report.
![Pie Example(V1234)](https://user-images.githubusercontent.com/91345686/161162580-d522f0ea-1fbe-480f-b6d1-daa14c960621.png)

[Final Paper](https://github.com/DzidzaBidza/16S-rRna-Bacterial-Identification/blob/main/Final%20Paper%20-%2016S%20rRNA%20Bacterial%20Identification) can be found here.
