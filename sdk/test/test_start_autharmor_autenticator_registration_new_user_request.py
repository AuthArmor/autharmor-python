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

from autharmor_python.models.start_autharmor_autenticator_registration_new_user_request import StartAutharmorAutenticatorRegistrationNewUserRequest  # noqa: E501

class TestStartAutharmorAutenticatorRegistrationNewUserRequest(unittest.TestCase):
    """StartAutharmorAutenticatorRegistrationNewUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StartAutharmorAutenticatorRegistrationNewUserRequest:
        """Test StartAutharmorAutenticatorRegistrationNewUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StartAutharmorAutenticatorRegistrationNewUserRequest`
        """
        model = StartAutharmorAutenticatorRegistrationNewUserRequest()  # noqa: E501
        if include_optional:
            return StartAutharmorAutenticatorRegistrationNewUserRequest(
                username = '01',
                timeout_in_seconds = 56
            )
        else:
            return StartAutharmorAutenticatorRegistrationNewUserRequest(
                username = '01',
        )
        """

    def testStartAutharmorAutenticatorRegistrationNewUserRequest(self):
        """Test StartAutharmorAutenticatorRegistrationNewUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
