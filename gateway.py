# This file is part account_payment_gateway_redsys module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Equal

__all__ = ['AccountPaymentGateway']
__metaclass__ = PoolMeta


class AccountPaymentGateway:
    __name__ = 'account.payment.gateway'
    redsys_merchant_name = fields.Char('Merchant Name',
        states={
            'required': Equal(Eval('method'), 'redsys'),
            'invisible': ~(Equal(Eval('method'), 'redsys')),
        }, help='Redsys Merchant Name')
    redsys_merchant_code = fields.Char('Merchant Code',
        states={
            'required': Equal(Eval('method'), 'redsys'),
            'invisible': ~(Equal(Eval('method'), 'redsys')),
        }, help='Redsys Merchant Code')
    redsys_secret_key = fields.Char('Secret Key',
        states={
            'required': Equal(Eval('method'), 'redsys'),
            'invisible': ~(Equal(Eval('method'), 'redsys')),
        }, help='Redsys Secret Key')
    redsys_terminal = fields.Integer('Terminal',
        states={
            'required': Equal(Eval('method'), 'redsys'),
            'invisible': ~(Equal(Eval('method'), 'redsys')),
        }, help='Redsys Terminal')
    redsys_currency = fields.Integer('Currency',
        states={
            'required': Equal(Eval('method'), 'redsys'),
            'invisible': ~(Equal(Eval('method'), 'redsys')),
        }, help='Redsys Currency')
    redsys_transaction_type = fields.Integer('Transaction Type',
        states={
            'required': Equal(Eval('method'), 'redsys'),
            'invisible': ~(Equal(Eval('method'), 'redsys')),
        }, help='Redsys Transaction Type')
    redsys_sequence = fields.Many2One('ir.sequence', 'Sequence',
        states={
            'required': Equal(Eval('method'), 'redsys'),
            'invisible': ~(Equal(Eval('method'), 'redsys')),
        }, domain=[
            ('company', 'in',
            [Eval('context', {}).get('company', -1), None]),
        ], help='Redsys Sequence. Min. 4N. Max. 12 AN')

    @classmethod
    def get_methods(cls):
        res = super(AccountPaymentGateway, cls).get_methods()
        res.append(('redsys', 'Redsys'))
        return res
