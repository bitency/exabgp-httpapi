Simple ExaBGP http API for Python3.

Example Config EXABGP:
https://github.com/bitency/exabgp-httpapi/blob/main/example-exabgp-config

Example Curl:
curl --form "command=announce route 100.10.11.0/24 next-hop self" http://localhost:5001/


Basic rewrite from: https://thepacketgeek.com/exabgp/http-api/ (only fort Python2)
