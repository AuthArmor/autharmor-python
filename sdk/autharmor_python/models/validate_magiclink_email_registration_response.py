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


from typing import Dict, Optional
from pydantic import BaseModel, StrictStr
from autharmor_python.models.magiclink_email_registration_type import MagiclinkEmailRegistrationType

class ValidateMagiclinkEmailRegistrationResponse(BaseModel):
    """
    ValidateMagiclinkEmailRegistrationResponse
    """
    magiclink_email_registration_type: Optional[MagiclinkEmailRegistrationType] = None
    user_id: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    email_address: Optional[StrictStr] = None
    context_data: Optional[Dict[str, StrictStr]] = None
    __properties = ["magiclink_email_registration_type", "user_id", "username", "email_address", "context_data"]

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
    def from_json(cls, json_str: str) -> ValidateMagiclinkEmailRegistrationResponse:
        """Create an instance of ValidateMagiclinkEmailRegistrationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        # set to None if email_address (nullable) is None
        # and __fields_set__ contains the field
        if self.email_address is None and "email_address" in self.__fields_set__:
            _dict['email_address'] = None

        # set to None if context_data (nullable) is None
        # and __fields_set__ contains the field
        if self.context_data is None and "context_data" in self.__fields_set__:
            _dict['context_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidateMagiclinkEmailRegistrationResponse:
        """Create an instance of ValidateMagiclinkEmailRegistrationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidateMagiclinkEmailRegistrationResponse.parse_obj(obj)

        _obj = ValidateMagiclinkEmailRegistrationResponse.parse_obj({
            "magiclink_email_registration_type": obj.get("magiclink_email_registration_type"),
            "user_id": obj.get("user_id"),
            "username": obj.get("username"),
            "email_address": obj.get("email_address"),
            "context_data": obj.get("context_data")
        })
        return _obj


