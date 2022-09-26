"""
Relationships/Entities

- ParkingSpotType
    - Small
    - Medium
    - Large
    - Handicapped
- Car
    - Make and Model
- Payment
- ParkingSpot
    - Size of the lot
    - Occupied: bool
    - Car: Car
- Floor
    - ViewVacantParkingSpots()
- Parking
    - Floors: list[Floor[ParkingSpot]]
- Admin
    - AddCars()
    - RemoveCars()
    - ViewCars()
- User
    - Name
    - Email
    - Address
    - Car: list[Car]
    - ExistingParkings()
"""



