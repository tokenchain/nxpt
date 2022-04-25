"""Generated wrapper for TransactionManager Solidity contract."""

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
# constructor for TransactionManager below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        TransactionManagerValidator,
    )
except ImportError:

    class TransactionManagerValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class ITransactionManagerTransactionData(TypedDict):
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

    receivingChainTxManagerAddress: str

    user: str

    router: str

    initiator: str

    sendingAssetId: str

    receivingAssetId: str

    sendingChainFallback: str

    receivingAddress: str

    callTo: str

    callDataHash: Union[bytes, str]

    transactionId: Union[bytes, str]

    sendingChainId: int

    receivingChainId: int

    amount: int

    expiry: int

    preparedBlockNumber: int


class ITransactionManagerCancelArgs(TypedDict):
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

    txData: ITransactionManagerTransactionData

    signature: Union[bytes, str]

    encodedMeta: Union[bytes, str]


class ITransactionManagerFulfillArgs(TypedDict):
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

    txData: ITransactionManagerTransactionData

    relayerFee: int

    signature: Union[bytes, str]

    callData: Union[bytes, str]

    encodedMeta: Union[bytes, str]


class ITransactionManagerInvariantTransactionData(TypedDict):
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

    receivingChainTxManagerAddress: str

    user: str

    router: str

    initiator: str

    sendingAssetId: str

    receivingAssetId: str

    sendingChainFallback: str

    receivingAddress: str

    callTo: str

    sendingChainId: int

    receivingChainId: int

    callDataHash: Union[bytes, str]

    transactionId: Union[bytes, str]


class ITransactionManagerPrepareArgs(TypedDict):
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

    invariantData: ITransactionManagerInvariantTransactionData

    amount: int

    expiry: int

    encryptedCallData: Union[bytes, str]

    encodedBid: Union[bytes, str]

    bidSignature: Union[bytes, str]

    encodedMeta: Union[bytes, str]


class MaxTimeoutMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the MAX_TIMEOUT method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("MAX_TIMEOUT")



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

                self._on_receipt_handle("max_timeout", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: max_timeout")
            message = f"Error {er}: max_timeout"
            self._on_fail("max_timeout", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, max_timeout: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, max_timeout. Reason: Unknown")

            self._on_fail("max_timeout", message)

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

class MinTimeoutMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the MIN_TIMEOUT method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("MIN_TIMEOUT")



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

                self._on_receipt_handle("min_timeout", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: min_timeout")
            message = f"Error {er}: min_timeout"
            self._on_fail("min_timeout", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, min_timeout: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, min_timeout. Reason: Unknown")

            self._on_fail("min_timeout", message)

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

class AddAssetIdMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addAssetId method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addAssetId")

    def validate_and_normalize_inputs(self, asset_id: str)->any:
        """Validate the inputs to the addAssetId method."""
        self.validator.assert_valid(
            method_name='addAssetId',
            parameter_name='assetId',
            argument_value=asset_id,
        )
        asset_id = self.validate_and_checksum_address(asset_id)
        return (asset_id)



    def block_send(self, asset_id: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(asset_id)
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

                self._on_receipt_handle("add_asset_id", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_asset_id")
            message = f"Error {er}: add_asset_id"
            self._on_fail("add_asset_id", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_asset_id: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_asset_id. Reason: Unknown")

            self._on_fail("add_asset_id", message)

    def send_transaction(self, asset_id: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (asset_id) = self.validate_and_normalize_inputs(asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id).transact(tx_params.as_dict())

    def build_transaction(self, asset_id: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_id) = self.validate_and_normalize_inputs(asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, asset_id: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (asset_id) = self.validate_and_normalize_inputs(asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id).estimateGas(tx_params.as_dict())

class AddLiquidityMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addLiquidity method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addLiquidity")

    def validate_and_normalize_inputs(self, amount: int, asset_id: str)->any:
        """Validate the inputs to the addLiquidity method."""
        self.validator.assert_valid(
            method_name='addLiquidity',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='addLiquidity',
            parameter_name='assetId',
            argument_value=asset_id,
        )
        asset_id = self.validate_and_checksum_address(asset_id)
        return (amount, asset_id)



    def block_send(self, amount: int, asset_id: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, asset_id)
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

                self._on_receipt_handle("add_liquidity", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_liquidity")
            message = f"Error {er}: add_liquidity"
            self._on_fail("add_liquidity", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_liquidity: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_liquidity. Reason: Unknown")

            self._on_fail("add_liquidity", message)

    def send_transaction(self, amount: int, asset_id: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, asset_id) = self.validate_and_normalize_inputs(amount, asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, asset_id: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, asset_id) = self.validate_and_normalize_inputs(amount, asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, asset_id: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, asset_id) = self.validate_and_normalize_inputs(amount, asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id).estimateGas(tx_params.as_dict())

class AddLiquidityForMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addLiquidityFor method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addLiquidityFor")

    def validate_and_normalize_inputs(self, amount: int, asset_id: str, router: str)->any:
        """Validate the inputs to the addLiquidityFor method."""
        self.validator.assert_valid(
            method_name='addLiquidityFor',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='addLiquidityFor',
            parameter_name='assetId',
            argument_value=asset_id,
        )
        asset_id = self.validate_and_checksum_address(asset_id)
        self.validator.assert_valid(
            method_name='addLiquidityFor',
            parameter_name='router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (amount, asset_id, router)



    def block_send(self, amount: int, asset_id: str, router: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, asset_id, router)
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

                self._on_receipt_handle("add_liquidity_for", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_liquidity_for")
            message = f"Error {er}: add_liquidity_for"
            self._on_fail("add_liquidity_for", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_liquidity_for: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_liquidity_for. Reason: Unknown")

            self._on_fail("add_liquidity_for", message)

    def send_transaction(self, amount: int, asset_id: str, router: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, asset_id, router) = self.validate_and_normalize_inputs(amount, asset_id, router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, router).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, asset_id: str, router: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, asset_id, router) = self.validate_and_normalize_inputs(amount, asset_id, router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, router).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, asset_id: str, router: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, asset_id, router) = self.validate_and_normalize_inputs(amount, asset_id, router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, router).estimateGas(tx_params.as_dict())

class AddRouterMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addRouter method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addRouter")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the addRouter method."""
        self.validator.assert_valid(
            method_name='addRouter',
            parameter_name='router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (router)



    def block_send(self, router: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(router)
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

                self._on_receipt_handle("add_router", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_router")
            message = f"Error {er}: add_router"
            self._on_fail("add_router", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_router: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_router. Reason: Unknown")

            self._on_fail("add_router", message)

    def send_transaction(self, router: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (router) = self.validate_and_normalize_inputs(router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router).transact(tx_params.as_dict())

    def build_transaction(self, router: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (router) = self.validate_and_normalize_inputs(router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, router: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (router) = self.validate_and_normalize_inputs(router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router).estimateGas(tx_params.as_dict())

class ApprovedAssetsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approvedAssets method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("approvedAssets")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the approvedAssets method."""
        self.validator.assert_valid(
            method_name='approvedAssets',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> bool:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, index_0: str,_valeth:int=0) -> bool:
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

                self._on_receipt_handle("approved_assets", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: approved_assets")
            message = f"Error {er}: approved_assets"
            self._on_fail("approved_assets", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approved_assets: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approved_assets. Reason: Unknown")

            self._on_fail("approved_assets", message)

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

class ApprovedRoutersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approvedRouters method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("approvedRouters")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the approvedRouters method."""
        self.validator.assert_valid(
            method_name='approvedRouters',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> bool:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, index_0: str,_valeth:int=0) -> bool:
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

                self._on_receipt_handle("approved_routers", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: approved_routers")
            message = f"Error {er}: approved_routers"
            self._on_fail("approved_routers", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approved_routers: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approved_routers. Reason: Unknown")

            self._on_fail("approved_routers", message)

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

class CancelMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the cancel method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("cancel")

    def validate_and_normalize_inputs(self, args: ITransactionManagerCancelArgs)->any:
        """Validate the inputs to the cancel method."""
        self.validator.assert_valid(
            method_name='cancel',
            parameter_name='args',
            argument_value=args,
        )
        return (args)



    def block_send(self, args: ITransactionManagerCancelArgs,_valeth:int=0) -> ITransactionManagerTransactionData:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(args)
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

                self._on_receipt_handle("cancel", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: cancel")
            message = f"Error {er}: cancel"
            self._on_fail("cancel", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, cancel: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, cancel. Reason: Unknown")

            self._on_fail("cancel", message)

    def send_transaction(self, args: ITransactionManagerCancelArgs, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).transact(tx_params.as_dict())

    def build_transaction(self, args: ITransactionManagerCancelArgs, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: ITransactionManagerCancelArgs, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).estimateGas(tx_params.as_dict())

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

class FulfillMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the fulfill method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("fulfill")

    def validate_and_normalize_inputs(self, args: ITransactionManagerFulfillArgs)->any:
        """Validate the inputs to the fulfill method."""
        self.validator.assert_valid(
            method_name='fulfill',
            parameter_name='args',
            argument_value=args,
        )
        return (args)



    def block_send(self, args: ITransactionManagerFulfillArgs,_valeth:int=0) -> ITransactionManagerTransactionData:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(args)
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

                self._on_receipt_handle("fulfill", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: fulfill")
            message = f"Error {er}: fulfill"
            self._on_fail("fulfill", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, fulfill: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, fulfill. Reason: Unknown")

            self._on_fail("fulfill", message)

    def send_transaction(self, args: ITransactionManagerFulfillArgs, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).transact(tx_params.as_dict())

    def build_transaction(self, args: ITransactionManagerFulfillArgs, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: ITransactionManagerFulfillArgs, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).estimateGas(tx_params.as_dict())

class GetChainIdMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getChainId method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getChainId")



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

                self._on_receipt_handle("get_chain_id", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_chain_id")
            message = f"Error {er}: get_chain_id"
            self._on_fail("get_chain_id", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_chain_id: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_chain_id. Reason: Unknown")

            self._on_fail("get_chain_id", message)

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

class GetStoredChainIdMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getStoredChainId method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getStoredChainId")



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

                self._on_receipt_handle("get_stored_chain_id", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_stored_chain_id")
            message = f"Error {er}: get_stored_chain_id"
            self._on_fail("get_stored_chain_id", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_stored_chain_id: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_stored_chain_id. Reason: Unknown")

            self._on_fail("get_stored_chain_id", message)

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

class InterpreterMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the interpreter method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("interpreter")



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

                self._on_receipt_handle("interpreter", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: interpreter")
            message = f"Error {er}: interpreter"
            self._on_fail("interpreter", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, interpreter: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, interpreter. Reason: Unknown")

            self._on_fail("interpreter", message)

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

class PrepareMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the prepare method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("prepare")

    def validate_and_normalize_inputs(self, args: ITransactionManagerPrepareArgs)->any:
        """Validate the inputs to the prepare method."""
        self.validator.assert_valid(
            method_name='prepare',
            parameter_name='args',
            argument_value=args,
        )
        return (args)



    def block_send(self, args: ITransactionManagerPrepareArgs,_valeth:int=0) -> ITransactionManagerTransactionData:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(args)
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

                self._on_receipt_handle("prepare", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: prepare")
            message = f"Error {er}: prepare"
            self._on_fail("prepare", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, prepare: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, prepare. Reason: Unknown")

            self._on_fail("prepare", message)

    def send_transaction(self, args: ITransactionManagerPrepareArgs, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).transact(tx_params.as_dict())

    def build_transaction(self, args: ITransactionManagerPrepareArgs, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: ITransactionManagerPrepareArgs, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).estimateGas(tx_params.as_dict())

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

class RemoveAssetIdMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeAssetId method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeAssetId")

    def validate_and_normalize_inputs(self, asset_id: str)->any:
        """Validate the inputs to the removeAssetId method."""
        self.validator.assert_valid(
            method_name='removeAssetId',
            parameter_name='assetId',
            argument_value=asset_id,
        )
        asset_id = self.validate_and_checksum_address(asset_id)
        return (asset_id)



    def block_send(self, asset_id: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(asset_id)
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

                self._on_receipt_handle("remove_asset_id", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remove_asset_id")
            message = f"Error {er}: remove_asset_id"
            self._on_fail("remove_asset_id", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_asset_id: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_asset_id. Reason: Unknown")

            self._on_fail("remove_asset_id", message)

    def send_transaction(self, asset_id: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (asset_id) = self.validate_and_normalize_inputs(asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id).transact(tx_params.as_dict())

    def build_transaction(self, asset_id: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_id) = self.validate_and_normalize_inputs(asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, asset_id: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (asset_id) = self.validate_and_normalize_inputs(asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id).estimateGas(tx_params.as_dict())

class RemoveLiquidityMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeLiquidity method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeLiquidity")

    def validate_and_normalize_inputs(self, amount: int, asset_id: str, recipient: str)->any:
        """Validate the inputs to the removeLiquidity method."""
        self.validator.assert_valid(
            method_name='removeLiquidity',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='removeLiquidity',
            parameter_name='assetId',
            argument_value=asset_id,
        )
        asset_id = self.validate_and_checksum_address(asset_id)
        self.validator.assert_valid(
            method_name='removeLiquidity',
            parameter_name='recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (amount, asset_id, recipient)



    def block_send(self, amount: int, asset_id: str, recipient: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, asset_id, recipient)
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

                self._on_receipt_handle("remove_liquidity", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remove_liquidity")
            message = f"Error {er}: remove_liquidity"
            self._on_fail("remove_liquidity", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_liquidity: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_liquidity. Reason: Unknown")

            self._on_fail("remove_liquidity", message)

    def send_transaction(self, amount: int, asset_id: str, recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, asset_id, recipient) = self.validate_and_normalize_inputs(amount, asset_id, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, recipient).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, asset_id: str, recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, asset_id, recipient) = self.validate_and_normalize_inputs(amount, asset_id, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, asset_id: str, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, asset_id, recipient) = self.validate_and_normalize_inputs(amount, asset_id, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, recipient).estimateGas(tx_params.as_dict())

class RemoveRouterMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeRouter method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeRouter")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the removeRouter method."""
        self.validator.assert_valid(
            method_name='removeRouter',
            parameter_name='router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (router)



    def block_send(self, router: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(router)
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

                self._on_receipt_handle("remove_router", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remove_router")
            message = f"Error {er}: remove_router"
            self._on_fail("remove_router", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_router: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_router. Reason: Unknown")

            self._on_fail("remove_router", message)

    def send_transaction(self, router: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (router) = self.validate_and_normalize_inputs(router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router).transact(tx_params.as_dict())

    def build_transaction(self, router: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (router) = self.validate_and_normalize_inputs(router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, router: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (router) = self.validate_and_normalize_inputs(router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router).estimateGas(tx_params.as_dict())

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

class RouterBalancesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerBalances method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerBalances")

    def validate_and_normalize_inputs(self, index_0: str, index_1: str)->any:
        """Validate the inputs to the routerBalances method."""
        self.validator.assert_valid(
            method_name='routerBalances',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        self.validator.assert_valid(
            method_name='routerBalances',
            parameter_name='index_1',
            argument_value=index_1,
        )
        index_1 = self.validate_and_checksum_address(index_1)
        return (index_0, index_1)



    def block_call(self,index_0: str, index_1: str, debug:bool=False) -> int:
        _fn = self._underlying_method(index_0, index_1)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, index_0: str, index_1: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0, index_1)
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

                self._on_receipt_handle("router_balances", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_balances")
            message = f"Error {er}: router_balances"
            self._on_fail("router_balances", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_balances: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_balances. Reason: Unknown")

            self._on_fail("router_balances", message)

    def send_transaction(self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, index_1: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0, index_1) = self.validate_and_normalize_inputs(index_0, index_1)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0, index_1).estimateGas(tx_params.as_dict())

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

class VariantTransactionDataMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the variantTransactionData method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("variantTransactionData")

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str])->any:
        """Validate the inputs to the variantTransactionData method."""
        self.validator.assert_valid(
            method_name='variantTransactionData',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)



    def block_call(self,index_0: Union[bytes, str], debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, index_0: Union[bytes, str],_valeth:int=0) -> Union[bytes, str]:
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

                self._on_receipt_handle("variant_transaction_data", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: variant_transaction_data")
            message = f"Error {er}: variant_transaction_data"
            self._on_fail("variant_transaction_data", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, variant_transaction_data: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, variant_transaction_data. Reason: Unknown")

            self._on_fail("variant_transaction_data", message)

    def send_transaction(self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """
    def __init__(self, abi: any):
        super().__init__(abi)

    def max_timeout(self) -> str:
        return self._function_signatures["MAX_TIMEOUT"]
    def min_timeout(self) -> str:
        return self._function_signatures["MIN_TIMEOUT"]
    def accept_proposed_owner(self) -> str:
        return self._function_signatures["acceptProposedOwner"]
    def add_asset_id(self) -> str:
        return self._function_signatures["addAssetId"]
    def add_liquidity(self) -> str:
        return self._function_signatures["addLiquidity"]
    def add_liquidity_for(self) -> str:
        return self._function_signatures["addLiquidityFor"]
    def add_router(self) -> str:
        return self._function_signatures["addRouter"]
    def approved_assets(self) -> str:
        return self._function_signatures["approvedAssets"]
    def approved_routers(self) -> str:
        return self._function_signatures["approvedRouters"]
    def asset_ownership_timestamp(self) -> str:
        return self._function_signatures["assetOwnershipTimestamp"]
    def cancel(self) -> str:
        return self._function_signatures["cancel"]
    def delay(self) -> str:
        return self._function_signatures["delay"]
    def fulfill(self) -> str:
        return self._function_signatures["fulfill"]
    def get_chain_id(self) -> str:
        return self._function_signatures["getChainId"]
    def get_stored_chain_id(self) -> str:
        return self._function_signatures["getStoredChainId"]
    def interpreter(self) -> str:
        return self._function_signatures["interpreter"]
    def is_asset_ownership_renounced(self) -> str:
        return self._function_signatures["isAssetOwnershipRenounced"]
    def is_router_ownership_renounced(self) -> str:
        return self._function_signatures["isRouterOwnershipRenounced"]
    def owner(self) -> str:
        return self._function_signatures["owner"]
    def prepare(self) -> str:
        return self._function_signatures["prepare"]
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
    def remove_asset_id(self) -> str:
        return self._function_signatures["removeAssetId"]
    def remove_liquidity(self) -> str:
        return self._function_signatures["removeLiquidity"]
    def remove_router(self) -> str:
        return self._function_signatures["removeRouter"]
    def renounce_asset_ownership(self) -> str:
        return self._function_signatures["renounceAssetOwnership"]
    def renounce_ownership(self) -> str:
        return self._function_signatures["renounceOwnership"]
    def renounce_router_ownership(self) -> str:
        return self._function_signatures["renounceRouterOwnership"]
    def renounced(self) -> str:
        return self._function_signatures["renounced"]
    def router_balances(self) -> str:
        return self._function_signatures["routerBalances"]
    def router_ownership_timestamp(self) -> str:
        return self._function_signatures["routerOwnershipTimestamp"]
    def variant_transaction_data(self) -> str:
        return self._function_signatures["variantTransactionData"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class TransactionManager(ContractBase):
    """Wrapper class for TransactionManager Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    _fn_max_timeout: MaxTimeoutMethod
    """Constructor-initialized instance of
    :class:`MaxTimeoutMethod`.
    """

    _fn_min_timeout: MinTimeoutMethod
    """Constructor-initialized instance of
    :class:`MinTimeoutMethod`.
    """

    _fn_accept_proposed_owner: AcceptProposedOwnerMethod
    """Constructor-initialized instance of
    :class:`AcceptProposedOwnerMethod`.
    """

    _fn_add_asset_id: AddAssetIdMethod
    """Constructor-initialized instance of
    :class:`AddAssetIdMethod`.
    """

    _fn_add_liquidity: AddLiquidityMethod
    """Constructor-initialized instance of
    :class:`AddLiquidityMethod`.
    """

    _fn_add_liquidity_for: AddLiquidityForMethod
    """Constructor-initialized instance of
    :class:`AddLiquidityForMethod`.
    """

    _fn_add_router: AddRouterMethod
    """Constructor-initialized instance of
    :class:`AddRouterMethod`.
    """

    _fn_approved_assets: ApprovedAssetsMethod
    """Constructor-initialized instance of
    :class:`ApprovedAssetsMethod`.
    """

    _fn_approved_routers: ApprovedRoutersMethod
    """Constructor-initialized instance of
    :class:`ApprovedRoutersMethod`.
    """

    _fn_asset_ownership_timestamp: AssetOwnershipTimestampMethod
    """Constructor-initialized instance of
    :class:`AssetOwnershipTimestampMethod`.
    """

    _fn_cancel: CancelMethod
    """Constructor-initialized instance of
    :class:`CancelMethod`.
    """

    _fn_delay: DelayMethod
    """Constructor-initialized instance of
    :class:`DelayMethod`.
    """

    _fn_fulfill: FulfillMethod
    """Constructor-initialized instance of
    :class:`FulfillMethod`.
    """

    _fn_get_chain_id: GetChainIdMethod
    """Constructor-initialized instance of
    :class:`GetChainIdMethod`.
    """

    _fn_get_stored_chain_id: GetStoredChainIdMethod
    """Constructor-initialized instance of
    :class:`GetStoredChainIdMethod`.
    """

    _fn_interpreter: InterpreterMethod
    """Constructor-initialized instance of
    :class:`InterpreterMethod`.
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

    _fn_prepare: PrepareMethod
    """Constructor-initialized instance of
    :class:`PrepareMethod`.
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

    _fn_remove_asset_id: RemoveAssetIdMethod
    """Constructor-initialized instance of
    :class:`RemoveAssetIdMethod`.
    """

    _fn_remove_liquidity: RemoveLiquidityMethod
    """Constructor-initialized instance of
    :class:`RemoveLiquidityMethod`.
    """

    _fn_remove_router: RemoveRouterMethod
    """Constructor-initialized instance of
    :class:`RemoveRouterMethod`.
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

    _fn_router_balances: RouterBalancesMethod
    """Constructor-initialized instance of
    :class:`RouterBalancesMethod`.
    """

    _fn_router_ownership_timestamp: RouterOwnershipTimestampMethod
    """Constructor-initialized instance of
    :class:`RouterOwnershipTimestampMethod`.
    """

    _fn_variant_transaction_data: VariantTransactionDataMethod
    """Constructor-initialized instance of
    :class:`VariantTransactionDataMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: TransactionManagerValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, TransactionManager.abi())
        web3 = core_lib.w3

        if not validator:
            validator = TransactionManagerValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=TransactionManager.abi()).functions
        self._signatures = SignatureGenerator(TransactionManager.abi())
        validator.bindSignatures(self._signatures)

        self._fn_max_timeout = MaxTimeoutMethod(core_lib, contract_address, functions.MAX_TIMEOUT, validator)
        self._fn_min_timeout = MinTimeoutMethod(core_lib, contract_address, functions.MIN_TIMEOUT, validator)
        self._fn_accept_proposed_owner = AcceptProposedOwnerMethod(core_lib, contract_address, functions.acceptProposedOwner, validator)
        self._fn_add_asset_id = AddAssetIdMethod(core_lib, contract_address, functions.addAssetId, validator)
        self._fn_add_liquidity = AddLiquidityMethod(core_lib, contract_address, functions.addLiquidity, validator)
        self._fn_add_liquidity_for = AddLiquidityForMethod(core_lib, contract_address, functions.addLiquidityFor, validator)
        self._fn_add_router = AddRouterMethod(core_lib, contract_address, functions.addRouter, validator)
        self._fn_approved_assets = ApprovedAssetsMethod(core_lib, contract_address, functions.approvedAssets, validator)
        self._fn_approved_routers = ApprovedRoutersMethod(core_lib, contract_address, functions.approvedRouters, validator)
        self._fn_asset_ownership_timestamp = AssetOwnershipTimestampMethod(core_lib, contract_address, functions.assetOwnershipTimestamp, validator)
        self._fn_cancel = CancelMethod(core_lib, contract_address, functions.cancel, validator)
        self._fn_delay = DelayMethod(core_lib, contract_address, functions.delay, validator)
        self._fn_fulfill = FulfillMethod(core_lib, contract_address, functions.fulfill, validator)
        self._fn_get_chain_id = GetChainIdMethod(core_lib, contract_address, functions.getChainId, validator)
        self._fn_get_stored_chain_id = GetStoredChainIdMethod(core_lib, contract_address, functions.getStoredChainId, validator)
        self._fn_interpreter = InterpreterMethod(core_lib, contract_address, functions.interpreter, validator)
        self._fn_is_asset_ownership_renounced = IsAssetOwnershipRenouncedMethod(core_lib, contract_address, functions.isAssetOwnershipRenounced, validator)
        self._fn_is_router_ownership_renounced = IsRouterOwnershipRenouncedMethod(core_lib, contract_address, functions.isRouterOwnershipRenounced, validator)
        self._fn_owner = OwnerMethod(core_lib, contract_address, functions.owner, validator)
        self._fn_prepare = PrepareMethod(core_lib, contract_address, functions.prepare, validator)
        self._fn_propose_asset_ownership_renunciation = ProposeAssetOwnershipRenunciationMethod(core_lib, contract_address, functions.proposeAssetOwnershipRenunciation, validator)
        self._fn_propose_new_owner = ProposeNewOwnerMethod(core_lib, contract_address, functions.proposeNewOwner, validator)
        self._fn_propose_router_ownership_renunciation = ProposeRouterOwnershipRenunciationMethod(core_lib, contract_address, functions.proposeRouterOwnershipRenunciation, validator)
        self._fn_proposed = ProposedMethod(core_lib, contract_address, functions.proposed, validator)
        self._fn_proposed_timestamp = ProposedTimestampMethod(core_lib, contract_address, functions.proposedTimestamp, validator)
        self._fn_remove_asset_id = RemoveAssetIdMethod(core_lib, contract_address, functions.removeAssetId, validator)
        self._fn_remove_liquidity = RemoveLiquidityMethod(core_lib, contract_address, functions.removeLiquidity, validator)
        self._fn_remove_router = RemoveRouterMethod(core_lib, contract_address, functions.removeRouter, validator)
        self._fn_renounce_asset_ownership = RenounceAssetOwnershipMethod(core_lib, contract_address, functions.renounceAssetOwnership, validator)
        self._fn_renounce_ownership = RenounceOwnershipMethod(core_lib, contract_address, functions.renounceOwnership, validator)
        self._fn_renounce_router_ownership = RenounceRouterOwnershipMethod(core_lib, contract_address, functions.renounceRouterOwnership, validator)
        self._fn_renounced = RenouncedMethod(core_lib, contract_address, functions.renounced, validator)
        self._fn_router_balances = RouterBalancesMethod(core_lib, contract_address, functions.routerBalances, validator)
        self._fn_router_ownership_timestamp = RouterOwnershipTimestampMethod(core_lib, contract_address, functions.routerOwnershipTimestamp, validator)
        self._fn_variant_transaction_data = VariantTransactionDataMethod(core_lib, contract_address, functions.variantTransactionData, validator)

    
    
    def event_asset_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_added in contract TransactionManager
        Get log entry for AssetAdded event.
                :param tx_hash: hash of transaction emitting AssetAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.AssetAdded().processReceipt(tx_receipt)
    
    
    def event_asset_ownership_renounced(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_ownership_renounced in contract TransactionManager
        Get log entry for AssetOwnershipRenounced event.
                :param tx_hash: hash of transaction emitting AssetOwnershipRenounced
                event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.AssetOwnershipRenounced().processReceipt(tx_receipt)
    
    
    def event_asset_ownership_renunciation_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_ownership_renunciation_proposed in contract TransactionManager
        Get log entry for AssetOwnershipRenunciationProposed event.
                :param tx_hash: hash of transaction emitting
                AssetOwnershipRenunciationProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.AssetOwnershipRenunciationProposed().processReceipt(tx_receipt)
    
    
    def event_asset_removed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_removed in contract TransactionManager
        Get log entry for AssetRemoved event.
                :param tx_hash: hash of transaction emitting AssetRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.AssetRemoved().processReceipt(tx_receipt)
    
    
    def event_liquidity_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event liquidity_added in contract TransactionManager
        Get log entry for LiquidityAdded event.
                :param tx_hash: hash of transaction emitting LiquidityAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.LiquidityAdded().processReceipt(tx_receipt)
    
    
    def event_liquidity_removed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event liquidity_removed in contract TransactionManager
        Get log entry for LiquidityRemoved event.
                :param tx_hash: hash of transaction emitting LiquidityRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.LiquidityRemoved().processReceipt(tx_receipt)
    
    
    def event_ownership_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_proposed in contract TransactionManager
        Get log entry for OwnershipProposed event.
                :param tx_hash: hash of transaction emitting OwnershipProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.OwnershipProposed().processReceipt(tx_receipt)
    
    
    def event_ownership_transferred(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_transferred in contract TransactionManager
        Get log entry for OwnershipTransferred event.
                :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.OwnershipTransferred().processReceipt(tx_receipt)
    
    
    def event_router_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_added in contract TransactionManager
        Get log entry for RouterAdded event.
                :param tx_hash: hash of transaction emitting RouterAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.RouterAdded().processReceipt(tx_receipt)
    
    
    def event_router_ownership_renounced(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_ownership_renounced in contract TransactionManager
        Get log entry for RouterOwnershipRenounced event.
                :param tx_hash: hash of transaction emitting RouterOwnershipRenounced
                event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.RouterOwnershipRenounced().processReceipt(tx_receipt)
    
    
    def event_router_ownership_renunciation_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_ownership_renunciation_proposed in contract TransactionManager
        Get log entry for RouterOwnershipRenunciationProposed event.
                :param tx_hash: hash of transaction emitting
                RouterOwnershipRenunciationProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.RouterOwnershipRenunciationProposed().processReceipt(tx_receipt)
    
    
    def event_router_removed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_removed in contract TransactionManager
        Get log entry for RouterRemoved event.
                :param tx_hash: hash of transaction emitting RouterRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.RouterRemoved().processReceipt(tx_receipt)
    
    
    def event_transaction_cancelled(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event transaction_cancelled in contract TransactionManager
        Get log entry for TransactionCancelled event.
                :param tx_hash: hash of transaction emitting TransactionCancelled event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.TransactionCancelled().processReceipt(tx_receipt)
    
    
    def event_transaction_fulfilled(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event transaction_fulfilled in contract TransactionManager
        Get log entry for TransactionFulfilled event.
                :param tx_hash: hash of transaction emitting TransactionFulfilled event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.TransactionFulfilled().processReceipt(tx_receipt)
    
    
    def event_transaction_prepared(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event transaction_prepared in contract TransactionManager
        Get log entry for TransactionPrepared event.
                :param tx_hash: hash of transaction emitting TransactionPrepared event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=TransactionManager.abi()).events.TransactionPrepared().processReceipt(tx_receipt)

    
    
    
    def max_timeout(self) -> int:
        """
        Implementation of max_timeout in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_max_timeout.callback_onfail = self._callback_onfail
        self._fn_max_timeout.callback_onsuccess = self._callback_onsuccess
        self._fn_max_timeout.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_max_timeout.gas_limit = self.call_contract_fee_amount
        self._fn_max_timeout.gas_price_wei = self.call_contract_fee_price
        self._fn_max_timeout.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_max_timeout.block_call()
    
    
    
    def min_timeout(self) -> int:
        """
        Implementation of min_timeout in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_min_timeout.callback_onfail = self._callback_onfail
        self._fn_min_timeout.callback_onsuccess = self._callback_onsuccess
        self._fn_min_timeout.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_min_timeout.gas_limit = self.call_contract_fee_amount
        self._fn_min_timeout.gas_price_wei = self.call_contract_fee_price
        self._fn_min_timeout.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_min_timeout.block_call()
    
    
    
    def accept_proposed_owner(self) -> None:
        """
        Implementation of accept_proposed_owner in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_accept_proposed_owner.callback_onfail = self._callback_onfail
        self._fn_accept_proposed_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_accept_proposed_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_accept_proposed_owner.gas_limit = self.call_contract_fee_amount
        self._fn_accept_proposed_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_accept_proposed_owner.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_accept_proposed_owner.block_send()
    
    
    
    
    
    
    
    def add_asset_id(self, asset_id: str) -> None:
        """
        Implementation of add_asset_id in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_add_asset_id.callback_onfail = self._callback_onfail
        self._fn_add_asset_id.callback_onsuccess = self._callback_onsuccess
        self._fn_add_asset_id.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_asset_id.gas_limit = self.call_contract_fee_amount
        self._fn_add_asset_id.gas_price_wei = self.call_contract_fee_price
        self._fn_add_asset_id.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_add_asset_id.block_send(asset_id)
    
    
    
    
    
    
    
    def add_liquidity(self, amount: int, asset_id: str, wei:int=0) -> None:
        """
        Implementation of add_liquidity in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_add_liquidity.callback_onfail = self._callback_onfail
        self._fn_add_liquidity.callback_onsuccess = self._callback_onsuccess
        self._fn_add_liquidity.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_liquidity.gas_limit = self.call_contract_fee_amount
        self._fn_add_liquidity.gas_price_wei = self.call_contract_fee_price
        self._fn_add_liquidity.debug_method = self.call_contract_debug_flag
    
        self._fn_add_liquidity.wei_value = wei
    
    
        return self._fn_add_liquidity.block_send(amount, asset_id, wei)
    
    
    
    
    
    
    def add_liquidity_for(self, amount: int, asset_id: str, router: str, wei:int=0) -> None:
        """
        Implementation of add_liquidity_for in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_add_liquidity_for.callback_onfail = self._callback_onfail
        self._fn_add_liquidity_for.callback_onsuccess = self._callback_onsuccess
        self._fn_add_liquidity_for.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_liquidity_for.gas_limit = self.call_contract_fee_amount
        self._fn_add_liquidity_for.gas_price_wei = self.call_contract_fee_price
        self._fn_add_liquidity_for.debug_method = self.call_contract_debug_flag
    
        self._fn_add_liquidity_for.wei_value = wei
    
    
        return self._fn_add_liquidity_for.block_send(amount, asset_id, router, wei)
    
    
    
    
    
    
    def add_router(self, router: str) -> None:
        """
        Implementation of add_router in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_add_router.callback_onfail = self._callback_onfail
        self._fn_add_router.callback_onsuccess = self._callback_onsuccess
        self._fn_add_router.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_router.gas_limit = self.call_contract_fee_amount
        self._fn_add_router.gas_price_wei = self.call_contract_fee_price
        self._fn_add_router.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_add_router.block_send(router)
    
    
    
    
    
    
    
    def approved_assets(self, index_0: str) -> bool:
        """
        Implementation of approved_assets in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_approved_assets.callback_onfail = self._callback_onfail
        self._fn_approved_assets.callback_onsuccess = self._callback_onsuccess
        self._fn_approved_assets.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_approved_assets.gas_limit = self.call_contract_fee_amount
        self._fn_approved_assets.gas_price_wei = self.call_contract_fee_price
        self._fn_approved_assets.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_approved_assets.block_call(index_0)
    
    
    
    def approved_routers(self, index_0: str) -> bool:
        """
        Implementation of approved_routers in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_approved_routers.callback_onfail = self._callback_onfail
        self._fn_approved_routers.callback_onsuccess = self._callback_onsuccess
        self._fn_approved_routers.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_approved_routers.gas_limit = self.call_contract_fee_amount
        self._fn_approved_routers.gas_price_wei = self.call_contract_fee_price
        self._fn_approved_routers.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_approved_routers.block_call(index_0)
    
    
    
    def asset_ownership_timestamp(self) -> int:
        """
        Implementation of asset_ownership_timestamp in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_asset_ownership_timestamp.callback_onfail = self._callback_onfail
        self._fn_asset_ownership_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_asset_ownership_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_asset_ownership_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_asset_ownership_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_asset_ownership_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_asset_ownership_timestamp.block_call()
    
    
    
    def cancel(self, args: ITransactionManagerCancelArgs) -> ITransactionManagerTransactionData:
        """
        Implementation of cancel in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_cancel.callback_onfail = self._callback_onfail
        self._fn_cancel.callback_onsuccess = self._callback_onsuccess
        self._fn_cancel.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_cancel.gas_limit = self.call_contract_fee_amount
        self._fn_cancel.gas_price_wei = self.call_contract_fee_price
        self._fn_cancel.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_cancel.block_send(args)
    
    
    
    
    
    
    
    def delay(self) -> int:
        """
        Implementation of delay in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_delay.callback_onfail = self._callback_onfail
        self._fn_delay.callback_onsuccess = self._callback_onsuccess
        self._fn_delay.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_delay.gas_limit = self.call_contract_fee_amount
        self._fn_delay.gas_price_wei = self.call_contract_fee_price
        self._fn_delay.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_delay.block_call()
    
    
    
    def fulfill(self, args: ITransactionManagerFulfillArgs) -> ITransactionManagerTransactionData:
        """
        Implementation of fulfill in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_fulfill.callback_onfail = self._callback_onfail
        self._fn_fulfill.callback_onsuccess = self._callback_onsuccess
        self._fn_fulfill.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_fulfill.gas_limit = self.call_contract_fee_amount
        self._fn_fulfill.gas_price_wei = self.call_contract_fee_price
        self._fn_fulfill.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_fulfill.block_send(args)
    
    
    
    
    
    
    
    def get_chain_id(self) -> int:
        """
        Implementation of get_chain_id in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_get_chain_id.callback_onfail = self._callback_onfail
        self._fn_get_chain_id.callback_onsuccess = self._callback_onsuccess
        self._fn_get_chain_id.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_chain_id.gas_limit = self.call_contract_fee_amount
        self._fn_get_chain_id.gas_price_wei = self.call_contract_fee_price
        self._fn_get_chain_id.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_chain_id.block_call()
    
    
    
    def get_stored_chain_id(self) -> int:
        """
        Implementation of get_stored_chain_id in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_get_stored_chain_id.callback_onfail = self._callback_onfail
        self._fn_get_stored_chain_id.callback_onsuccess = self._callback_onsuccess
        self._fn_get_stored_chain_id.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_stored_chain_id.gas_limit = self.call_contract_fee_amount
        self._fn_get_stored_chain_id.gas_price_wei = self.call_contract_fee_price
        self._fn_get_stored_chain_id.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_stored_chain_id.block_call()
    
    
    
    def interpreter(self) -> str:
        """
        Implementation of interpreter in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_interpreter.callback_onfail = self._callback_onfail
        self._fn_interpreter.callback_onsuccess = self._callback_onsuccess
        self._fn_interpreter.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_interpreter.gas_limit = self.call_contract_fee_amount
        self._fn_interpreter.gas_price_wei = self.call_contract_fee_price
        self._fn_interpreter.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_interpreter.block_call()
    
    
    
    def is_asset_ownership_renounced(self) -> bool:
        """
        Implementation of is_asset_ownership_renounced in contract TransactionManager
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
        Implementation of is_router_ownership_renounced in contract TransactionManager
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
        Implementation of owner in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_owner.callback_onfail = self._callback_onfail
        self._fn_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_owner.gas_limit = self.call_contract_fee_amount
        self._fn_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_owner.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_owner.block_call()
    
    
    
    def prepare(self, args: ITransactionManagerPrepareArgs, wei:int=0) -> ITransactionManagerTransactionData:
        """
        Implementation of prepare in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_prepare.callback_onfail = self._callback_onfail
        self._fn_prepare.callback_onsuccess = self._callback_onsuccess
        self._fn_prepare.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_prepare.gas_limit = self.call_contract_fee_amount
        self._fn_prepare.gas_price_wei = self.call_contract_fee_price
        self._fn_prepare.debug_method = self.call_contract_debug_flag
    
        self._fn_prepare.wei_value = wei
    
    
        return self._fn_prepare.block_send(args, wei)
    
    
    
    
    
    
    def propose_asset_ownership_renunciation(self) -> None:
        """
        Implementation of propose_asset_ownership_renunciation in contract TransactionManager
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
        Implementation of propose_new_owner in contract TransactionManager
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
        Implementation of propose_router_ownership_renunciation in contract TransactionManager
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
        Implementation of proposed in contract TransactionManager
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
        Implementation of proposed_timestamp in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_proposed_timestamp.callback_onfail = self._callback_onfail
        self._fn_proposed_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_proposed_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_proposed_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_proposed_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_proposed_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_proposed_timestamp.block_call()
    
    
    
    def remove_asset_id(self, asset_id: str) -> None:
        """
        Implementation of remove_asset_id in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_remove_asset_id.callback_onfail = self._callback_onfail
        self._fn_remove_asset_id.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_asset_id.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_asset_id.gas_limit = self.call_contract_fee_amount
        self._fn_remove_asset_id.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_asset_id.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_asset_id.block_send(asset_id)
    
    
    
    
    
    
    
    def remove_liquidity(self, amount: int, asset_id: str, recipient: str) -> None:
        """
        Implementation of remove_liquidity in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_remove_liquidity.callback_onfail = self._callback_onfail
        self._fn_remove_liquidity.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_liquidity.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_liquidity.gas_limit = self.call_contract_fee_amount
        self._fn_remove_liquidity.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_liquidity.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_liquidity.block_send(amount, asset_id, recipient)
    
    
    
    
    
    
    
    def remove_router(self, router: str) -> None:
        """
        Implementation of remove_router in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_remove_router.callback_onfail = self._callback_onfail
        self._fn_remove_router.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_router.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_router.gas_limit = self.call_contract_fee_amount
        self._fn_remove_router.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_router.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_router.block_send(router)
    
    
    
    
    
    
    
    def renounce_asset_ownership(self) -> None:
        """
        Implementation of renounce_asset_ownership in contract TransactionManager
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
        Implementation of renounce_ownership in contract TransactionManager
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
        Implementation of renounce_router_ownership in contract TransactionManager
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
        Implementation of renounced in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_renounced.callback_onfail = self._callback_onfail
        self._fn_renounced.callback_onsuccess = self._callback_onsuccess
        self._fn_renounced.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounced.gas_limit = self.call_contract_fee_amount
        self._fn_renounced.gas_price_wei = self.call_contract_fee_price
        self._fn_renounced.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_renounced.block_call()
    
    
    
    def router_balances(self, index_0: str, index_1: str) -> int:
        """
        Implementation of router_balances in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_router_balances.callback_onfail = self._callback_onfail
        self._fn_router_balances.callback_onsuccess = self._callback_onsuccess
        self._fn_router_balances.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_balances.gas_limit = self.call_contract_fee_amount
        self._fn_router_balances.gas_price_wei = self.call_contract_fee_price
        self._fn_router_balances.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_balances.block_call(index_0, index_1)
    
    
    
    def router_ownership_timestamp(self) -> int:
        """
        Implementation of router_ownership_timestamp in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_router_ownership_timestamp.callback_onfail = self._callback_onfail
        self._fn_router_ownership_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_router_ownership_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_ownership_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_router_ownership_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_router_ownership_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_ownership_timestamp.block_call()
    
    
    
    def variant_transaction_data(self, index_0: Union[bytes, str]) -> Union[bytes, str]:
        """
        Implementation of variant_transaction_data in contract TransactionManager
        Method of the function
    
        """
    
        self._fn_variant_transaction_data.callback_onfail = self._callback_onfail
        self._fn_variant_transaction_data.callback_onsuccess = self._callback_onsuccess
        self._fn_variant_transaction_data.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_variant_transaction_data.gas_limit = self.call_contract_fee_amount
        self._fn_variant_transaction_data.gas_price_wei = self.call_contract_fee_price
        self._fn_variant_transaction_data.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_variant_transaction_data.block_call(index_0)

    def CallContractWait(self, t_long:int)-> "TransactionManager":
        self._fn_max_timeout.setWait(t_long)
        self._fn_min_timeout.setWait(t_long)
        self._fn_accept_proposed_owner.setWait(t_long)
        self._fn_add_asset_id.setWait(t_long)
        self._fn_add_liquidity.setWait(t_long)
        self._fn_add_liquidity_for.setWait(t_long)
        self._fn_add_router.setWait(t_long)
        self._fn_approved_assets.setWait(t_long)
        self._fn_approved_routers.setWait(t_long)
        self._fn_asset_ownership_timestamp.setWait(t_long)
        self._fn_cancel.setWait(t_long)
        self._fn_delay.setWait(t_long)
        self._fn_fulfill.setWait(t_long)
        self._fn_get_chain_id.setWait(t_long)
        self._fn_get_stored_chain_id.setWait(t_long)
        self._fn_interpreter.setWait(t_long)
        self._fn_is_asset_ownership_renounced.setWait(t_long)
        self._fn_is_router_ownership_renounced.setWait(t_long)
        self._fn_owner.setWait(t_long)
        self._fn_prepare.setWait(t_long)
        self._fn_propose_asset_ownership_renunciation.setWait(t_long)
        self._fn_propose_new_owner.setWait(t_long)
        self._fn_propose_router_ownership_renunciation.setWait(t_long)
        self._fn_proposed.setWait(t_long)
        self._fn_proposed_timestamp.setWait(t_long)
        self._fn_remove_asset_id.setWait(t_long)
        self._fn_remove_liquidity.setWait(t_long)
        self._fn_remove_router.setWait(t_long)
        self._fn_renounce_asset_ownership.setWait(t_long)
        self._fn_renounce_ownership.setWait(t_long)
        self._fn_renounce_router_ownership.setWait(t_long)
        self._fn_renounced.setWait(t_long)
        self._fn_router_balances.setWait(t_long)
        self._fn_router_ownership_timestamp.setWait(t_long)
        self._fn_variant_transaction_data.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"uint256","name":"_chainId","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addedAssetId","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AssetAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"renounced","type":"bool"}],"name":"AssetOwnershipRenounced","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"AssetOwnershipRenunciationProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"removedAssetId","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"AssetRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"router","type":"address"},{"indexed":true,"internalType":"address","name":"assetId","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"LiquidityAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"router","type":"address"},{"indexed":true,"internalType":"address","name":"assetId","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"}],"name":"LiquidityRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"proposedOwner","type":"address"}],"name":"OwnershipProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addedRouter","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"RouterAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"renounced","type":"bool"}],"name":"RouterOwnershipRenounced","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"RouterOwnershipRenunciationProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"removedRouter","type":"address"},{"indexed":true,"internalType":"address","name":"caller","type":"address"}],"name":"RouterRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"router","type":"address"},{"indexed":true,"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"indexed":false,"internalType":"struct ITransactionManager.CancelArgs","name":"args","type":"tuple"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"TransactionCancelled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"router","type":"address"},{"indexed":true,"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"internalType":"uint256","name":"relayerFee","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"callData","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"indexed":false,"internalType":"struct ITransactionManager.FulfillArgs","name":"args","type":"tuple"},{"indexed":false,"internalType":"bool","name":"success","type":"bool"},{"indexed":false,"internalType":"bool","name":"isContract","type":"bool"},{"indexed":false,"internalType":"bytes","name":"returnData","type":"bytes"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"TransactionFulfilled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"router","type":"address"},{"indexed":true,"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"indexed":false,"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"indexed":false,"internalType":"address","name":"caller","type":"address"},{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"}],"internalType":"struct ITransactionManager.InvariantTransactionData","name":"invariantData","type":"tuple"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"bytes","name":"encryptedCallData","type":"bytes"},{"internalType":"bytes","name":"encodedBid","type":"bytes"},{"internalType":"bytes","name":"bidSignature","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"indexed":false,"internalType":"struct ITransactionManager.PrepareArgs","name":"args","type":"tuple"}],"name":"TransactionPrepared","type":"event"},{"inputs":[],"name":"MAX_TIMEOUT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MIN_TIMEOUT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"acceptProposedOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"assetId","type":"address"}],"name":"addAssetId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"assetId","type":"address"}],"name":"addLiquidity","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"assetId","type":"address"},{"internalType":"address","name":"router","type":"address"}],"name":"addLiquidityFor","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"}],"name":"addRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"approvedAssets","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"approvedRouters","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"assetOwnershipTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"internalType":"struct ITransactionManager.CancelArgs","name":"args","type":"tuple"}],"name":"cancel","outputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"delay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"internalType":"uint256","name":"relayerFee","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"callData","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"internalType":"struct ITransactionManager.FulfillArgs","name":"args","type":"tuple"}],"name":"fulfill","outputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getChainId","outputs":[{"internalType":"uint256","name":"_chainId","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getStoredChainId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"interpreter","outputs":[{"internalType":"contract IFulfillInterpreter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isAssetOwnershipRenounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isRouterOwnershipRenounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"}],"internalType":"struct ITransactionManager.InvariantTransactionData","name":"invariantData","type":"tuple"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"bytes","name":"encryptedCallData","type":"bytes"},{"internalType":"bytes","name":"encodedBid","type":"bytes"},{"internalType":"bytes","name":"bidSignature","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"internalType":"struct ITransactionManager.PrepareArgs","name":"args","type":"tuple"}],"name":"prepare","outputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"","type":"tuple"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"proposeAssetOwnershipRenunciation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newlyProposed","type":"address"}],"name":"proposeNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposeRouterOwnershipRenunciation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposed","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposedTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"assetId","type":"address"}],"name":"removeAssetId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"assetId","type":"address"},{"internalType":"address payable","name":"recipient","type":"address"}],"name":"removeLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"}],"name":"removeRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceAssetOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceRouterOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"}],"name":"routerBalances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"routerOwnershipTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"variantTransactionData","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
