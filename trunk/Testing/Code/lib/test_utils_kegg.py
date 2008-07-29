#---------------------------------------
#
# Author     Perry Evans
#            evansjp@mail.med.upenn.edu
# 2008
#---------------------------------------
""" Testing for utils_kegg.py """
import utils_kegg, nose.tools

def test_colorAllGreen():
    """ Make sure you can color all the green in the KEGG pathways. """
    pass
#    paths = utils_kegg.getPathways('hsa')
#    for path in paths:
#        genes = utils_kegg.getPathwayGenes(path)
#        utils_kegg.prepAndColor_gene_dict(path, genes, 'black')

def test_colorCellCommnication():
    """ See why cell comunication fails to color. """
    
    genes = utils_kegg.getPathwayGenes('path:hsa01430')    
    nose.tools.assert_not_equal(len(genes.keys()), 0,
                                'Cell Communication has no genes')
    utils_kegg.prepAndColor_gene_dict('path:hsa01430', genes, 'black')


