from test import traverse_recov

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
