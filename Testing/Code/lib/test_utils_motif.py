#---------------------------------------
#
# Author     Perry Evans
#            evansjp@mail.med.upenn.edu
# 2008
#---------------------------------------
"""
Tests for utils_motif.py
"""

import utils_motif, nose.tools, os

def test_mkProteinPlot_oneAlignment():
    utils_motif.mkProteinPlot('alignment1.motifs', './',
                              'alignmentMatrix1.png')

def test_mkProteinPlot_twoAlignments():
    utils_motif.mkProteinPlot('alignment2.motifs', './',
                              'alignmentMatrix2.png')

def test_mkProteinPlot_sixAlignments():
    utils_motif.mkProteinPlot('alignment6.motifs', './',
                              'alignmentMatrix6.png')

def test_mkProteinPlot_nineAlignments():
    utils_motif.mkProteinPlot('alignment9.motifs', './',
                              'alignmentMatrix9.png')

def test_getELMpage():
    seq = 'MLRNNKTIIIKYFLNLINGAFLVLGLLFMGFGAWLLLDRNNFLTAFDENNHFIVPISQILIGMGSSTVLFCLLGYIGIHNEIRWLLIVYAVLITWTFAVQVVLSAFIITKKEEVQQLWHDKIDFVISEYGSKDKPEDITKWTILNALQKTLQCCGQHNYTDWIKNKNKENSGQVPCSCTKSTLRKWFCDEPLNATYLEGCENKISAWYNVNVLTLIGINFGLLTSEVFQVSLTVCFFKNIKNIIHAEM'
    utils_motif.getELMpage('myid_0', seq, 'testELMpage.html')
    os.system('tidy testELMpage.html > testELMpage_tidy.html')
    parsed_standard = utils_motif.parseELMpage('myid_0', 'standardELMpage.html')
    parsed_test = utils_motif.parseELMpage('myid_0', 'testELMpage_tidy.html')
    nose.tools.assert_equal(len(parsed_test), len(parsed_standard),
                            'myid_0 html is wrong from server')


def test_mergeMotifs_surrounded():
    exclude_motifs = []
    for start, stop in [ [154, 232],
                         [172, 211],
                         [12, 34],
                         [56, 78],
                         [85, 107] ]:
        utils_motif.mergeMotifs(start, stop, exclude_motifs)
    for start1, stop1 in [ [154, 232],
                           [12, 34],
                         [56, 78],
                         [85, 107] ]:
        found = False
        for start2, stop2 in exclude_motifs:
            if start1 == start2 and stop1 == stop2:
                found = True
        nose.tools.assert_true(found,
                               'missing '
                               + str(start1) + ', '
                               + str(start2))

def test_parseELMpage():
    parsed_table = utils_motif.parseELMpage('myid_0', 'standardELMpage.html')
    nose.tools.assert_equal(len(parsed_table), 47, 'myid_0 html parsed wrong found ' 
                            + str(len(parsed_table))
                            + ' ELMs, but needed 47')
