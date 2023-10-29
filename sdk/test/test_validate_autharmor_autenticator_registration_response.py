# coding: utf-8

"""
    Autharmor

    Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

    The version of the OpenAPI document: v4
    Contact: support@autharmor.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from autharmor_python.models.validate_autharmor_autenticator_registration_response import ValidateAutharmorAutenticatorRegistrationResponse  # noqa: E501

class TestValidateAutharmorAutenticatorRegistrationResponse(unittest.TestCase):
    """ValidateAutharmorAutenticatorRegistrationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateAutharmorAutenticatorRegistrationResponse:
        """Test ValidateAutharmorAutenticatorRegistrationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateAutharmorAutenticatorRegistrationResponse`
        """
        model = ValidateAutharmorAutenticatorRegistrationResponse()  # noqa: E501
        if include_optional:
            return ValidateAutharmorAutenticatorRegistrationResponse(
                credential_id = '',
                user_id = '',
                username = ''
            )
        else:
            return ValidateAutharmorAutenticatorRegistrationResponse(
        )
        """

    def testValidateAutharmorAutenticatorRegistrationResponse(self):
        """Test ValidateAutharmorAutenticatorRegistrationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()