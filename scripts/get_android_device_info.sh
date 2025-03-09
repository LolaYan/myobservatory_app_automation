#!/bin/bash
# 获取设备信息
platformVersion=$(adb shell getprop ro.build.version.release)
deviceName=$(adb shell getprop ro.product.model)

# 获取当前前台应用包名和 Activity
currentApp=$(adb shell dumpsys window | grep mCurrentFocus)
appPackage=$(echo "$currentApp" | cut -d '/' -f1 | awk -F '.' '{print $NF}')
appActivity=$(echo "$currentApp" | cut -d '/' -f2 | sed 's/}//')

echo "Platform Version: $platformVersion"
echo "Device Name: $deviceName"
echo "App Package: $appPackage"
echo "App Activity: $appActivity"