# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.pool import Pool


class SaleProjectInvoiceMilestoneTestCase(ModuleTestCase):
    'Test Sale Project Invoice Milestone module'
    module = 'sale_project_invoice_milestone'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleProjectInvoiceMilestoneTestCase))
    return suite
