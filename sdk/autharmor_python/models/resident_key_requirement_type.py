# coding: utf-8

"""
    Autharmor

    Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

    The version of the OpenAPI document: v4
    Contact: support@autharmor.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ResidentKeyRequirementType(str, Enum):
    """
    ResidentKeyRequirementType
    """

    """
    allowed enum values
    """
    REQUIRED = 'required'
    PREFERRED = 'preferred'
    DISCOURAGED = 'discouraged'

    @classmethod
    def from_json(cls, json_str: str) -> ResidentKeyRequirementType:
        """Create an instance of ResidentKeyRequirementType from a JSON string"""
        return ResidentKeyRequirementType(json.loads(json_str))

