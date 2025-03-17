from abc import ABC, abstractmethod
from ..Abstracts.InterfaceAbstract import InterfaceAbstract
from ..Abstracts.ConectorAbstract import ConectorAbstract

class ControllerAbstract(ABC):
    @abstractmethod
    def __init__(self, interface: InterfaceAbstract, conector: ConectorAbstract):
        pass

    @abstractmethod
    def processar(self):
        pass