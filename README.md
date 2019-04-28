# Frida-Tools
A set of scripts that ease working with Frida

## Usage
For both of the scripts, I assume you have a device connected via USB.

### Using Activity_Tracer.js
You might have an apk file and you want to know what activities will run and in what sequence. In this case you can use `activity_tracer.js`:

`frida -U -f com.pkg.xxx.yyy -l activity_tracer.js --no-pause`

### Using Hooketh.py
In case you want to list all methods of a class and you want to know what a methods returns, you can use `hooketh.py`:

```

python hooketh.py -h
usage: hooketh.py [-h] [-n NUMBER] [-c CLASS_NAME] [-t RETURN_TRUE]
                  [-p PACKAGE_NAME]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        index number of the method to overload
  -c CLASS_NAME, --class_name CLASS_NAME
                        FQDM name of the target class
  -t RETURN_TRUE, --return_true RETURN_TRUE
                        make method return true(type 1 or true)
  -p PACKAGE_NAME, --package_name PACKAGE_NAME
                        FQDM of the app (ex: com.app.name, you can find it in
                        the manifest file)

# If you do not provide a method number the script will use "3" as a method number because that is the "init" method
python3 hooker.py -c java.lang.String -p com.name1.name2.demo

# Make method 10 in the MainActivity return true
python3 hooker.py -c com.name1.name2.demo.MainActivity -p com.name1.name2.demo -n 10 -t true
```

**Note** that once you provide a class name and a number to the `hooker.py` script it will list all the methods of the class and number them. After that you can provide a number listed to get what that methods returns. I always start with 3 because that is the initialisation method. 
