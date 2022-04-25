"""Generated wrapper for PriceOracle Solidity contract."""

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
# constructor for PriceOracle below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        PriceOracleValidator,
    )
except ImportError:

    class PriceOracleValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class GetTokenPriceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getTokenPrice method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getTokenPrice")

    def validate_and_normalize_inputs(self, token: str)->any:
        """Validate the inputs to the getTokenPrice method."""
        self.validator.assert_valid(
            method_name='getTokenPrice',
            parameter_name='token',
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        return (token)



    def block_call(self,token: str, debug:bool=False) -> int:
        _fn = self._underlying_method(token)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, token: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token)
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

                self._on_receipt_handle("get_token_price", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_token_price")
            message = f"Error {er}: get_token_price"
            self._on_fail("get_token_price", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_token_price: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_token_price. Reason: Unknown")

            self._on_fail("get_token_price", message)

    def send_transaction(self, token: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token) = self.validate_and_normalize_inputs(token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token).transact(tx_params.as_dict())

    def build_transaction(self, token: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token) = self.validate_and_normalize_inputs(token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token) = self.validate_and_normalize_inputs(token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token).estimateGas(tx_params.as_dict())

class IsPriceOracleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isPriceOracle method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("isPriceOracle")



    def block_call(self, debug:bool=False) -> bool:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, _valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
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

                self._on_receipt_handle("is_price_oracle", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: is_price_oracle")
            message = f"Error {er}: is_price_oracle"
            self._on_fail("is_price_oracle", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_price_oracle: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_price_oracle. Reason: Unknown")

            self._on_fail("is_price_oracle", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """
    def __init__(self, abi: any):
        super().__init__(abi)

    def get_token_price(self) -> str:
        return self._function_signatures["getTokenPrice"]
    def is_price_oracle(self) -> str:
        return self._function_signatures["isPriceOracle"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class PriceOracle(ContractBase):
    """Wrapper class for PriceOracle Solidity contract."""
    _fn_get_token_price: GetTokenPriceMethod
    """Constructor-initialized instance of
    :class:`GetTokenPriceMethod`.
    """

    _fn_is_price_oracle: IsPriceOracleMethod
    """Constructor-initialized instance of
    :class:`IsPriceOracleMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: PriceOracleValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, PriceOracle.abi())
        web3 = core_lib.w3

        if not validator:
            validator = PriceOracleValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=PriceOracle.abi()).functions
        self._signatures = SignatureGenerator(PriceOracle.abi())
        validator.bindSignatures(self._signatures)

        self._fn_get_token_price = GetTokenPriceMethod(core_lib, contract_address, functions.getTokenPrice, validator)
        self._fn_is_price_oracle = IsPriceOracleMethod(core_lib, contract_address, functions.isPriceOracle, validator)


    
    
    
    def get_token_price(self, token: str) -> int:
        """
        Implementation of get_token_price in contract PriceOracle
        Method of the function
    
        """
    
        self._fn_get_token_price.callback_onfail = self._callback_onfail
        self._fn_get_token_price.callback_onsuccess = self._callback_onsuccess
        self._fn_get_token_price.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_token_price.gas_limit = self.call_contract_fee_amount
        self._fn_get_token_price.gas_price_wei = self.call_contract_fee_price
        self._fn_get_token_price.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_token_price.block_call(token)
    
    
    
    def is_price_oracle(self) -> bool:
        """
        Implementation of is_price_oracle in contract PriceOracle
        Method of the function
    
        """
    
        self._fn_is_price_oracle.callback_onfail = self._callback_onfail
        self._fn_is_price_oracle.callback_onsuccess = self._callback_onsuccess
        self._fn_is_price_oracle.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_is_price_oracle.gas_limit = self.call_contract_fee_amount
        self._fn_is_price_oracle.gas_price_wei = self.call_contract_fee_price
        self._fn_is_price_oracle.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_is_price_oracle.block_call()

    def CallContractWait(self, t_long:int)-> "PriceOracle":
        self._fn_get_token_price.setWait(t_long)
        self._fn_is_price_oracle.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"getTokenPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPriceOracle","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
