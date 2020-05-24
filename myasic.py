
import time
import config
import subprocess

def whatspython():
    py = ''
    mod_inst = subprocess.Popen("python --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    mod_inst.wait()
    if mod_inst.returncode == 0:
        py = 'python'
        pass
    else:
        mod_inst = subprocess.Popen("py --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        mod_inst.wait()
        if mod_inst.returncode == 0:
            py = 'py'
            pass
        else:
            mod_inst = subprocess.Popen("python3 --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            mod_inst.wait()
            if mod_inst.returncode == 0:
                py = 'python3'
                pass
    return py

def getplatform():
    import platform
    if platform.system() == 'Windows':
        return 0
    else:
        return 1

def  installwin(module):
    mod_inst = subprocess.Popen(pypy + " -m pip install --upgrade --no-python-version-warning -q -q -q " + module, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    mod_inst.wait()
    if mod_inst.returncode == 0:
        pass
    return 0

def  installlinux(module):
    mod_inst = subprocess.Popen(pypy + " -m pip install --upgrade --no-python-version-warning -q -q -q " + module, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    mod_inst.wait()
    if mod_inst.returncode == 0:
        pass
    return 0

pypy = whatspython()
try:
    if getplatform() == 0:
        try:
            installwin('pip')
            installwin('wheel')
            installwin('myasicAPI')
            installwin('telepot')
            installwin('requests')
        except:
            pass

    else:
        try:
            mod_inst = subprocess.Popen("sudo apt-get install --upgrade python3-pip", shell=True,
                                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            mod_inst.wait()
            if mod_inst.returncode == 0:
                pass
        except:
            try:
                mod_inst = subprocess.Popen("apt-get install --upgrade python3-pip", shell=True,
                                            stdout=subprocess.DEVNULL,
                                            stderr=subprocess.DEVNULL)
                mod_inst.wait()
                if mod_inst.returncode == 0:
                    pass
            except:
                pass
        try:
            installlinux('wheel')
            installlinux('myasicAPI')
        except:
            pass
except:
    print('ERROR 1: Cant install some modules!')
    pass

# MAIN##################################################################################################################
while True:
    try:
        import myasicAPI
        myasicAPI.monitoring()
        time.sleep(config.interval_sec)

    except Exception as e:
        pass
