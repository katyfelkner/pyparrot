import paramiko
import os
from scp import SCPClient

p = paramiko.SSHClient()
p.load_system_host_keys()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect("172.20.10.3", port=22, username="pi", password="amolinguamlatinam")
with SCPClient(p.get_transport()) as scp:
   scp.put('/Volumes/data/katy/banana-test.jpg', remote_path="/home/pi/images")
# secure copy image from my mac to the pi
#os.system("scp banana-test.jpg pi@172.20.10.3:/home/pi/images")
# classify the image
stdin, stdout, stderr = p.exec_command("AIY-projects-python/src/examples/vision/image_classification.py -i images/banana-test.jpg")
opt = stdout.readlines()
opt = "".join(opt)
print(opt)

if "banana" in opt:
    print(True)
else:
    print(False)