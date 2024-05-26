import subprocess

folder_in = "/home/zerg/tst"
folder_out = "/home/zerg/out"

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def test_step1():
    assert checkout("cd /home/zerg/tst; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"

def test_step2():
    result_1 = checkout("cd /home/zerg/out; 7z e arx2.7z -o/home/zerg/folder1 -y", "Everything is Ok")
    result_2 = checkout("cd /home/zerg/out; ls", "test1")
    result_3 = checkout("cd /home/zerg/out; ls", "test2")
    assert result_1 and result_2 and result_3, "test2 FAIL"

def test_step3():
    result_1 = checkout("cd /home/zerg/out; 7z l arx2.7z", "test1")
    result_2 = checkout("cd /home/zerg/out; 7z l arx2.7z", "test2")
    assert result_1 and result_2, "test3 FAIL"

def test_step4():
    result_1 = checkout("cd /home/zerg/out; 7z x arx2.7z -o/home/zerg/folder1", "Everything is Ok")
    result_2 = checkout("cd /home/zerg/folder1; ls", "test1")
    result_3 = checkout("cd /home/zerg/folder1; ls", "test2")
    assert result_1 and result_2 and result_3, "test4 FAIL"

def test_step5():
    assert checkout("cd /home/zerg/out; 7z t arx2.7z", "Everything is Ok"), "test5 FAIL"

def test_step6():
    assert checkout("cd {}; 7z u arx2.7z".format(folder_in), "Everything is Ok"), "test6 FAIL"

def test_step7():
    assert checkout("cd {}; 7z d arx2.7z".format(folder_out), "Everything is Ok"), "test6 FAIL"



