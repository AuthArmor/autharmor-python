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

from autharmor_python.models.start_authenticator_auth_request import StartAuthenticatorAuthRequest  # noqa: E501

class TestStartAuthenticatorAuthRequest(unittest.TestCase):
    """StartAuthenticatorAuthRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StartAuthenticatorAuthRequest:
        """Test StartAuthenticatorAuthRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StartAuthenticatorAuthRequest`
        """
        model = StartAuthenticatorAuthRequest()  # noqa: E501
        if include_optional:
            return StartAuthenticatorAuthRequest(
                username = '',
                user_id = '',
                nonce = '',
                send_push = True,
                use_visual_verify = True,
                timeout_in_seconds = 56,
                origin_location_data = autharmor_python.models.location_data.location_data(
                    latitude = '', 
                    longitude = '', 
                    ip_address = '', ),
                action_name = '',
                short_msg = '',
                ip_address = '',
                user_agent = ''
            )
        else:
            return StartAuthenticatorAuthRequest(
        )
        """

    def testStartAuthenticatorAuthRequest(self):
        """Test StartAuthenticatorAuthRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
