from src.main import add

def test_add():
    assert add(1,2)==3
    assert add(3,3)==7
    assert add(0,0)==0