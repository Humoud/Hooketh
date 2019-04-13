# Hooker.py: Automates hooking
import frida, sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("number", type=int, help="index number of the method to overload")
parser.add_argument("class_name", help="FQDM name of the target class")
parser.add_argument("package_name", help="FQDM of the app (ex: com.app.name, you can find it in the manifest file)")
args = parser.parse_args()



jscode = """
Java.perform(function(){
    TARGET_METHOD=<ARG_METHOD_NUM>;
	TARGET_CLASS='<ARG_CLASS_NAME>';
	
	console.log('Listing all class memebers:');
	var methods = Object.getOwnPropertyNames(Java.use(TARGET_CLASS).__proto__);
	methods.forEach(function(method,index) {
		console.log('Method #'+index+': '+method);
	});
		
	console.log('Overloading class: '+TARGET_CLASS);	
	var using = Java.use(TARGET_CLASS);
	methods.forEach(function(method,index) {
		if(index==TARGET_METHOD){
			console.log('Method #'+index+': '+method);
			const clazz = Java.use(TARGET_CLASS);
			// get overload parameters
			overloads = clazz[method].overloads;
			for (i in overloads) {
				if (overloads[i].hasOwnProperty('argumentTypes')) {
				    var parameters = [];
				    for (j in overloads[i].argumentTypes) {
				        parameters.push(overloads[i].argumentTypes[j].className);
				    }

					console.log('Overloadable Params found: '+parameters);
					clazz[method].overload.apply('this', parameters).implementation = function(a,b,c,d,e,f,g,h,i,j,k){
						console.log('In target method: '+method+', dumping params:');
						console.log('Param1:   '+a);
						console.log('Param2:   '+b);
						console.log('Param3:   '+c);
						console.log('Param4:   '+d);
						console.log('Param5:   '+e);
						console.log('Param6:   '+f);
						console.log('Param7:   '+g);
						console.log('Param8:   '+h);
						console.log('Param9:   '+i);
						console.log('Param10:  '+j);		
                        console.log('Param11:  '+k);	
                        // continue executing, does not modify funcs implementation	
						var result = this[method].overload.apply('this', parameters).call(this,a,b,c,d,e,f,g,h,i,j,k);
                        console.log('+++>method returns: '+ result);
                        return this[method].overload.apply('this', parameters).call(this,a,b,c,d,e,f,g,h,i,j,k);
					}
				}
			}
		}
	});
});
""".replace('<ARG_METHOD_NUM>',str(args.number)).replace('<ARG_CLASS_NAME>',args.class_name)


# pick up device
device = frida.get_device_manager().enumerate_devices()[-1]
# spawn process and get PID
pid = device.spawn([args.package_name])
# attach to PID
process = device.attach(pid)
# create script form code
script = process.create_script(jscode)
# inject code
script.load()
device.resume(pid)
print("running...")
sys.stdin.read()
process.detach()
