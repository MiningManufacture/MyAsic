################################################ =@MyAsic 2020=#########################################################
# Monitoring of Bitmain miners S9,S17,L3+################################################################################
# @MiningManufacture by @Niko_Irk############################################################################################
import os
import time
import config
import subprocess
import sys

# MAIN###################################################################################################################
while True:
    try:
        mod_inst = subprocess.Popen("py -m pip install --upgrade -q -q -q pip", shell=True, stdout=subprocess.DEVNULL)
        mod_inst.wait()
        if mod_inst.returncode == 0:
            pass
        else:
            # print('package: pip3 not found .. try to install')
            try:
                mod_inst = subprocess.Popen("sudo apt-get install python3-pip", shell=True, stdout=subprocess.DEVNULL)
                mod_inst.wait()
                if mod_inst.returncode == 0:
                    # print('package: installed')
                    pass
                else:
                    print('package: pip installation FAILED! View READMI.md ')
            except:
                pass
    except:
        pass

    try:
        mod_inst = subprocess.Popen("py -m pip install --upgrade --no-python-version-warning -q -q -q wheel", shell=True, stdout=subprocess.DEVNULL)
        mod_inst.wait()
        import wheel

    except:
        # print('package: myasicAPI not found .. try to install')
        try:
            mod_inst = subprocess.Popen("pip3 install --upgrade -q -q -q wheel", shell=True, stdout=subprocess.DEVNULL)
            mod_inst.wait()
            # print('package: installed')
        except Exception as e:
            # print(e)
            try:
                import wheel
            except:
                print('package: wheel installation FAILED! View READMI.md ')
                pass

    try:
        mod_inst = subprocess.Popen("py -m pip install --upgrade --no-python-version-warning -q -q -q myasicAPI", shell=True, stdout=subprocess.DEVNULL)
        mod_inst.wait()
        import myasicAPI

    except:
        # print('package: myasicAPI not found .. try to install')
        try:
            mod_inst = subprocess.Popen("pip3 install --upgrade -q -q -q myasicAPI", shell=True, stdout=subprocess.DEVNULL)
            mod_inst.wait()
            import myasicAPI
            # print('package: installed')
        except Exception as e:
            # print(e)
            try:
                import myasicAPI
            except:
                print('package: myasicAPI installation FAILED! View READMI.md ')
                pass

    try:
        import myasicAPI
        # import myasicAPI_
        myasicAPI.monitoring()
        time.sleep(config.interval_sec)

    except Exception as e:
        pass
