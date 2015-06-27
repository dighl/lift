# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-06-27 15:34
# modified : 2015-06-27 15:34
"""
LIFT to TSV Converter (powered by Python).
"""

__author__="Johann-Mattis List"
__date__="2015-06-27"

import re
from sys import argv

infile = argv[1]

with open(infile) as f:
    data = f.read()

# get the entries
entries = re.findall(
        '<entry ([^>]*)>(.*?)</entry>',
        data,
        re.DOTALL
        )

D = {}
idx = 1
header = []
for meta,entry in entries:

    # check for bad spans
    if 'span' in entry:
        entry = re.sub('<span .*?>(.*?)</span>',r'\1',entry)
    
    # get the date-created stuff
    tmp = dict(re.findall('([a-zA-Z]+)="([^"]+)"', meta)
          )
    if 'id' in tmp:
        tmp['oid'] = tmp['id']
        del tmp['id']

    # get the content
    lng,wrd = re.findall(
            '<lexical-unit>.*?<form lang="([^"]+)".*?>.*?<text>(.*?)</text>.*?</form>.*?</lexical-unit>',
            entry,
            re.DOTALL
            )[0]

    # get form in source
    try:
        lis,fis = re.findall(
                '<field .*?type="Original form".*?>.*?<form lang="([^"]+)".*?>.*?<text>(.*?)</text>.*?</form>.*?</field>',
                entry,
                re.DOTALL
                )[0]
    except IndexError:
        lis,fis = '',''

    # get bibliography
    try:
        bib = re.findall(
                '<note .*?type="bibliography".*?>.*?<form .*?>.*?<text>.*?([^<>]*?).*?</text>.*?</form>.*?</note>',
                entry,
                re.DOTALL
                )[0]
    except IndexError:
        bib = ''

    if 'morph-type' in entry:
        mtp = re.findall('<trait name="morph-type" value="(.*?)"/>',
                entry)
    else:
        mtp = ''

    # get the sense
    senses = re.findall('<sense id="(.*?)">(.*?)</sense>', entry,
            re.DOTALL)

    pos = ''

    for sid,sense in senses:
        if 'grammatical-info' in sense:
            pos = re.findall('<grammatical-info value="(.*?)">.*?</grammatical-info>',
                    sense
                    )
            if not pos:
                pos = ''
            else:
                pos = pos[0]
        else:
            pos = ''
        
        glosses = re.findall(

                '<gloss lang="(.*?)">.*?<text>(.*?)</text>.*?</gloss>',
                sense,
                re.DOTALL
                )
        for l,g in glosses:
            tmp[l+'_gloss'] = g

            if l == 'en':
                tmp['concept'] = g

              

    

    tmp['language'] = lng
    tmp['orthography'] = wrd
    tmp['language_in_source'] = lis
    tmp['form_in_source'] = fis
    tmp['reference'] = bib
    tmp['sense_id'] = sid
    tmp['pos'] = pos

    if 'concept' in tmp:
        D[idx] = tmp

    header += list(tmp.keys())


    idx += 1

header = sorted(set(header))
D[0] = [h.lower() for h in header]
for k in [i for i in D.keys() if i > 0]:

    D[k] = [D[k][h] if h in D[k] else '' for h in header]

with open(argv[1].replace('.lift','.tsv'), 'w') as f:
    
    f.write('ID\t'+'\t'.join([h.upper() for h in D[0]])+'\n')
    for k in range(1,len(D)):
        f.write(str(k)+'\t'+'\t'.join(D[k])+'\n')

print("Data was successfully written to file.")
