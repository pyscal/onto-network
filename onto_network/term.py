import xml.etree.ElementTree as ET

class OntoTerm:
    def __init__(self, uri, node_type=None, 
                domain=[], range=[], data_type=None, 
                 node_id=None, delimiter='/'):
        """
        This is class that represents an ontology element
        """
        self.uri = uri
        #name of the class
        self._name = None
        #type: can be object property, data property, or class
        self.node_type = node_type
        #now we need domain and range
        self.domain = domain
        self.range = range
        #datatype, that is only need for data properties
        self.data_type = data_type
        #identifier
        self.node_id = node_id
        self.subclasses = []
        self.delimiter = delimiter

    @property
    def uri(self):
        return self._uri
    
    @uri.setter
    def uri(self, val):
        self._uri = val
        if isinstance(val, BNode):
            self.node_id = val
        
    @property
    def name(self):
        uri_split = self.uri.split(self.delimiter)
        if len(uri_split)>1:
            return ":".join(uri_split[-2:])
        else:
            return self.uri