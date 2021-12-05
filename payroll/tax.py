from dataclasses import dataclass
from typing import List, TextIO
import json
import sys


class InvalidTaxRateConfig(Exception):
    pass

@dataclass
class TaxItem:
    tax_rate: int
    low: int
    high: int

    def __str__(self) -> str:
        return f"{self.tax_rate}c for each $1 from ${self.low} to ${self.high}"


class TaxConfig:
    @classmethod
    def from_json(cls, json_file: TextIO) -> List[TaxItem]:
        data = json.load(json_file)
        try:
            tax_table = [
                TaxItem(item['rate'], item.get('low', 0), item.get('high', sys.maxsize))
                for item in data['rates']
            ]
            if cls.validate(tax_table):
                return tax_table
            else:
                raise InvalidTaxRateConfig
        except KeyError:
            print(f"Invalid tax item config in {data}")
            raise InvalidTaxRateConfig

    @classmethod
    def validate(cls, tax_table: List[TaxItem]) -> bool:
        return all(
            ((low_rate.high+1) == high_rate.low)
            for low_rate, high_rate in zip(tax_table, tax_table[1:])
        )


def calculate_tax(tax_items: List[TaxItem], gross_amount: float) -> float:
    total_tax = 0
    for item in tax_items:
        if gross_amount < item.low:
            break
        tax = (min(gross_amount, item.high) - item.low + 1) * item.tax_rate / 100
        total_tax += tax

    return total_tax





