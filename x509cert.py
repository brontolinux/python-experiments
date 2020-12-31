import cryptography
from cryptography import x509
import os
import os.path
import datetime

class X509Cert():
    _cert_file = None
    _cert_data = None
    _cert_type = None
    _cert_backend = None
    _cert_obj = None
    _supported_types = ('pem','der')
    _load_cert = {
        'pem': x509.load_pem_x509_certificate,
        'der': x509.load_der_x509_certificate
    }

    def __init__(self, cert_file, cert_type=None, cert_backend=None):
        # Validate file name
        if not isinstance(cert_file,str):
            raise TypeError("cert_file parameter must be a string")

        if cert_file == "":
            raise ValueError("cert_file parameter must me a non-empty string")

        # Validate backend
        if cert_backend is None:
            self._cert_backend = cryptography.hazmat.backends.default_backend()
        else:
            self._cert_backend = cert_backend

        # Load certificate data
        try:
            with open(cert_file,'rb') as f:
                self._cert_file = cert_file
                self._cert_data = f.read()
        except OSError as err:
            print(f'Cannot read certificate: {err}')
            raise err

        if cert_type is None:
            # try to load the certificate anyway
            for c_type in self.supported_types:
                try:
                    self._cert_obj = self._load_cert[c_type](self._cert_data,self._cert_backend)
                except:
                    print(f'Cannot load {self._cert_file} as a {c_type} certificate')
                    continue
                else:
                    self._cert_type = c_type
                    break
            if self._cert_type is None:
                # The loop is done and we don't know the certificate type, so...
                raise ValueError("Cannot guess certificate type")
        else:
            # Validate certificate type
            if not cert_type in self.supported_types:
                raise ValueError(f'Unknown certificate type "{cert_type}"')
            self._cert_type = cert_type
            try:
                self._cert_obj = self._load_cert[self._cert_type](self._cert_data,self._cert_backend)
            except:
                raise NotImplementedError(f'Certificate load error (file is not a {self._cert_type} certificate?)')

    @property
    def certificate(self): return self._cert_obj

    @property
    def supported_types(self): return self._supported_types

    @property
    def expiration_date(self): return self.certificate.not_valid_after

    @property
    def days_valid(self):
        delta_valid = self.expiration_date - datetime.datetime.now()
        return delta_valid.days

    @property
    def cert_file(self): return self._cert_file

    @property
    def cert_type(self): return self._cert_type

