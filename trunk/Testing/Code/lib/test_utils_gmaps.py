import utils_gmaps, PyMozilla, nose.tools

def test_drivingDirections_assumptions():
    """ Make sure the url form is right and the return html is in the format I think it is in.
    """

    moz_emu = PyMozilla.MozillaEmulator(cacher=None, trycount=0)
    web_page = moz_emu.download('http://maps.google.com/maps?f=d&source=s_d&hl=en&geocode=&saddr=mesquite%2C+tx&daddr=philadelphia%2C+pa&btnG=Get+Directions&output=js')
    distance = web_page.split('timedist')[1].split(';')[0].split('\\')[-2].split('e')[1].replace(',', '')
    nose.tools.assert_equal('1460', distance, 'Did not parse distance #')
    unit = web_page.split('timedist')[1].split(';')[1].split('\\')[0].strip()
    nose.tools.assert_equal('mi', unit, 'Did not parse distance unit')

def test_drivingDirections_names():
    """ Make sure drivingDirection's inputs are handled correctly for place names.
    """

    [distance, unit] = utils_gmaps.drivingDistance('mesquite, tx',
                                                   'philadelphia, pa')
    nose.tools.assert_equal('1460', distance)
    nose.tools.assert_equal('mi', unit)
    
    [distance, unit] = utils_gmaps.drivingDistance('san diego, ca',
                                      'philadelphia, pa')
    nose.tools.assert_equal('2739', distance)
    nose.tools.assert_equal('mi', unit)
    
    [distance, unit] = utils_gmaps.drivingDistance('hood canal, wa',
                                      'tampa, fl')
    nose.tools.assert_equal('3230', distance)
    nose.tools.assert_equal('mi', unit)

def test_drivingDirections_latitude_longitude():
    """ Make sure drivingDirection's inputs are handled correctly for latitude/longitude.
    """

    [distance, unit] = utils_gmaps.drivingDistance('39.9522222, -75.1641667',
                                      '32.7833333, -96.8000000')
    nose.tools.assert_equal('1467', distance)
    nose.tools.assert_equal('mi', unit)
    
def test_drivingDirections_latitude_longitude_examples():
    """ Test a list of lat/lon coords. """

    f=open('gmaps_lat_lon_coords')
    ls = []
    for line in f:
        ls.append(line.strip().split('\t'))    
    f.close()

    for i in xrange(len(ls)):
        for j in xrange(len(ls)):
            if i != j:
                [lat1, lon1] = ls[i]
                [lat2, lon2] = ls[j]
                print lat1 + ',' + lon1, lat2 + ',' + lon2
                [distance, unit] = utils_gmaps.drivingDistance(lat1 + ', ' + lon1,
                                                               lat2 + ', ' + lon2)
                print lat1 + '\t' + lon1 + '\t' \
                      + lat2 + '\t' + lon2 + '\t' \
                      + distance + '\t' + unit
