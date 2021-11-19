#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#how to use: list_extract.py target.fasta list.txt

import sys
from Bio import SeqIO

newfasta_1= open('extracted.fasta', 'w')
newfasta_2= open('rest.fasta', 'w')

fasta_in = sys.argv[1]
query = sys.argv[2]
hit = 0

for record in SeqIO.parse(fasta_in, 'fasta'):
    id_part = record.id
    m_part = id_part.rstrip()
    description_part = record.description
    seq = record.seq
    for q in open(query, "r"):
        if m_part == q.rstrip():
            fasta_seq = '>' + description_part + '\n' + seq + '\n'
            newfasta_1.writelines(fasta_seq)
            hit += 1
    if hit == 0:
        fasta_seq = '>' + description_part + '\n' + seq + '\n'
        newfasta_2.writelines(fasta_seq)
    hit = 0

newfasta_1.close()
newfasta_2.close()

