# coding: utf-8

"""
    Autharmor

    Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

    The version of the OpenAPI document: v4
    Contact: support@autharmor.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr

class LocationData(BaseModel):
    """
    LocationData
    """
    latitude: Optional[StrictStr] = None
    longitude: Optional[StrictStr] = None
    ip_address: Optional[StrictStr] = None
    __properties = ["latitude", "longitude", "ip_address"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LocationData:
        """Create an instance of LocationData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if latitude (nullable) is None
        # and __fields_set__ contains the field
        if self.latitude is None and "latitude" in self.__fields_set__:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and __fields_set__ contains the field
        if self.longitude is None and "longitude" in self.__fields_set__:
            _dict['longitude'] = None

        # set to None if ip_address (nullable) is None
        # and __fields_set__ contains the field
        if self.ip_address is None and "ip_address" in self.__fields_set__:
            _dict['ip_address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LocationData:
        """Create an instance of LocationData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LocationData.parse_obj(obj)

        _obj = LocationData.parse_obj({
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "ip_address": obj.get("ip_address")
        })
        return _obj


