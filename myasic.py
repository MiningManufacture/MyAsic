################################################ =@MyAsic 2020=#########################################################
# Monitoring of Bitmain miners S9,S17,L3+################################################################################
# @MiningManufacture by @Niko_Irk############################################################################################
import time
import config
import subprocess

# MAIN###################################################################################################################
while True:
    try:
        mod_inst = subprocess.Popen("pip3", shell=True, stdout=subprocess.DEVNULL)
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
                    print('package: pip installation FAILED! .. try "sudo apt install python3-pip" in hand mode! ')
            except:
                pass
    except:
        pass

    try:
        mod_inst = subprocess.Popen("pip3 install --upgrade myasicAPI", shell=True, stdout=subprocess.DEVNULL)
        mod_inst.wait()
        import myasicAPI

    except:
        print('package: myasicAPI not found .. try to install')
        try:
            mod_inst = subprocess.Popen("pip3 install --upgrade myasicAPI", shell=True, stdout=subprocess.DEVNULL)
            mod_inst.wait()
            import myasicAPI
            # print('package: installed')
        except Exception as e:
            # print(e)
            try:
                import myasicAPI
            except:
                print('package: myasicAPI installation FAILED! .. try "pip3 install myasicAPI" in hand mode! ')
                pass

    try:
        import myasicAPI
        myasicAPI.monitoring()
        print('run Ok! waiting ...')
        time.sleep(config.interval_sec)

    except Exception as e:
        pass
