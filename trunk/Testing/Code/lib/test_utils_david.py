#---------------------------------------
#
# Author     Perry Evans
#            evansjp@mail.med.upenn.edu
# 2008
#---------------------------------------
""" 
Testing automation of DAVID and parsing of DAVID results.
"""
import utils_david
import nose.tools

def test_automation_annotation_webpage():
    """ Make sure DAVID annotation webpage result ends in newline, but does not begin with one.
    """
    
    results = '../../../../Projects/Human_Virus/Data/Motif_Search/HPRD/Restrict_Domain_by_ELM_Restrict_ELM_by_Domain/all.H12'
    web_page = utils_david.getAllTerms_web(results)
    line_split = web_page.split('\n')
    nose.tools.assert_not_equal('', line_split[0],
                            'DAVID results start in newline.')
    nose.tools.assert_equal('', line_split[-1],
                            'DAVID results do not end in newline.')

def test_automation_significance_wegpage():
    """ Make sure DAVID chart webpage results ends in newline, but does not begin with one.
    """
    
    results = '../../../../Projects/Human_Virus/Data/Motif_Search/HPRD/Restrict_Domain_by_ELM_Restrict_ELM_by_Domain/all.H12'
    web_page = utils_david.getSigTerms_web(results, '../../../../Data/Networks/Human/HPRD_FLAT_FILES_090107/hprd.intr.ls')
    line_split = web_page.split('\n')
    nose.tools.assert_not_equal('', line_split[0],
                            'DAVID results starts in newline.')
    nose.tools.assert_equal('', line_split[-1],
                            'DAVID results do not end in newline.')

def test_automation_annotation_cats():
    """ Annotaiton: Do I get the right categories in the automation?
    """

    results = '../../../../Projects/Human_Virus/Data/Motif_Search/HPRD/Restrict_Domain_by_ELM_Restrict_ELM_by_Domain/all.H12'
    cat2term2protein = utils_david.getAllTerms(results)
    cats = cat2term2protein.keys()
    req_cats = {"KEGG_PATHWAY":True,
                "GOTERM_BP_5":True,
                "GOTERM_MF_5":True,
                "GOTERM_CC_5":True}
    nose.tools.assert_equal(len(req_cats), len(cats), 
                            'wrong # of categories: ' + str(cats))
    for cat in cats:
        nose.tools.assert_true(req_cats.has_key(cat), 'missing category ' + cat)

def test_parsing_browser_annotation_cats():
    """ Annotation: Do I get the right categories in the browser parsing?
    """

    cat2term2protein = utils_david.cat2term2protein_allFile('annotationExample')
    cats = cat2term2protein.keys()
    req_cats = {"KEGG_PATHWAY":True,
                "GOTERM_BP_5":True,
                "GOTERM_MF_5":True,
                "GOTERM_CC_5":True}
    nose.tools.assert_equal(len(req_cats), len(cats), 'wrong # of categories: ' + str(cats))
    for cat in cats:
        nose.tools.assert_true(req_cats.has_key(cat), 'missing category ' + cat)

