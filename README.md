# lift

Convert lift (lexical interchange format) to TSV format.

This repo is work in progress. I don't really understand the full output of FLEX databases yet, so I'll add more groups to conversion on an item-to-item basis.
Instead of writing a full parsers, this script just uses regular expressions, it should, however, be reasonably well regarding speed and accuracy.

You'll need Python 3 for this to work (I am currently too lazy to adapt it to python2).

Usage: python lift.py inputfile.lift


