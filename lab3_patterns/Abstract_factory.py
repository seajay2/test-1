from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

class VictorianChair(Chair):
    def sit_on(self):
        return 'Sitting on Victorian chair'

class ModernChair(Chair):
    def sit_on(self):
        return 'Sitting on Modern chair'

class VictorianSofa(Sofa):
    def lie_on(self):
        return 'Lying on Victorian sofa'

class ModernSofa(Sofa):
    def lie_on(self):
        return 'Lying on Modern sofa'

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    def create_sofa(self) -> Sofa:
        return VictorianSofa()

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    def create_sofa(self) -> Sofa:
        return ModernSofa()

if __name__ == '__main__':
    factories = [VictorianFurnitureFactory(), ModernFurnitureFactory()]
    for factory in factories:
        chair = factory.create_chair()
        sofa = factory.create_sofa()
        print(chair.sit_on())
        print(sofa.lie_on())
