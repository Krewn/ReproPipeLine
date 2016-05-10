#!/bin/bash
echo '1 - Generating geneFeilds'
python FlowWidIt.py
echo '2 - Writeing HTML'
mkdir geneFieldsOP13
python MakeGeneFieldReport.py
echo '3 - Drawing GeneFields '
cd geneFieldsOP13
octave DrawGF.m
