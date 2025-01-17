The [ONVIF](https://www.home-assistant.io/integrations/onvif/) integration in `Home Assistant` is very conservative.
It does not work with many cameras because some bugs are not fixed for years.
It is impossible to setup some cameras at all. Some cameras can be added, but sensors do not work. 
See [this issue](https://github.com/home-assistant/core/issues/45513) for more details.

This integration depends on [onvif-zeep-async==1.2.1](https://github.com/hunterjm/python-onvif-zeep-async) and `onvif-zeep-async` depends on [zeep[async]==4.1.0](https://github.com/mvantellingen/python-zeep).

Zeep 4.0.0 has been released in October 2020. It contains a lot of pull request for many months. I have no idea if my [patch](https://github.com/mvantellingen/python-zeep/pull/1206) will be merged and when.
After that, you need to wait for a new release and it should be integrated into Home Assistant.
Perhaps you need to wait another year. Perhaps this will never happen. Who knows?

*UPD: Zeep 4.1.0 has been released in August 2021. My patch was merged and then reverted. It seems the official ONVIF component won't be fixed in the coming years.*

[This merge request](https://github.com/home-assistant/core/pull/53432) is very revealing too.

I have collected few own patches to `zeep` and `ONVIF integration`.
I have renamed `zeep` and `onvif-zeep-async` modules to avoid conflicts and fixed the `ONVIF integration` to use these modules.

If you need to use `XM` (XiongMai, XMEye, iCSee), `Wansview` and many other `ONVIF` cameras, which are not supported yet, with `Home Assistant` `ONVIF integration` right now,
just unpack [ha_custom_onvif.zip](https://github.com/slydiman/ha_custom_onvif/releases/latest) to `config`/`custom_components` folder of your `Home Assistant` and restart it.

I hope one day this will no longer be necessary.

Known bugs: `Wanscam` `ONVIF` implementation is very buggy. Some `Wanscam` cameras can be added after disabling `Renew` request immediately after creating `PullPointSubscription` (`event.py`, line 86).
But it still does not work because `GetStreamUri` request fails. It seems `Wanscam` expects `<Stream` or `<tt:Stream` tag, but got `<ns1:Stream xmlns:ns1="http://www.onvif.org/ver10/schema">`.
Currently I don't know how to gracefully clean namespaces ns0, ns1, etc. in the soap request generated by zeep. There is no way to provide a custom nsmap.

Note: I have inverted the value of binary_sensors `Tamper Detection`, `Motion Alarm`, `Cell Motion Detection` and `Digital Input`, because it is necessary at least for XM cameras.
If you don't need it, just change `Value != "true"` to `Value == "true"` in the file `parsers.py`.
