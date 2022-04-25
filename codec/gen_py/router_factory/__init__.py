"""Generated wrapper for RouterFactory Solidity contract."""

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
# constructor for RouterFactory below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        RouterFactoryValidator,
    )
except ImportError:

    class RouterFactoryValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class CreateRouterMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the createRouter method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("createRouter")

    def validate_and_normalize_inputs(self, router_signer: str, recipient: str)->any:
        """Validate the inputs to the createRouter method."""
        self.validator.assert_valid(
            method_name='createRouter',
            parameter_name='routerSigner',
            argument_value=router_signer,
        )
        router_signer = self.validate_and_checksum_address(router_signer)
        self.validator.assert_valid(
            method_name='createRouter',
            parameter_name='recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (router_signer, recipient)



    def block_send(self, router_signer: str, recipient: str,_valeth:int=0) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(router_signer, recipient)
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

                self._on_receipt_handle("create_router", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: create_router")
            message = f"Error {er}: create_router"
            self._on_fail("create_router", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, create_router: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, create_router. Reason: Unknown")

            self._on_fail("create_router", message)

    def send_transaction(self, router_signer: str, recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (router_signer, recipient) = self.validate_and_normalize_inputs(router_signer, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router_signer, recipient).transact(tx_params.as_dict())

    def build_transaction(self, router_signer: str, recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (router_signer, recipient) = self.validate_and_normalize_inputs(router_signer, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router_signer, recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, router_signer: str, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (router_signer, recipient) = self.validate_and_normalize_inputs(router_signer, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router_signer, recipient).estimateGas(tx_params.as_dict())

class GetRouterAddressMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getRouterAddress method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getRouterAddress")

    def validate_and_normalize_inputs(self, router_signer: str)->any:
        """Validate the inputs to the getRouterAddress method."""
        self.validator.assert_valid(
            method_name='getRouterAddress',
            parameter_name='routerSigner',
            argument_value=router_signer,
        )
        router_signer = self.validate_and_checksum_address(router_signer)
        return (router_signer)



    def block_call(self,router_signer: str, debug:bool=False) -> str:
        _fn = self._underlying_method(router_signer)
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, router_signer: str,_valeth:int=0) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(router_signer)
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

                self._on_receipt_handle("get_router_address", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_router_address")
            message = f"Error {er}: get_router_address"
            self._on_fail("get_router_address", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_router_address: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_router_address. Reason: Unknown")

            self._on_fail("get_router_address", message)

    def send_transaction(self, router_signer: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (router_signer) = self.validate_and_normalize_inputs(router_signer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router_signer).transact(tx_params.as_dict())

    def build_transaction(self, router_signer: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (router_signer) = self.validate_and_normalize_inputs(router_signer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router_signer).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, router_signer: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (router_signer) = self.validate_and_normalize_inputs(router_signer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router_signer).estimateGas(tx_params.as_dict())

class InitMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the init method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("init")

    def validate_and_normalize_inputs(self, transaction_manager: str)->any:
        """Validate the inputs to the init method."""
        self.validator.assert_valid(
            method_name='init',
            parameter_name='_transactionManager',
            argument_value=transaction_manager,
        )
        transaction_manager = self.validate_and_checksum_address(transaction_manager)
        return (transaction_manager)



    def block_send(self, transaction_manager: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(transaction_manager)
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

                self._on_receipt_handle("init", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: init")
            message = f"Error {er}: init"
            self._on_fail("init", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, init: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, init. Reason: Unknown")

            self._on_fail("init", message)

    def send_transaction(self, transaction_manager: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (transaction_manager) = self.validate_and_normalize_inputs(transaction_manager)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_manager).transact(tx_params.as_dict())

    def build_transaction(self, transaction_manager: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (transaction_manager) = self.validate_and_normalize_inputs(transaction_manager)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_manager).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, transaction_manager: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (transaction_manager) = self.validate_and_normalize_inputs(transaction_manager)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_manager).estimateGas(tx_params.as_dict())

class OwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the owner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("owner")



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

                self._on_receipt_handle("owner", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: owner")
            message = f"Error {er}: owner"
            self._on_fail("owner", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, owner: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, owner. Reason: Unknown")

            self._on_fail("owner", message)

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

class RenounceOwnershipMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the renounceOwnership method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("renounceOwnership")



    def block_send(self, _valeth:int=0) -> None:
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

                self._on_receipt_handle("renounce_ownership", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: renounce_ownership")
            message = f"Error {er}: renounce_ownership"
            self._on_fail("renounce_ownership", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounce_ownership: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounce_ownership. Reason: Unknown")

            self._on_fail("renounce_ownership", message)

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

class RouterAddressesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerAddresses method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerAddresses")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the routerAddresses method."""
        self.validator.assert_valid(
            method_name='routerAddresses',
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

                self._on_receipt_handle("router_addresses", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_addresses")
            message = f"Error {er}: router_addresses"
            self._on_fail("router_addresses", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_addresses: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_addresses. Reason: Unknown")

            self._on_fail("router_addresses", message)

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

class TransactionManagerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the transactionManager method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("transactionManager")



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

                self._on_receipt_handle("transaction_manager", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: transaction_manager")
            message = f"Error {er}: transaction_manager"
            self._on_fail("transaction_manager", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transaction_manager: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transaction_manager. Reason: Unknown")

            self._on_fail("transaction_manager", message)

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

class TransferOwnershipMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the transferOwnership method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("transferOwnership")

    def validate_and_normalize_inputs(self, new_owner: str)->any:
        """Validate the inputs to the transferOwnership method."""
        self.validator.assert_valid(
            method_name='transferOwnership',
            parameter_name='newOwner',
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return (new_owner)



    def block_send(self, new_owner: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(new_owner)
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

                self._on_receipt_handle("transfer_ownership", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: transfer_ownership")
            message = f"Error {er}: transfer_ownership"
            self._on_fail("transfer_ownership", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transfer_ownership: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transfer_ownership. Reason: Unknown")

            self._on_fail("transfer_ownership", message)

    def send_transaction(self, new_owner: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).transact(tx_params.as_dict())

    def build_transaction(self, new_owner: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, new_owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).estimateGas(tx_params.as_dict())

class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """
    def __init__(self, abi: any):
        super().__init__(abi)

    def create_router(self) -> str:
        return self._function_signatures["createRouter"]
    def get_router_address(self) -> str:
        return self._function_signatures["getRouterAddress"]
    def init(self) -> str:
        return self._function_signatures["init"]
    def owner(self) -> str:
        return self._function_signatures["owner"]
    def renounce_ownership(self) -> str:
        return self._function_signatures["renounceOwnership"]
    def router_addresses(self) -> str:
        return self._function_signatures["routerAddresses"]
    def transaction_manager(self) -> str:
        return self._function_signatures["transactionManager"]
    def transfer_ownership(self) -> str:
        return self._function_signatures["transferOwnership"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class RouterFactory(ContractBase):
    """Wrapper class for RouterFactory Solidity contract."""
    _fn_create_router: CreateRouterMethod
    """Constructor-initialized instance of
    :class:`CreateRouterMethod`.
    """

    _fn_get_router_address: GetRouterAddressMethod
    """Constructor-initialized instance of
    :class:`GetRouterAddressMethod`.
    """

    _fn_init: InitMethod
    """Constructor-initialized instance of
    :class:`InitMethod`.
    """

    _fn_owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    _fn_renounce_ownership: RenounceOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceOwnershipMethod`.
    """

    _fn_router_addresses: RouterAddressesMethod
    """Constructor-initialized instance of
    :class:`RouterAddressesMethod`.
    """

    _fn_transaction_manager: TransactionManagerMethod
    """Constructor-initialized instance of
    :class:`TransactionManagerMethod`.
    """

    _fn_transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: RouterFactoryValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, RouterFactory.abi())
        web3 = core_lib.w3

        if not validator:
            validator = RouterFactoryValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=RouterFactory.abi()).functions
        self._signatures = SignatureGenerator(RouterFactory.abi())
        validator.bindSignatures(self._signatures)

        self._fn_create_router = CreateRouterMethod(core_lib, contract_address, functions.createRouter, validator)
        self._fn_get_router_address = GetRouterAddressMethod(core_lib, contract_address, functions.getRouterAddress, validator)
        self._fn_init = InitMethod(core_lib, contract_address, functions.init, validator)
        self._fn_owner = OwnerMethod(core_lib, contract_address, functions.owner, validator)
        self._fn_renounce_ownership = RenounceOwnershipMethod(core_lib, contract_address, functions.renounceOwnership, validator)
        self._fn_router_addresses = RouterAddressesMethod(core_lib, contract_address, functions.routerAddresses, validator)
        self._fn_transaction_manager = TransactionManagerMethod(core_lib, contract_address, functions.transactionManager, validator)
        self._fn_transfer_ownership = TransferOwnershipMethod(core_lib, contract_address, functions.transferOwnership, validator)

    
    
    def event_ownership_transferred(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_transferred in contract RouterFactory
        Get log entry for OwnershipTransferred event.
                :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=RouterFactory.abi()).events.OwnershipTransferred().processReceipt(tx_receipt)
    
    
    def event_router_created(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_created in contract RouterFactory
        Get log entry for RouterCreated event.
                :param tx_hash: hash of transaction emitting RouterCreated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=RouterFactory.abi()).events.RouterCreated().processReceipt(tx_receipt)

    
    
    
    def create_router(self, router_signer: str, recipient: str) -> str:
        """
        Implementation of create_router in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_create_router.callback_onfail = self._callback_onfail
        self._fn_create_router.callback_onsuccess = self._callback_onsuccess
        self._fn_create_router.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_create_router.gas_limit = self.call_contract_fee_amount
        self._fn_create_router.gas_price_wei = self.call_contract_fee_price
        self._fn_create_router.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_create_router.block_send(router_signer, recipient)
    
    
    
    
    
    
    
    def get_router_address(self, router_signer: str) -> str:
        """
        Implementation of get_router_address in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_get_router_address.callback_onfail = self._callback_onfail
        self._fn_get_router_address.callback_onsuccess = self._callback_onsuccess
        self._fn_get_router_address.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_router_address.gas_limit = self.call_contract_fee_amount
        self._fn_get_router_address.gas_price_wei = self.call_contract_fee_price
        self._fn_get_router_address.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_router_address.block_call(router_signer)
    
    
    
    def init(self, transaction_manager: str) -> None:
        """
        Implementation of init in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_init.callback_onfail = self._callback_onfail
        self._fn_init.callback_onsuccess = self._callback_onsuccess
        self._fn_init.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_init.gas_limit = self.call_contract_fee_amount
        self._fn_init.gas_price_wei = self.call_contract_fee_price
        self._fn_init.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_init.block_send(transaction_manager)
    
    
    
    
    
    
    
    def owner(self) -> str:
        """
        Implementation of owner in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_owner.callback_onfail = self._callback_onfail
        self._fn_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_owner.gas_limit = self.call_contract_fee_amount
        self._fn_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_owner.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_owner.block_call()
    
    
    
    def renounce_ownership(self) -> None:
        """
        Implementation of renounce_ownership in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_renounce_ownership.callback_onfail = self._callback_onfail
        self._fn_renounce_ownership.callback_onsuccess = self._callback_onsuccess
        self._fn_renounce_ownership.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounce_ownership.gas_limit = self.call_contract_fee_amount
        self._fn_renounce_ownership.gas_price_wei = self.call_contract_fee_price
        self._fn_renounce_ownership.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_renounce_ownership.block_send()
    
    
    
    
    
    
    
    def router_addresses(self, index_0: str) -> str:
        """
        Implementation of router_addresses in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_router_addresses.callback_onfail = self._callback_onfail
        self._fn_router_addresses.callback_onsuccess = self._callback_onsuccess
        self._fn_router_addresses.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_addresses.gas_limit = self.call_contract_fee_amount
        self._fn_router_addresses.gas_price_wei = self.call_contract_fee_price
        self._fn_router_addresses.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_addresses.block_call(index_0)
    
    
    
    def transaction_manager(self) -> str:
        """
        Implementation of transaction_manager in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_transaction_manager.callback_onfail = self._callback_onfail
        self._fn_transaction_manager.callback_onsuccess = self._callback_onsuccess
        self._fn_transaction_manager.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_transaction_manager.gas_limit = self.call_contract_fee_amount
        self._fn_transaction_manager.gas_price_wei = self.call_contract_fee_price
        self._fn_transaction_manager.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_transaction_manager.block_call()
    
    
    
    def transfer_ownership(self, new_owner: str) -> None:
        """
        Implementation of transfer_ownership in contract RouterFactory
        Method of the function
    
        """
    
        self._fn_transfer_ownership.callback_onfail = self._callback_onfail
        self._fn_transfer_ownership.callback_onsuccess = self._callback_onsuccess
        self._fn_transfer_ownership.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_transfer_ownership.gas_limit = self.call_contract_fee_amount
        self._fn_transfer_ownership.gas_price_wei = self.call_contract_fee_price
        self._fn_transfer_ownership.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_transfer_ownership.block_send(new_owner)
    
    
    
    

    def CallContractWait(self, t_long:int)-> "RouterFactory":
        self._fn_create_router.setWait(t_long)
        self._fn_get_router_address.setWait(t_long)
        self._fn_init.setWait(t_long)
        self._fn_owner.setWait(t_long)
        self._fn_renounce_ownership.setWait(t_long)
        self._fn_router_addresses.setWait(t_long)
        self._fn_transaction_manager.setWait(t_long)
        self._fn_transfer_ownership.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"router","type":"address"},{"indexed":false,"internalType":"address","name":"routerSigner","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"address","name":"transactionManager","type":"address"}],"name":"RouterCreated","type":"event"},{"inputs":[{"internalType":"address","name":"routerSigner","type":"address"},{"internalType":"address","name":"recipient","type":"address"}],"name":"createRouter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"routerSigner","type":"address"}],"name":"getRouterAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_transactionManager","type":"address"}],"name":"init","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"routerAddresses","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"transactionManager","outputs":[{"internalType":"contract ITransactionManager","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
