from main import convertTime

def test_ok():
    dictDate = convertTime( "2023:04:04 11:18:54" )
    assert( dictDate )

def test_nospace():
    dictDate = convertTime( "2023:04:0411:18:54" )
    assert( not dictDate )

def test_shortdate():
    dictDate = convertTime( "2023:04 11:18:54" )
    assert( not dictDate )

def test_shorttime():
    dictDate = convertTime( "2023:04:04 11:18" )
    assert( not dictDate )
