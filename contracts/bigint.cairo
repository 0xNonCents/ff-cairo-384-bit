%lang starknet
%builtins range_check

from lib.bigint import BigInt3, UnreducedBigInt3, UnreducedBigInt5, bigint_div_mod

# Returns the current balance.
@view
func div_mod{range_check_ptr}(x : UnreducedBigInt5, y : UnreducedBigInt3, p : BigInt3) -> (
    res : BigInt3
):
    let (res : BigInt3) = bigint_div_mod(x, y, p)
    return (res)
end
