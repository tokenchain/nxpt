"""Generated wrapper for ProposedOwnable Solidity contract."""

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
# constructor for ProposedOwnable below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ProposedOwnableValidator,
    )
except ImportError:

    class ProposedOwnableValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class AcceptProposedOwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the acceptProposedOwner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("acceptProposedOwner")



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

                self._on_receipt_handle("accept_proposed_owner", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: accept_proposed_owner")
            message = f"Error {er}: accept_proposed_owner"
            self._on_fail("accept_proposed_owner", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, accept_proposed_owner: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, accept_proposed_owner. Reason: Unknown")

            self._on_fail("accept_proposed_owner", message)

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

class AssetOwnershipTimestampMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the assetOwnershipTimestamp method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("assetOwnershipTimestamp")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _valeth:int=0) -> int:
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

                self._on_receipt_handle("asset_ownership_timestamp", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: asset_ownership_timestamp")
            message = f"Error {er}: asset_ownership_timestamp"
            self._on_fail("asset_ownership_timestamp", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, asset_ownership_timestamp: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, asset_ownership_timestamp. Reason: Unknown")

            self._on_fail("asset_ownership_timestamp", message)

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

class DelayMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the delay method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("delay")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _valeth:int=0) -> int:
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

                self._on_receipt_handle("delay", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: delay")
            message = f"Error {er}: delay"
            self._on_fail("delay", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, delay: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, delay. Reason: Unknown")

            self._on_fail("delay", message)

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

class IsAssetOwnershipRenouncedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isAssetOwnershipRenounced method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("isAssetOwnershipRenounced")



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

                self._on_receipt_handle("is_asset_ownership_renounced", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: is_asset_ownership_renounced")
            message = f"Error {er}: is_asset_ownership_renounced"
            self._on_fail("is_asset_ownership_renounced", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_asset_ownership_renounced: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_asset_ownership_renounced. Reason: Unknown")

            self._on_fail("is_asset_ownership_renounced", message)

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

class IsRouterOwnershipRenouncedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isRouterOwnershipRenounced method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("isRouterOwnershipRenounced")



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

                self._on_receipt_handle("is_router_ownership_renounced", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: is_router_ownership_renounced")
            message = f"Error {er}: is_router_ownership_renounced"
            self._on_fail("is_router_ownership_renounced", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_router_ownership_renounced: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_router_ownership_renounced. Reason: Unknown")

            self._on_fail("is_router_ownership_renounced", message)

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

class ProposeAssetOwnershipRenunciationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposeAssetOwnershipRenunciation method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposeAssetOwnershipRenunciation")



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

                self._on_receipt_handle("propose_asset_ownership_renunciation", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: propose_asset_ownership_renunciation")
            message = f"Error {er}: propose_asset_ownership_renunciation"
            self._on_fail("propose_asset_ownership_renunciation", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_asset_ownership_renunciation: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_asset_ownership_renunciation. Reason: Unknown")

            self._on_fail("propose_asset_ownership_renunciation", message)

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

class ProposeNewOwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposeNewOwner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposeNewOwner")

    def validate_and_normalize_inputs(self, newly_proposed: str)->any:
        """Validate the inputs to the proposeNewOwner method."""
        self.validator.assert_valid(
            method_name='proposeNewOwner',
            parameter_name='newlyProposed',
            argument_value=newly_proposed,
        )
        newly_proposed = self.validate_and_checksum_address(newly_proposed)
        return (newly_proposed)



    def block_send(self, newly_proposed: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(newly_proposed)
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

                self._on_receipt_handle("propose_new_owner", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: propose_new_owner")
            message = f"Error {er}: propose_new_owner"
            self._on_fail("propose_new_owner", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_new_owner: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_new_owner. Reason: Unknown")

            self._on_fail("propose_new_owner", message)

    def send_transaction(self, newly_proposed: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (newly_proposed) = self.validate_and_normalize_inputs(newly_proposed)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(newly_proposed).transact(tx_params.as_dict())

    def build_transaction(self, newly_proposed: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (newly_proposed) = self.validate_and_normalize_inputs(newly_proposed)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(newly_proposed).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, newly_proposed: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (newly_proposed) = self.validate_and_normalize_inputs(newly_proposed)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(newly_proposed).estimateGas(tx_params.as_dict())

class ProposeRouterOwnershipRenunciationMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposeRouterOwnershipRenunciation method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposeRouterOwnershipRenunciation")



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

                self._on_receipt_handle("propose_router_ownership_renunciation", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: propose_router_ownership_renunciation")
            message = f"Error {er}: propose_router_ownership_renunciation"
            self._on_fail("propose_router_ownership_renunciation", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_router_ownership_renunciation: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_router_ownership_renunciation. Reason: Unknown")

            self._on_fail("propose_router_ownership_renunciation", message)

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

class ProposedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposed method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposed")



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

                self._on_receipt_handle("proposed", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: proposed")
            message = f"Error {er}: proposed"
            self._on_fail("proposed", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed. Reason: Unknown")

            self._on_fail("proposed", message)

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

class ProposedTimestampMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposedTimestamp method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposedTimestamp")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _valeth:int=0) -> int:
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

                self._on_receipt_handle("proposed_timestamp", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: proposed_timestamp")
            message = f"Error {er}: proposed_timestamp"
            self._on_fail("proposed_timestamp", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed_timestamp: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed_timestamp. Reason: Unknown")

            self._on_fail("proposed_timestamp", message)

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

class RenounceAssetOwnershipMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the renounceAssetOwnership method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("renounceAssetOwnership")



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

                self._on_receipt_handle("renounce_asset_ownership", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: renounce_asset_ownership")
            message = f"Error {er}: renounce_asset_ownership"
            self._on_fail("renounce_asset_ownership", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounce_asset_ownership: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounce_asset_ownership. Reason: Unknown")

            self._on_fail("renounce_asset_ownership", message)

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

class RenounceRouterOwnershipMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the renounceRouterOwnership method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("renounceRouterOwnership")



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

                self._on_receipt_handle("renounce_router_ownership", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: renounce_router_ownership")
            message = f"Error {er}: renounce_router_ownership"
            self._on_fail("renounce_router_ownership", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounce_router_ownership: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounce_router_ownership. Reason: Unknown")

            self._on_fail("renounce_router_ownership", message)

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

class RenouncedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the renounced method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("renounced")



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

                self._on_receipt_handle("renounced", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: renounced")
            message = f"Error {er}: renounced"
            self._on_fail("renounced", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounced: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, renounced. Reason: Unknown")

            self._on_fail("renounced", message)

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

class RouterOwnershipTimestampMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerOwnershipTimestamp method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerOwnershipTimestamp")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _valeth:int=0) -> int:
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

                self._on_receipt_handle("router_ownership_timestamp", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_ownership_timestamp")
            message = f"Error {er}: router_ownership_timestamp"
            self._on_fail("router_ownership_timestamp", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_ownership_timestamp: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_ownership_timestamp. Reason: Unknown")

            self._on_fail("router_ownership_timestamp", message)

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

    def accept_proposed_owner(self) -> str:
        return self._function_signatures["acceptProposedOwner"]
    def asset_ownership_timestamp(self) -> str:
        return self._function_signatures["assetOwnershipTimestamp"]
    def delay(self) -> str:
        return self._function_signatures["delay"]
    def is_asset_ownership_renounced(self) -> str:
        return self._function_signatures["isAssetOwnershipRenounced"]
    def is_router_ownership_renounced(self) -> str:
        return self._function_signatures["isRouterOwnershipRenounced"]
    def owner(self) -> str:
        return self._function_signatures["owner"]
    def propose_asset_ownership_renunciation(self) -> str:
        return self._function_signatures["proposeAssetOwnershipRenunciation"]
    def propose_new_owner(self) -> str:
        return self._function_signatures["proposeNewOwner"]
    def propose_router_ownership_renunciation(self) -> str:
        return self._function_signatures["proposeRouterOwnershipRenunciation"]
    def proposed(self) -> str:
        return self._function_signatures["proposed"]
    def proposed_timestamp(self) -> str:
        return self._function_signatures["proposedTimestamp"]
    def renounce_asset_ownership(self) -> str:
        return self._function_signatures["renounceAssetOwnership"]
    def renounce_ownership(self) -> str:
        return self._function_signatures["renounceOwnership"]
    def renounce_router_ownership(self) -> str:
        return self._function_signatures["renounceRouterOwnership"]
    def renounced(self) -> str:
        return self._function_signatures["renounced"]
    def router_ownership_timestamp(self) -> str:
        return self._function_signatures["routerOwnershipTimestamp"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ProposedOwnable(ContractBase):
    """Wrapper class for ProposedOwnable Solidity contract."""
    _fn_accept_proposed_owner: AcceptProposedOwnerMethod
    """Constructor-initialized instance of
    :class:`AcceptProposedOwnerMethod`.
    """

    _fn_asset_ownership_timestamp: AssetOwnershipTimestampMethod
    """Constructor-initialized instance of
    :class:`AssetOwnershipTimestampMethod`.
    """

    _fn_delay: DelayMethod
    """Constructor-initialized instance of
    :class:`DelayMethod`.
    """

    _fn_is_asset_ownership_renounced: IsAssetOwnershipRenouncedMethod
    """Constructor-initialized instance of
    :class:`IsAssetOwnershipRenouncedMethod`.
    """

    _fn_is_router_ownership_renounced: IsRouterOwnershipRenouncedMethod
    """Constructor-initialized instance of
    :class:`IsRouterOwnershipRenouncedMethod`.
    """

    _fn_owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    _fn_propose_asset_ownership_renunciation: ProposeAssetOwnershipRenunciationMethod
    """Constructor-initialized instance of
    :class:`ProposeAssetOwnershipRenunciationMethod`.
    """

    _fn_propose_new_owner: ProposeNewOwnerMethod
    """Constructor-initialized instance of
    :class:`ProposeNewOwnerMethod`.
    """

    _fn_propose_router_ownership_renunciation: ProposeRouterOwnershipRenunciationMethod
    """Constructor-initialized instance of
    :class:`ProposeRouterOwnershipRenunciationMethod`.
    """

    _fn_proposed: ProposedMethod
    """Constructor-initialized instance of
    :class:`ProposedMethod`.
    """

    _fn_proposed_timestamp: ProposedTimestampMethod
    """Constructor-initialized instance of
    :class:`ProposedTimestampMethod`.
    """

    _fn_renounce_asset_ownership: RenounceAssetOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceAssetOwnershipMethod`.
    """

    _fn_renounce_ownership: RenounceOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceOwnershipMethod`.
    """

    _fn_renounce_router_ownership: RenounceRouterOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceRouterOwnershipMethod`.
    """

    _fn_renounced: RenouncedMethod
    """Constructor-initialized instance of
    :class:`RenouncedMethod`.
    """

    _fn_router_ownership_timestamp: RouterOwnershipTimestampMethod
    """Constructor-initialized instance of
    :class:`RouterOwnershipTimestampMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: ProposedOwnableValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, ProposedOwnable.abi())
        web3 = core_lib.w3

        if not validator:
            validator = ProposedOwnableValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=ProposedOwnable.abi()).functions
        self._signatures = SignatureGenerator(ProposedOwnable.abi())
        validator.bindSignatures(self._signatures)

        self._fn_accept_proposed_owner = AcceptProposedOwnerMethod(core_lib, contract_address, functions.acceptProposedOwner, validator)
        self._fn_asset_ownership_timestamp = AssetOwnershipTimestampMethod(core_lib, contract_address, functions.assetOwnershipTimestamp, validator)
        self._fn_delay = DelayMethod(core_lib, contract_address, functions.delay, validator)
        self._fn_is_asset_ownership_renounced = IsAssetOwnershipRenouncedMethod(core_lib, contract_address, functions.isAssetOwnershipRenounced, validator)
        self._fn_is_router_ownership_renounced = IsRouterOwnershipRenouncedMethod(core_lib, contract_address, functions.isRouterOwnershipRenounced, validator)
        self._fn_owner = OwnerMethod(core_lib, contract_address, functions.owner, validator)
        self._fn_propose_asset_ownership_renunciation = ProposeAssetOwnershipRenunciationMethod(core_lib, contract_address, functions.proposeAssetOwnershipRenunciation, validator)
        self._fn_propose_new_owner = ProposeNewOwnerMethod(core_lib, contract_address, functions.proposeNewOwner, validator)
        self._fn_propose_router_ownership_renunciation = ProposeRouterOwnershipRenunciationMethod(core_lib, contract_address, functions.proposeRouterOwnershipRenunciation, validator)
        self._fn_proposed = ProposedMethod(core_lib, contract_address, functions.proposed, validator)
        self._fn_proposed_timestamp = ProposedTimestampMethod(core_lib, contract_address, functions.proposedTimestamp, validator)
        self._fn_renounce_asset_ownership = RenounceAssetOwnershipMethod(core_lib, contract_address, functions.renounceAssetOwnership, validator)
        self._fn_renounce_ownership = RenounceOwnershipMethod(core_lib, contract_address, functions.renounceOwnership, validator)
        self._fn_renounce_router_ownership = RenounceRouterOwnershipMethod(core_lib, contract_address, functions.renounceRouterOwnership, validator)
        self._fn_renounced = RenouncedMethod(core_lib, contract_address, functions.renounced, validator)
        self._fn_router_ownership_timestamp = RouterOwnershipTimestampMethod(core_lib, contract_address, functions.routerOwnershipTimestamp, validator)

    
    
    def event_asset_ownership_renounced(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_ownership_renounced in contract ProposedOwnable
        Get log entry for AssetOwnershipRenounced event.
                :param tx_hash: hash of transaction emitting AssetOwnershipRenounced
                event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ProposedOwnable.abi()).events.AssetOwnershipRenounced().processReceipt(tx_receipt)
    
    
    def event_asset_ownership_renunciation_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_ownership_renunciation_proposed in contract ProposedOwnable
        Get log entry for AssetOwnershipRenunciationProposed event.
                :param tx_hash: hash of transaction emitting
                AssetOwnershipRenunciationProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ProposedOwnable.abi()).events.AssetOwnershipRenunciationProposed().processReceipt(tx_receipt)
    
    
    def event_ownership_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_proposed in contract ProposedOwnable
        Get log entry for OwnershipProposed event.
                :param tx_hash: hash of transaction emitting OwnershipProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ProposedOwnable.abi()).events.OwnershipProposed().processReceipt(tx_receipt)
    
    
    def event_ownership_transferred(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_transferred in contract ProposedOwnable
        Get log entry for OwnershipTransferred event.
                :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ProposedOwnable.abi()).events.OwnershipTransferred().processReceipt(tx_receipt)
    
    
    def event_router_ownership_renounced(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_ownership_renounced in contract ProposedOwnable
        Get log entry for RouterOwnershipRenounced event.
                :param tx_hash: hash of transaction emitting RouterOwnershipRenounced
                event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ProposedOwnable.abi()).events.RouterOwnershipRenounced().processReceipt(tx_receipt)
    
    
    def event_router_ownership_renunciation_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_ownership_renunciation_proposed in contract ProposedOwnable
        Get log entry for RouterOwnershipRenunciationProposed event.
                :param tx_hash: hash of transaction emitting
                RouterOwnershipRenunciationProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ProposedOwnable.abi()).events.RouterOwnershipRenunciationProposed().processReceipt(tx_receipt)

    
    
    
    def accept_proposed_owner(self) -> None:
        """
        Implementation of accept_proposed_owner in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_accept_proposed_owner.callback_onfail = self._callback_onfail
        self._fn_accept_proposed_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_accept_proposed_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_accept_proposed_owner.gas_limit = self.call_contract_fee_amount
        self._fn_accept_proposed_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_accept_proposed_owner.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_accept_proposed_owner.block_send()
    
    
    
    
    
    
    
    def asset_ownership_timestamp(self) -> int:
        """
        Implementation of asset_ownership_timestamp in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_asset_ownership_timestamp.callback_onfail = self._callback_onfail
        self._fn_asset_ownership_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_asset_ownership_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_asset_ownership_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_asset_ownership_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_asset_ownership_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_asset_ownership_timestamp.block_call()
    
    
    
    def delay(self) -> int:
        """
        Implementation of delay in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_delay.callback_onfail = self._callback_onfail
        self._fn_delay.callback_onsuccess = self._callback_onsuccess
        self._fn_delay.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_delay.gas_limit = self.call_contract_fee_amount
        self._fn_delay.gas_price_wei = self.call_contract_fee_price
        self._fn_delay.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_delay.block_call()
    
    
    
    def is_asset_ownership_renounced(self) -> bool:
        """
        Implementation of is_asset_ownership_renounced in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_is_asset_ownership_renounced.callback_onfail = self._callback_onfail
        self._fn_is_asset_ownership_renounced.callback_onsuccess = self._callback_onsuccess
        self._fn_is_asset_ownership_renounced.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_is_asset_ownership_renounced.gas_limit = self.call_contract_fee_amount
        self._fn_is_asset_ownership_renounced.gas_price_wei = self.call_contract_fee_price
        self._fn_is_asset_ownership_renounced.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_is_asset_ownership_renounced.block_call()
    
    
    
    def is_router_ownership_renounced(self) -> bool:
        """
        Implementation of is_router_ownership_renounced in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_is_router_ownership_renounced.callback_onfail = self._callback_onfail
        self._fn_is_router_ownership_renounced.callback_onsuccess = self._callback_onsuccess
        self._fn_is_router_ownership_renounced.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_is_router_ownership_renounced.gas_limit = self.call_contract_fee_amount
        self._fn_is_router_ownership_renounced.gas_price_wei = self.call_contract_fee_price
        self._fn_is_router_ownership_renounced.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_is_router_ownership_renounced.block_call()
    
    
    
    def owner(self) -> str:
        """
        Implementation of owner in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_owner.callback_onfail = self._callback_onfail
        self._fn_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_owner.gas_limit = self.call_contract_fee_amount
        self._fn_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_owner.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_owner.block_call()
    
    
    
    def propose_asset_ownership_renunciation(self) -> None:
        """
        Implementation of propose_asset_ownership_renunciation in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_propose_asset_ownership_renunciation.callback_onfail = self._callback_onfail
        self._fn_propose_asset_ownership_renunciation.callback_onsuccess = self._callback_onsuccess
        self._fn_propose_asset_ownership_renunciation.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_propose_asset_ownership_renunciation.gas_limit = self.call_contract_fee_amount
        self._fn_propose_asset_ownership_renunciation.gas_price_wei = self.call_contract_fee_price
        self._fn_propose_asset_ownership_renunciation.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_propose_asset_ownership_renunciation.block_send()
    
    
    
    
    
    
    
    def propose_new_owner(self, newly_proposed: str) -> None:
        """
        Implementation of propose_new_owner in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_propose_new_owner.callback_onfail = self._callback_onfail
        self._fn_propose_new_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_propose_new_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_propose_new_owner.gas_limit = self.call_contract_fee_amount
        self._fn_propose_new_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_propose_new_owner.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_propose_new_owner.block_send(newly_proposed)
    
    
    
    
    
    
    
    def propose_router_ownership_renunciation(self) -> None:
        """
        Implementation of propose_router_ownership_renunciation in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_propose_router_ownership_renunciation.callback_onfail = self._callback_onfail
        self._fn_propose_router_ownership_renunciation.callback_onsuccess = self._callback_onsuccess
        self._fn_propose_router_ownership_renunciation.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_propose_router_ownership_renunciation.gas_limit = self.call_contract_fee_amount
        self._fn_propose_router_ownership_renunciation.gas_price_wei = self.call_contract_fee_price
        self._fn_propose_router_ownership_renunciation.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_propose_router_ownership_renunciation.block_send()
    
    
    
    
    
    
    
    def proposed(self) -> str:
        """
        Implementation of proposed in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_proposed.callback_onfail = self._callback_onfail
        self._fn_proposed.callback_onsuccess = self._callback_onsuccess
        self._fn_proposed.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_proposed.gas_limit = self.call_contract_fee_amount
        self._fn_proposed.gas_price_wei = self.call_contract_fee_price
        self._fn_proposed.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_proposed.block_call()
    
    
    
    def proposed_timestamp(self) -> int:
        """
        Implementation of proposed_timestamp in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_proposed_timestamp.callback_onfail = self._callback_onfail
        self._fn_proposed_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_proposed_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_proposed_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_proposed_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_proposed_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_proposed_timestamp.block_call()
    
    
    
    def renounce_asset_ownership(self) -> None:
        """
        Implementation of renounce_asset_ownership in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_renounce_asset_ownership.callback_onfail = self._callback_onfail
        self._fn_renounce_asset_ownership.callback_onsuccess = self._callback_onsuccess
        self._fn_renounce_asset_ownership.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounce_asset_ownership.gas_limit = self.call_contract_fee_amount
        self._fn_renounce_asset_ownership.gas_price_wei = self.call_contract_fee_price
        self._fn_renounce_asset_ownership.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_renounce_asset_ownership.block_send()
    
    
    
    
    
    
    
    def renounce_ownership(self) -> None:
        """
        Implementation of renounce_ownership in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_renounce_ownership.callback_onfail = self._callback_onfail
        self._fn_renounce_ownership.callback_onsuccess = self._callback_onsuccess
        self._fn_renounce_ownership.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounce_ownership.gas_limit = self.call_contract_fee_amount
        self._fn_renounce_ownership.gas_price_wei = self.call_contract_fee_price
        self._fn_renounce_ownership.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_renounce_ownership.block_send()
    
    
    
    
    
    
    
    def renounce_router_ownership(self) -> None:
        """
        Implementation of renounce_router_ownership in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_renounce_router_ownership.callback_onfail = self._callback_onfail
        self._fn_renounce_router_ownership.callback_onsuccess = self._callback_onsuccess
        self._fn_renounce_router_ownership.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounce_router_ownership.gas_limit = self.call_contract_fee_amount
        self._fn_renounce_router_ownership.gas_price_wei = self.call_contract_fee_price
        self._fn_renounce_router_ownership.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_renounce_router_ownership.block_send()
    
    
    
    
    
    
    
    def renounced(self) -> bool:
        """
        Implementation of renounced in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_renounced.callback_onfail = self._callback_onfail
        self._fn_renounced.callback_onsuccess = self._callback_onsuccess
        self._fn_renounced.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounced.gas_limit = self.call_contract_fee_amount
        self._fn_renounced.gas_price_wei = self.call_contract_fee_price
        self._fn_renounced.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_renounced.block_call()
    
    
    
    def router_ownership_timestamp(self) -> int:
        """
        Implementation of router_ownership_timestamp in contract ProposedOwnable
        Method of the function
    
        """
    
        self._fn_router_ownership_timestamp.callback_onfail = self._callback_onfail
        self._fn_router_ownership_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_router_ownership_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_ownership_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_router_ownership_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_router_ownership_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_ownership_timestamp.block_call()

    def CallContractWait(self, t_long:int)-> "ProposedOwnable":
        self._fn_accept_proposed_owner.setWait(t_long)
        self._fn_asset_ownership_timestamp.setWait(t_long)
        self._fn_delay.setWait(t_long)
        self._fn_is_asset_ownership_renounced.setWait(t_long)
        self._fn_is_router_ownership_renounced.setWait(t_long)
        self._fn_owner.setWait(t_long)
        self._fn_propose_asset_ownership_renunciation.setWait(t_long)
        self._fn_propose_new_owner.setWait(t_long)
        self._fn_propose_router_ownership_renunciation.setWait(t_long)
        self._fn_proposed.setWait(t_long)
        self._fn_proposed_timestamp.setWait(t_long)
        self._fn_renounce_asset_ownership.setWait(t_long)
        self._fn_renounce_ownership.setWait(t_long)
        self._fn_renounce_router_ownership.setWait(t_long)
        self._fn_renounced.setWait(t_long)
        self._fn_router_ownership_timestamp.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"renounced","type":"bool"}],"name":"AssetOwnershipRenounced","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"AssetOwnershipRenunciationProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"proposedOwner","type":"address"}],"name":"OwnershipProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"renounced","type":"bool"}],"name":"RouterOwnershipRenounced","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"RouterOwnershipRenunciationProposed","type":"event"},{"inputs":[],"name":"acceptProposedOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"assetOwnershipTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"delay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isAssetOwnershipRenounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isRouterOwnershipRenounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposeAssetOwnershipRenunciation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newlyProposed","type":"address"}],"name":"proposeNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposeRouterOwnershipRenunciation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposed","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposedTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceAssetOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceRouterOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"routerOwnershipTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