def test_significance():
    """ Does chartExample (downloaded) match the automation?
    """

    automatedSig = utils_david.getSigTerms('../../../../Projects/Human_Virus/Data/Motif_Search/HPRD/Restrict_Domain_by_ELM_Restrict_ELM_by_Domain/all.H12', 
                                           '../../../../Data/Networks/Human/HPRD_FLAT_FILES_090107/hprd.intr.ls')
    browserSig = utils_david.cat2term2protein_sigFile('chartExample')

    nose_message = ''
    
    for cat in browserSig.keys():
        if automatedSig.has_key(cat):
            for term in browserSig[cat].keys():
                if automatedSig[cat].has_key(term):
                    if browserSig[cat][term]['pvalue'] != automatedSig[cat][term]['pvalue']:
                        nose_message = 'pvalues not eq for', cat, term, \
                                       ': browser =', browserSig[cat][term]['pvalue'], \
                                       'automated =', automatedSig[cat][term]['pvalue']
                    if browserSig[cat][term]['count'] != automatedSig[cat][term]['count']:
                        nose_message = 'counts not eq for', cat, term, \
                                       ': browser =', browserSig[cat][term]['count'], \
                                       'automated =', automatedSig[cat][term]['count']
                    for protein in browserSig[cat][term]['genes'].keys():
                        if not automatedSig[cat][term]['genes'].has_key(protein):
                            nose_message = 'automated', cat, term, 'does not have gene', protein
                else:
                    nose_message = 'automated does not have term', term, 'in cat', cat
        else:
            nose_message = 'automated does not have category', cat

    for cat in automatedSig.keys():
        if automatedSig.has_key(cat):
            for term in automatedSig[cat].keys():
                if automatedSig[cat].has_key(term):
                    if automatedSig[cat][term]['pvalue'] != browserSig[cat][term]['pvalue']:
                        nose_message = 'pvalues not eq for', cat, term, \
                                       ': automated =', automatedSig[cat][term]['pvalue'], \
                                       'browser =', browserSig[cat][term]['pvalue']
                    if automatedSig[cat][term]['count'] != browserSig[cat][term]['count']:
                        nose_message = 'counts not eq for', cat, term, \
                                       ': automated =', automatedSig[cat][term]['count'], \
                                       'browser =', browserSig[cat][term]['count']
                    for protein in automatedSig[cat][term]['genes'].keys():
                        if not browserSig[cat][term]['genes'].has_key(protein):
                            nose_message = 'browser', cat, term, 'does not have gene', protein
                else:
                    nose_message = 'browser does not have term', term, 'in cat', cat
        else: 
            nose_message = 'browser does not have category', cat

    nose.tools.assert_equal(nose_message, '', nose_message)

def test_annotation():
    """ Does annotationExample (downloaded) match the automation?
    """

    automatedAll = utils_david.getAllTerms('../../../../Projects/Human_Virus/Data/Motif_Search/HPRD/Restrict_Domain_by_ELM_Restrict_ELM_by_Domain/all.H12')
    browserAll = utils_david.cat2term2protein_allFile('annotationExample')

    nose_message = ''

    for cat in browserAll.keys():
        if automatedAll.has_key(cat):
            for term in browserAll[cat].keys():
                if automatedAll[cat].has_key(term):               
                    if browserAll[cat][term]['count'] != automatedAll[cat][term]['count']:
                        nose_message = 'counts not eq for', cat, term, ': browser =', \
                                       browserAll[cat][term]['count'], 'automated =', \
                                       automatedAll[cat][term]['count']
                    for protein in browserAll[cat][term]['genes'].keys():
                        if not automatedAll[cat][term]['genes'].has_key(protein):
                            nose_message = 'automated', cat, term, 'does not have gene', protein
                else:
                    nose_message = 'automated does not have term', term, 'in cat', cat
        else: 
            nose_message = 'automated does not have category', cat

    for cat in automatedAll.keys():
        if automatedAll.has_key(cat):
            for term in automatedAll[cat].keys():
                if automatedAll[cat].has_key(term):
                    if automatedAll[cat][term]['count'] != browserAll[cat][term]['count']:
                        nose_message = 'counts not eq for', cat, term, ': automated =', \
                                       automatedAll[cat][term]['count'], 'browser =', \
                                       browserAll[cat][term]['count']
                    for protein in automatedAll[cat][term]['genes'].keys():
                        if not browserAll[cat][term]['genes'].has_key(protein):
                            nose_message = 'browser', cat, term, 'does not have gene', protein
                else:
                    nose_message = 'browser does not have term', term, 'in cat', cat
        else: 
            nose_message = 'browser does not have category', cat
    
    nose.tools.assert_equal(nose_message, '', nose_message)


