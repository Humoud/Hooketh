# Frida-Tools
A set of scripts that ease working with Frida

## Usage
For both of the scripts, I assume you have a device connected via USB.

### Using Activity_Tracer.js
You might have an apk file and you want to know what activities will run and in what sequence. In this case you can use `activity_tracer.js`:

`frida -U -f com.pkg.xxx.yyy -l activity_tracer.js --no-pause`

### Using Hooker.py
In case you want to list all methods of a class and you want to know what a methods returns, you can use `hooker.py`:

```
python3 hooker.py METHOD_NUM CLASS_NAME_FQDN

# start with passing "3" as a method number because that is the "init" method
python3 hooker.py 3 java.lang.String

# after executing the above, the script will list all the methods and number them
# pick a number and pass it again
python3 hooker.py 5 java.lang.String
```

**Note** that once you provide a class name and a number to the `hooker.py` script it will list all the methods of the class and number them. After that you can provide a number listed to get what that methods returns. I always start with 3 because that is the initialisation method. 
