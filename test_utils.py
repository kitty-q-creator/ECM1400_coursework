from utils import *

def test_is_a_number():
    assert is_a_number(5)==True
    assert is_a_number(1.234)==True
    assert is_a_number("5")==True
    assert is_a_number("1.234")==True
    assert is_a_number("bob")==False
    assert is_a_number("1+34")==True

def test_median():
    assert median([3,8,5,1,99])==5

def test_sumvalues():
    sumvalues([1,6,8,9,4,2])==30

def test_maxvalue():
    maxvalue([3,88,6,876,45,123])==3

def test_minvalue():
    minvalue([7,5,8,9,3,1,6])==5

def test_meannvalue():
    meannvalue([1,2,3,4,5])==7.5
    meannvalue([10,15,20])==20

def test_countvalue():
    countvalue([1,1,4,6,1,4,5,1],1)==4
    countvalue([5,'g',5,2,'k','l','g'],'g')==2