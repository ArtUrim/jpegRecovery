from main import getTimes

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
