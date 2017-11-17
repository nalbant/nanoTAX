# nanoTAX
This repository contains the nanoTAX pathogen detection program. The program is in version 0.1

nanoTAX enables taxonomical classification of a set of reads obtained from Oxford Nanopore sequencing platform and which are stored in fasta format. The program currently enables classification via Relative Abundance Index (RAI) and Average Mutual Information (AMI) methods. Both methods are able to conduct read-by-read classifications and AMI method can also output in "batch mode" (i.e. all reads obtained from a sequencing file are classified to a single organism).


INSTALL:
The program consits of Python scripts and a C++ implementation of raiphy program. Firstly, the raiphy program should be installed via a C++ compiler (e.g. gcc) using the makefile:

cd <path_to_source_code_directory>
make clean
make

This will build the executable raiphy in the same directory with the main nanoTAX script.

USAGE:

nanoTAX can either i) Employ taxonomic classification on Nanopore sequencing fasta files given built databasesor ii) Build databases for classification

i) Taxonomic classification:

python nanoTAX.py <INPUT_DIRECTORY> <BATCH_MODE_ON> <ALGORITHM> <DATABASE_FILE> <METRIC>
  
  These arguments are mandatory:
  INPUT_DIRECTORY: (character string), The folder that contains the nanopore sequencing files. All fasta files in the directory are to be processed, so be sure to create a directory only with the required fasta siles.

  BATCH_MODE_ON: (1 or 0), if 1 all the sequenced reads will be classified to the most likely taxonomic unit, else each read will be processed individually.

  ALGORITHM: (RAI or AMI), if RAI, Relative Abundance index is employed for classification. if AMI average mutual information is employed for the classification.

  DATABASE_FILE: (character string) Path to the database file used for taxonomic classification.

  METRIC: ('corr', 'euclidian','L1')  This argument is mandatory only for AMI method. Determines the metric used to assign ami vectors to the database items; Pearson correlation, Euclidian distance, L1- city block distance for corr, euclidian, and L1 options respectively.

 ii) Building database:
 python nanoTAX_buildDB.py  <DATABASE_TYPE> <INPUT_DIRECTORY>

 DATABASE_TYPE: (AMI, RAI), The method to be used for taxonomic classification. The database is built for  RAI (Relative Abundance Index) or AMI (Average Mutual Information) correspondingly.

 INPUT_DIRECTORY: (character string) The folder that contains the fasta formatted files to be included in the database. Each database item will be labelled by the header ID of the fasta files.
