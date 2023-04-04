from main import isJpegType


def test_pentax_ok():
    assert( isJpegType('jpg/43745280.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail1():
    assert( False == isJpegType('jpg/508475585.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail2():
    assert( False == isJpegType('jpg/622326259.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail3():
    assert( False == isJpegType('jpg/ss.jpg',{'model':'PENTAX K-5 II s'}) )


if __name__ == "__main__":
    isJpegType('jpg/43745280.jpg',{'model':'PENTAX K-5 II s'})
