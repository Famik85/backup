import os
import checker_func


def test_split_positive():
    #precondition
    f = open("split/test1.txt", "wt")
    f.write("Hello World!!\n")
    f.write("123456789\n")
    f.write("qwerty+-!@\n")
    f.write("finish Him")
    f.close()
    #test
    checker_func.splitter("split/test0")
    f1 = open("split/test01.txt", "wt")
    assert f1.readline() == "Hello World!!\n"
    assert f1.readline() == "qwerty+-!@\n"

    f2 = open("split/test02.txt", "wt")
    assert f2.readline() == "123456789\n"
    assert f2.readline() == "finish Him"
    #postcondition
    os.remove(("split/test0.txt"))
    os.remove(("split/test01.txt"))
    os.remove(("split/test02.txt"))