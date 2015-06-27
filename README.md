# lift

Convert lift (lexical interchange format) to TSV format.

This repo is work in progress. I don't really understand the full output of FLEX databases yet, so I'll add more groups to conversion on an item-to-item basis.
Instead of writing a full parsers, this script just uses regular expressions, it should, however, be reasonably well regarding speed and accuracy.

You'll need Python 3 for this to work (I am currently too lazy to adapt it to python2).

## Usage

Usage: python lift.py inputfile.lift

## How to View the Output Files

Just take the file (ending in "tsv") and upload it to the 
[TSV-EDICTOR](http://tsv.lingpy.org?basics=DOCULECT|LANGUAGE|CONCEPT|COUNTERPART|POS) tool. Here, you can either specify the file location by clicking the "browse" button, or you just take the file and drag it to the very button. Then 

