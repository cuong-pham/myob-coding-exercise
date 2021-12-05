from dataclasses import dataclass

@dataclass
class Income:
    gross_amount: float
    income_tax: float

    @property
    def monthly_gross_amount(self) -> float:
        return self.gross_amount / 12

    @property
    def monthly_income_tax(self) -> float:
        return self.income_tax / 12

    @property
    def monthly_net_income(self) -> float:
        return self.monthly_gross_amount - self.monthly_income_tax

@dataclass
class Payslip:
    name: str
    monthly_gross_income: float
    monthly_income_tax: float
    monthly_net_income: float

    def __str__(self) -> str:
        return f"""
    Monthly Payslip for: {self.name}
    Gross Monthly Income: ${self.monthly_gross_income}
    Monthly Income Tax: ${self.monthly_income_tax}
    Monthly Net Income: ${self.monthly_net_income}
"""

    def __eq__(self, other):
        return self.name == other.name and \
            self.monthly_net_income == other.monthly_net_income and \
            self.monthly_gross_income == other.monthly_gross_income and \
            self.monthly_income_tax == other.monthly_income_tax