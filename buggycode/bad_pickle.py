# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security
import pickle
import subprocess
import base64

# Input injection
def transcode_file(filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!

# Assert statements
def foo(user):
   assert user.is_admin, 'user does not have access'
   # secure code...

# Pickles
class RunBinSh():
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))


print(base64.b64encode(pickle.dumps(RunBinSh())))