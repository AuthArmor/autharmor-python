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





class AuthMethods(str, Enum):
    """
    AuthMethods
    """

    """
    allowed enum values
    """
    MOBILEDEVICE = 'MobileDevice'
    SECURITYKEY = 'SecurityKey'
    AUTHARMORAUTHENTICATOR = 'AuthArmorAuthenticator'
    MAGICLINK_EMAIL = 'Magiclink_Email'
    MAIGCLINK_SMS = 'Maigclink_SMS'
    WEBAUTHN = 'WebAuthN'

    @classmethod
    def from_json(cls, json_str: str) -> AuthMethods:
        """Create an instance of AuthMethods from a JSON string"""
        return AuthMethods(json.loads(json_str))

