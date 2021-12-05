import pytest
import sys
from io import StringIO
from payroll.tax import TaxItem, TaxConfig, calculate_tax, InvalidTaxRateConfig


def test_calculate_tax(tax_rate_items):
    assert calculate_tax(tax_rate_items, 60000) == 6000


def test_zero_dollar_income(tax_rate_items):
    assert calculate_tax(tax_rate_items, 0) == 0


def test_high_brakcet_income(tax_rate_items):
    assert calculate_tax(tax_rate_items, 200000) == 48000


def test_validate_wrong_tax_table(invalid_tax_items):
    assert not TaxConfig.validate(invalid_tax_items)


def test_validate_correct_tax_table(tax_rate_items):
    assert TaxConfig.validate(tax_rate_items)


def test_load_correct_tax_config(tax_rates_io, tax_rate_items):
    assert TaxConfig.from_json(tax_rates_io) == tax_rate_items


def test_raise_exception_load_malfored_tax_config(malformed_tax_rates_io):
    with pytest.raises(InvalidTaxRateConfig):
        TaxConfig.from_json(malformed_tax_rates_io)


@pytest.fixture
def invalid_tax_items():
    return [
        TaxItem(10, 0, 100),
        TaxItem(20, 101, 200),
        TaxItem(30, 205, 400)
    ]

@pytest.fixture
def tax_rate_items():
    return [
        TaxItem(0, 0, 20000),
        TaxItem(10, 20001, 40000),
        TaxItem(20, 40001, 80000),
        TaxItem(30, 80001, 180000),
        TaxItem(40, 180001, sys.maxsize)
    ]


@pytest.fixture
def tax_rates_io():
    return StringIO("""
    {"rates": [
        {"rate": 0, "high": 20000},
        {"rate": 10, "low": 20001, "high": 40000},
        {"rate": 20, "low": 40001, "high": 80000},
        {"rate": 30, "low": 80001, "high": 180000},
        {"rate": 40, "low": 180001}
    ]}
    """)

@pytest.fixture
def malformed_tax_rates_io():
    return StringIO("""
    {"rates": [
        {"tax_rate": 0, "high": 20000},
        {"tax_rate": 10, "low": 20001, "high": 40000},
        {"tax_rate": 20, "low": 40001, "high": 80000},
        {"tax_rate": 30, "low": 80001, "high": 180000},
        {"tax_rate": 40, "low": 180001}
    ]}
    """)