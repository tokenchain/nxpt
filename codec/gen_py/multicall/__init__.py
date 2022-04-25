"""Generated wrapper for Multicall Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)
import time
from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider
from web3.exceptions import ContractLogicError
from moody.m.bases import ContractMethod, Validator, ContractBase, Signatures
from moody.m.tx_params import TxParams
from moody.libeb import MiliDoS
from moody import Bolors

# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for Multicall below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        MulticallValidator,
    )
except ImportError:

    class MulticallValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class MulticallCall(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    target: str

    callData: Union[bytes, str]


class AggregateMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the aggregate method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("aggregate")

    def validate_and_normalize_inputs(self, calls: List[MulticallCall])->any:
        """Validate the inputs to the aggregate method."""
        self.validator.assert_valid(
            method_name='aggregate',
            parameter_name='calls',
            argument_value=calls,
        )
        return (calls)



    def block_send(self, calls: List[MulticallCall],_valeth:int=0) -> Tuple[int, List[Union[bytes, str]]]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(calls)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("aggregate", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: aggregate")
            message = f"Error {er}: aggregate"
            self._on_fail("aggregate", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, aggregate: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, aggregate. Reason: Unknown")

            self._on_fail("aggregate", message)

    def send_transaction(self, calls: List[MulticallCall], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (calls) = self.validate_and_normalize_inputs(calls)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(calls).transact(tx_params.as_dict())

    def build_transaction(self, calls: List[MulticallCall], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (calls) = self.validate_and_normalize_inputs(calls)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(calls).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, calls: List[MulticallCall], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (calls) = self.validate_and_normalize_inputs(calls)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(calls).estimateGas(tx_params.as_dict())

class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """
    def __init__(self, abi: any):
        super().__init__(abi)

    def aggregate(self) -> str:
        return self._function_signatures["aggregate"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Multicall(ContractBase):
    """Wrapper class for Multicall Solidity contract."""
    _fn_aggregate: AggregateMethod
    """Constructor-initialized instance of
    :class:`AggregateMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: MulticallValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, Multicall.abi())
        web3 = core_lib.w3

        if not validator:
            validator = MulticallValidator(web3, contract_address)




        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=Multicall.abi()).functions
        self._signatures = SignatureGenerator(Multicall.abi())
        validator.bindSignatures(self._signatures)

        self._fn_aggregate = AggregateMethod(core_lib, contract_address, functions.aggregate, validator)


    
    
    
    def aggregate(self, calls: List[MulticallCall]) -> Tuple[int, List[Union[bytes, str]]]:
        """
        Implementation of aggregate in contract Multicall
        Method of the function
    
        """
    
        self._fn_aggregate.callback_onfail = self._callback_onfail
        self._fn_aggregate.callback_onsuccess = self._callback_onsuccess
        self._fn_aggregate.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_aggregate.gas_limit = self.call_contract_fee_amount
        self._fn_aggregate.gas_price_wei = self.call_contract_fee_price
        self._fn_aggregate.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_aggregate.block_send(calls)
    
    
    
    

    def CallContractWait(self, t_long:int)-> "Multicall":
        self._fn_aggregate.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall.Call[]","name":"calls","type":"tuple[]"}],"name":"aggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes[]","name":"returnData","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
