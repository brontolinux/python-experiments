#!/usr/bin/python3

import unittest
from x509cert import X509Cert
import cryptography
import os.path

class CertLoadCase(unittest.TestCase):
    test_cert = os.path.join(os.path.dirname(os.path.realpath(__file__)),'DigiCert_Global_Root_CA.crt')

    def test_open_pem(self):
        cert = X509Cert(self.test_cert,'pem')
        self.assertIsInstance(cert,X509Cert)

    def test_open_generic(self):
        cert = X509Cert(self.test_cert,'pem')
        self.assertIsInstance(cert,X509Cert)

    def test_open_invalid_file(self):
        with self.assertRaises(ValueError):
            cert = X509Cert(__file__)

    def test_open_invalid_file_with_type(self):
        with self.assertRaises(NotImplementedError):
            cert = X509Cert(__file__,'pem')

    def test_open_invalid_type(self):
        with self.assertRaises(ValueError):
            cert = X509Cert(self.test_cert,'boom')

class CertTestInputCase(unittest.TestCase):
    def test_null_filename(self):
        with self.assertRaises(ValueError):
            cert = X509Cert("")

    def test_wrong_type_filename(self):
        with self.assertRaises(TypeError):
            cert = X509Cert([])

    def test_non_existent_filename(self):
        with self.assertRaises(OSError):
            cert = X509Cert('I_really_hope_you_dont_have_such_a_file_in_this_directory_do_you')

class CertTestOutputCase(unittest.TestCase):
    def setUp(self):
        self.test_cert = os.path.join(os.path.dirname(os.path.realpath(__file__)),'DigiCert_Global_Root_CA.crt')
        self.cert = X509Cert(self.test_cert,'pem')

    def test_certificate_type(self):
        self.assertIsInstance(self.cert.certificate,cryptography.x509.Certificate)

    def test_supported_types_type(self):
        self.assertIsInstance(self.cert.supported_types,tuple)

    def test_days_valid_type(self):
        self.assertIsInstance(self.cert.days_valid,int)

    def test_cert_file_type(self):
        self.assertIsInstance(self.cert.cert_file,str)

    def test_cert_type_type(self):
        self.assertIsInstance(self.cert.cert_type,str)



if __name__ == '__main__':
    unittest.main(verbosity=2)