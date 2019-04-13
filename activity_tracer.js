////////////#################
/// TRACE ACTIVITIES
///
Java.perform(function () {
    send("Listing activities in sequence:")

    var System = Java.use('java.lang.System');
    var ActivityThread = Java.use("android.app.ActivityThread");
    Java.use("android.app.Activity").onCreate.overload("android.os.Bundle").implementation = function (savedInstanceState) {
        var currentActivity = this;

        // Get Main Activity
        var application = ActivityThread.currentApplication();
        var launcherIntent = application.getPackageManager().getLaunchIntentForPackage(application.getPackageName());
        var launchActivityInfo = launcherIntent.resolveActivityInfo(application.getPackageManager(), 0);

        // Alert Will Only Execute On Main Package Activity Creation
        if (launchActivityInfo.name.value === this.getComponentName().getClassName()) {
            // Create Alert
            send("got main activity and component(dont know wtf this is so dont ask me)");
            send("---MAIN-->" + launchActivityInfo.name.value);
            send("--MAIN-->" + this.getComponentName().getClassName());
        }
        send("-++--" + launchActivityInfo.name.value);
        send("-+/--" + this.getComponentName().getClassName());
        return this.onCreate.overload("android.os.Bundle").call(this, savedInstanceState);
    };
});
