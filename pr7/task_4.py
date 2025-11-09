from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class IScanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class ICopier(ABC):
    @abstractmethod
    def copy_document(self):
        pass

class NetworkMachine(IPrinter, IScanner, ICopier):
    def print_document(self, document):
        print(f"Printing: {document} via network")

    def scan_document(self):
        print("Scanning document via network...")

    def copy_document(self):
        print("Copying document...")

class SimplePrinter(IPrinter):
    def print_document(self, document):
        print(f"Printing: {document} on simple printer")

class SimpleScanner(IScanner):
    def scan_document(self):
        print("Scanning document on simple scanner...")
