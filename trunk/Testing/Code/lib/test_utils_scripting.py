import nose.tools, utils_scripting

def test_equals_pass():
    pass

def test_equals_fail():
    pass

def test_greater_pass():
    pass

def test_greater_fail():
    pass

def test_sortedIntDictAsLs():
    d = {'1':-1, '-1':5, '0':10}
    sorted_ls = utils_scripting.sortedIntDictAsLs(d)
    for index in xrange(len(sorted_ls) - 1):
        nose.tools.assert_true(sorted_ls[index] <= sorted_ls[index + 1],
                               'List is not sorted')
        
