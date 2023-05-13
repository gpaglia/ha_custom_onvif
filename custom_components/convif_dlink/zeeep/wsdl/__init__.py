"""
    zeep.wsdl
    ---------

    The wsdl module is responsible for parsing the WSDL document. This includes
    the bindings and messages.

    The structure and naming of the modules and classses closely follows the
    WSDL 1.1 specification.

    The serialization and deserialization of the SOAP/HTTP messages is done
    by the zeep.wsdl.messages modules.


"""
from zeeep.wsdl.wsdl import Document  # noqa
