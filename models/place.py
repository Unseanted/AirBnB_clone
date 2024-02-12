#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): Name of the place.
        description (str): Description of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        number_rooms (int): The number of rooms at the place.
        number_bathrooms (int): The number of bathrooms at the place.
        max_guest (int): The maximum number of guests the place can take.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    amenity_ids = []
