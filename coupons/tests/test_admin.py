from packaging.version import Version
from unittest import skipIf

import django
from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from coupons.admin import CouponAdmin
from coupons.models import Coupon


class MockRequest(object):
    pass


request = MockRequest()


class CouponAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()

    @skipIf(
        Version(django.get_version()) < Version("1.7"),
        "Skip list display test due to missing method.",
    )
    def test_list_display(self):
        admin = CouponAdmin(Coupon, self.site)

        self.assertEqual(
            list(admin.get_fields(request)),
            ["value", "code", "type", "user_limit", "valid_until", "campaign"],
        )
