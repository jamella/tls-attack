from enum import *

from tls_attack.structure.TLSStructure import *

class TLSCertificateStruct(TLSStructure):
    certificates_length = TLSField(size = 3,  type = "int")
    certificates        = TLSField(
                                size = TLSFieldRef(name = "certificates_length"),
                                type = "TLSCertificate",
                                type_list = True
                            )