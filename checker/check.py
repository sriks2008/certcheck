from OpenSSL.crypto import *
import sys

def main():
    if (len(sys.argv) != 3):
        print "Usage: certchecker pathtofile privatekeypassword"
        exit(1)

    fileName = sys.argv[1]
    privateKeyPassword = sys.argv[2]

    print "Values for %s and %s" % (fileName, privateKeyPassword)

    try:
        p12 = load_pkcs12(file(fileName, 'rb').read(), privateKeyPassword)
    except Error as e:
        sys.exit(e.message)

    print "read certificate"
    p12.get_certificate() 

    print "read private key"
    p12.get_privatekey()

    print "read ca certificates"
    cacerts = p12.get_ca_certificates()

    if cacerts is None:
        sys.exit("Cert chain is empty. INVALID CERT")
    else:
        print "VALID CERT"

