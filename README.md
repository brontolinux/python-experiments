# Python libraries

## FileFinder

Helps finding files with exact match, glob or regex.

See [filefinder.py](filefinder.py)

### Dependencies

Standard library only


## X509Cert

Helps dealing with X509 Certificates (p.e. SSL/TLS). Simplifies the interface of the most tedious parts of `cryptography.x509`, namely:

* loading certificates
* check the expiration date
* check how many days of validity are left

See [x509cert.py](x509cert.py).

An example is available in the [examples directory](examplex/x509cert.py). It should work out of the box on any Debian distribution (or a derivative thereof) where the package `ca-certificates` is installed.

### Dependencies

* `cryptography`
* standard library

# Running tests

To perform all tests from the top directory, run

```shell
python3 -m unittest discover -v test
```

(where `python3` is the python 3 interpreter).