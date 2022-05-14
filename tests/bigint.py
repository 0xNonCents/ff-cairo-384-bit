import pytest
from utils import (
    split,
    pack,
    field_modulus,
)
from math import sqrt
from hypothesis import given, strategies as st, settings

largest_factor = sqrt(2 ** (64 * 11))



@pytest.mark.asyncio
async def test_bigint_div_mod(bigint_factory):

    x = (10, 0, 0, 0, 0)
    y = (2, 0, 0)
    p = split(field_modulus)

    print(p)

    contract = bigint_factory
    execution_info = await contract.div_mod(x, y, p).call()

    result = pack(execution_info.result[0])

    assert result == (x + y) % field_modulus