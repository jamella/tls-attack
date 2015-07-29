from enum import *

from tls_attack.structure.TLSStructure import *

class TLSVersion(Enum):
    SSLv3  = 0x0300
    TLS10  = 0x0301
    TLS11  = 0x0302
    TLS12  = 0x0303

class TLSContentType(Enum):
    TLSChangeCipherSpec = 20
    TLSAlert            = 21
    TLSHandshake        = 22
    TLSApplicationData  = 23
    TLSHeartbeat        = 24

class TLSHeader(TLSStructure):
    content_type = TLSField(size = 1, type = "int")
    version      = TLSField(size = 2, type = "int")
    length       = TLSField(size = 2, type = "int")
    body         = TLSField(
                        size = TLSFieldRef(name = "length"), 
                        type = TLSFieldRef(name = "content_type"),
                        type_ref = TLSContentType,
                        encryptable = True
                    )

