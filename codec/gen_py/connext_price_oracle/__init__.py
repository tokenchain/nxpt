"""Generated wrapper for ConnextPriceOracle Solidity contract."""

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
# constructor for ConnextPriceOracle below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ConnextPriceOracleValidator,
    )
except ImportError:

    class ConnextPriceOracleValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class AdminMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the admin method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("admin")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _valeth:int=0) -> str:
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

                self._on_receipt_handle("admin", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: admin")
            message = f"Error {er}: admin"
            self._on_fail("admin", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, admin: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, admin. Reason: Unknown")

            self._on_fail("admin", message)

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

class AggregatorsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the aggregators method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("aggregators")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the aggregators method."""
        self.validator.assert_valid(
            method_name='aggregators',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> str:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, index_0: str,_valeth:int=0) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
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

                self._on_receipt_handle("aggregators", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: aggregators")
            message = f"Error {er}: aggregators"
            self._on_fail("aggregators", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, aggregators: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, aggregators. Reason: Unknown")

            self._on_fail("aggregators", message)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class AssetPricesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the assetPrices method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("assetPrices")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the assetPrices method."""
        self.validator.assert_valid(
            method_name='assetPrices',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> int:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, index_0: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
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

                self._on_receipt_handle("asset_prices", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: asset_prices")
            message = f"Error {er}: asset_prices"
            self._on_fail("asset_prices", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, asset_prices: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, asset_prices. Reason: Unknown")

            self._on_fail("asset_prices", message)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class GetPriceFromChainlinkMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getPriceFromChainlink method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getPriceFromChainlink")

    def validate_and_normalize_inputs(self, token_address: str)->any:
        """Validate the inputs to the getPriceFromChainlink method."""
        self.validator.assert_valid(
            method_name='getPriceFromChainlink',
            parameter_name='_tokenAddress',
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        return (token_address)



    def block_call(self,token_address: str, debug:bool=False) -> int:
        _fn = self._underlying_method(token_address)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, token_address: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token_address)
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

                self._on_receipt_handle("get_price_from_chainlink", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_price_from_chainlink")
            message = f"Error {er}: get_price_from_chainlink"
            self._on_fail("get_price_from_chainlink", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_price_from_chainlink: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_price_from_chainlink. Reason: Unknown")

            self._on_fail("get_price_from_chainlink", message)

    def send_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).transact(tx_params.as_dict())

    def build_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_address: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).estimateGas(tx_params.as_dict())

class GetPriceFromDexMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getPriceFromDex method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getPriceFromDex")

    def validate_and_normalize_inputs(self, token_address: str)->any:
        """Validate the inputs to the getPriceFromDex method."""
        self.validator.assert_valid(
            method_name='getPriceFromDex',
            parameter_name='_tokenAddress',
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        return (token_address)



    def block_call(self,token_address: str, debug:bool=False) -> int:
        _fn = self._underlying_method(token_address)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, token_address: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token_address)
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

                self._on_receipt_handle("get_price_from_dex", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_price_from_dex")
            message = f"Error {er}: get_price_from_dex"
            self._on_fail("get_price_from_dex", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_price_from_dex: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_price_from_dex. Reason: Unknown")

            self._on_fail("get_price_from_dex", message)

    def send_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).transact(tx_params.as_dict())

    def build_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_address: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).estimateGas(tx_params.as_dict())

class GetPriceFromOracleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getPriceFromOracle method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getPriceFromOracle")

    def validate_and_normalize_inputs(self, token_address: str)->any:
        """Validate the inputs to the getPriceFromOracle method."""
        self.validator.assert_valid(
            method_name='getPriceFromOracle',
            parameter_name='_tokenAddress',
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        return (token_address)



    def block_call(self,token_address: str, debug:bool=False) -> int:
        _fn = self._underlying_method(token_address)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, token_address: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token_address)
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

                self._on_receipt_handle("get_price_from_oracle", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_price_from_oracle")
            message = f"Error {er}: get_price_from_oracle"
            self._on_fail("get_price_from_oracle", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_price_from_oracle: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_price_from_oracle. Reason: Unknown")

            self._on_fail("get_price_from_oracle", message)

    def send_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).transact(tx_params.as_dict())

    def build_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_address: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).estimateGas(tx_params.as_dict())

class GetTokenPriceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getTokenPrice method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getTokenPrice")

    def validate_and_normalize_inputs(self, token_address: str)->any:
        """Validate the inputs to the getTokenPrice method."""
        self.validator.assert_valid(
            method_name='getTokenPrice',
            parameter_name='_tokenAddress',
            argument_value=token_address,
        )
        token_address = self.validate_and_checksum_address(token_address)
        return (token_address)



    def block_call(self,token_address: str, debug:bool=False) -> int:
        _fn = self._underlying_method(token_address)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, token_address: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token_address)
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

    def send_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).transact(tx_params.as_dict())

    def build_transaction(self, token_address: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_address: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_address) = self.validate_and_normalize_inputs(token_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_address).estimateGas(tx_params.as_dict())

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

class PriceRecordsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the priceRecords method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("priceRecords")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the priceRecords method."""
        self.validator.assert_valid(
            method_name='priceRecords',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> Tuple[str, str, str, bool]:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return (returned[0],returned[1],returned[2],returned[3],)
    def block_send(self, index_0: str,_valeth:int=0) -> Tuple[str, str, str, bool]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
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

                self._on_receipt_handle("price_records", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: price_records")
            message = f"Error {er}: price_records"
            self._on_fail("price_records", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, price_records: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, price_records. Reason: Unknown")

            self._on_fail("price_records", message)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class SetAdminMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setAdmin method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setAdmin")

    def validate_and_normalize_inputs(self, new_admin: str)->any:
        """Validate the inputs to the setAdmin method."""
        self.validator.assert_valid(
            method_name='setAdmin',
            parameter_name='newAdmin',
            argument_value=new_admin,
        )
        new_admin = self.validate_and_checksum_address(new_admin)
        return (new_admin)



    def block_send(self, new_admin: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(new_admin)
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

                self._on_receipt_handle("set_admin", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_admin")
            message = f"Error {er}: set_admin"
            self._on_fail("set_admin", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_admin: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_admin. Reason: Unknown")

            self._on_fail("set_admin", message)

    def send_transaction(self, new_admin: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_admin) = self.validate_and_normalize_inputs(new_admin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_admin).transact(tx_params.as_dict())

    def build_transaction(self, new_admin: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_admin) = self.validate_and_normalize_inputs(new_admin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_admin).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, new_admin: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (new_admin) = self.validate_and_normalize_inputs(new_admin)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_admin).estimateGas(tx_params.as_dict())

class SetAggregatorsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setAggregators method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setAggregators")

    def validate_and_normalize_inputs(self, token_addresses: List[str], sources: List[str])->any:
        """Validate the inputs to the setAggregators method."""
        self.validator.assert_valid(
            method_name='setAggregators',
            parameter_name='tokenAddresses',
            argument_value=token_addresses,
        )
        self.validator.assert_valid(
            method_name='setAggregators',
            parameter_name='sources',
            argument_value=sources,
        )
        return (token_addresses, sources)



    def block_send(self, token_addresses: List[str], sources: List[str],_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token_addresses, sources)
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

                self._on_receipt_handle("set_aggregators", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_aggregators")
            message = f"Error {er}: set_aggregators"
            self._on_fail("set_aggregators", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_aggregators: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_aggregators. Reason: Unknown")

            self._on_fail("set_aggregators", message)

    def send_transaction(self, token_addresses: List[str], sources: List[str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token_addresses, sources) = self.validate_and_normalize_inputs(token_addresses, sources)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_addresses, sources).transact(tx_params.as_dict())

    def build_transaction(self, token_addresses: List[str], sources: List[str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token_addresses, sources) = self.validate_and_normalize_inputs(token_addresses, sources)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_addresses, sources).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token_addresses: List[str], sources: List[str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token_addresses, sources) = self.validate_and_normalize_inputs(token_addresses, sources)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token_addresses, sources).estimateGas(tx_params.as_dict())

class SetDexPriceInfoMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setDexPriceInfo method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setDexPriceInfo")

    def validate_and_normalize_inputs(self, token: str, base_token: str, lp_token: str, active: bool)->any:
        """Validate the inputs to the setDexPriceInfo method."""
        self.validator.assert_valid(
            method_name='setDexPriceInfo',
            parameter_name='_token',
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        self.validator.assert_valid(
            method_name='setDexPriceInfo',
            parameter_name='_baseToken',
            argument_value=base_token,
        )
        base_token = self.validate_and_checksum_address(base_token)
        self.validator.assert_valid(
            method_name='setDexPriceInfo',
            parameter_name='_lpToken',
            argument_value=lp_token,
        )
        lp_token = self.validate_and_checksum_address(lp_token)
        self.validator.assert_valid(
            method_name='setDexPriceInfo',
            parameter_name='_active',
            argument_value=active,
        )
        return (token, base_token, lp_token, active)



    def block_send(self, token: str, base_token: str, lp_token: str, active: bool,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token, base_token, lp_token, active)
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

                self._on_receipt_handle("set_dex_price_info", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_dex_price_info")
            message = f"Error {er}: set_dex_price_info"
            self._on_fail("set_dex_price_info", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_dex_price_info: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_dex_price_info. Reason: Unknown")

            self._on_fail("set_dex_price_info", message)

    def send_transaction(self, token: str, base_token: str, lp_token: str, active: bool, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token, base_token, lp_token, active) = self.validate_and_normalize_inputs(token, base_token, lp_token, active)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, base_token, lp_token, active).transact(tx_params.as_dict())

    def build_transaction(self, token: str, base_token: str, lp_token: str, active: bool, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token, base_token, lp_token, active) = self.validate_and_normalize_inputs(token, base_token, lp_token, active)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, base_token, lp_token, active).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token: str, base_token: str, lp_token: str, active: bool, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token, base_token, lp_token, active) = self.validate_and_normalize_inputs(token, base_token, lp_token, active)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, base_token, lp_token, active).estimateGas(tx_params.as_dict())

class SetDirectPriceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setDirectPrice method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setDirectPrice")

    def validate_and_normalize_inputs(self, token: str, price: int)->any:
        """Validate the inputs to the setDirectPrice method."""
        self.validator.assert_valid(
            method_name='setDirectPrice',
            parameter_name='_token',
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        self.validator.assert_valid(
            method_name='setDirectPrice',
            parameter_name='_price',
            argument_value=price,
        )
        # safeguard against fractional inputs
        price = int(price)
        return (token, price)



    def block_send(self, token: str, price: int,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(token, price)
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

                self._on_receipt_handle("set_direct_price", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_direct_price")
            message = f"Error {er}: set_direct_price"
            self._on_fail("set_direct_price", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_direct_price: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_direct_price. Reason: Unknown")

            self._on_fail("set_direct_price", message)

    def send_transaction(self, token: str, price: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token, price) = self.validate_and_normalize_inputs(token, price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, price).transact(tx_params.as_dict())

    def build_transaction(self, token: str, price: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (token, price) = self.validate_and_normalize_inputs(token, price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, price).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, token: str, price: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (token, price) = self.validate_and_normalize_inputs(token, price)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, price).estimateGas(tx_params.as_dict())

class SetV1PriceOracleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setV1PriceOracle method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setV1PriceOracle")

    def validate_and_normalize_inputs(self, v1_price_oracle: str)->any:
        """Validate the inputs to the setV1PriceOracle method."""
        self.validator.assert_valid(
            method_name='setV1PriceOracle',
            parameter_name='_v1PriceOracle',
            argument_value=v1_price_oracle,
        )
        v1_price_oracle = self.validate_and_checksum_address(v1_price_oracle)
        return (v1_price_oracle)



    def block_send(self, v1_price_oracle: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(v1_price_oracle)
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

                self._on_receipt_handle("set_v1_price_oracle", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_v1_price_oracle")
            message = f"Error {er}: set_v1_price_oracle"
            self._on_fail("set_v1_price_oracle", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_v1_price_oracle: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_v1_price_oracle. Reason: Unknown")

            self._on_fail("set_v1_price_oracle", message)

    def send_transaction(self, v1_price_oracle: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (v1_price_oracle) = self.validate_and_normalize_inputs(v1_price_oracle)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(v1_price_oracle).transact(tx_params.as_dict())

    def build_transaction(self, v1_price_oracle: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (v1_price_oracle) = self.validate_and_normalize_inputs(v1_price_oracle)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(v1_price_oracle).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, v1_price_oracle: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (v1_price_oracle) = self.validate_and_normalize_inputs(v1_price_oracle)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(v1_price_oracle).estimateGas(tx_params.as_dict())

class V1PriceOracleMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the v1PriceOracle method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("v1PriceOracle")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _valeth:int=0) -> str:
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

                self._on_receipt_handle("v1_price_oracle", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: v1_price_oracle")
            message = f"Error {er}: v1_price_oracle"
            self._on_fail("v1_price_oracle", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, v1_price_oracle: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, v1_price_oracle. Reason: Unknown")

            self._on_fail("v1_price_oracle", message)

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

class WrappedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the wrapped method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("wrapped")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _valeth:int=0) -> str:
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

                self._on_receipt_handle("wrapped", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: wrapped")
            message = f"Error {er}: wrapped"
            self._on_fail("wrapped", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, wrapped: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, wrapped. Reason: Unknown")

            self._on_fail("wrapped", message)

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

    def admin(self) -> str:
        return self._function_signatures["admin"]
    def aggregators(self) -> str:
        return self._function_signatures["aggregators"]
    def asset_prices(self) -> str:
        return self._function_signatures["assetPrices"]
    def get_price_from_chainlink(self) -> str:
        return self._function_signatures["getPriceFromChainlink"]
    def get_price_from_dex(self) -> str:
        return self._function_signatures["getPriceFromDex"]
    def get_price_from_oracle(self) -> str:
        return self._function_signatures["getPriceFromOracle"]
    def get_token_price(self) -> str:
        return self._function_signatures["getTokenPrice"]
    def is_price_oracle(self) -> str:
        return self._function_signatures["isPriceOracle"]
    def price_records(self) -> str:
        return self._function_signatures["priceRecords"]
    def set_admin(self) -> str:
        return self._function_signatures["setAdmin"]
    def set_aggregators(self) -> str:
        return self._function_signatures["setAggregators"]
    def set_dex_price_info(self) -> str:
        return self._function_signatures["setDexPriceInfo"]
    def set_direct_price(self) -> str:
        return self._function_signatures["setDirectPrice"]
    def set_v1_price_oracle(self) -> str:
        return self._function_signatures["setV1PriceOracle"]
    def v1_price_oracle(self) -> str:
        return self._function_signatures["v1PriceOracle"]
    def wrapped(self) -> str:
        return self._function_signatures["wrapped"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ConnextPriceOracle(ContractBase):
    """Wrapper class for ConnextPriceOracle Solidity contract."""
    _fn_admin: AdminMethod
    """Constructor-initialized instance of
    :class:`AdminMethod`.
    """

    _fn_aggregators: AggregatorsMethod
    """Constructor-initialized instance of
    :class:`AggregatorsMethod`.
    """

    _fn_asset_prices: AssetPricesMethod
    """Constructor-initialized instance of
    :class:`AssetPricesMethod`.
    """

    _fn_get_price_from_chainlink: GetPriceFromChainlinkMethod
    """Constructor-initialized instance of
    :class:`GetPriceFromChainlinkMethod`.
    """

    _fn_get_price_from_dex: GetPriceFromDexMethod
    """Constructor-initialized instance of
    :class:`GetPriceFromDexMethod`.
    """

    _fn_get_price_from_oracle: GetPriceFromOracleMethod
    """Constructor-initialized instance of
    :class:`GetPriceFromOracleMethod`.
    """

    _fn_get_token_price: GetTokenPriceMethod
    """Constructor-initialized instance of
    :class:`GetTokenPriceMethod`.
    """

    _fn_is_price_oracle: IsPriceOracleMethod
    """Constructor-initialized instance of
    :class:`IsPriceOracleMethod`.
    """

    _fn_price_records: PriceRecordsMethod
    """Constructor-initialized instance of
    :class:`PriceRecordsMethod`.
    """

    _fn_set_admin: SetAdminMethod
    """Constructor-initialized instance of
    :class:`SetAdminMethod`.
    """

    _fn_set_aggregators: SetAggregatorsMethod
    """Constructor-initialized instance of
    :class:`SetAggregatorsMethod`.
    """

    _fn_set_dex_price_info: SetDexPriceInfoMethod
    """Constructor-initialized instance of
    :class:`SetDexPriceInfoMethod`.
    """

    _fn_set_direct_price: SetDirectPriceMethod
    """Constructor-initialized instance of
    :class:`SetDirectPriceMethod`.
    """

    _fn_set_v1_price_oracle: SetV1PriceOracleMethod
    """Constructor-initialized instance of
    :class:`SetV1PriceOracleMethod`.
    """

    _fn_v1_price_oracle: V1PriceOracleMethod
    """Constructor-initialized instance of
    :class:`V1PriceOracleMethod`.
    """

    _fn_wrapped: WrappedMethod
    """Constructor-initialized instance of
    :class:`WrappedMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: ConnextPriceOracleValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, ConnextPriceOracle.abi())
        web3 = core_lib.w3

        if not validator:
            validator = ConnextPriceOracleValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=ConnextPriceOracle.abi()).functions
        self._signatures = SignatureGenerator(ConnextPriceOracle.abi())
        validator.bindSignatures(self._signatures)

        self._fn_admin = AdminMethod(core_lib, contract_address, functions.admin, validator)
        self._fn_aggregators = AggregatorsMethod(core_lib, contract_address, functions.aggregators, validator)
        self._fn_asset_prices = AssetPricesMethod(core_lib, contract_address, functions.assetPrices, validator)
        self._fn_get_price_from_chainlink = GetPriceFromChainlinkMethod(core_lib, contract_address, functions.getPriceFromChainlink, validator)
        self._fn_get_price_from_dex = GetPriceFromDexMethod(core_lib, contract_address, functions.getPriceFromDex, validator)
        self._fn_get_price_from_oracle = GetPriceFromOracleMethod(core_lib, contract_address, functions.getPriceFromOracle, validator)
        self._fn_get_token_price = GetTokenPriceMethod(core_lib, contract_address, functions.getTokenPrice, validator)
        self._fn_is_price_oracle = IsPriceOracleMethod(core_lib, contract_address, functions.isPriceOracle, validator)
        self._fn_price_records = PriceRecordsMethod(core_lib, contract_address, functions.priceRecords, validator)
        self._fn_set_admin = SetAdminMethod(core_lib, contract_address, functions.setAdmin, validator)
        self._fn_set_aggregators = SetAggregatorsMethod(core_lib, contract_address, functions.setAggregators, validator)
        self._fn_set_dex_price_info = SetDexPriceInfoMethod(core_lib, contract_address, functions.setDexPriceInfo, validator)
        self._fn_set_direct_price = SetDirectPriceMethod(core_lib, contract_address, functions.setDirectPrice, validator)
        self._fn_set_v1_price_oracle = SetV1PriceOracleMethod(core_lib, contract_address, functions.setV1PriceOracle, validator)
        self._fn_v1_price_oracle = V1PriceOracleMethod(core_lib, contract_address, functions.v1PriceOracle, validator)
        self._fn_wrapped = WrappedMethod(core_lib, contract_address, functions.wrapped, validator)

    
    
    def event_aggregator_updated(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event aggregator_updated in contract ConnextPriceOracle
        Get log entry for AggregatorUpdated event.
                :param tx_hash: hash of transaction emitting AggregatorUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ConnextPriceOracle.abi()).events.AggregatorUpdated().processReceipt(tx_receipt)
    
    
    def event_direct_price_updated(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event direct_price_updated in contract ConnextPriceOracle
        Get log entry for DirectPriceUpdated event.
                :param tx_hash: hash of transaction emitting DirectPriceUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ConnextPriceOracle.abi()).events.DirectPriceUpdated().processReceipt(tx_receipt)
    
    
    def event_new_admin(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event new_admin in contract ConnextPriceOracle
        Get log entry for NewAdmin event.
                :param tx_hash: hash of transaction emitting NewAdmin event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ConnextPriceOracle.abi()).events.NewAdmin().processReceipt(tx_receipt)
    
    
    def event_price_record_updated(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event price_record_updated in contract ConnextPriceOracle
        Get log entry for PriceRecordUpdated event.
                :param tx_hash: hash of transaction emitting PriceRecordUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ConnextPriceOracle.abi()).events.PriceRecordUpdated().processReceipt(tx_receipt)
    
    
    def event_v1_price_oracle_updated(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event v1_price_oracle_updated in contract ConnextPriceOracle
        Get log entry for V1PriceOracleUpdated event.
                :param tx_hash: hash of transaction emitting V1PriceOracleUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ConnextPriceOracle.abi()).events.V1PriceOracleUpdated().processReceipt(tx_receipt)

    
    
    
    def admin(self) -> str:
        """
        Implementation of admin in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_admin.callback_onfail = self._callback_onfail
        self._fn_admin.callback_onsuccess = self._callback_onsuccess
        self._fn_admin.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_admin.gas_limit = self.call_contract_fee_amount
        self._fn_admin.gas_price_wei = self.call_contract_fee_price
        self._fn_admin.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_admin.block_call()
    
    
    
    def aggregators(self, index_0: str) -> str:
        """
        Implementation of aggregators in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_aggregators.callback_onfail = self._callback_onfail
        self._fn_aggregators.callback_onsuccess = self._callback_onsuccess
        self._fn_aggregators.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_aggregators.gas_limit = self.call_contract_fee_amount
        self._fn_aggregators.gas_price_wei = self.call_contract_fee_price
        self._fn_aggregators.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_aggregators.block_call(index_0)
    
    
    
    def asset_prices(self, index_0: str) -> int:
        """
        Implementation of asset_prices in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_asset_prices.callback_onfail = self._callback_onfail
        self._fn_asset_prices.callback_onsuccess = self._callback_onsuccess
        self._fn_asset_prices.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_asset_prices.gas_limit = self.call_contract_fee_amount
        self._fn_asset_prices.gas_price_wei = self.call_contract_fee_price
        self._fn_asset_prices.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_asset_prices.block_call(index_0)
    
    
    
    def get_price_from_chainlink(self, token_address: str) -> int:
        """
        Implementation of get_price_from_chainlink in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_get_price_from_chainlink.callback_onfail = self._callback_onfail
        self._fn_get_price_from_chainlink.callback_onsuccess = self._callback_onsuccess
        self._fn_get_price_from_chainlink.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_price_from_chainlink.gas_limit = self.call_contract_fee_amount
        self._fn_get_price_from_chainlink.gas_price_wei = self.call_contract_fee_price
        self._fn_get_price_from_chainlink.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_price_from_chainlink.block_call(token_address)
    
    
    
    def get_price_from_dex(self, token_address: str) -> int:
        """
        Implementation of get_price_from_dex in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_get_price_from_dex.callback_onfail = self._callback_onfail
        self._fn_get_price_from_dex.callback_onsuccess = self._callback_onsuccess
        self._fn_get_price_from_dex.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_price_from_dex.gas_limit = self.call_contract_fee_amount
        self._fn_get_price_from_dex.gas_price_wei = self.call_contract_fee_price
        self._fn_get_price_from_dex.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_price_from_dex.block_call(token_address)
    
    
    
    def get_price_from_oracle(self, token_address: str) -> int:
        """
        Implementation of get_price_from_oracle in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_get_price_from_oracle.callback_onfail = self._callback_onfail
        self._fn_get_price_from_oracle.callback_onsuccess = self._callback_onsuccess
        self._fn_get_price_from_oracle.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_price_from_oracle.gas_limit = self.call_contract_fee_amount
        self._fn_get_price_from_oracle.gas_price_wei = self.call_contract_fee_price
        self._fn_get_price_from_oracle.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_price_from_oracle.block_call(token_address)
    
    
    
    def get_token_price(self, token_address: str) -> int:
        """
        Implementation of get_token_price in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_get_token_price.callback_onfail = self._callback_onfail
        self._fn_get_token_price.callback_onsuccess = self._callback_onsuccess
        self._fn_get_token_price.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_token_price.gas_limit = self.call_contract_fee_amount
        self._fn_get_token_price.gas_price_wei = self.call_contract_fee_price
        self._fn_get_token_price.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_token_price.block_call(token_address)
    
    
    
    def is_price_oracle(self) -> bool:
        """
        Implementation of is_price_oracle in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_is_price_oracle.callback_onfail = self._callback_onfail
        self._fn_is_price_oracle.callback_onsuccess = self._callback_onsuccess
        self._fn_is_price_oracle.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_is_price_oracle.gas_limit = self.call_contract_fee_amount
        self._fn_is_price_oracle.gas_price_wei = self.call_contract_fee_price
        self._fn_is_price_oracle.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_is_price_oracle.block_call()
    
    
    
    def price_records(self, index_0: str) -> Tuple[str, str, str, bool]:
        """
        Implementation of price_records in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_price_records.callback_onfail = self._callback_onfail
        self._fn_price_records.callback_onsuccess = self._callback_onsuccess
        self._fn_price_records.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_price_records.gas_limit = self.call_contract_fee_amount
        self._fn_price_records.gas_price_wei = self.call_contract_fee_price
        self._fn_price_records.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_price_records.block_call(index_0)
    
    
    
    def set_admin(self, new_admin: str) -> None:
        """
        Implementation of set_admin in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_set_admin.callback_onfail = self._callback_onfail
        self._fn_set_admin.callback_onsuccess = self._callback_onsuccess
        self._fn_set_admin.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_admin.gas_limit = self.call_contract_fee_amount
        self._fn_set_admin.gas_price_wei = self.call_contract_fee_price
        self._fn_set_admin.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_admin.block_send(new_admin)
    
    
    
    
    
    
    
    def set_aggregators(self, token_addresses: List[str], sources: List[str]) -> None:
        """
        Implementation of set_aggregators in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_set_aggregators.callback_onfail = self._callback_onfail
        self._fn_set_aggregators.callback_onsuccess = self._callback_onsuccess
        self._fn_set_aggregators.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_aggregators.gas_limit = self.call_contract_fee_amount
        self._fn_set_aggregators.gas_price_wei = self.call_contract_fee_price
        self._fn_set_aggregators.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_aggregators.block_send(token_addresses, sources)
    
    
    
    
    
    
    
    def set_dex_price_info(self, token: str, base_token: str, lp_token: str, active: bool) -> None:
        """
        Implementation of set_dex_price_info in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_set_dex_price_info.callback_onfail = self._callback_onfail
        self._fn_set_dex_price_info.callback_onsuccess = self._callback_onsuccess
        self._fn_set_dex_price_info.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_dex_price_info.gas_limit = self.call_contract_fee_amount
        self._fn_set_dex_price_info.gas_price_wei = self.call_contract_fee_price
        self._fn_set_dex_price_info.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_dex_price_info.block_send(token, base_token, lp_token, active)
    
    
    
    
    
    
    
    def set_direct_price(self, token: str, price: int) -> None:
        """
        Implementation of set_direct_price in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_set_direct_price.callback_onfail = self._callback_onfail
        self._fn_set_direct_price.callback_onsuccess = self._callback_onsuccess
        self._fn_set_direct_price.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_direct_price.gas_limit = self.call_contract_fee_amount
        self._fn_set_direct_price.gas_price_wei = self.call_contract_fee_price
        self._fn_set_direct_price.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_direct_price.block_send(token, price)
    
    
    
    
    
    
    
    def set_v1_price_oracle(self, v1_price_oracle: str) -> None:
        """
        Implementation of set_v1_price_oracle in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_set_v1_price_oracle.callback_onfail = self._callback_onfail
        self._fn_set_v1_price_oracle.callback_onsuccess = self._callback_onsuccess
        self._fn_set_v1_price_oracle.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_v1_price_oracle.gas_limit = self.call_contract_fee_amount
        self._fn_set_v1_price_oracle.gas_price_wei = self.call_contract_fee_price
        self._fn_set_v1_price_oracle.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_v1_price_oracle.block_send(v1_price_oracle)
    
    
    
    
    
    
    
    def v1_price_oracle(self) -> str:
        """
        Implementation of v1_price_oracle in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_v1_price_oracle.callback_onfail = self._callback_onfail
        self._fn_v1_price_oracle.callback_onsuccess = self._callback_onsuccess
        self._fn_v1_price_oracle.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_v1_price_oracle.gas_limit = self.call_contract_fee_amount
        self._fn_v1_price_oracle.gas_price_wei = self.call_contract_fee_price
        self._fn_v1_price_oracle.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_v1_price_oracle.block_call()
    
    
    
    def wrapped(self) -> str:
        """
        Implementation of wrapped in contract ConnextPriceOracle
        Method of the function
    
        """
    
        self._fn_wrapped.callback_onfail = self._callback_onfail
        self._fn_wrapped.callback_onsuccess = self._callback_onsuccess
        self._fn_wrapped.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_wrapped.gas_limit = self.call_contract_fee_amount
        self._fn_wrapped.gas_price_wei = self.call_contract_fee_price
        self._fn_wrapped.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_wrapped.block_call()

    def CallContractWait(self, t_long:int)-> "ConnextPriceOracle":
        self._fn_admin.setWait(t_long)
        self._fn_aggregators.setWait(t_long)
        self._fn_asset_prices.setWait(t_long)
        self._fn_get_price_from_chainlink.setWait(t_long)
        self._fn_get_price_from_dex.setWait(t_long)
        self._fn_get_price_from_oracle.setWait(t_long)
        self._fn_get_token_price.setWait(t_long)
        self._fn_is_price_oracle.setWait(t_long)
        self._fn_price_records.setWait(t_long)
        self._fn_set_admin.setWait(t_long)
        self._fn_set_aggregators.setWait(t_long)
        self._fn_set_dex_price_info.setWait(t_long)
        self._fn_set_direct_price.setWait(t_long)
        self._fn_set_v1_price_oracle.setWait(t_long)
        self._fn_v1_price_oracle.setWait(t_long)
        self._fn_wrapped.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_wrapped","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"tokenAddress","type":"address"},{"indexed":false,"internalType":"address","name":"source","type":"address"}],"name":"AggregatorUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"oldPrice","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newPrice","type":"uint256"}],"name":"DirectPriceUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"NewAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"baseToken","type":"address"},{"indexed":false,"internalType":"address","name":"lpToken","type":"address"},{"indexed":false,"internalType":"bool","name":"_active","type":"bool"}],"name":"PriceRecordUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldAddress","type":"address"},{"indexed":false,"internalType":"address","name":"newAddress","type":"address"}],"name":"V1PriceOracleUpdated","type":"event"},{"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"aggregators","outputs":[{"internalType":"contract AggregatorV3Interface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"assetPrices","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getPriceFromChainlink","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getPriceFromDex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getPriceFromOracle","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"getTokenPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPriceOracle","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"priceRecords","outputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"baseToken","type":"address"},{"internalType":"address","name":"lpToken","type":"address"},{"internalType":"bool","name":"active","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newAdmin","type":"address"}],"name":"setAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"tokenAddresses","type":"address[]"},{"internalType":"address[]","name":"sources","type":"address[]"}],"name":"setAggregators","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_baseToken","type":"address"},{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"bool","name":"_active","type":"bool"}],"name":"setDexPriceInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"setDirectPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_v1PriceOracle","type":"address"}],"name":"setV1PriceOracle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"v1PriceOracle","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"wrapped","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
