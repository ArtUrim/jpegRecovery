from test import traverse_recov
from test import isJpegType
from test import getTimes

def test_trav():
    dd = traverse_recov("jpg")
    assert(dd)

def test_trav_fail():
    dd = traverse_recov("jpeg")
    assert(len(dd) == 0 )

def test_trav_fail2():
    dd = traverse_recov("test.py")
    assert(len(dd) == 0 )

def test_trav_fail3():
    dd = traverse_recov("share")
    assert(len(dd) == 0 )

def test_pentax_ok():
    assert( isJpegType('jpg/43745280.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail1():
    assert( False == isJpegType('jpg/508475585.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail2():
    assert( False == isJpegType('jpg/622326259.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail3():
    assert( False == isJpegType('jpg/ss.jpg',{'model':'PENTAX K-5 II s'}) )

def test_gettime_ok():
    assert( 3 == len(getTimes('jpg/43745280.jpg') ) )

def test_gettime_fail1():
    assert( 0 == len(getTimes('jpg/508475585.jpg') ) )

def test_gettime_fail2():
    assert( 0 == len(getTimes('jpg/622326259.jpg') ) )

def test_gettime_fail3():
    assert( 0 == len(getTimes('jpg/ss.jpg') ) )

if __name__ == "__main__":
    getTimes('jpg/622326259.jpg')
