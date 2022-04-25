"""Generated wrapper for Router Solidity contract."""

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
# constructor for Router below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        RouterValidator,
    )
except ImportError:

    class RouterValidator(  # type: ignore
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


class AddRelayerFeeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addRelayerFee method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addRelayerFee")

    def validate_and_normalize_inputs(self, amount: int, asset_id: str)->any:
        """Validate the inputs to the addRelayerFee method."""
        self.validator.assert_valid(
            method_name='addRelayerFee',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='addRelayerFee',
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

                self._on_receipt_handle("add_relayer_fee", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_relayer_fee")
            message = f"Error {er}: add_relayer_fee"
            self._on_fail("add_relayer_fee", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_relayer_fee: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_relayer_fee. Reason: Unknown")

            self._on_fail("add_relayer_fee", message)

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

class CancelMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the cancel method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("cancel")

    def validate_and_normalize_inputs(self, args: ITransactionManagerCancelArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str])->any:
        """Validate the inputs to the cancel method."""
        self.validator.assert_valid(
            method_name='cancel',
            parameter_name='args',
            argument_value=args,
        )
        self.validator.assert_valid(
            method_name='cancel',
            parameter_name='routerRelayerFeeAsset',
            argument_value=router_relayer_fee_asset,
        )
        router_relayer_fee_asset = self.validate_and_checksum_address(router_relayer_fee_asset)
        self.validator.assert_valid(
            method_name='cancel',
            parameter_name='routerRelayerFee',
            argument_value=router_relayer_fee,
        )
        # safeguard against fractional inputs
        router_relayer_fee = int(router_relayer_fee)
        self.validator.assert_valid(
            method_name='cancel',
            parameter_name='signature',
            argument_value=signature,
        )
        return (args, router_relayer_fee_asset, router_relayer_fee, signature)



    def block_send(self, args: ITransactionManagerCancelArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str],_valeth:int=0) -> ITransactionManagerTransactionData:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature)
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

    def send_transaction(self, args: ITransactionManagerCancelArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).transact(tx_params.as_dict())

    def build_transaction(self, args: ITransactionManagerCancelArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: ITransactionManagerCancelArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).estimateGas(tx_params.as_dict())

class FulfillMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the fulfill method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("fulfill")

    def validate_and_normalize_inputs(self, args: ITransactionManagerFulfillArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str])->any:
        """Validate the inputs to the fulfill method."""
        self.validator.assert_valid(
            method_name='fulfill',
            parameter_name='args',
            argument_value=args,
        )
        self.validator.assert_valid(
            method_name='fulfill',
            parameter_name='routerRelayerFeeAsset',
            argument_value=router_relayer_fee_asset,
        )
        router_relayer_fee_asset = self.validate_and_checksum_address(router_relayer_fee_asset)
        self.validator.assert_valid(
            method_name='fulfill',
            parameter_name='routerRelayerFee',
            argument_value=router_relayer_fee,
        )
        # safeguard against fractional inputs
        router_relayer_fee = int(router_relayer_fee)
        self.validator.assert_valid(
            method_name='fulfill',
            parameter_name='signature',
            argument_value=signature,
        )
        return (args, router_relayer_fee_asset, router_relayer_fee, signature)



    def block_send(self, args: ITransactionManagerFulfillArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str],_valeth:int=0) -> ITransactionManagerTransactionData:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature)
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

    def send_transaction(self, args: ITransactionManagerFulfillArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).transact(tx_params.as_dict())

    def build_transaction(self, args: ITransactionManagerFulfillArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: ITransactionManagerFulfillArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).estimateGas(tx_params.as_dict())

class InitMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the init method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("init")

    def validate_and_normalize_inputs(self, transaction_manager: str, chain_id: int, router_signer: str, recipient: str, owner: str)->any:
        """Validate the inputs to the init method."""
        self.validator.assert_valid(
            method_name='init',
            parameter_name='_transactionManager',
            argument_value=transaction_manager,
        )
        transaction_manager = self.validate_and_checksum_address(transaction_manager)
        self.validator.assert_valid(
            method_name='init',
            parameter_name='_chainId',
            argument_value=chain_id,
        )
        # safeguard against fractional inputs
        chain_id = int(chain_id)
        self.validator.assert_valid(
            method_name='init',
            parameter_name='_routerSigner',
            argument_value=router_signer,
        )
        router_signer = self.validate_and_checksum_address(router_signer)
        self.validator.assert_valid(
            method_name='init',
            parameter_name='_recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        self.validator.assert_valid(
            method_name='init',
            parameter_name='_owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        return (transaction_manager, chain_id, router_signer, recipient, owner)



    def block_send(self, transaction_manager: str, chain_id: int, router_signer: str, recipient: str, owner: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(transaction_manager, chain_id, router_signer, recipient, owner)
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

    def send_transaction(self, transaction_manager: str, chain_id: int, router_signer: str, recipient: str, owner: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (transaction_manager, chain_id, router_signer, recipient, owner) = self.validate_and_normalize_inputs(transaction_manager, chain_id, router_signer, recipient, owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_manager, chain_id, router_signer, recipient, owner).transact(tx_params.as_dict())

    def build_transaction(self, transaction_manager: str, chain_id: int, router_signer: str, recipient: str, owner: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (transaction_manager, chain_id, router_signer, recipient, owner) = self.validate_and_normalize_inputs(transaction_manager, chain_id, router_signer, recipient, owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_manager, chain_id, router_signer, recipient, owner).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, transaction_manager: str, chain_id: int, router_signer: str, recipient: str, owner: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (transaction_manager, chain_id, router_signer, recipient, owner) = self.validate_and_normalize_inputs(transaction_manager, chain_id, router_signer, recipient, owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transaction_manager, chain_id, router_signer, recipient, owner).estimateGas(tx_params.as_dict())

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

    def validate_and_normalize_inputs(self, args: ITransactionManagerPrepareArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str])->any:
        """Validate the inputs to the prepare method."""
        self.validator.assert_valid(
            method_name='prepare',
            parameter_name='args',
            argument_value=args,
        )
        self.validator.assert_valid(
            method_name='prepare',
            parameter_name='routerRelayerFeeAsset',
            argument_value=router_relayer_fee_asset,
        )
        router_relayer_fee_asset = self.validate_and_checksum_address(router_relayer_fee_asset)
        self.validator.assert_valid(
            method_name='prepare',
            parameter_name='routerRelayerFee',
            argument_value=router_relayer_fee,
        )
        # safeguard against fractional inputs
        router_relayer_fee = int(router_relayer_fee)
        self.validator.assert_valid(
            method_name='prepare',
            parameter_name='signature',
            argument_value=signature,
        )
        return (args, router_relayer_fee_asset, router_relayer_fee, signature)



    def block_send(self, args: ITransactionManagerPrepareArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str],_valeth:int=0) -> ITransactionManagerTransactionData:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature)
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

    def send_transaction(self, args: ITransactionManagerPrepareArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).transact(tx_params.as_dict())

    def build_transaction(self, args: ITransactionManagerPrepareArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: ITransactionManagerPrepareArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(args, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args, router_relayer_fee_asset, router_relayer_fee, signature).estimateGas(tx_params.as_dict())

class RecipientMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the recipient method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("recipient")



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

                self._on_receipt_handle("recipient", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: recipient")
            message = f"Error {er}: recipient"
            self._on_fail("recipient", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, recipient: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, recipient. Reason: Unknown")

            self._on_fail("recipient", message)

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

class RemoveLiquidityMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeLiquidity method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeLiquidity")

    def validate_and_normalize_inputs(self, amount: int, asset_id: str, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str])->any:
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
            parameter_name='routerRelayerFeeAsset',
            argument_value=router_relayer_fee_asset,
        )
        router_relayer_fee_asset = self.validate_and_checksum_address(router_relayer_fee_asset)
        self.validator.assert_valid(
            method_name='removeLiquidity',
            parameter_name='routerRelayerFee',
            argument_value=router_relayer_fee,
        )
        # safeguard against fractional inputs
        router_relayer_fee = int(router_relayer_fee)
        self.validator.assert_valid(
            method_name='removeLiquidity',
            parameter_name='signature',
            argument_value=signature,
        )
        return (amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature)



    def block_send(self, amount: int, asset_id: str, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str],_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature)
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

    def send_transaction(self, amount: int, asset_id: str, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, asset_id: str, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, asset_id: str, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature) = self.validate_and_normalize_inputs(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature).estimateGas(tx_params.as_dict())

class RemoveRelayerFeeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeRelayerFee method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeRelayerFee")

    def validate_and_normalize_inputs(self, amount: int, asset_id: str)->any:
        """Validate the inputs to the removeRelayerFee method."""
        self.validator.assert_valid(
            method_name='removeRelayerFee',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='removeRelayerFee',
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

                self._on_receipt_handle("remove_relayer_fee", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remove_relayer_fee")
            message = f"Error {er}: remove_relayer_fee"
            self._on_fail("remove_relayer_fee", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_relayer_fee: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_relayer_fee. Reason: Unknown")

            self._on_fail("remove_relayer_fee", message)

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

class RouterFactoryMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerFactory method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerFactory")



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

                self._on_receipt_handle("router_factory", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_factory")
            message = f"Error {er}: router_factory"
            self._on_fail("router_factory", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_factory: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_factory. Reason: Unknown")

            self._on_fail("router_factory", message)

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

class RouterSignerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerSigner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerSigner")



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

                self._on_receipt_handle("router_signer", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_signer")
            message = f"Error {er}: router_signer"
            self._on_fail("router_signer", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_signer: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_signer. Reason: Unknown")

            self._on_fail("router_signer", message)

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

class SetRecipientMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setRecipient method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setRecipient")

    def validate_and_normalize_inputs(self, recipient: str)->any:
        """Validate the inputs to the setRecipient method."""
        self.validator.assert_valid(
            method_name='setRecipient',
            parameter_name='_recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (recipient)



    def block_send(self, recipient: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(recipient)
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

                self._on_receipt_handle("set_recipient", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_recipient")
            message = f"Error {er}: set_recipient"
            self._on_fail("set_recipient", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_recipient: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_recipient. Reason: Unknown")

            self._on_fail("set_recipient", message)

    def send_transaction(self, recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (recipient) = self.validate_and_normalize_inputs(recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(recipient).transact(tx_params.as_dict())

    def build_transaction(self, recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (recipient) = self.validate_and_normalize_inputs(recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (recipient) = self.validate_and_normalize_inputs(recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(recipient).estimateGas(tx_params.as_dict())

class SetSignerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setSigner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setSigner")

    def validate_and_normalize_inputs(self, router_signer: str)->any:
        """Validate the inputs to the setSigner method."""
        self.validator.assert_valid(
            method_name='setSigner',
            parameter_name='_routerSigner',
            argument_value=router_signer,
        )
        router_signer = self.validate_and_checksum_address(router_signer)
        return (router_signer)



    def block_send(self, router_signer: str,_valeth:int=0) -> None:
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

                self._on_receipt_handle("set_signer", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_signer")
            message = f"Error {er}: set_signer"
            self._on_fail("set_signer", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_signer: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_signer. Reason: Unknown")

            self._on_fail("set_signer", message)

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

    def add_relayer_fee(self) -> str:
        return self._function_signatures["addRelayerFee"]
    def cancel(self) -> str:
        return self._function_signatures["cancel"]
    def fulfill(self) -> str:
        return self._function_signatures["fulfill"]
    def init(self) -> str:
        return self._function_signatures["init"]
    def owner(self) -> str:
        return self._function_signatures["owner"]
    def prepare(self) -> str:
        return self._function_signatures["prepare"]
    def recipient(self) -> str:
        return self._function_signatures["recipient"]
    def remove_liquidity(self) -> str:
        return self._function_signatures["removeLiquidity"]
    def remove_relayer_fee(self) -> str:
        return self._function_signatures["removeRelayerFee"]
    def renounce_ownership(self) -> str:
        return self._function_signatures["renounceOwnership"]
    def router_factory(self) -> str:
        return self._function_signatures["routerFactory"]
    def router_signer(self) -> str:
        return self._function_signatures["routerSigner"]
    def set_recipient(self) -> str:
        return self._function_signatures["setRecipient"]
    def set_signer(self) -> str:
        return self._function_signatures["setSigner"]
    def transaction_manager(self) -> str:
        return self._function_signatures["transactionManager"]
    def transfer_ownership(self) -> str:
        return self._function_signatures["transferOwnership"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Router(ContractBase):
    """Wrapper class for Router Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    _fn_add_relayer_fee: AddRelayerFeeMethod
    """Constructor-initialized instance of
    :class:`AddRelayerFeeMethod`.
    """

    _fn_cancel: CancelMethod
    """Constructor-initialized instance of
    :class:`CancelMethod`.
    """

    _fn_fulfill: FulfillMethod
    """Constructor-initialized instance of
    :class:`FulfillMethod`.
    """

    _fn_init: InitMethod
    """Constructor-initialized instance of
    :class:`InitMethod`.
    """

    _fn_owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    _fn_prepare: PrepareMethod
    """Constructor-initialized instance of
    :class:`PrepareMethod`.
    """

    _fn_recipient: RecipientMethod
    """Constructor-initialized instance of
    :class:`RecipientMethod`.
    """

    _fn_remove_liquidity: RemoveLiquidityMethod
    """Constructor-initialized instance of
    :class:`RemoveLiquidityMethod`.
    """

    _fn_remove_relayer_fee: RemoveRelayerFeeMethod
    """Constructor-initialized instance of
    :class:`RemoveRelayerFeeMethod`.
    """

    _fn_renounce_ownership: RenounceOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceOwnershipMethod`.
    """

    _fn_router_factory: RouterFactoryMethod
    """Constructor-initialized instance of
    :class:`RouterFactoryMethod`.
    """

    _fn_router_signer: RouterSignerMethod
    """Constructor-initialized instance of
    :class:`RouterSignerMethod`.
    """

    _fn_set_recipient: SetRecipientMethod
    """Constructor-initialized instance of
    :class:`SetRecipientMethod`.
    """

    _fn_set_signer: SetSignerMethod
    """Constructor-initialized instance of
    :class:`SetSignerMethod`.
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
        validator: RouterValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, Router.abi())
        web3 = core_lib.w3

        if not validator:
            validator = RouterValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=Router.abi()).functions
        self._signatures = SignatureGenerator(Router.abi())
        validator.bindSignatures(self._signatures)

        self._fn_add_relayer_fee = AddRelayerFeeMethod(core_lib, contract_address, functions.addRelayerFee, validator)
        self._fn_cancel = CancelMethod(core_lib, contract_address, functions.cancel, validator)
        self._fn_fulfill = FulfillMethod(core_lib, contract_address, functions.fulfill, validator)
        self._fn_init = InitMethod(core_lib, contract_address, functions.init, validator)
        self._fn_owner = OwnerMethod(core_lib, contract_address, functions.owner, validator)
        self._fn_prepare = PrepareMethod(core_lib, contract_address, functions.prepare, validator)
        self._fn_recipient = RecipientMethod(core_lib, contract_address, functions.recipient, validator)
        self._fn_remove_liquidity = RemoveLiquidityMethod(core_lib, contract_address, functions.removeLiquidity, validator)
        self._fn_remove_relayer_fee = RemoveRelayerFeeMethod(core_lib, contract_address, functions.removeRelayerFee, validator)
        self._fn_renounce_ownership = RenounceOwnershipMethod(core_lib, contract_address, functions.renounceOwnership, validator)
        self._fn_router_factory = RouterFactoryMethod(core_lib, contract_address, functions.routerFactory, validator)
        self._fn_router_signer = RouterSignerMethod(core_lib, contract_address, functions.routerSigner, validator)
        self._fn_set_recipient = SetRecipientMethod(core_lib, contract_address, functions.setRecipient, validator)
        self._fn_set_signer = SetSignerMethod(core_lib, contract_address, functions.setSigner, validator)
        self._fn_transaction_manager = TransactionManagerMethod(core_lib, contract_address, functions.transactionManager, validator)
        self._fn_transfer_ownership = TransferOwnershipMethod(core_lib, contract_address, functions.transferOwnership, validator)

    
    
    def event_cancel(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event cancel in contract Router
        Get log entry for Cancel event.
                :param tx_hash: hash of transaction emitting Cancel event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Router.abi()).events.Cancel().processReceipt(tx_receipt)
    
    
    def event_fulfill(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event fulfill in contract Router
        Get log entry for Fulfill event.
                :param tx_hash: hash of transaction emitting Fulfill event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Router.abi()).events.Fulfill().processReceipt(tx_receipt)
    
    
    def event_ownership_transferred(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_transferred in contract Router
        Get log entry for OwnershipTransferred event.
                :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Router.abi()).events.OwnershipTransferred().processReceipt(tx_receipt)
    
    
    def event_prepare(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event prepare in contract Router
        Get log entry for Prepare event.
                :param tx_hash: hash of transaction emitting Prepare event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Router.abi()).events.Prepare().processReceipt(tx_receipt)
    
    
    def event_relayer_fee_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event relayer_fee_added in contract Router
        Get log entry for RelayerFeeAdded event.
                :param tx_hash: hash of transaction emitting RelayerFeeAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Router.abi()).events.RelayerFeeAdded().processReceipt(tx_receipt)
    
    
    def event_relayer_fee_removed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event relayer_fee_removed in contract Router
        Get log entry for RelayerFeeRemoved event.
                :param tx_hash: hash of transaction emitting RelayerFeeRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Router.abi()).events.RelayerFeeRemoved().processReceipt(tx_receipt)
    
    
    def event_remove_liquidity(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event remove_liquidity in contract Router
        Get log entry for RemoveLiquidity event.
                :param tx_hash: hash of transaction emitting RemoveLiquidity event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Router.abi()).events.RemoveLiquidity().processReceipt(tx_receipt)

    
    
    
    def add_relayer_fee(self, amount: int, asset_id: str, wei:int=0) -> None:
        """
        Implementation of add_relayer_fee in contract Router
        Method of the function
    
        """
    
        self._fn_add_relayer_fee.callback_onfail = self._callback_onfail
        self._fn_add_relayer_fee.callback_onsuccess = self._callback_onsuccess
        self._fn_add_relayer_fee.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_relayer_fee.gas_limit = self.call_contract_fee_amount
        self._fn_add_relayer_fee.gas_price_wei = self.call_contract_fee_price
        self._fn_add_relayer_fee.debug_method = self.call_contract_debug_flag
    
        self._fn_add_relayer_fee.wei_value = wei
    
    
        return self._fn_add_relayer_fee.block_send(amount, asset_id, wei)
    
    
    
    
    
    
    def cancel(self, args: ITransactionManagerCancelArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str]) -> ITransactionManagerTransactionData:
        """
        Implementation of cancel in contract Router
        Method of the function
    
        """
    
        self._fn_cancel.callback_onfail = self._callback_onfail
        self._fn_cancel.callback_onsuccess = self._callback_onsuccess
        self._fn_cancel.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_cancel.gas_limit = self.call_contract_fee_amount
        self._fn_cancel.gas_price_wei = self.call_contract_fee_price
        self._fn_cancel.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_cancel.block_send(args, router_relayer_fee_asset, router_relayer_fee, signature)
    
    
    
    
    
    
    
    def fulfill(self, args: ITransactionManagerFulfillArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str]) -> ITransactionManagerTransactionData:
        """
        Implementation of fulfill in contract Router
        Method of the function
    
        """
    
        self._fn_fulfill.callback_onfail = self._callback_onfail
        self._fn_fulfill.callback_onsuccess = self._callback_onsuccess
        self._fn_fulfill.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_fulfill.gas_limit = self.call_contract_fee_amount
        self._fn_fulfill.gas_price_wei = self.call_contract_fee_price
        self._fn_fulfill.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_fulfill.block_send(args, router_relayer_fee_asset, router_relayer_fee, signature)
    
    
    
    
    
    
    
    def init(self, transaction_manager: str, chain_id: int, router_signer: str, recipient: str, owner: str) -> None:
        """
        Implementation of init in contract Router
        Method of the function
    
        """
    
        self._fn_init.callback_onfail = self._callback_onfail
        self._fn_init.callback_onsuccess = self._callback_onsuccess
        self._fn_init.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_init.gas_limit = self.call_contract_fee_amount
        self._fn_init.gas_price_wei = self.call_contract_fee_price
        self._fn_init.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_init.block_send(transaction_manager, chain_id, router_signer, recipient, owner)
    
    
    
    
    
    
    
    def owner(self) -> str:
        """
        Implementation of owner in contract Router
        Method of the function
    
        """
    
        self._fn_owner.callback_onfail = self._callback_onfail
        self._fn_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_owner.gas_limit = self.call_contract_fee_amount
        self._fn_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_owner.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_owner.block_call()
    
    
    
    def prepare(self, args: ITransactionManagerPrepareArgs, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str], wei:int=0) -> ITransactionManagerTransactionData:
        """
        Implementation of prepare in contract Router
        Method of the function
    
        """
    
        self._fn_prepare.callback_onfail = self._callback_onfail
        self._fn_prepare.callback_onsuccess = self._callback_onsuccess
        self._fn_prepare.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_prepare.gas_limit = self.call_contract_fee_amount
        self._fn_prepare.gas_price_wei = self.call_contract_fee_price
        self._fn_prepare.debug_method = self.call_contract_debug_flag
    
        self._fn_prepare.wei_value = wei
    
    
        return self._fn_prepare.block_send(args, router_relayer_fee_asset, router_relayer_fee, signature, wei)
    
    
    
    
    
    
    def recipient(self) -> str:
        """
        Implementation of recipient in contract Router
        Method of the function
    
        """
    
        self._fn_recipient.callback_onfail = self._callback_onfail
        self._fn_recipient.callback_onsuccess = self._callback_onsuccess
        self._fn_recipient.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_recipient.gas_limit = self.call_contract_fee_amount
        self._fn_recipient.gas_price_wei = self.call_contract_fee_price
        self._fn_recipient.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_recipient.block_call()
    
    
    
    def remove_liquidity(self, amount: int, asset_id: str, router_relayer_fee_asset: str, router_relayer_fee: int, signature: Union[bytes, str]) -> None:
        """
        Implementation of remove_liquidity in contract Router
        Method of the function
    
        """
    
        self._fn_remove_liquidity.callback_onfail = self._callback_onfail
        self._fn_remove_liquidity.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_liquidity.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_liquidity.gas_limit = self.call_contract_fee_amount
        self._fn_remove_liquidity.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_liquidity.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_liquidity.block_send(amount, asset_id, router_relayer_fee_asset, router_relayer_fee, signature)
    
    
    
    
    
    
    
    def remove_relayer_fee(self, amount: int, asset_id: str) -> None:
        """
        Implementation of remove_relayer_fee in contract Router
        Method of the function
    
        """
    
        self._fn_remove_relayer_fee.callback_onfail = self._callback_onfail
        self._fn_remove_relayer_fee.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_relayer_fee.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_relayer_fee.gas_limit = self.call_contract_fee_amount
        self._fn_remove_relayer_fee.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_relayer_fee.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_relayer_fee.block_send(amount, asset_id)
    
    
    
    
    
    
    
    def renounce_ownership(self) -> None:
        """
        Implementation of renounce_ownership in contract Router
        Method of the function
    
        """
    
        self._fn_renounce_ownership.callback_onfail = self._callback_onfail
        self._fn_renounce_ownership.callback_onsuccess = self._callback_onsuccess
        self._fn_renounce_ownership.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounce_ownership.gas_limit = self.call_contract_fee_amount
        self._fn_renounce_ownership.gas_price_wei = self.call_contract_fee_price
        self._fn_renounce_ownership.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_renounce_ownership.block_send()
    
    
    
    
    
    
    
    def router_factory(self) -> str:
        """
        Implementation of router_factory in contract Router
        Method of the function
    
        """
    
        self._fn_router_factory.callback_onfail = self._callback_onfail
        self._fn_router_factory.callback_onsuccess = self._callback_onsuccess
        self._fn_router_factory.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_factory.gas_limit = self.call_contract_fee_amount
        self._fn_router_factory.gas_price_wei = self.call_contract_fee_price
        self._fn_router_factory.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_factory.block_call()
    
    
    
    def router_signer(self) -> str:
        """
        Implementation of router_signer in contract Router
        Method of the function
    
        """
    
        self._fn_router_signer.callback_onfail = self._callback_onfail
        self._fn_router_signer.callback_onsuccess = self._callback_onsuccess
        self._fn_router_signer.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_signer.gas_limit = self.call_contract_fee_amount
        self._fn_router_signer.gas_price_wei = self.call_contract_fee_price
        self._fn_router_signer.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_signer.block_call()
    
    
    
    def set_recipient(self, recipient: str) -> None:
        """
        Implementation of set_recipient in contract Router
        Method of the function
    
        """
    
        self._fn_set_recipient.callback_onfail = self._callback_onfail
        self._fn_set_recipient.callback_onsuccess = self._callback_onsuccess
        self._fn_set_recipient.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_recipient.gas_limit = self.call_contract_fee_amount
        self._fn_set_recipient.gas_price_wei = self.call_contract_fee_price
        self._fn_set_recipient.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_recipient.block_send(recipient)
    
    
    
    
    
    
    
    def set_signer(self, router_signer: str) -> None:
        """
        Implementation of set_signer in contract Router
        Method of the function
    
        """
    
        self._fn_set_signer.callback_onfail = self._callback_onfail
        self._fn_set_signer.callback_onsuccess = self._callback_onsuccess
        self._fn_set_signer.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_signer.gas_limit = self.call_contract_fee_amount
        self._fn_set_signer.gas_price_wei = self.call_contract_fee_price
        self._fn_set_signer.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_signer.block_send(router_signer)
    
    
    
    
    
    
    
    def transaction_manager(self) -> str:
        """
        Implementation of transaction_manager in contract Router
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
        Implementation of transfer_ownership in contract Router
        Method of the function
    
        """
    
        self._fn_transfer_ownership.callback_onfail = self._callback_onfail
        self._fn_transfer_ownership.callback_onsuccess = self._callback_onsuccess
        self._fn_transfer_ownership.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_transfer_ownership.gas_limit = self.call_contract_fee_amount
        self._fn_transfer_ownership.gas_price_wei = self.call_contract_fee_price
        self._fn_transfer_ownership.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_transfer_ownership.block_send(new_owner)
    
    
    
    

    def CallContractWait(self, t_long:int)-> "Router":
        self._fn_add_relayer_fee.setWait(t_long)
        self._fn_cancel.setWait(t_long)
        self._fn_fulfill.setWait(t_long)
        self._fn_init.setWait(t_long)
        self._fn_owner.setWait(t_long)
        self._fn_prepare.setWait(t_long)
        self._fn_recipient.setWait(t_long)
        self._fn_remove_liquidity.setWait(t_long)
        self._fn_remove_relayer_fee.setWait(t_long)
        self._fn_renounce_ownership.setWait(t_long)
        self._fn_router_factory.setWait(t_long)
        self._fn_router_signer.setWait(t_long)
        self._fn_set_recipient.setWait(t_long)
        self._fn_set_signer.setWait(t_long)
        self._fn_transaction_manager.setWait(t_long)
        self._fn_transfer_ownership.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_routerFactory","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"indexed":false,"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"indexed":false,"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"indexed":false,"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"Cancel","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"indexed":false,"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"indexed":false,"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"indexed":false,"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"Fulfill","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"}],"indexed":false,"internalType":"struct ITransactionManager.InvariantTransactionData","name":"invariantData","type":"tuple"},{"indexed":false,"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"indexed":false,"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"Prepare","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"assetId","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"RelayerFeeAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"assetId","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"RelayerFeeRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"assetId","type":"address"},{"indexed":false,"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"indexed":false,"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"RemoveLiquidity","type":"event"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"assetId","type":"address"}],"name":"addRelayerFee","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"internalType":"struct ITransactionManager.CancelArgs","name":"args","type":"tuple"},{"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"cancel","outputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"txData","type":"tuple"},{"internalType":"uint256","name":"relayerFee","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes","name":"callData","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"internalType":"struct ITransactionManager.FulfillArgs","name":"args","type":"tuple"},{"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"fulfill","outputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_transactionManager","type":"address"},{"internalType":"uint256","name":"_chainId","type":"uint256"},{"internalType":"address","name":"_routerSigner","type":"address"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"address","name":"_owner","type":"address"}],"name":"init","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"}],"internalType":"struct ITransactionManager.InvariantTransactionData","name":"invariantData","type":"tuple"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"bytes","name":"encryptedCallData","type":"bytes"},{"internalType":"bytes","name":"encodedBid","type":"bytes"},{"internalType":"bytes","name":"bidSignature","type":"bytes"},{"internalType":"bytes","name":"encodedMeta","type":"bytes"}],"internalType":"struct ITransactionManager.PrepareArgs","name":"args","type":"tuple"},{"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"prepare","outputs":[{"components":[{"internalType":"address","name":"receivingChainTxManagerAddress","type":"address"},{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"initiator","type":"address"},{"internalType":"address","name":"sendingAssetId","type":"address"},{"internalType":"address","name":"receivingAssetId","type":"address"},{"internalType":"address","name":"sendingChainFallback","type":"address"},{"internalType":"address","name":"receivingAddress","type":"address"},{"internalType":"address","name":"callTo","type":"address"},{"internalType":"bytes32","name":"callDataHash","type":"bytes32"},{"internalType":"bytes32","name":"transactionId","type":"bytes32"},{"internalType":"uint256","name":"sendingChainId","type":"uint256"},{"internalType":"uint256","name":"receivingChainId","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"preparedBlockNumber","type":"uint256"}],"internalType":"struct ITransactionManager.TransactionData","name":"","type":"tuple"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"recipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"assetId","type":"address"},{"internalType":"address","name":"routerRelayerFeeAsset","type":"address"},{"internalType":"uint256","name":"routerRelayerFee","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"removeLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"assetId","type":"address"}],"name":"removeRelayerFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"routerFactory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"routerSigner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"}],"name":"setRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_routerSigner","type":"address"}],"name":"setSigner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"transactionManager","outputs":[{"internalType":"contract ITransactionManager","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
