"""
Entities/Relationships
1. Size - Small, Medium, Large (list of all sizes)
2. Package
    1. Package Id
    2. Package Size
    3. get_size()
    4. Package Status
3. Locker
    1. Locker ID
    2. Address
    3. Create Compartments
4. Compartment
    1. Compartment ID
    2. Packege
    3. Compartment Size
    4. Compartment Status
"""

import enum

class Size(enum.Emum):
    SMALL, MEDIUM, LARGE = 1, 2, 3

class PackageStatus(enum.Enum):
    PLACED, TAKEN = 1, 2

class Address:
    def __init__(self, locker_name, building_number, street, city, state, country, zip):
        self._locker_name = locker_name
        self._building_number = building_number
        self._street = street
        self._city = city
        self._state = state
        self._country = country
        self._zip = zip

class Package:
    def __init__(self, package_id: str, package_size: Size, package_status: PackageStatus):
        self._package_id = package_id
        self._package_size = package_size
        self._package_status = package_status
    
    def get_package_status(self):
        return self._package_status
    
    def get_package_size(self):
        return self._package_size

class Compartment:
    def __init__(self, compartment_id, compartment_size: Size):
        self._compartment_id = compartment_id
        self._package: Package = None
        self._compartmnet_size = compartment_size

    def add_package(self, package)  -> bool:
        if self._package != None:
            self._package = package
            return True
        else:
            return False

class Locker:
    def __init__(self, address: Address, locker_id: str):
        self._compartments: dict[str, list[Compartment]] = {size: list[Compartment] for size in Size}
        self._address = address

    def add_package(self, package: Package, size: Size):
        for compartment in self._compartments[size]:
            if not compartment._package:
                compartment._package = package
                return compartment._compartment_id
        
        if size == Size.LARGE:
            return False
        
        elif size == Size.SMALL:
            for size in [Size.MEDIUM, Size.LARGE]:
                pass
        elif size == Size.MEDIUM:
            for compartment in self._compartments[Size.LARGE]:
                pass
        
    def remove_package(self, package: Package) -> bool:
        pass
    



        


    




