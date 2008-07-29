import utils_graph
import os

# page grabber for mkFASTA
def wget(query, outputName):
    os.system("wget ----tries=100 -O " + outputName
              + " 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id="
              + query.strip(',') + "&rettype=gp'")

# parser for mkFASTA
# strip away the sequence
# from the wget file
def parseWget(wget_file, fout):
    f = open(wget_file)
    f.close()
    os.system('rm ' + wget_file)

# input
#       file w/ a list of GIs or EntrezGeneIDs
#
# output
#       fasta file @ the specified location
def mkFASTA(geneLsFile, outputFile):
    genes = utils_graph.getNodes(geneLsFile)
    query = ''
    count = 0
    for gene in genes:
        query = query + gene + ','
        count += 1
        if count % 500 == 0:
            wget_name = 'ncbi.query_' + str(count/500)
            wget_files.append(wget_name)
            wget(query, wget_name)
        query = ''
        wget(query)
    wget_name = 'ncbi.query_' + str(count/500 + 1)
    wget(query, wget_name)
    wget_files.append(wget_name)
    fout = open(outputFile, 'w')
    for f in wget_files:
        parseWget(f, fout)
    fout.close()
        
