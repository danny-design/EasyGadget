import os
import shutil
import subprocess
import zipfile

#用CMD运行objection命令
subprocess.call(["cmd.exe", "/c", "objection patchapk --source example.apk"])

#获取当前adb设备的架构类型
output = subprocess.check_output(["adb", "shell", "getprop", "ro.product.cpu.abi"])
device_arch = output.decode("utf-8").strip()

#将libhook.so和libfrida-gadget.so复制到apk的lib文件夹中对应设备架构的文件夹内
apk_path = "example.objection.apk"
apk_zip = zipfile.ZipFile(apk_path, "a")
lib_dir = "lib/" + device_arch + "/"
if not os.path.exists(lib_dir):
    os.makedirs(lib_dir)
shutil.copy("example.js", "libhook.so")
shutil.copy("libfrida-gadget.config.so", lib_dir)
apk_zip.write("libhook.so", lib_dir + "libhook.so")
apk_zip.write("libfrida-gadget.config.so", lib_dir + "libfrida-gadget.config.so")
apk_zip.close()
os.remove("libhook.so")
shutil.rmtree("lib")