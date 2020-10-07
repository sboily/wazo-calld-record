Add record control to wazo-calld

Installation
------------

    wazo-plugind-cli -c "install git https://github.com/sboily/wazo-calld-record"

Use
---

Check the API in your wazo in calld section in http://wazo_ip/api

ACL
---

Please add the correct ACL in /etc/wazo-auth-keys/config.yml for the user wazo-calld to talking with amid.

Then launch:
    wazo-auth-keys service update



All channels in a conversation:

MixMonitor
MixMonitorMute
StopMixMonitor

One channel:

Monitor
StopMonitor
PauseMonitor
UnPauseMonitor
ChangeMonitor

Events:

MonitorStart
MonitorStop
