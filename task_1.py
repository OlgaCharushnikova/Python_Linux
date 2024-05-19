import subprocess
def func(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    lst = out.split("\n")
    if text in lst and result.returncode == 0:
        print('True')
    else:
        print('False')
