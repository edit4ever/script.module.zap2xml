# script.module.zap2xml

Zap2xml is an epg grabber which creates an xmltv file from data scraped from Zap2it or TVguide listings.

This addon is designed for use as a replacement for the perl xmltv apps that are difficult to use on a LibreELEC/OpenELEC distro since perl is not available.

It has been tested using LibreELEC and OpenELEC running Tvheadend for the backend.


### Installing the addon manually:

1. Download and move the script.module.zap2xml.zip to your LibreELEC/OpenELEC machine using whatever method you are the most comfortable with.
2. Navigate to SYSTEM->Addons->Install from zip
    == use the file browser to navigate to the file and select it.
3. Navigate to SYSTEM->Addons->My Addons->Program Addons->zap2xml
4. Select Configure and set your username, password and options.
5. Reboot
6. Configure your tv backend to use tv_grab_zap2xml

Notes:
This addon is derived from the work of [FastEddyCurrent] (https://github.com/FastEddyCurrent/zap2xml)who ported the original perl based http://zap2xml.awardspace.info/ to Python.

