# insight.py: Automates hooking with Frida
import frida, sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--class_name", help="FQDM name of the target class")
parser.add_argument("-p", "--package_name", help="FQDM of the app (ex: com.app.name, you can find it in the manifest file)")
args = parser.parse_args()


banner = """
-----------------------
insight.py
A tool based on Frida
-----------------------
"""
print(banner)

###########################################################################
jscode_enum = """
Java.perform(function(){
	var TARGET_CLASS='<ARG_CLASS_NAME>';
	
	console.log('Listing all class memebers:');
	var methods = Object.getOwnPropertyNames(Java.use(TARGET_CLASS).__proto__);
	methods.forEach(function(method,index) {
		console.log('Method #'+index+': '+method);
	});
});
""".replace('<ARG_CLASS_NAME>',args.class_name)

# pick up device
device = frida.get_device_manager().enumerate_devices()[-1]
# spawn process and get PID
pid = device.spawn([args.package_name])
# attach to PID
process = device.attach(pid)
# create script form code
script = process.create_script(jscode_enum)
# inject code
script.load()
device.resume(pid)
print("running...")
sys.stdin.read()
process.detach()
