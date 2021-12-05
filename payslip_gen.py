#!/usr/bin/env python3

import argparse
import sys
from payroll.tax import calculate_tax, TaxConfig
from payroll.payslip import Income, Payslip


def get_pay_slip(name: str, amount: float) -> Payslip:
    with open("config/tax.json", "r") as f:
        tax_table = TaxConfig.from_json(f)
        tax = calculate_tax(tax_table, amount)

        income = Income(gross_amount=amount, income_tax=tax)
        return Payslip(
            name=name,
            monthly_income_tax=income.monthly_income_tax,
            monthly_net_income=income.monthly_net_income,
            monthly_gross_income=income.monthly_gross_amount
        )


def main(args):  # pragma: no cover
    parser = argparse.ArgumentParser("Generate Payslip")

    parser.add_argument("--name", dest="name", type=str, required = True, help="input fixed width file")
    parser.add_argument("--amount", dest="amount", type=float, required=True, help="output file")

    options = parser.parse_args(args)

    pay_slip = get_pay_slip(options.name, options.amount)

    print(pay_slip)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))