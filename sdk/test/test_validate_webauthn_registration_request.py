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

from autharmor_python.models.validate_webauthn_registration_request import ValidateWebauthnRegistrationRequest  # noqa: E501

class TestValidateWebauthnRegistrationRequest(unittest.TestCase):
    """ValidateWebauthnRegistrationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateWebauthnRegistrationRequest:
        """Test ValidateWebauthnRegistrationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateWebauthnRegistrationRequest`
        """
        model = ValidateWebauthnRegistrationRequest()  # noqa: E501
        if include_optional:
            return ValidateWebauthnRegistrationRequest(
                registration_validation_token = ''
            )
        else:
            return ValidateWebauthnRegistrationRequest(
        )
        """

    def testValidateWebauthnRegistrationRequest(self):
        """Test ValidateWebauthnRegistrationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()