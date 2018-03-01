# This file is part account_payment_gateway_redsys module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.account_payment_gateway_redsys.tests.test_account_payment_gateway_redsys import suite
except ImportError:
    from .test_account_payment_gateway_redsys import suite

__all__ = ['suite']
