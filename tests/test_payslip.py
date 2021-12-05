from payroll.payslip import Income, Payslip
from payslip_gen import get_pay_slip

def test_net_income():
    income = Income(gross_amount=60000, income_tax=6000)

    assert income.monthly_net_income == 4500


def test_get_pay_slip():
    payslip = get_pay_slip("steve", 60000)

    assert payslip == Payslip("steve", 5000, 500, 4500)