#!/usr/bin/python3

from filefinder import FileFinder
from x509cert import X509Cert

dcroot_path = '/usr/share/ca-certificates/mozilla'
dcroot_glob = ['DigiCert_Global_Root_*.crt']

dc_certs = FileFinder(dcroot_path).glob(dcroot_glob)
if len(dc_certs) == 0:
    print(f'no certificates in {dcroot_path} match the given glob {dcroot_glob[0]}')
    exit

for cert_file in dc_certs:
    cert = X509Cert(cert_file,'pem')
    expiration = cert.expiration_date
    delta_days = cert.days_valid

    if delta_days > 1:
        print(f'Certificate in file {cert_file} expires in {delta_days} days, on {expiration}')
    elif delta_days == 1:
        print(f'Certificate in file {cert_file} expires TOMORROW!!!')
    elif delta_days == 0:
        print(f'Certificate in file {cert_file} expires TODAY!!!')
    else:
        print(f'Certificate in file {cert_file} HAS ALREADY EXPIRED!!!')
