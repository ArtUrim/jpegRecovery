from main import isJpegType


def test_pentax_ok():
    assert( isJpegType('jpg/43745280.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail1():
    assert( False == isJpegType('jpg/508475585.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail2():
    assert( False == isJpegType('jpg/622326259.jpg',{'model':'PENTAX K-5 II s'}) )

def test_pentax_fail3():
    assert( False == isJpegType('jpg/ss.jpg',{'model':'PENTAX K-5 II s'}) )

def test_empty():
    assert isJpegType( 'jpg/ss.jpg', {'model': None} )

def test_two():
    assert isJpegType( 'jpg/ss.jpg', {'model': 'Sia Sjung','orientation':1} )

def test_two_with_None():
    assert isJpegType( 'jpg/ss.jpg', {'model': 'Sia Sjung','orientation':None} )

def test_Fail_one():
    assert False == isJpegType( 'jpg/ss.jpg', {'model': 'Sia Sjng','orientation':None} )

def test_Fail_two():
    assert False == isJpegType( 'jpg/ss.jpg', {'model': 'Sia Sjung','orientation':2} )

if __name__ == "__main__":
    isJpegType( 'jpg/622326259.jpg', {'model': 'Sia Sjung','colorspace':'Uncalibrated'} )
