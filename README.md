# Next Five Rocket Launches

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A Python 3 command-line tool to display upcoming launches from a JSON API. HTTPS only, network timeout, maximum response size, robust optional-field handling and a configurable display limit. No third-party Python dependencies.

```sh
python3 RocketLaunch.py
python3 RocketLaunch.py --limit 10
python3 -m unittest discover -s tests -v
```

The default feed is `https://astrometry.ch/rockets.json`; its availability, accuracy and freshness depend on the external provider. Network integration is not part of the offline unit tests.

Historical code: [old branch](https://github.com/hamdyaea/Next_five_rocket_launches/tree/old).
