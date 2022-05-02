"""Generated wrapper for Connext Solidity contract."""

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
# constructor for Connext below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ConnextValidator,
    )
except ImportError:

    class ConnextValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IConnextCallParams(TypedDict):
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

    to: str

    callData: Union[bytes, str]

    originDomain: int

    destinationDomain: int


class IConnextExecuteArgs(TypedDict):
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

    params: IConnextCallParams

    local: str

    routers: List[str]

    feePercentage: int

    amount: int

    nonce: int

    relayerSignature: Union[bytes, str]

    originSender: str


class IConnextXCallArgs(TypedDict):
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

    params: IConnextCallParams

    transactingAssetId: str

    amount: int


class IConnextExecutedTransfer(TypedDict):
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

    routers: List[str]

    amount: int


class BridgeMessageTokenId(TypedDict):
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

    domain: int

    id: Union[bytes, str]


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

class AcceptProposedRouterOwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the acceptProposedRouterOwner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("acceptProposedRouterOwner")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the acceptProposedRouterOwner method."""
        self.validator.assert_valid(
            method_name='acceptProposedRouterOwner',
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

                self._on_receipt_handle("accept_proposed_router_owner", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: accept_proposed_router_owner")
            message = f"Error {er}: accept_proposed_router_owner"
            self._on_fail("accept_proposed_router_owner", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, accept_proposed_router_owner: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, accept_proposed_router_owner. Reason: Unknown")

            self._on_fail("accept_proposed_router_owner", message)

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

class AddLiquidityMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addLiquidity method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addLiquidity")

    def validate_and_normalize_inputs(self, amount: int, local: str)->any:
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
            parameter_name='local',
            argument_value=local,
        )
        local = self.validate_and_checksum_address(local)
        return (amount, local)



    def block_send(self, amount: int, local: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, local)
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

    def send_transaction(self, amount: int, local: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, local) = self.validate_and_normalize_inputs(amount, local)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, local: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, local) = self.validate_and_normalize_inputs(amount, local)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, local: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, local) = self.validate_and_normalize_inputs(amount, local)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local).estimateGas(tx_params.as_dict())

class AddLiquidityForMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addLiquidityFor method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addLiquidityFor")

    def validate_and_normalize_inputs(self, amount: int, local: str, router: str)->any:
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
            parameter_name='local',
            argument_value=local,
        )
        local = self.validate_and_checksum_address(local)
        self.validator.assert_valid(
            method_name='addLiquidityFor',
            parameter_name='router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (amount, local, router)



    def block_send(self, amount: int, local: str, router: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, local, router)
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

    def send_transaction(self, amount: int, local: str, router: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, local, router) = self.validate_and_normalize_inputs(amount, local, router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local, router).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, local: str, router: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, local, router) = self.validate_and_normalize_inputs(amount, local, router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local, router).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, local: str, router: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, local, router) = self.validate_and_normalize_inputs(amount, local, router)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local, router).estimateGas(tx_params.as_dict())

class AddRelayerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addRelayer method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addRelayer")

    def validate_and_normalize_inputs(self, relayer: str)->any:
        """Validate the inputs to the addRelayer method."""
        self.validator.assert_valid(
            method_name='addRelayer',
            parameter_name='relayer',
            argument_value=relayer,
        )
        relayer = self.validate_and_checksum_address(relayer)
        return (relayer)



    def block_send(self, relayer: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(relayer)
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

                self._on_receipt_handle("add_relayer", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_relayer")
            message = f"Error {er}: add_relayer"
            self._on_fail("add_relayer", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_relayer: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_relayer. Reason: Unknown")

            self._on_fail("add_relayer", message)

    def send_transaction(self, relayer: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (relayer) = self.validate_and_normalize_inputs(relayer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(relayer).transact(tx_params.as_dict())

    def build_transaction(self, relayer: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (relayer) = self.validate_and_normalize_inputs(relayer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(relayer).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, relayer: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (relayer) = self.validate_and_normalize_inputs(relayer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(relayer).estimateGas(tx_params.as_dict())

class AddRelayerFeesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addRelayerFees method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addRelayerFees")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the addRelayerFees method."""
        self.validator.assert_valid(
            method_name='addRelayerFees',
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

                self._on_receipt_handle("add_relayer_fees", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_relayer_fees")
            message = f"Error {er}: add_relayer_fees"
            self._on_fail("add_relayer_fees", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_relayer_fees: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_relayer_fees. Reason: Unknown")

            self._on_fail("add_relayer_fees", message)

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

class AddStableSwapPoolMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addStableSwapPool method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addStableSwapPool")

    def validate_and_normalize_inputs(self, canonical: BridgeMessageTokenId, stable_swap_pool: str)->any:
        """Validate the inputs to the addStableSwapPool method."""
        self.validator.assert_valid(
            method_name='addStableSwapPool',
            parameter_name='canonical',
            argument_value=canonical,
        )
        self.validator.assert_valid(
            method_name='addStableSwapPool',
            parameter_name='stableSwapPool',
            argument_value=stable_swap_pool,
        )
        stable_swap_pool = self.validate_and_checksum_address(stable_swap_pool)
        return (canonical, stable_swap_pool)



    def block_send(self, canonical: BridgeMessageTokenId, stable_swap_pool: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(canonical, stable_swap_pool)
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

                self._on_receipt_handle("add_stable_swap_pool", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_stable_swap_pool")
            message = f"Error {er}: add_stable_swap_pool"
            self._on_fail("add_stable_swap_pool", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_stable_swap_pool: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_stable_swap_pool. Reason: Unknown")

            self._on_fail("add_stable_swap_pool", message)

    def send_transaction(self, canonical: BridgeMessageTokenId, stable_swap_pool: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (canonical, stable_swap_pool) = self.validate_and_normalize_inputs(canonical, stable_swap_pool)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical, stable_swap_pool).transact(tx_params.as_dict())

    def build_transaction(self, canonical: BridgeMessageTokenId, stable_swap_pool: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (canonical, stable_swap_pool) = self.validate_and_normalize_inputs(canonical, stable_swap_pool)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical, stable_swap_pool).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, canonical: BridgeMessageTokenId, stable_swap_pool: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (canonical, stable_swap_pool) = self.validate_and_normalize_inputs(canonical, stable_swap_pool)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical, stable_swap_pool).estimateGas(tx_params.as_dict())

class AdoptedToCanonicalMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the adoptedToCanonical method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("adoptedToCanonical")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the adoptedToCanonical method."""
        self.validator.assert_valid(
            method_name='adoptedToCanonical',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> Tuple[int, Union[bytes, str]]:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return (returned[0],returned[1],)
    def block_send(self, index_0: str,_valeth:int=0) -> Tuple[int, Union[bytes, str]]:
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

                self._on_receipt_handle("adopted_to_canonical", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: adopted_to_canonical")
            message = f"Error {er}: adopted_to_canonical"
            self._on_fail("adopted_to_canonical", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, adopted_to_canonical: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, adopted_to_canonical. Reason: Unknown")

            self._on_fail("adopted_to_canonical", message)

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

class AdoptedToLocalPoolsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the adoptedToLocalPools method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("adoptedToLocalPools")

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str])->any:
        """Validate the inputs to the adoptedToLocalPools method."""
        self.validator.assert_valid(
            method_name='adoptedToLocalPools',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)



    def block_call(self,index_0: Union[bytes, str], debug:bool=False) -> str:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, index_0: Union[bytes, str],_valeth:int=0) -> str:
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

                self._on_receipt_handle("adopted_to_local_pools", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: adopted_to_local_pools")
            message = f"Error {er}: adopted_to_local_pools"
            self._on_fail("adopted_to_local_pools", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, adopted_to_local_pools: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, adopted_to_local_pools. Reason: Unknown")

            self._on_fail("adopted_to_local_pools", message)

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

class ApprovedAssetsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approvedAssets method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("approvedAssets")

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str])->any:
        """Validate the inputs to the approvedAssets method."""
        self.validator.assert_valid(
            method_name='approvedAssets',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)



    def block_call(self,index_0: Union[bytes, str], debug:bool=False) -> bool:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, index_0: Union[bytes, str],_valeth:int=0) -> bool:
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

class ApprovedRelayersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approvedRelayers method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("approvedRelayers")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the approvedRelayers method."""
        self.validator.assert_valid(
            method_name='approvedRelayers',
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

                self._on_receipt_handle("approved_relayers", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: approved_relayers")
            message = f"Error {er}: approved_relayers"
            self._on_fail("approved_relayers", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approved_relayers: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approved_relayers. Reason: Unknown")

            self._on_fail("approved_relayers", message)

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

    def validate_and_normalize_inputs(self, approved: str)->any:
        """Validate the inputs to the approvedRouters method."""
        self.validator.assert_valid(
            method_name='approvedRouters',
            parameter_name='_approved',
            argument_value=approved,
        )
        approved = self.validate_and_checksum_address(approved)
        return (approved)



    def block_call(self,approved: str, debug:bool=False) -> bool:
        _fn = self._underlying_method(approved)
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, approved: str,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(approved)
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

    def send_transaction(self, approved: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (approved) = self.validate_and_normalize_inputs(approved)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(approved).transact(tx_params.as_dict())

    def build_transaction(self, approved: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (approved) = self.validate_and_normalize_inputs(approved)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(approved).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, approved: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (approved) = self.validate_and_normalize_inputs(approved)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(approved).estimateGas(tx_params.as_dict())

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

class BridgeRouterMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the bridgeRouter method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("bridgeRouter")



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

                self._on_receipt_handle("bridge_router", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: bridge_router")
            message = f"Error {er}: bridge_router"
            self._on_fail("bridge_router", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, bridge_router: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, bridge_router. Reason: Unknown")

            self._on_fail("bridge_router", message)

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

class CanonicalToAdoptedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the canonicalToAdopted method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("canonicalToAdopted")

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str])->any:
        """Validate the inputs to the canonicalToAdopted method."""
        self.validator.assert_valid(
            method_name='canonicalToAdopted',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)



    def block_call(self,index_0: Union[bytes, str], debug:bool=False) -> str:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, index_0: Union[bytes, str],_valeth:int=0) -> str:
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

                self._on_receipt_handle("canonical_to_adopted", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: canonical_to_adopted")
            message = f"Error {er}: canonical_to_adopted"
            self._on_fail("canonical_to_adopted", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, canonical_to_adopted: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, canonical_to_adopted. Reason: Unknown")

            self._on_fail("canonical_to_adopted", message)

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

class DomainMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the domain method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("domain")



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

                self._on_receipt_handle("domain", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: domain")
            message = f"Error {er}: domain"
            self._on_fail("domain", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, domain: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, domain. Reason: Unknown")

            self._on_fail("domain", message)

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

class ExecuteMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the execute method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("execute")

    def validate_and_normalize_inputs(self, args: IConnextExecuteArgs)->any:
        """Validate the inputs to the execute method."""
        self.validator.assert_valid(
            method_name='execute',
            parameter_name='_args',
            argument_value=args,
        )
        return (args)



    def block_send(self, args: IConnextExecuteArgs,_valeth:int=0) -> Union[bytes, str]:
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

                self._on_receipt_handle("execute", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: execute")
            message = f"Error {er}: execute"
            self._on_fail("execute", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, execute: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, execute. Reason: Unknown")

            self._on_fail("execute", message)

    def send_transaction(self, args: IConnextExecuteArgs, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).transact(tx_params.as_dict())

    def build_transaction(self, args: IConnextExecuteArgs, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: IConnextExecuteArgs, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).estimateGas(tx_params.as_dict())

class ExecutorMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the executor method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("executor")



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

                self._on_receipt_handle("executor", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: executor")
            message = f"Error {er}: executor"
            self._on_fail("executor", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, executor: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, executor. Reason: Unknown")

            self._on_fail("executor", message)

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

class InitializeMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the initialize method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("initialize")

    def validate_and_normalize_inputs(self, domain: int, bridge_router: str, token_registry: str, wrapped_native: str)->any:
        """Validate the inputs to the initialize method."""
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_domain',
            argument_value=domain,
        )
        # safeguard against fractional inputs
        domain = int(domain)
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_bridgeRouter',
            argument_value=bridge_router,
        )
        bridge_router = self.validate_and_checksum_address(bridge_router)
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_tokenRegistry',
            argument_value=token_registry,
        )
        token_registry = self.validate_and_checksum_address(token_registry)
        self.validator.assert_valid(
            method_name='initialize',
            parameter_name='_wrappedNative',
            argument_value=wrapped_native,
        )
        wrapped_native = self.validate_and_checksum_address(wrapped_native)
        return (domain, bridge_router, token_registry, wrapped_native)



    def block_send(self, domain: int, bridge_router: str, token_registry: str, wrapped_native: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(domain, bridge_router, token_registry, wrapped_native)
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

                self._on_receipt_handle("initialize", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: initialize")
            message = f"Error {er}: initialize"
            self._on_fail("initialize", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, initialize: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, initialize. Reason: Unknown")

            self._on_fail("initialize", message)

    def send_transaction(self, domain: int, bridge_router: str, token_registry: str, wrapped_native: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (domain, bridge_router, token_registry, wrapped_native) = self.validate_and_normalize_inputs(domain, bridge_router, token_registry, wrapped_native)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(domain, bridge_router, token_registry, wrapped_native).transact(tx_params.as_dict())

    def build_transaction(self, domain: int, bridge_router: str, token_registry: str, wrapped_native: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (domain, bridge_router, token_registry, wrapped_native) = self.validate_and_normalize_inputs(domain, bridge_router, token_registry, wrapped_native)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(domain, bridge_router, token_registry, wrapped_native).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, domain: int, bridge_router: str, token_registry: str, wrapped_native: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (domain, bridge_router, token_registry, wrapped_native) = self.validate_and_normalize_inputs(domain, bridge_router, token_registry, wrapped_native)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(domain, bridge_router, token_registry, wrapped_native).estimateGas(tx_params.as_dict())

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

class MaxRoutersPerTransferMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the maxRoutersPerTransfer method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("maxRoutersPerTransfer")



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

                self._on_receipt_handle("max_routers_per_transfer", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: max_routers_per_transfer")
            message = f"Error {er}: max_routers_per_transfer"
            self._on_fail("max_routers_per_transfer", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, max_routers_per_transfer: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, max_routers_per_transfer. Reason: Unknown")

            self._on_fail("max_routers_per_transfer", message)

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

class NonceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the nonce method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("nonce")



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

                self._on_receipt_handle("nonce", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: nonce")
            message = f"Error {er}: nonce"
            self._on_fail("nonce", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, nonce: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, nonce. Reason: Unknown")

            self._on_fail("nonce", message)

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

class ProposeRouterOwnerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposeRouterOwner method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposeRouterOwner")

    def validate_and_normalize_inputs(self, router: str, proposed: str)->any:
        """Validate the inputs to the proposeRouterOwner method."""
        self.validator.assert_valid(
            method_name='proposeRouterOwner',
            parameter_name='router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        self.validator.assert_valid(
            method_name='proposeRouterOwner',
            parameter_name='proposed',
            argument_value=proposed,
        )
        proposed = self.validate_and_checksum_address(proposed)
        return (router, proposed)



    def block_send(self, router: str, proposed: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(router, proposed)
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

                self._on_receipt_handle("propose_router_owner", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: propose_router_owner")
            message = f"Error {er}: propose_router_owner"
            self._on_fail("propose_router_owner", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_router_owner: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, propose_router_owner. Reason: Unknown")

            self._on_fail("propose_router_owner", message)

    def send_transaction(self, router: str, proposed: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (router, proposed) = self.validate_and_normalize_inputs(router, proposed)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, proposed).transact(tx_params.as_dict())

    def build_transaction(self, router: str, proposed: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (router, proposed) = self.validate_and_normalize_inputs(router, proposed)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, proposed).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, router: str, proposed: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (router, proposed) = self.validate_and_normalize_inputs(router, proposed)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, proposed).estimateGas(tx_params.as_dict())

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

class ProposedRouterOwnersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposedRouterOwners method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposedRouterOwners")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the proposedRouterOwners method."""
        self.validator.assert_valid(
            method_name='proposedRouterOwners',
            parameter_name='_router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (router)



    def block_call(self,router: str, debug:bool=False) -> str:
        _fn = self._underlying_method(router)
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, router: str,_valeth:int=0) -> str:
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

                self._on_receipt_handle("proposed_router_owners", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: proposed_router_owners")
            message = f"Error {er}: proposed_router_owners"
            self._on_fail("proposed_router_owners", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed_router_owners: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed_router_owners. Reason: Unknown")

            self._on_fail("proposed_router_owners", message)

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

class ProposedRouterTimestampMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the proposedRouterTimestamp method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("proposedRouterTimestamp")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the proposedRouterTimestamp method."""
        self.validator.assert_valid(
            method_name='proposedRouterTimestamp',
            parameter_name='_router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (router)



    def block_call(self,router: str, debug:bool=False) -> int:
        _fn = self._underlying_method(router)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, router: str,_valeth:int=0) -> int:
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

                self._on_receipt_handle("proposed_router_timestamp", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: proposed_router_timestamp")
            message = f"Error {er}: proposed_router_timestamp"
            self._on_fail("proposed_router_timestamp", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed_router_timestamp: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, proposed_router_timestamp. Reason: Unknown")

            self._on_fail("proposed_router_timestamp", message)

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

class ReconcileMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the reconcile method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("reconcile")

    def validate_and_normalize_inputs(self, transfer_id: Union[bytes, str], origin: int, local: str, recipient: str, amount: int)->any:
        """Validate the inputs to the reconcile method."""
        self.validator.assert_valid(
            method_name='reconcile',
            parameter_name='_transferId',
            argument_value=transfer_id,
        )
        self.validator.assert_valid(
            method_name='reconcile',
            parameter_name='_origin',
            argument_value=origin,
        )
        self.validator.assert_valid(
            method_name='reconcile',
            parameter_name='_local',
            argument_value=local,
        )
        local = self.validate_and_checksum_address(local)
        self.validator.assert_valid(
            method_name='reconcile',
            parameter_name='_recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        self.validator.assert_valid(
            method_name='reconcile',
            parameter_name='_amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (transfer_id, origin, local, recipient, amount)



    def block_send(self, transfer_id: Union[bytes, str], origin: int, local: str, recipient: str, amount: int,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(transfer_id, origin, local, recipient, amount)
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

                self._on_receipt_handle("reconcile", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: reconcile")
            message = f"Error {er}: reconcile"
            self._on_fail("reconcile", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, reconcile: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, reconcile. Reason: Unknown")

            self._on_fail("reconcile", message)

    def send_transaction(self, transfer_id: Union[bytes, str], origin: int, local: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (transfer_id, origin, local, recipient, amount) = self.validate_and_normalize_inputs(transfer_id, origin, local, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transfer_id, origin, local, recipient, amount).transact(tx_params.as_dict())

    def build_transaction(self, transfer_id: Union[bytes, str], origin: int, local: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (transfer_id, origin, local, recipient, amount) = self.validate_and_normalize_inputs(transfer_id, origin, local, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transfer_id, origin, local, recipient, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, transfer_id: Union[bytes, str], origin: int, local: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (transfer_id, origin, local, recipient, amount) = self.validate_and_normalize_inputs(transfer_id, origin, local, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(transfer_id, origin, local, recipient, amount).estimateGas(tx_params.as_dict())

class ReconciledTransfersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the reconciledTransfers method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("reconciledTransfers")

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str])->any:
        """Validate the inputs to the reconciledTransfers method."""
        self.validator.assert_valid(
            method_name='reconciledTransfers',
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

                self._on_receipt_handle("reconciled_transfers", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: reconciled_transfers")
            message = f"Error {er}: reconciled_transfers"
            self._on_fail("reconciled_transfers", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, reconciled_transfers: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, reconciled_transfers. Reason: Unknown")

            self._on_fail("reconciled_transfers", message)

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

class RemoveAssetIdMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeAssetId method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeAssetId")

    def validate_and_normalize_inputs(self, canonical_id: Union[bytes, str], adopted_asset_id: str)->any:
        """Validate the inputs to the removeAssetId method."""
        self.validator.assert_valid(
            method_name='removeAssetId',
            parameter_name='canonicalId',
            argument_value=canonical_id,
        )
        self.validator.assert_valid(
            method_name='removeAssetId',
            parameter_name='adoptedAssetId',
            argument_value=adopted_asset_id,
        )
        adopted_asset_id = self.validate_and_checksum_address(adopted_asset_id)
        return (canonical_id, adopted_asset_id)



    def block_send(self, canonical_id: Union[bytes, str], adopted_asset_id: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(canonical_id, adopted_asset_id)
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

    def send_transaction(self, canonical_id: Union[bytes, str], adopted_asset_id: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (canonical_id, adopted_asset_id) = self.validate_and_normalize_inputs(canonical_id, adopted_asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical_id, adopted_asset_id).transact(tx_params.as_dict())

    def build_transaction(self, canonical_id: Union[bytes, str], adopted_asset_id: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (canonical_id, adopted_asset_id) = self.validate_and_normalize_inputs(canonical_id, adopted_asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical_id, adopted_asset_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, canonical_id: Union[bytes, str], adopted_asset_id: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (canonical_id, adopted_asset_id) = self.validate_and_normalize_inputs(canonical_id, adopted_asset_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical_id, adopted_asset_id).estimateGas(tx_params.as_dict())

class RemoveLiquidityMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeLiquidity method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeLiquidity")

    def validate_and_normalize_inputs(self, amount: int, local: str, to: str)->any:
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
            parameter_name='local',
            argument_value=local,
        )
        local = self.validate_and_checksum_address(local)
        self.validator.assert_valid(
            method_name='removeLiquidity',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        return (amount, local, to)



    def block_send(self, amount: int, local: str, to: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, local, to)
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

    def send_transaction(self, amount: int, local: str, to: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, local, to) = self.validate_and_normalize_inputs(amount, local, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local, to).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, local: str, to: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, local, to) = self.validate_and_normalize_inputs(amount, local, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local, to).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, local: str, to: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, local, to) = self.validate_and_normalize_inputs(amount, local, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, local, to).estimateGas(tx_params.as_dict())

class RemoveRelayerMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeRelayer method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeRelayer")

    def validate_and_normalize_inputs(self, relayer: str)->any:
        """Validate the inputs to the removeRelayer method."""
        self.validator.assert_valid(
            method_name='removeRelayer',
            parameter_name='relayer',
            argument_value=relayer,
        )
        relayer = self.validate_and_checksum_address(relayer)
        return (relayer)



    def block_send(self, relayer: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(relayer)
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

                self._on_receipt_handle("remove_relayer", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remove_relayer")
            message = f"Error {er}: remove_relayer"
            self._on_fail("remove_relayer", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_relayer: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_relayer. Reason: Unknown")

            self._on_fail("remove_relayer", message)

    def send_transaction(self, relayer: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (relayer) = self.validate_and_normalize_inputs(relayer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(relayer).transact(tx_params.as_dict())

    def build_transaction(self, relayer: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (relayer) = self.validate_and_normalize_inputs(relayer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(relayer).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, relayer: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (relayer) = self.validate_and_normalize_inputs(relayer)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(relayer).estimateGas(tx_params.as_dict())

class RemoveRelayerFeesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeRelayerFees method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeRelayerFees")

    def validate_and_normalize_inputs(self, amount: int, to: str)->any:
        """Validate the inputs to the removeRelayerFees method."""
        self.validator.assert_valid(
            method_name='removeRelayerFees',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        self.validator.assert_valid(
            method_name='removeRelayerFees',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        return (amount, to)



    def block_send(self, amount: int, to: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(amount, to)
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

                self._on_receipt_handle("remove_relayer_fees", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remove_relayer_fees")
            message = f"Error {er}: remove_relayer_fees"
            self._on_fail("remove_relayer_fees", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_relayer_fees: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_relayer_fees. Reason: Unknown")

            self._on_fail("remove_relayer_fees", message)

    def send_transaction(self, amount: int, to: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount, to) = self.validate_and_normalize_inputs(amount, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, to).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, to: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount, to) = self.validate_and_normalize_inputs(amount, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, to).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, to: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount, to) = self.validate_and_normalize_inputs(amount, to)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount, to).estimateGas(tx_params.as_dict())

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

class RoutedTransfersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routedTransfers method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routedTransfers")

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str])->any:
        """Validate the inputs to the routedTransfers method."""
        self.validator.assert_valid(
            method_name='routedTransfers',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)



    def block_call(self,index_0: Union[bytes, str], debug:bool=False) -> int:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, index_0: Union[bytes, str],_valeth:int=0) -> int:
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

                self._on_receipt_handle("routed_transfers", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: routed_transfers")
            message = f"Error {er}: routed_transfers"
            self._on_fail("routed_transfers", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, routed_transfers: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, routed_transfers. Reason: Unknown")

            self._on_fail("routed_transfers", message)

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

class RoutedTransfersGasMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routedTransfersGas method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routedTransfersGas")

    def validate_and_normalize_inputs(self, index_0: Union[bytes, str])->any:
        """Validate the inputs to the routedTransfersGas method."""
        self.validator.assert_valid(
            method_name='routedTransfersGas',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)



    def block_call(self,index_0: Union[bytes, str], debug:bool=False) -> Tuple[int, int]:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return (returned[0],returned[1],)
    def block_send(self, index_0: Union[bytes, str],_valeth:int=0) -> Tuple[int, int]:
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

                self._on_receipt_handle("routed_transfers_gas", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: routed_transfers_gas")
            message = f"Error {er}: routed_transfers_gas"
            self._on_fail("routed_transfers_gas", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, routed_transfers_gas: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, routed_transfers_gas. Reason: Unknown")

            self._on_fail("routed_transfers_gas", message)

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

class RouterOwnersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerOwners method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerOwners")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the routerOwners method."""
        self.validator.assert_valid(
            method_name='routerOwners',
            parameter_name='_router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (router)



    def block_call(self,router: str, debug:bool=False) -> str:
        _fn = self._underlying_method(router)
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, router: str,_valeth:int=0) -> str:
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

                self._on_receipt_handle("router_owners", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_owners")
            message = f"Error {er}: router_owners"
            self._on_fail("router_owners", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_owners: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_owners. Reason: Unknown")

            self._on_fail("router_owners", message)

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

class RouterRecipientsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerRecipients method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerRecipients")

    def validate_and_normalize_inputs(self, router: str)->any:
        """Validate the inputs to the routerRecipients method."""
        self.validator.assert_valid(
            method_name='routerRecipients',
            parameter_name='_router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        return (router)



    def block_call(self,router: str, debug:bool=False) -> str:
        _fn = self._underlying_method(router)
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, router: str,_valeth:int=0) -> str:
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

                self._on_receipt_handle("router_recipients", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_recipients")
            message = f"Error {er}: router_recipients"
            self._on_fail("router_recipients", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_recipients: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_recipients. Reason: Unknown")

            self._on_fail("router_recipients", message)

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

class RouterRelayerFeesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the routerRelayerFees method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("routerRelayerFees")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the routerRelayerFees method."""
        self.validator.assert_valid(
            method_name='routerRelayerFees',
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

                self._on_receipt_handle("router_relayer_fees", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: router_relayer_fees")
            message = f"Error {er}: router_relayer_fees"
            self._on_fail("router_relayer_fees", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_relayer_fees: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, router_relayer_fees. Reason: Unknown")

            self._on_fail("router_relayer_fees", message)

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

class SetMaxRoutersPerTransferMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setMaxRoutersPerTransfer method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setMaxRoutersPerTransfer")

    def validate_and_normalize_inputs(self, new_max_routers: int)->any:
        """Validate the inputs to the setMaxRoutersPerTransfer method."""
        self.validator.assert_valid(
            method_name='setMaxRoutersPerTransfer',
            parameter_name='newMaxRouters',
            argument_value=new_max_routers,
        )
        # safeguard against fractional inputs
        new_max_routers = int(new_max_routers)
        return (new_max_routers)



    def block_send(self, new_max_routers: int,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(new_max_routers)
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

                self._on_receipt_handle("set_max_routers_per_transfer", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_max_routers_per_transfer")
            message = f"Error {er}: set_max_routers_per_transfer"
            self._on_fail("set_max_routers_per_transfer", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_max_routers_per_transfer: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_max_routers_per_transfer. Reason: Unknown")

            self._on_fail("set_max_routers_per_transfer", message)

    def send_transaction(self, new_max_routers: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_max_routers) = self.validate_and_normalize_inputs(new_max_routers)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_max_routers).transact(tx_params.as_dict())

    def build_transaction(self, new_max_routers: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_max_routers) = self.validate_and_normalize_inputs(new_max_routers)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_max_routers).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, new_max_routers: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (new_max_routers) = self.validate_and_normalize_inputs(new_max_routers)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_max_routers).estimateGas(tx_params.as_dict())

class SetRouterRecipientMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setRouterRecipient method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setRouterRecipient")

    def validate_and_normalize_inputs(self, router: str, recipient: str)->any:
        """Validate the inputs to the setRouterRecipient method."""
        self.validator.assert_valid(
            method_name='setRouterRecipient',
            parameter_name='router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        self.validator.assert_valid(
            method_name='setRouterRecipient',
            parameter_name='recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (router, recipient)



    def block_send(self, router: str, recipient: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(router, recipient)
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

                self._on_receipt_handle("set_router_recipient", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_router_recipient")
            message = f"Error {er}: set_router_recipient"
            self._on_fail("set_router_recipient", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_router_recipient: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_router_recipient. Reason: Unknown")

            self._on_fail("set_router_recipient", message)

    def send_transaction(self, router: str, recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (router, recipient) = self.validate_and_normalize_inputs(router, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, recipient).transact(tx_params.as_dict())

    def build_transaction(self, router: str, recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (router, recipient) = self.validate_and_normalize_inputs(router, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, router: str, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (router, recipient) = self.validate_and_normalize_inputs(router, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, recipient).estimateGas(tx_params.as_dict())

class SetupAssetMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setupAsset method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setupAsset")

    def validate_and_normalize_inputs(self, canonical: BridgeMessageTokenId, adopted_asset_id: str, stable_swap_pool: str)->any:
        """Validate the inputs to the setupAsset method."""
        self.validator.assert_valid(
            method_name='setupAsset',
            parameter_name='canonical',
            argument_value=canonical,
        )
        self.validator.assert_valid(
            method_name='setupAsset',
            parameter_name='adoptedAssetId',
            argument_value=adopted_asset_id,
        )
        adopted_asset_id = self.validate_and_checksum_address(adopted_asset_id)
        self.validator.assert_valid(
            method_name='setupAsset',
            parameter_name='stableSwapPool',
            argument_value=stable_swap_pool,
        )
        stable_swap_pool = self.validate_and_checksum_address(stable_swap_pool)
        return (canonical, adopted_asset_id, stable_swap_pool)



    def block_send(self, canonical: BridgeMessageTokenId, adopted_asset_id: str, stable_swap_pool: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(canonical, adopted_asset_id, stable_swap_pool)
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

                self._on_receipt_handle("setup_asset", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: setup_asset")
            message = f"Error {er}: setup_asset"
            self._on_fail("setup_asset", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, setup_asset: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, setup_asset. Reason: Unknown")

            self._on_fail("setup_asset", message)

    def send_transaction(self, canonical: BridgeMessageTokenId, adopted_asset_id: str, stable_swap_pool: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (canonical, adopted_asset_id, stable_swap_pool) = self.validate_and_normalize_inputs(canonical, adopted_asset_id, stable_swap_pool)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical, adopted_asset_id, stable_swap_pool).transact(tx_params.as_dict())

    def build_transaction(self, canonical: BridgeMessageTokenId, adopted_asset_id: str, stable_swap_pool: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (canonical, adopted_asset_id, stable_swap_pool) = self.validate_and_normalize_inputs(canonical, adopted_asset_id, stable_swap_pool)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical, adopted_asset_id, stable_swap_pool).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, canonical: BridgeMessageTokenId, adopted_asset_id: str, stable_swap_pool: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (canonical, adopted_asset_id, stable_swap_pool) = self.validate_and_normalize_inputs(canonical, adopted_asset_id, stable_swap_pool)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(canonical, adopted_asset_id, stable_swap_pool).estimateGas(tx_params.as_dict())

class SetupRouterMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setupRouter method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setupRouter")

    def validate_and_normalize_inputs(self, router: str, owner: str, recipient: str)->any:
        """Validate the inputs to the setupRouter method."""
        self.validator.assert_valid(
            method_name='setupRouter',
            parameter_name='router',
            argument_value=router,
        )
        router = self.validate_and_checksum_address(router)
        self.validator.assert_valid(
            method_name='setupRouter',
            parameter_name='owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name='setupRouter',
            parameter_name='recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        return (router, owner, recipient)



    def block_send(self, router: str, owner: str, recipient: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(router, owner, recipient)
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

                self._on_receipt_handle("setup_router", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: setup_router")
            message = f"Error {er}: setup_router"
            self._on_fail("setup_router", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, setup_router: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, setup_router. Reason: Unknown")

            self._on_fail("setup_router", message)

    def send_transaction(self, router: str, owner: str, recipient: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (router, owner, recipient) = self.validate_and_normalize_inputs(router, owner, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, owner, recipient).transact(tx_params.as_dict())

    def build_transaction(self, router: str, owner: str, recipient: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (router, owner, recipient) = self.validate_and_normalize_inputs(router, owner, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, owner, recipient).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, router: str, owner: str, recipient: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (router, owner, recipient) = self.validate_and_normalize_inputs(router, owner, recipient)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(router, owner, recipient).estimateGas(tx_params.as_dict())

class TokenRegistryMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the tokenRegistry method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("tokenRegistry")



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

                self._on_receipt_handle("token_registry", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: token_registry")
            message = f"Error {er}: token_registry"
            self._on_fail("token_registry", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, token_registry: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, token_registry. Reason: Unknown")

            self._on_fail("token_registry", message)

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

class WrapperMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the wrapper method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("wrapper")



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

                self._on_receipt_handle("wrapper", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: wrapper")
            message = f"Error {er}: wrapper"
            self._on_fail("wrapper", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, wrapper: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, wrapper. Reason: Unknown")

            self._on_fail("wrapper", message)

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

class XcallMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the xcall method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("xcall")

    def validate_and_normalize_inputs(self, args: IConnextXCallArgs)->any:
        """Validate the inputs to the xcall method."""
        self.validator.assert_valid(
            method_name='xcall',
            parameter_name='_args',
            argument_value=args,
        )
        return (args)



    def block_send(self, args: IConnextXCallArgs,_valeth:int=0) -> Union[bytes, str]:
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

                self._on_receipt_handle("xcall", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: xcall")
            message = f"Error {er}: xcall"
            self._on_fail("xcall", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, xcall: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, xcall. Reason: Unknown")

            self._on_fail("xcall", message)

    def send_transaction(self, args: IConnextXCallArgs, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).transact(tx_params.as_dict())

    def build_transaction(self, args: IConnextXCallArgs, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, args: IConnextXCallArgs, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (args) = self.validate_and_normalize_inputs(args)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(args).estimateGas(tx_params.as_dict())

class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """
    def __init__(self, abi: any):
        super().__init__(abi)

    def accept_proposed_owner(self) -> str:
        return self._function_signatures["acceptProposedOwner"]
    def accept_proposed_router_owner(self) -> str:
        return self._function_signatures["acceptProposedRouterOwner"]
    def add_liquidity(self) -> str:
        return self._function_signatures["addLiquidity"]
    def add_liquidity_for(self) -> str:
        return self._function_signatures["addLiquidityFor"]
    def add_relayer(self) -> str:
        return self._function_signatures["addRelayer"]
    def add_relayer_fees(self) -> str:
        return self._function_signatures["addRelayerFees"]
    def add_stable_swap_pool(self) -> str:
        return self._function_signatures["addStableSwapPool"]
    def adopted_to_canonical(self) -> str:
        return self._function_signatures["adoptedToCanonical"]
    def adopted_to_local_pools(self) -> str:
        return self._function_signatures["adoptedToLocalPools"]
    def approved_assets(self) -> str:
        return self._function_signatures["approvedAssets"]
    def approved_relayers(self) -> str:
        return self._function_signatures["approvedRelayers"]
    def approved_routers(self) -> str:
        return self._function_signatures["approvedRouters"]
    def asset_ownership_timestamp(self) -> str:
        return self._function_signatures["assetOwnershipTimestamp"]
    def bridge_router(self) -> str:
        return self._function_signatures["bridgeRouter"]
    def canonical_to_adopted(self) -> str:
        return self._function_signatures["canonicalToAdopted"]
    def delay(self) -> str:
        return self._function_signatures["delay"]
    def domain(self) -> str:
        return self._function_signatures["domain"]
    def execute(self) -> str:
        return self._function_signatures["execute"]
    def executor(self) -> str:
        return self._function_signatures["executor"]
    def initialize(self) -> str:
        return self._function_signatures["initialize"]
    def is_asset_ownership_renounced(self) -> str:
        return self._function_signatures["isAssetOwnershipRenounced"]
    def is_router_ownership_renounced(self) -> str:
        return self._function_signatures["isRouterOwnershipRenounced"]
    def max_routers_per_transfer(self) -> str:
        return self._function_signatures["maxRoutersPerTransfer"]
    def nonce(self) -> str:
        return self._function_signatures["nonce"]
    def owner(self) -> str:
        return self._function_signatures["owner"]
    def propose_asset_ownership_renunciation(self) -> str:
        return self._function_signatures["proposeAssetOwnershipRenunciation"]
    def propose_new_owner(self) -> str:
        return self._function_signatures["proposeNewOwner"]
    def propose_router_owner(self) -> str:
        return self._function_signatures["proposeRouterOwner"]
    def propose_router_ownership_renunciation(self) -> str:
        return self._function_signatures["proposeRouterOwnershipRenunciation"]
    def proposed(self) -> str:
        return self._function_signatures["proposed"]
    def proposed_router_owners(self) -> str:
        return self._function_signatures["proposedRouterOwners"]
    def proposed_router_timestamp(self) -> str:
        return self._function_signatures["proposedRouterTimestamp"]
    def proposed_timestamp(self) -> str:
        return self._function_signatures["proposedTimestamp"]
    def reconcile(self) -> str:
        return self._function_signatures["reconcile"]
    def reconciled_transfers(self) -> str:
        return self._function_signatures["reconciledTransfers"]
    def remove_asset_id(self) -> str:
        return self._function_signatures["removeAssetId"]
    def remove_liquidity(self) -> str:
        return self._function_signatures["removeLiquidity"]
    def remove_relayer(self) -> str:
        return self._function_signatures["removeRelayer"]
    def remove_relayer_fees(self) -> str:
        return self._function_signatures["removeRelayerFees"]
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
    def routed_transfers(self) -> str:
        return self._function_signatures["routedTransfers"]
    def routed_transfers_gas(self) -> str:
        return self._function_signatures["routedTransfersGas"]
    def router_balances(self) -> str:
        return self._function_signatures["routerBalances"]
    def router_owners(self) -> str:
        return self._function_signatures["routerOwners"]
    def router_ownership_timestamp(self) -> str:
        return self._function_signatures["routerOwnershipTimestamp"]
    def router_recipients(self) -> str:
        return self._function_signatures["routerRecipients"]
    def router_relayer_fees(self) -> str:
        return self._function_signatures["routerRelayerFees"]
    def set_max_routers_per_transfer(self) -> str:
        return self._function_signatures["setMaxRoutersPerTransfer"]
    def set_router_recipient(self) -> str:
        return self._function_signatures["setRouterRecipient"]
    def setup_asset(self) -> str:
        return self._function_signatures["setupAsset"]
    def setup_router(self) -> str:
        return self._function_signatures["setupRouter"]
    def token_registry(self) -> str:
        return self._function_signatures["tokenRegistry"]
    def wrapper(self) -> str:
        return self._function_signatures["wrapper"]
    def xcall(self) -> str:
        return self._function_signatures["xcall"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Connext(ContractBase):
    """Wrapper class for Connext Solidity contract."""
    _fn_accept_proposed_owner: AcceptProposedOwnerMethod
    """Constructor-initialized instance of
    :class:`AcceptProposedOwnerMethod`.
    """

    _fn_accept_proposed_router_owner: AcceptProposedRouterOwnerMethod
    """Constructor-initialized instance of
    :class:`AcceptProposedRouterOwnerMethod`.
    """

    _fn_add_liquidity: AddLiquidityMethod
    """Constructor-initialized instance of
    :class:`AddLiquidityMethod`.
    """

    _fn_add_liquidity_for: AddLiquidityForMethod
    """Constructor-initialized instance of
    :class:`AddLiquidityForMethod`.
    """

    _fn_add_relayer: AddRelayerMethod
    """Constructor-initialized instance of
    :class:`AddRelayerMethod`.
    """

    _fn_add_relayer_fees: AddRelayerFeesMethod
    """Constructor-initialized instance of
    :class:`AddRelayerFeesMethod`.
    """

    _fn_add_stable_swap_pool: AddStableSwapPoolMethod
    """Constructor-initialized instance of
    :class:`AddStableSwapPoolMethod`.
    """

    _fn_adopted_to_canonical: AdoptedToCanonicalMethod
    """Constructor-initialized instance of
    :class:`AdoptedToCanonicalMethod`.
    """

    _fn_adopted_to_local_pools: AdoptedToLocalPoolsMethod
    """Constructor-initialized instance of
    :class:`AdoptedToLocalPoolsMethod`.
    """

    _fn_approved_assets: ApprovedAssetsMethod
    """Constructor-initialized instance of
    :class:`ApprovedAssetsMethod`.
    """

    _fn_approved_relayers: ApprovedRelayersMethod
    """Constructor-initialized instance of
    :class:`ApprovedRelayersMethod`.
    """

    _fn_approved_routers: ApprovedRoutersMethod
    """Constructor-initialized instance of
    :class:`ApprovedRoutersMethod`.
    """

    _fn_asset_ownership_timestamp: AssetOwnershipTimestampMethod
    """Constructor-initialized instance of
    :class:`AssetOwnershipTimestampMethod`.
    """

    _fn_bridge_router: BridgeRouterMethod
    """Constructor-initialized instance of
    :class:`BridgeRouterMethod`.
    """

    _fn_canonical_to_adopted: CanonicalToAdoptedMethod
    """Constructor-initialized instance of
    :class:`CanonicalToAdoptedMethod`.
    """

    _fn_delay: DelayMethod
    """Constructor-initialized instance of
    :class:`DelayMethod`.
    """

    _fn_domain: DomainMethod
    """Constructor-initialized instance of
    :class:`DomainMethod`.
    """

    _fn_execute: ExecuteMethod
    """Constructor-initialized instance of
    :class:`ExecuteMethod`.
    """

    _fn_executor: ExecutorMethod
    """Constructor-initialized instance of
    :class:`ExecutorMethod`.
    """

    _fn_initialize: InitializeMethod
    """Constructor-initialized instance of
    :class:`InitializeMethod`.
    """

    _fn_is_asset_ownership_renounced: IsAssetOwnershipRenouncedMethod
    """Constructor-initialized instance of
    :class:`IsAssetOwnershipRenouncedMethod`.
    """

    _fn_is_router_ownership_renounced: IsRouterOwnershipRenouncedMethod
    """Constructor-initialized instance of
    :class:`IsRouterOwnershipRenouncedMethod`.
    """

    _fn_max_routers_per_transfer: MaxRoutersPerTransferMethod
    """Constructor-initialized instance of
    :class:`MaxRoutersPerTransferMethod`.
    """

    _fn_nonce: NonceMethod
    """Constructor-initialized instance of
    :class:`NonceMethod`.
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

    _fn_propose_router_owner: ProposeRouterOwnerMethod
    """Constructor-initialized instance of
    :class:`ProposeRouterOwnerMethod`.
    """

    _fn_propose_router_ownership_renunciation: ProposeRouterOwnershipRenunciationMethod
    """Constructor-initialized instance of
    :class:`ProposeRouterOwnershipRenunciationMethod`.
    """

    _fn_proposed: ProposedMethod
    """Constructor-initialized instance of
    :class:`ProposedMethod`.
    """

    _fn_proposed_router_owners: ProposedRouterOwnersMethod
    """Constructor-initialized instance of
    :class:`ProposedRouterOwnersMethod`.
    """

    _fn_proposed_router_timestamp: ProposedRouterTimestampMethod
    """Constructor-initialized instance of
    :class:`ProposedRouterTimestampMethod`.
    """

    _fn_proposed_timestamp: ProposedTimestampMethod
    """Constructor-initialized instance of
    :class:`ProposedTimestampMethod`.
    """

    _fn_reconcile: ReconcileMethod
    """Constructor-initialized instance of
    :class:`ReconcileMethod`.
    """

    _fn_reconciled_transfers: ReconciledTransfersMethod
    """Constructor-initialized instance of
    :class:`ReconciledTransfersMethod`.
    """

    _fn_remove_asset_id: RemoveAssetIdMethod
    """Constructor-initialized instance of
    :class:`RemoveAssetIdMethod`.
    """

    _fn_remove_liquidity: RemoveLiquidityMethod
    """Constructor-initialized instance of
    :class:`RemoveLiquidityMethod`.
    """

    _fn_remove_relayer: RemoveRelayerMethod
    """Constructor-initialized instance of
    :class:`RemoveRelayerMethod`.
    """

    _fn_remove_relayer_fees: RemoveRelayerFeesMethod
    """Constructor-initialized instance of
    :class:`RemoveRelayerFeesMethod`.
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

    _fn_routed_transfers: RoutedTransfersMethod
    """Constructor-initialized instance of
    :class:`RoutedTransfersMethod`.
    """

    _fn_routed_transfers_gas: RoutedTransfersGasMethod
    """Constructor-initialized instance of
    :class:`RoutedTransfersGasMethod`.
    """

    _fn_router_balances: RouterBalancesMethod
    """Constructor-initialized instance of
    :class:`RouterBalancesMethod`.
    """

    _fn_router_owners: RouterOwnersMethod
    """Constructor-initialized instance of
    :class:`RouterOwnersMethod`.
    """

    _fn_router_ownership_timestamp: RouterOwnershipTimestampMethod
    """Constructor-initialized instance of
    :class:`RouterOwnershipTimestampMethod`.
    """

    _fn_router_recipients: RouterRecipientsMethod
    """Constructor-initialized instance of
    :class:`RouterRecipientsMethod`.
    """

    _fn_router_relayer_fees: RouterRelayerFeesMethod
    """Constructor-initialized instance of
    :class:`RouterRelayerFeesMethod`.
    """

    _fn_set_max_routers_per_transfer: SetMaxRoutersPerTransferMethod
    """Constructor-initialized instance of
    :class:`SetMaxRoutersPerTransferMethod`.
    """

    _fn_set_router_recipient: SetRouterRecipientMethod
    """Constructor-initialized instance of
    :class:`SetRouterRecipientMethod`.
    """

    _fn_setup_asset: SetupAssetMethod
    """Constructor-initialized instance of
    :class:`SetupAssetMethod`.
    """

    _fn_setup_router: SetupRouterMethod
    """Constructor-initialized instance of
    :class:`SetupRouterMethod`.
    """

    _fn_token_registry: TokenRegistryMethod
    """Constructor-initialized instance of
    :class:`TokenRegistryMethod`.
    """

    _fn_wrapper: WrapperMethod
    """Constructor-initialized instance of
    :class:`WrapperMethod`.
    """

    _fn_xcall: XcallMethod
    """Constructor-initialized instance of
    :class:`XcallMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: ConnextValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, Connext.abi())
        web3 = core_lib.w3

        if not validator:
            validator = ConnextValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=Connext.abi()).functions
        self._signatures = SignatureGenerator(Connext.abi())
        validator.bindSignatures(self._signatures)

        self._fn_accept_proposed_owner = AcceptProposedOwnerMethod(core_lib, contract_address, functions.acceptProposedOwner, validator)
        self._fn_accept_proposed_router_owner = AcceptProposedRouterOwnerMethod(core_lib, contract_address, functions.acceptProposedRouterOwner, validator)
        self._fn_add_liquidity = AddLiquidityMethod(core_lib, contract_address, functions.addLiquidity, validator)
        self._fn_add_liquidity_for = AddLiquidityForMethod(core_lib, contract_address, functions.addLiquidityFor, validator)
        self._fn_add_relayer = AddRelayerMethod(core_lib, contract_address, functions.addRelayer, validator)
        self._fn_add_relayer_fees = AddRelayerFeesMethod(core_lib, contract_address, functions.addRelayerFees, validator)
        self._fn_add_stable_swap_pool = AddStableSwapPoolMethod(core_lib, contract_address, functions.addStableSwapPool, validator)
        self._fn_adopted_to_canonical = AdoptedToCanonicalMethod(core_lib, contract_address, functions.adoptedToCanonical, validator)
        self._fn_adopted_to_local_pools = AdoptedToLocalPoolsMethod(core_lib, contract_address, functions.adoptedToLocalPools, validator)
        self._fn_approved_assets = ApprovedAssetsMethod(core_lib, contract_address, functions.approvedAssets, validator)
        self._fn_approved_relayers = ApprovedRelayersMethod(core_lib, contract_address, functions.approvedRelayers, validator)
        self._fn_approved_routers = ApprovedRoutersMethod(core_lib, contract_address, functions.approvedRouters, validator)
        self._fn_asset_ownership_timestamp = AssetOwnershipTimestampMethod(core_lib, contract_address, functions.assetOwnershipTimestamp, validator)
        self._fn_bridge_router = BridgeRouterMethod(core_lib, contract_address, functions.bridgeRouter, validator)
        self._fn_canonical_to_adopted = CanonicalToAdoptedMethod(core_lib, contract_address, functions.canonicalToAdopted, validator)
        self._fn_delay = DelayMethod(core_lib, contract_address, functions.delay, validator)
        self._fn_domain = DomainMethod(core_lib, contract_address, functions.domain, validator)
        self._fn_execute = ExecuteMethod(core_lib, contract_address, functions.execute, validator)
        self._fn_executor = ExecutorMethod(core_lib, contract_address, functions.executor, validator)
        self._fn_initialize = InitializeMethod(core_lib, contract_address, functions.initialize, validator)
        self._fn_is_asset_ownership_renounced = IsAssetOwnershipRenouncedMethod(core_lib, contract_address, functions.isAssetOwnershipRenounced, validator)
        self._fn_is_router_ownership_renounced = IsRouterOwnershipRenouncedMethod(core_lib, contract_address, functions.isRouterOwnershipRenounced, validator)
        self._fn_max_routers_per_transfer = MaxRoutersPerTransferMethod(core_lib, contract_address, functions.maxRoutersPerTransfer, validator)
        self._fn_nonce = NonceMethod(core_lib, contract_address, functions.nonce, validator)
        self._fn_owner = OwnerMethod(core_lib, contract_address, functions.owner, validator)
        self._fn_propose_asset_ownership_renunciation = ProposeAssetOwnershipRenunciationMethod(core_lib, contract_address, functions.proposeAssetOwnershipRenunciation, validator)
        self._fn_propose_new_owner = ProposeNewOwnerMethod(core_lib, contract_address, functions.proposeNewOwner, validator)
        self._fn_propose_router_owner = ProposeRouterOwnerMethod(core_lib, contract_address, functions.proposeRouterOwner, validator)
        self._fn_propose_router_ownership_renunciation = ProposeRouterOwnershipRenunciationMethod(core_lib, contract_address, functions.proposeRouterOwnershipRenunciation, validator)
        self._fn_proposed = ProposedMethod(core_lib, contract_address, functions.proposed, validator)
        self._fn_proposed_router_owners = ProposedRouterOwnersMethod(core_lib, contract_address, functions.proposedRouterOwners, validator)
        self._fn_proposed_router_timestamp = ProposedRouterTimestampMethod(core_lib, contract_address, functions.proposedRouterTimestamp, validator)
        self._fn_proposed_timestamp = ProposedTimestampMethod(core_lib, contract_address, functions.proposedTimestamp, validator)
        self._fn_reconcile = ReconcileMethod(core_lib, contract_address, functions.reconcile, validator)
        self._fn_reconciled_transfers = ReconciledTransfersMethod(core_lib, contract_address, functions.reconciledTransfers, validator)
        self._fn_remove_asset_id = RemoveAssetIdMethod(core_lib, contract_address, functions.removeAssetId, validator)
        self._fn_remove_liquidity = RemoveLiquidityMethod(core_lib, contract_address, functions.removeLiquidity, validator)
        self._fn_remove_relayer = RemoveRelayerMethod(core_lib, contract_address, functions.removeRelayer, validator)
        self._fn_remove_relayer_fees = RemoveRelayerFeesMethod(core_lib, contract_address, functions.removeRelayerFees, validator)
        self._fn_remove_router = RemoveRouterMethod(core_lib, contract_address, functions.removeRouter, validator)
        self._fn_renounce_asset_ownership = RenounceAssetOwnershipMethod(core_lib, contract_address, functions.renounceAssetOwnership, validator)
        self._fn_renounce_ownership = RenounceOwnershipMethod(core_lib, contract_address, functions.renounceOwnership, validator)
        self._fn_renounce_router_ownership = RenounceRouterOwnershipMethod(core_lib, contract_address, functions.renounceRouterOwnership, validator)
        self._fn_renounced = RenouncedMethod(core_lib, contract_address, functions.renounced, validator)
        self._fn_routed_transfers = RoutedTransfersMethod(core_lib, contract_address, functions.routedTransfers, validator)
        self._fn_routed_transfers_gas = RoutedTransfersGasMethod(core_lib, contract_address, functions.routedTransfersGas, validator)
        self._fn_router_balances = RouterBalancesMethod(core_lib, contract_address, functions.routerBalances, validator)
        self._fn_router_owners = RouterOwnersMethod(core_lib, contract_address, functions.routerOwners, validator)
        self._fn_router_ownership_timestamp = RouterOwnershipTimestampMethod(core_lib, contract_address, functions.routerOwnershipTimestamp, validator)
        self._fn_router_recipients = RouterRecipientsMethod(core_lib, contract_address, functions.routerRecipients, validator)
        self._fn_router_relayer_fees = RouterRelayerFeesMethod(core_lib, contract_address, functions.routerRelayerFees, validator)
        self._fn_set_max_routers_per_transfer = SetMaxRoutersPerTransferMethod(core_lib, contract_address, functions.setMaxRoutersPerTransfer, validator)
        self._fn_set_router_recipient = SetRouterRecipientMethod(core_lib, contract_address, functions.setRouterRecipient, validator)
        self._fn_setup_asset = SetupAssetMethod(core_lib, contract_address, functions.setupAsset, validator)
        self._fn_setup_router = SetupRouterMethod(core_lib, contract_address, functions.setupRouter, validator)
        self._fn_token_registry = TokenRegistryMethod(core_lib, contract_address, functions.tokenRegistry, validator)
        self._fn_wrapper = WrapperMethod(core_lib, contract_address, functions.wrapper, validator)
        self._fn_xcall = XcallMethod(core_lib, contract_address, functions.xcall, validator)

    
    
    def event_asset_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_added in contract Connext
        Get log entry for AssetAdded event.
                :param tx_hash: hash of transaction emitting AssetAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.AssetAdded().processReceipt(tx_receipt)
    
    
    def event_asset_ownership_renounced(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_ownership_renounced in contract Connext
        Get log entry for AssetOwnershipRenounced event.
                :param tx_hash: hash of transaction emitting AssetOwnershipRenounced
                event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.AssetOwnershipRenounced().processReceipt(tx_receipt)
    
    
    def event_asset_ownership_renunciation_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_ownership_renunciation_proposed in contract Connext
        Get log entry for AssetOwnershipRenunciationProposed event.
                :param tx_hash: hash of transaction emitting
                AssetOwnershipRenunciationProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.AssetOwnershipRenunciationProposed().processReceipt(tx_receipt)
    
    
    def event_asset_removed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event asset_removed in contract Connext
        Get log entry for AssetRemoved event.
                :param tx_hash: hash of transaction emitting AssetRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.AssetRemoved().processReceipt(tx_receipt)
    
    
    def event_executed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event executed in contract Connext
        Get log entry for Executed event.
                :param tx_hash: hash of transaction emitting Executed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.Executed().processReceipt(tx_receipt)
    
    
    def event_initialized(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event initialized in contract Connext
        Get log entry for Initialized event.
                :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.Initialized().processReceipt(tx_receipt)
    
    
    def event_liquidity_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event liquidity_added in contract Connext
        Get log entry for LiquidityAdded event.
                :param tx_hash: hash of transaction emitting LiquidityAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.LiquidityAdded().processReceipt(tx_receipt)
    
    
    def event_liquidity_removed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event liquidity_removed in contract Connext
        Get log entry for LiquidityRemoved event.
                :param tx_hash: hash of transaction emitting LiquidityRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.LiquidityRemoved().processReceipt(tx_receipt)
    
    
    def event_max_routers_per_transfer_updated(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event max_routers_per_transfer_updated in contract Connext
        Get log entry for MaxRoutersPerTransferUpdated event.
                :param tx_hash: hash of transaction emitting
                MaxRoutersPerTransferUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.MaxRoutersPerTransferUpdated().processReceipt(tx_receipt)
    
    
    def event_ownership_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_proposed in contract Connext
        Get log entry for OwnershipProposed event.
                :param tx_hash: hash of transaction emitting OwnershipProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.OwnershipProposed().processReceipt(tx_receipt)
    
    
    def event_ownership_transferred(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event ownership_transferred in contract Connext
        Get log entry for OwnershipTransferred event.
                :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.OwnershipTransferred().processReceipt(tx_receipt)
    
    
    def event_reconciled(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event reconciled in contract Connext
        Get log entry for Reconciled event.
                :param tx_hash: hash of transaction emitting Reconciled event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.Reconciled().processReceipt(tx_receipt)
    
    
    def event_relayer_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event relayer_added in contract Connext
        Get log entry for RelayerAdded event.
                :param tx_hash: hash of transaction emitting RelayerAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.RelayerAdded().processReceipt(tx_receipt)
    
    
    def event_relayer_removed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event relayer_removed in contract Connext
        Get log entry for RelayerRemoved event.
                :param tx_hash: hash of transaction emitting RelayerRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.RelayerRemoved().processReceipt(tx_receipt)
    
    
    def event_router_ownership_renounced(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_ownership_renounced in contract Connext
        Get log entry for RouterOwnershipRenounced event.
                :param tx_hash: hash of transaction emitting RouterOwnershipRenounced
                event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.RouterOwnershipRenounced().processReceipt(tx_receipt)
    
    
    def event_router_ownership_renunciation_proposed(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event router_ownership_renunciation_proposed in contract Connext
        Get log entry for RouterOwnershipRenunciationProposed event.
                :param tx_hash: hash of transaction emitting
                RouterOwnershipRenunciationProposed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.RouterOwnershipRenunciationProposed().processReceipt(tx_receipt)
    
    
    def event_stable_swap_added(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event stable_swap_added in contract Connext
        Get log entry for StableSwapAdded event.
                :param tx_hash: hash of transaction emitting StableSwapAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.StableSwapAdded().processReceipt(tx_receipt)
    
    
    def event_x_called(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event x_called in contract Connext
        Get log entry for XCalled event.
                :param tx_hash: hash of transaction emitting XCalled event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=Connext.abi()).events.XCalled().processReceipt(tx_receipt)

    
    
    
    def accept_proposed_owner(self) -> None:
        """
        Implementation of accept_proposed_owner in contract Connext
        Method of the function
    
        """
    
        self._fn_accept_proposed_owner.callback_onfail = self._callback_onfail
        self._fn_accept_proposed_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_accept_proposed_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_accept_proposed_owner.gas_limit = self.call_contract_fee_amount
        self._fn_accept_proposed_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_accept_proposed_owner.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_accept_proposed_owner.block_send()
    
    
    
    
    
    
    
    def accept_proposed_router_owner(self, router: str) -> None:
        """
        Implementation of accept_proposed_router_owner in contract Connext
        Method of the function
    
        """
    
        self._fn_accept_proposed_router_owner.callback_onfail = self._callback_onfail
        self._fn_accept_proposed_router_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_accept_proposed_router_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_accept_proposed_router_owner.gas_limit = self.call_contract_fee_amount
        self._fn_accept_proposed_router_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_accept_proposed_router_owner.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_accept_proposed_router_owner.block_send(router)
    
    
    
    
    
    
    
    def add_liquidity(self, amount: int, local: str, wei:int=0) -> None:
        """
        Implementation of add_liquidity in contract Connext
        Method of the function
    
        """
    
        self._fn_add_liquidity.callback_onfail = self._callback_onfail
        self._fn_add_liquidity.callback_onsuccess = self._callback_onsuccess
        self._fn_add_liquidity.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_liquidity.gas_limit = self.call_contract_fee_amount
        self._fn_add_liquidity.gas_price_wei = self.call_contract_fee_price
        self._fn_add_liquidity.debug_method = self.call_contract_debug_flag
    
        self._fn_add_liquidity.wei_value = wei
    
    
        return self._fn_add_liquidity.block_send(amount, local, wei)
    
    
    
    
    
    
    def add_liquidity_for(self, amount: int, local: str, router: str, wei:int=0) -> None:
        """
        Implementation of add_liquidity_for in contract Connext
        Method of the function
    
        """
    
        self._fn_add_liquidity_for.callback_onfail = self._callback_onfail
        self._fn_add_liquidity_for.callback_onsuccess = self._callback_onsuccess
        self._fn_add_liquidity_for.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_liquidity_for.gas_limit = self.call_contract_fee_amount
        self._fn_add_liquidity_for.gas_price_wei = self.call_contract_fee_price
        self._fn_add_liquidity_for.debug_method = self.call_contract_debug_flag
    
        self._fn_add_liquidity_for.wei_value = wei
    
    
        return self._fn_add_liquidity_for.block_send(amount, local, router, wei)
    
    
    
    
    
    
    def add_relayer(self, relayer: str) -> None:
        """
        Implementation of add_relayer in contract Connext
        Method of the function
    
        """
    
        self._fn_add_relayer.callback_onfail = self._callback_onfail
        self._fn_add_relayer.callback_onsuccess = self._callback_onsuccess
        self._fn_add_relayer.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_relayer.gas_limit = self.call_contract_fee_amount
        self._fn_add_relayer.gas_price_wei = self.call_contract_fee_price
        self._fn_add_relayer.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_add_relayer.block_send(relayer)
    
    
    
    
    
    
    
    def add_relayer_fees(self, router: str, wei:int=0) -> None:
        """
        Implementation of add_relayer_fees in contract Connext
        Method of the function
    
        """
    
        self._fn_add_relayer_fees.callback_onfail = self._callback_onfail
        self._fn_add_relayer_fees.callback_onsuccess = self._callback_onsuccess
        self._fn_add_relayer_fees.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_relayer_fees.gas_limit = self.call_contract_fee_amount
        self._fn_add_relayer_fees.gas_price_wei = self.call_contract_fee_price
        self._fn_add_relayer_fees.debug_method = self.call_contract_debug_flag
    
        self._fn_add_relayer_fees.wei_value = wei
    
    
        return self._fn_add_relayer_fees.block_send(router, wei)
    
    
    
    
    
    
    def add_stable_swap_pool(self, canonical: BridgeMessageTokenId, stable_swap_pool: str) -> None:
        """
        Implementation of add_stable_swap_pool in contract Connext
        Method of the function
    
        """
    
        self._fn_add_stable_swap_pool.callback_onfail = self._callback_onfail
        self._fn_add_stable_swap_pool.callback_onsuccess = self._callback_onsuccess
        self._fn_add_stable_swap_pool.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_stable_swap_pool.gas_limit = self.call_contract_fee_amount
        self._fn_add_stable_swap_pool.gas_price_wei = self.call_contract_fee_price
        self._fn_add_stable_swap_pool.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_add_stable_swap_pool.block_send(canonical, stable_swap_pool)
    
    
    
    
    
    
    
    def adopted_to_canonical(self, index_0: str) -> Tuple[int, Union[bytes, str]]:
        """
        Implementation of adopted_to_canonical in contract Connext
        Method of the function
    
        """
    
        self._fn_adopted_to_canonical.callback_onfail = self._callback_onfail
        self._fn_adopted_to_canonical.callback_onsuccess = self._callback_onsuccess
        self._fn_adopted_to_canonical.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_adopted_to_canonical.gas_limit = self.call_contract_fee_amount
        self._fn_adopted_to_canonical.gas_price_wei = self.call_contract_fee_price
        self._fn_adopted_to_canonical.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_adopted_to_canonical.block_call(index_0)
    
    
    
    def adopted_to_local_pools(self, index_0: Union[bytes, str]) -> str:
        """
        Implementation of adopted_to_local_pools in contract Connext
        Method of the function
    
        """
    
        self._fn_adopted_to_local_pools.callback_onfail = self._callback_onfail
        self._fn_adopted_to_local_pools.callback_onsuccess = self._callback_onsuccess
        self._fn_adopted_to_local_pools.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_adopted_to_local_pools.gas_limit = self.call_contract_fee_amount
        self._fn_adopted_to_local_pools.gas_price_wei = self.call_contract_fee_price
        self._fn_adopted_to_local_pools.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_adopted_to_local_pools.block_call(index_0)
    
    
    
    def approved_assets(self, index_0: Union[bytes, str]) -> bool:
        """
        Implementation of approved_assets in contract Connext
        Method of the function
    
        """
    
        self._fn_approved_assets.callback_onfail = self._callback_onfail
        self._fn_approved_assets.callback_onsuccess = self._callback_onsuccess
        self._fn_approved_assets.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_approved_assets.gas_limit = self.call_contract_fee_amount
        self._fn_approved_assets.gas_price_wei = self.call_contract_fee_price
        self._fn_approved_assets.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_approved_assets.block_call(index_0)
    
    
    
    def approved_relayers(self, index_0: str) -> bool:
        """
        Implementation of approved_relayers in contract Connext
        Method of the function
    
        """
    
        self._fn_approved_relayers.callback_onfail = self._callback_onfail
        self._fn_approved_relayers.callback_onsuccess = self._callback_onsuccess
        self._fn_approved_relayers.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_approved_relayers.gas_limit = self.call_contract_fee_amount
        self._fn_approved_relayers.gas_price_wei = self.call_contract_fee_price
        self._fn_approved_relayers.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_approved_relayers.block_call(index_0)
    
    
    
    def approved_routers(self, approved: str) -> bool:
        """
        Implementation of approved_routers in contract Connext
        Method of the function
    
        """
    
        self._fn_approved_routers.callback_onfail = self._callback_onfail
        self._fn_approved_routers.callback_onsuccess = self._callback_onsuccess
        self._fn_approved_routers.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_approved_routers.gas_limit = self.call_contract_fee_amount
        self._fn_approved_routers.gas_price_wei = self.call_contract_fee_price
        self._fn_approved_routers.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_approved_routers.block_call(approved)
    
    
    
    def asset_ownership_timestamp(self) -> int:
        """
        Implementation of asset_ownership_timestamp in contract Connext
        Method of the function
    
        """
    
        self._fn_asset_ownership_timestamp.callback_onfail = self._callback_onfail
        self._fn_asset_ownership_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_asset_ownership_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_asset_ownership_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_asset_ownership_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_asset_ownership_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_asset_ownership_timestamp.block_call()
    
    
    
    def bridge_router(self) -> str:
        """
        Implementation of bridge_router in contract Connext
        Method of the function
    
        """
    
        self._fn_bridge_router.callback_onfail = self._callback_onfail
        self._fn_bridge_router.callback_onsuccess = self._callback_onsuccess
        self._fn_bridge_router.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_bridge_router.gas_limit = self.call_contract_fee_amount
        self._fn_bridge_router.gas_price_wei = self.call_contract_fee_price
        self._fn_bridge_router.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_bridge_router.block_call()
    
    
    
    def canonical_to_adopted(self, index_0: Union[bytes, str]) -> str:
        """
        Implementation of canonical_to_adopted in contract Connext
        Method of the function
    
        """
    
        self._fn_canonical_to_adopted.callback_onfail = self._callback_onfail
        self._fn_canonical_to_adopted.callback_onsuccess = self._callback_onsuccess
        self._fn_canonical_to_adopted.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_canonical_to_adopted.gas_limit = self.call_contract_fee_amount
        self._fn_canonical_to_adopted.gas_price_wei = self.call_contract_fee_price
        self._fn_canonical_to_adopted.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_canonical_to_adopted.block_call(index_0)
    
    
    
    def delay(self) -> int:
        """
        Implementation of delay in contract Connext
        Method of the function
    
        """
    
        self._fn_delay.callback_onfail = self._callback_onfail
        self._fn_delay.callback_onsuccess = self._callback_onsuccess
        self._fn_delay.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_delay.gas_limit = self.call_contract_fee_amount
        self._fn_delay.gas_price_wei = self.call_contract_fee_price
        self._fn_delay.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_delay.block_call()
    
    
    
    def domain(self) -> int:
        """
        Implementation of domain in contract Connext
        Method of the function
    
        """
    
        self._fn_domain.callback_onfail = self._callback_onfail
        self._fn_domain.callback_onsuccess = self._callback_onsuccess
        self._fn_domain.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_domain.gas_limit = self.call_contract_fee_amount
        self._fn_domain.gas_price_wei = self.call_contract_fee_price
        self._fn_domain.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_domain.block_call()
    
    
    
    def execute(self, args: IConnextExecuteArgs) -> Union[bytes, str]:
        """
        Implementation of execute in contract Connext
        Method of the function
    
        """
    
        self._fn_execute.callback_onfail = self._callback_onfail
        self._fn_execute.callback_onsuccess = self._callback_onsuccess
        self._fn_execute.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_execute.gas_limit = self.call_contract_fee_amount
        self._fn_execute.gas_price_wei = self.call_contract_fee_price
        self._fn_execute.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_execute.block_send(args)
    
    
    
    
    
    
    
    def executor(self) -> str:
        """
        Implementation of executor in contract Connext
        Method of the function
    
        """
    
        self._fn_executor.callback_onfail = self._callback_onfail
        self._fn_executor.callback_onsuccess = self._callback_onsuccess
        self._fn_executor.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_executor.gas_limit = self.call_contract_fee_amount
        self._fn_executor.gas_price_wei = self.call_contract_fee_price
        self._fn_executor.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_executor.block_call()
    
    
    
    def initialize(self, domain: int, bridge_router: str, token_registry: str, wrapped_native: str) -> None:
        """
        Implementation of initialize in contract Connext
        Method of the function
    
        """
    
        self._fn_initialize.callback_onfail = self._callback_onfail
        self._fn_initialize.callback_onsuccess = self._callback_onsuccess
        self._fn_initialize.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_initialize.gas_limit = self.call_contract_fee_amount
        self._fn_initialize.gas_price_wei = self.call_contract_fee_price
        self._fn_initialize.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_initialize.block_send(domain, bridge_router, token_registry, wrapped_native)
    
    
    
    
    
    
    
    def is_asset_ownership_renounced(self) -> bool:
        """
        Implementation of is_asset_ownership_renounced in contract Connext
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
        Implementation of is_router_ownership_renounced in contract Connext
        Method of the function
    
        """
    
        self._fn_is_router_ownership_renounced.callback_onfail = self._callback_onfail
        self._fn_is_router_ownership_renounced.callback_onsuccess = self._callback_onsuccess
        self._fn_is_router_ownership_renounced.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_is_router_ownership_renounced.gas_limit = self.call_contract_fee_amount
        self._fn_is_router_ownership_renounced.gas_price_wei = self.call_contract_fee_price
        self._fn_is_router_ownership_renounced.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_is_router_ownership_renounced.block_call()
    
    
    
    def max_routers_per_transfer(self) -> int:
        """
        Implementation of max_routers_per_transfer in contract Connext
        Method of the function
    
        """
    
        self._fn_max_routers_per_transfer.callback_onfail = self._callback_onfail
        self._fn_max_routers_per_transfer.callback_onsuccess = self._callback_onsuccess
        self._fn_max_routers_per_transfer.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_max_routers_per_transfer.gas_limit = self.call_contract_fee_amount
        self._fn_max_routers_per_transfer.gas_price_wei = self.call_contract_fee_price
        self._fn_max_routers_per_transfer.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_max_routers_per_transfer.block_call()
    
    
    
    def nonce(self) -> int:
        """
        Implementation of nonce in contract Connext
        Method of the function
    
        """
    
        self._fn_nonce.callback_onfail = self._callback_onfail
        self._fn_nonce.callback_onsuccess = self._callback_onsuccess
        self._fn_nonce.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_nonce.gas_limit = self.call_contract_fee_amount
        self._fn_nonce.gas_price_wei = self.call_contract_fee_price
        self._fn_nonce.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_nonce.block_call()
    
    
    
    def owner(self) -> str:
        """
        Implementation of owner in contract Connext
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
        Implementation of propose_asset_ownership_renunciation in contract Connext
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
        Implementation of propose_new_owner in contract Connext
        Method of the function
    
        """
    
        self._fn_propose_new_owner.callback_onfail = self._callback_onfail
        self._fn_propose_new_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_propose_new_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_propose_new_owner.gas_limit = self.call_contract_fee_amount
        self._fn_propose_new_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_propose_new_owner.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_propose_new_owner.block_send(newly_proposed)
    
    
    
    
    
    
    
    def propose_router_owner(self, router: str, proposed: str) -> None:
        """
        Implementation of propose_router_owner in contract Connext
        Method of the function
    
        """
    
        self._fn_propose_router_owner.callback_onfail = self._callback_onfail
        self._fn_propose_router_owner.callback_onsuccess = self._callback_onsuccess
        self._fn_propose_router_owner.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_propose_router_owner.gas_limit = self.call_contract_fee_amount
        self._fn_propose_router_owner.gas_price_wei = self.call_contract_fee_price
        self._fn_propose_router_owner.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_propose_router_owner.block_send(router, proposed)
    
    
    
    
    
    
    
    def propose_router_ownership_renunciation(self) -> None:
        """
        Implementation of propose_router_ownership_renunciation in contract Connext
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
        Implementation of proposed in contract Connext
        Method of the function
    
        """
    
        self._fn_proposed.callback_onfail = self._callback_onfail
        self._fn_proposed.callback_onsuccess = self._callback_onsuccess
        self._fn_proposed.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_proposed.gas_limit = self.call_contract_fee_amount
        self._fn_proposed.gas_price_wei = self.call_contract_fee_price
        self._fn_proposed.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_proposed.block_call()
    
    
    
    def proposed_router_owners(self, router: str) -> str:
        """
        Implementation of proposed_router_owners in contract Connext
        Method of the function
    
        """
    
        self._fn_proposed_router_owners.callback_onfail = self._callback_onfail
        self._fn_proposed_router_owners.callback_onsuccess = self._callback_onsuccess
        self._fn_proposed_router_owners.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_proposed_router_owners.gas_limit = self.call_contract_fee_amount
        self._fn_proposed_router_owners.gas_price_wei = self.call_contract_fee_price
        self._fn_proposed_router_owners.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_proposed_router_owners.block_call(router)
    
    
    
    def proposed_router_timestamp(self, router: str) -> int:
        """
        Implementation of proposed_router_timestamp in contract Connext
        Method of the function
    
        """
    
        self._fn_proposed_router_timestamp.callback_onfail = self._callback_onfail
        self._fn_proposed_router_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_proposed_router_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_proposed_router_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_proposed_router_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_proposed_router_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_proposed_router_timestamp.block_call(router)
    
    
    
    def proposed_timestamp(self) -> int:
        """
        Implementation of proposed_timestamp in contract Connext
        Method of the function
    
        """
    
        self._fn_proposed_timestamp.callback_onfail = self._callback_onfail
        self._fn_proposed_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_proposed_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_proposed_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_proposed_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_proposed_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_proposed_timestamp.block_call()
    
    
    
    def reconcile(self, transfer_id: Union[bytes, str], origin: int, local: str, recipient: str, amount: int, wei:int=0) -> None:
        """
        Implementation of reconcile in contract Connext
        Method of the function
    
        """
    
        self._fn_reconcile.callback_onfail = self._callback_onfail
        self._fn_reconcile.callback_onsuccess = self._callback_onsuccess
        self._fn_reconcile.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_reconcile.gas_limit = self.call_contract_fee_amount
        self._fn_reconcile.gas_price_wei = self.call_contract_fee_price
        self._fn_reconcile.debug_method = self.call_contract_debug_flag
    
        self._fn_reconcile.wei_value = wei
    
    
        return self._fn_reconcile.block_send(transfer_id, origin, local, recipient, amount, wei)
    
    
    
    
    
    
    def reconciled_transfers(self, index_0: Union[bytes, str]) -> Union[bytes, str]:
        """
        Implementation of reconciled_transfers in contract Connext
        Method of the function
    
        """
    
        self._fn_reconciled_transfers.callback_onfail = self._callback_onfail
        self._fn_reconciled_transfers.callback_onsuccess = self._callback_onsuccess
        self._fn_reconciled_transfers.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_reconciled_transfers.gas_limit = self.call_contract_fee_amount
        self._fn_reconciled_transfers.gas_price_wei = self.call_contract_fee_price
        self._fn_reconciled_transfers.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_reconciled_transfers.block_call(index_0)
    
    
    
    def remove_asset_id(self, canonical_id: Union[bytes, str], adopted_asset_id: str) -> None:
        """
        Implementation of remove_asset_id in contract Connext
        Method of the function
    
        """
    
        self._fn_remove_asset_id.callback_onfail = self._callback_onfail
        self._fn_remove_asset_id.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_asset_id.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_asset_id.gas_limit = self.call_contract_fee_amount
        self._fn_remove_asset_id.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_asset_id.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_asset_id.block_send(canonical_id, adopted_asset_id)
    
    
    
    
    
    
    
    def remove_liquidity(self, amount: int, local: str, to: str) -> None:
        """
        Implementation of remove_liquidity in contract Connext
        Method of the function
    
        """
    
        self._fn_remove_liquidity.callback_onfail = self._callback_onfail
        self._fn_remove_liquidity.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_liquidity.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_liquidity.gas_limit = self.call_contract_fee_amount
        self._fn_remove_liquidity.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_liquidity.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_liquidity.block_send(amount, local, to)
    
    
    
    
    
    
    
    def remove_relayer(self, relayer: str) -> None:
        """
        Implementation of remove_relayer in contract Connext
        Method of the function
    
        """
    
        self._fn_remove_relayer.callback_onfail = self._callback_onfail
        self._fn_remove_relayer.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_relayer.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_relayer.gas_limit = self.call_contract_fee_amount
        self._fn_remove_relayer.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_relayer.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_relayer.block_send(relayer)
    
    
    
    
    
    
    
    def remove_relayer_fees(self, amount: int, to: str) -> None:
        """
        Implementation of remove_relayer_fees in contract Connext
        Method of the function
    
        """
    
        self._fn_remove_relayer_fees.callback_onfail = self._callback_onfail
        self._fn_remove_relayer_fees.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_relayer_fees.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_relayer_fees.gas_limit = self.call_contract_fee_amount
        self._fn_remove_relayer_fees.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_relayer_fees.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_relayer_fees.block_send(amount, to)
    
    
    
    
    
    
    
    def remove_router(self, router: str) -> None:
        """
        Implementation of remove_router in contract Connext
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
        Implementation of renounce_asset_ownership in contract Connext
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
        Implementation of renounce_ownership in contract Connext
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
        Implementation of renounce_router_ownership in contract Connext
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
        Implementation of renounced in contract Connext
        Method of the function
    
        """
    
        self._fn_renounced.callback_onfail = self._callback_onfail
        self._fn_renounced.callback_onsuccess = self._callback_onsuccess
        self._fn_renounced.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_renounced.gas_limit = self.call_contract_fee_amount
        self._fn_renounced.gas_price_wei = self.call_contract_fee_price
        self._fn_renounced.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_renounced.block_call()
    
    
    
    def routed_transfers(self, index_0: Union[bytes, str]) -> int:
        """
        Implementation of routed_transfers in contract Connext
        Method of the function
    
        """
    
        self._fn_routed_transfers.callback_onfail = self._callback_onfail
        self._fn_routed_transfers.callback_onsuccess = self._callback_onsuccess
        self._fn_routed_transfers.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_routed_transfers.gas_limit = self.call_contract_fee_amount
        self._fn_routed_transfers.gas_price_wei = self.call_contract_fee_price
        self._fn_routed_transfers.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_routed_transfers.block_call(index_0)
    
    
    
    def routed_transfers_gas(self, index_0: Union[bytes, str]) -> Tuple[int, int]:
        """
        Implementation of routed_transfers_gas in contract Connext
        Method of the function
    
        """
    
        self._fn_routed_transfers_gas.callback_onfail = self._callback_onfail
        self._fn_routed_transfers_gas.callback_onsuccess = self._callback_onsuccess
        self._fn_routed_transfers_gas.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_routed_transfers_gas.gas_limit = self.call_contract_fee_amount
        self._fn_routed_transfers_gas.gas_price_wei = self.call_contract_fee_price
        self._fn_routed_transfers_gas.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_routed_transfers_gas.block_call(index_0)
    
    
    
    def router_balances(self, index_0: str, index_1: str) -> int:
        """
        Implementation of router_balances in contract Connext
        Method of the function
    
        """
    
        self._fn_router_balances.callback_onfail = self._callback_onfail
        self._fn_router_balances.callback_onsuccess = self._callback_onsuccess
        self._fn_router_balances.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_balances.gas_limit = self.call_contract_fee_amount
        self._fn_router_balances.gas_price_wei = self.call_contract_fee_price
        self._fn_router_balances.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_balances.block_call(index_0, index_1)
    
    
    
    def router_owners(self, router: str) -> str:
        """
        Implementation of router_owners in contract Connext
        Method of the function
    
        """
    
        self._fn_router_owners.callback_onfail = self._callback_onfail
        self._fn_router_owners.callback_onsuccess = self._callback_onsuccess
        self._fn_router_owners.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_owners.gas_limit = self.call_contract_fee_amount
        self._fn_router_owners.gas_price_wei = self.call_contract_fee_price
        self._fn_router_owners.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_owners.block_call(router)
    
    
    
    def router_ownership_timestamp(self) -> int:
        """
        Implementation of router_ownership_timestamp in contract Connext
        Method of the function
    
        """
    
        self._fn_router_ownership_timestamp.callback_onfail = self._callback_onfail
        self._fn_router_ownership_timestamp.callback_onsuccess = self._callback_onsuccess
        self._fn_router_ownership_timestamp.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_ownership_timestamp.gas_limit = self.call_contract_fee_amount
        self._fn_router_ownership_timestamp.gas_price_wei = self.call_contract_fee_price
        self._fn_router_ownership_timestamp.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_ownership_timestamp.block_call()
    
    
    
    def router_recipients(self, router: str) -> str:
        """
        Implementation of router_recipients in contract Connext
        Method of the function
    
        """
    
        self._fn_router_recipients.callback_onfail = self._callback_onfail
        self._fn_router_recipients.callback_onsuccess = self._callback_onsuccess
        self._fn_router_recipients.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_recipients.gas_limit = self.call_contract_fee_amount
        self._fn_router_recipients.gas_price_wei = self.call_contract_fee_price
        self._fn_router_recipients.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_recipients.block_call(router)
    
    
    
    def router_relayer_fees(self, index_0: str) -> int:
        """
        Implementation of router_relayer_fees in contract Connext
        Method of the function
    
        """
    
        self._fn_router_relayer_fees.callback_onfail = self._callback_onfail
        self._fn_router_relayer_fees.callback_onsuccess = self._callback_onsuccess
        self._fn_router_relayer_fees.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_router_relayer_fees.gas_limit = self.call_contract_fee_amount
        self._fn_router_relayer_fees.gas_price_wei = self.call_contract_fee_price
        self._fn_router_relayer_fees.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_router_relayer_fees.block_call(index_0)
    
    
    
    def set_max_routers_per_transfer(self, new_max_routers: int) -> None:
        """
        Implementation of set_max_routers_per_transfer in contract Connext
        Method of the function
    
        """
    
        self._fn_set_max_routers_per_transfer.callback_onfail = self._callback_onfail
        self._fn_set_max_routers_per_transfer.callback_onsuccess = self._callback_onsuccess
        self._fn_set_max_routers_per_transfer.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_max_routers_per_transfer.gas_limit = self.call_contract_fee_amount
        self._fn_set_max_routers_per_transfer.gas_price_wei = self.call_contract_fee_price
        self._fn_set_max_routers_per_transfer.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_max_routers_per_transfer.block_send(new_max_routers)
    
    
    
    
    
    
    
    def set_router_recipient(self, router: str, recipient: str) -> None:
        """
        Implementation of set_router_recipient in contract Connext
        Method of the function
    
        """
    
        self._fn_set_router_recipient.callback_onfail = self._callback_onfail
        self._fn_set_router_recipient.callback_onsuccess = self._callback_onsuccess
        self._fn_set_router_recipient.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_router_recipient.gas_limit = self.call_contract_fee_amount
        self._fn_set_router_recipient.gas_price_wei = self.call_contract_fee_price
        self._fn_set_router_recipient.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_router_recipient.block_send(router, recipient)
    
    
    
    
    
    
    
    def setup_asset(self, canonical: BridgeMessageTokenId, adopted_asset_id: str, stable_swap_pool: str) -> None:
        """
        Implementation of setup_asset in contract Connext
        Method of the function
    
        """
    
        self._fn_setup_asset.callback_onfail = self._callback_onfail
        self._fn_setup_asset.callback_onsuccess = self._callback_onsuccess
        self._fn_setup_asset.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_setup_asset.gas_limit = self.call_contract_fee_amount
        self._fn_setup_asset.gas_price_wei = self.call_contract_fee_price
        self._fn_setup_asset.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_setup_asset.block_send(canonical, adopted_asset_id, stable_swap_pool)
    
    
    
    
    
    
    
    def setup_router(self, router: str, owner: str, recipient: str) -> None:
        """
        Implementation of setup_router in contract Connext
        Method of the function
    
        """
    
        self._fn_setup_router.callback_onfail = self._callback_onfail
        self._fn_setup_router.callback_onsuccess = self._callback_onsuccess
        self._fn_setup_router.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_setup_router.gas_limit = self.call_contract_fee_amount
        self._fn_setup_router.gas_price_wei = self.call_contract_fee_price
        self._fn_setup_router.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_setup_router.block_send(router, owner, recipient)
    
    
    
    
    
    
    
    def token_registry(self) -> str:
        """
        Implementation of token_registry in contract Connext
        Method of the function
    
        """
    
        self._fn_token_registry.callback_onfail = self._callback_onfail
        self._fn_token_registry.callback_onsuccess = self._callback_onsuccess
        self._fn_token_registry.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_token_registry.gas_limit = self.call_contract_fee_amount
        self._fn_token_registry.gas_price_wei = self.call_contract_fee_price
        self._fn_token_registry.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_token_registry.block_call()
    
    
    
    def wrapper(self) -> str:
        """
        Implementation of wrapper in contract Connext
        Method of the function
    
        """
    
        self._fn_wrapper.callback_onfail = self._callback_onfail
        self._fn_wrapper.callback_onsuccess = self._callback_onsuccess
        self._fn_wrapper.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_wrapper.gas_limit = self.call_contract_fee_amount
        self._fn_wrapper.gas_price_wei = self.call_contract_fee_price
        self._fn_wrapper.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_wrapper.block_call()
    
    
    
    def xcall(self, args: IConnextXCallArgs, wei:int=0) -> Union[bytes, str]:
        """
        Implementation of xcall in contract Connext
        Method of the function
    
        """
    
        self._fn_xcall.callback_onfail = self._callback_onfail
        self._fn_xcall.callback_onsuccess = self._callback_onsuccess
        self._fn_xcall.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_xcall.gas_limit = self.call_contract_fee_amount
        self._fn_xcall.gas_price_wei = self.call_contract_fee_price
        self._fn_xcall.debug_method = self.call_contract_debug_flag
    
        self._fn_xcall.wei_value = wei
    
    
        return self._fn_xcall.block_send(args, wei)
    
    
    

    def CallContractWait(self, t_long:int)-> "Connext":
        self._fn_accept_proposed_owner.setWait(t_long)
        self._fn_accept_proposed_router_owner.setWait(t_long)
        self._fn_add_liquidity.setWait(t_long)
        self._fn_add_liquidity_for.setWait(t_long)
        self._fn_add_relayer.setWait(t_long)
        self._fn_add_relayer_fees.setWait(t_long)
        self._fn_add_stable_swap_pool.setWait(t_long)
        self._fn_adopted_to_canonical.setWait(t_long)
        self._fn_adopted_to_local_pools.setWait(t_long)
        self._fn_approved_assets.setWait(t_long)
        self._fn_approved_relayers.setWait(t_long)
        self._fn_approved_routers.setWait(t_long)
        self._fn_asset_ownership_timestamp.setWait(t_long)
        self._fn_bridge_router.setWait(t_long)
        self._fn_canonical_to_adopted.setWait(t_long)
        self._fn_delay.setWait(t_long)
        self._fn_domain.setWait(t_long)
        self._fn_execute.setWait(t_long)
        self._fn_executor.setWait(t_long)
        self._fn_initialize.setWait(t_long)
        self._fn_is_asset_ownership_renounced.setWait(t_long)
        self._fn_is_router_ownership_renounced.setWait(t_long)
        self._fn_max_routers_per_transfer.setWait(t_long)
        self._fn_nonce.setWait(t_long)
        self._fn_owner.setWait(t_long)
        self._fn_propose_asset_ownership_renunciation.setWait(t_long)
        self._fn_propose_new_owner.setWait(t_long)
        self._fn_propose_router_owner.setWait(t_long)
        self._fn_propose_router_ownership_renunciation.setWait(t_long)
        self._fn_proposed.setWait(t_long)
        self._fn_proposed_router_owners.setWait(t_long)
        self._fn_proposed_router_timestamp.setWait(t_long)
        self._fn_proposed_timestamp.setWait(t_long)
        self._fn_reconcile.setWait(t_long)
        self._fn_reconciled_transfers.setWait(t_long)
        self._fn_remove_asset_id.setWait(t_long)
        self._fn_remove_liquidity.setWait(t_long)
        self._fn_remove_relayer.setWait(t_long)
        self._fn_remove_relayer_fees.setWait(t_long)
        self._fn_remove_router.setWait(t_long)
        self._fn_renounce_asset_ownership.setWait(t_long)
        self._fn_renounce_ownership.setWait(t_long)
        self._fn_renounce_router_ownership.setWait(t_long)
        self._fn_renounced.setWait(t_long)
        self._fn_routed_transfers.setWait(t_long)
        self._fn_routed_transfers_gas.setWait(t_long)
        self._fn_router_balances.setWait(t_long)
        self._fn_router_owners.setWait(t_long)
        self._fn_router_ownership_timestamp.setWait(t_long)
        self._fn_router_recipients.setWait(t_long)
        self._fn_router_relayer_fees.setWait(t_long)
        self._fn_set_max_routers_per_transfer.setWait(t_long)
        self._fn_set_router_recipient.setWait(t_long)
        self._fn_setup_asset.setWait(t_long)
        self._fn_setup_router.setWait(t_long)
        self._fn_token_registry.setWait(t_long)
        self._fn_wrapper.setWait(t_long)
        self._fn_xcall.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"name":"AssetLogic__transferAssetFromContract_notNative","type":"error"},{"inputs":[],"name":"Connext__addAssetId_alreadyAdded","type":"error"},{"inputs":[],"name":"Connext__addLiquidityForRouter_amountIsZero","type":"error"},{"inputs":[],"name":"Connext__addLiquidityForRouter_badAsset","type":"error"},{"inputs":[],"name":"Connext__addLiquidityForRouter_badRouter","type":"error"},{"inputs":[],"name":"Connext__addLiquidityForRouter_routerEmpty","type":"error"},{"inputs":[],"name":"Connext__addRelayerFees_notValue","type":"error"},{"inputs":[],"name":"Connext__addRelayer_alreadyApproved","type":"error"},{"inputs":[],"name":"Connext__decrementLiquidity_maxRoutersExceeded","type":"error"},{"inputs":[],"name":"Connext__decrementLiquidity_notEmpty","type":"error"},{"inputs":[],"name":"Connext__execute_notSlowParams","type":"error"},{"inputs":[],"name":"Connext__handleRelayerFees_notApprovedRelayer","type":"error"},{"inputs":[],"name":"Connext__handleRelayerFees_notRtrSig","type":"error"},{"inputs":[],"name":"Connext__onlyBridgeRouter_notBridge","type":"error"},{"inputs":[],"name":"Connext__removeAssetId_notAdded","type":"error"},{"inputs":[],"name":"Connext__removeLiquidity_amountIsZero","type":"error"},{"inputs":[],"name":"Connext__removeLiquidity_insufficientFunds","type":"error"},{"inputs":[],"name":"Connext__removeLiquidity_recipientEmpty","type":"error"},{"inputs":[],"name":"Connext__removeRelayer_notApproved","type":"error"},{"inputs":[],"name":"Connext__setMaxRoutersPerTransfer_invalidMaxRoutersPerTransfer","type":"error"},{"inputs":[],"name":"Connext__xcall_notSupportedAsset","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__acceptProposedOwner_delayNotElapsed","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__acceptProposedOwner_noOwnershipChange","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__onlyOwner_notOwner","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__onlyProposed_notProposedOwner","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__proposeAssetOwnershipRenunciation_noOwnershipChange","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__proposeNewOwner_invalidProposal","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__proposeNewOwner_noOwnershipChange","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__proposeRouterOwnershipRenunciation_noOwnershipChange","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceAssetOwnership_delayNotElapsed","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceAssetOwnership_noOwnershipChange","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceAssetOwnership_noProposal","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceOwnership_delayNotElapsed","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceOwnership_invalidProposal","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceOwnership_noProposal","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceRouterOwnership_delayNotElapsed","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceRouterOwnership_noOwnershipChange","type":"error"},{"inputs":[],"name":"ProposedOwnableUpgradeable__renounceRouterOwnership_noProposal","type":"error"},{"inputs":[],"name":"RouterPermissionsManagerLogic__setupRouter_amountIsZero","type":"error"},{"inputs":[],"name":"RouterPermissionsManagerLogic__setupRouter_routerEmpty","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"canonicalId","type":"bytes32"},{"indexed":false,"internalType":"uint32","name":"domain","type":"uint32"},{"indexed":false,"internalType":"address","name":"adoptedAsset","type":"address"},{"indexed":false,"internalType":"address","name":"supportedAsset","type":"address"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"AssetAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"renounced","type":"bool"}],"name":"AssetOwnershipRenounced","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"AssetOwnershipRenunciationProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"canonicalId","type":"bytes32"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"AssetRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"transferId","type":"bytes32"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"address","name":"router","type":"address"},{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"},{"internalType":"uint32","name":"originDomain","type":"uint32"},{"internalType":"uint32","name":"destinationDomain","type":"uint32"}],"indexed":false,"internalType":"struct IConnext.CallParams","name":"params","type":"tuple"},{"indexed":false,"internalType":"address","name":"localAsset","type":"address"},{"indexed":false,"internalType":"address","name":"transactingAsset","type":"address"},{"indexed":false,"internalType":"uint256","name":"localAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"transactingAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"Executed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"router","type":"address"},{"indexed":false,"internalType":"address","name":"local","type":"address"},{"indexed":false,"internalType":"bytes32","name":"canonicalId","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"LiquidityAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"router","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"address","name":"local","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"LiquidityRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"maxRoutersPerTransfer","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"MaxRoutersPerTransferUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"proposedOwner","type":"address"}],"name":"OwnershipProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"transferId","type":"bytes32"},{"indexed":true,"internalType":"uint32","name":"origin","type":"uint32"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"address","name":"localAsset","type":"address"},{"indexed":false,"internalType":"uint256","name":"localAmount","type":"uint256"},{"components":[{"internalType":"address[]","name":"routers","type":"address[]"},{"internalType":"uint256","name":"amount","type":"uint256"}],"indexed":false,"internalType":"struct IConnext.ExecutedTransfer","name":"executed","type":"tuple"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"Reconciled","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"relayer","type":"address"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"RelayerAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"relayer","type":"address"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"RelayerRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"renounced","type":"bool"}],"name":"RouterOwnershipRenounced","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"RouterOwnershipRenunciationProposed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"canonicalId","type":"bytes32"},{"indexed":false,"internalType":"uint32","name":"domain","type":"uint32"},{"indexed":false,"internalType":"address","name":"swapPool","type":"address"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"StableSwapAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"transferId","type":"bytes32"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"},{"internalType":"uint32","name":"originDomain","type":"uint32"},{"internalType":"uint32","name":"destinationDomain","type":"uint32"}],"indexed":false,"internalType":"struct IConnext.CallParams","name":"params","type":"tuple"},{"indexed":false,"internalType":"address","name":"transactingAsset","type":"address"},{"indexed":false,"internalType":"address","name":"localAsset","type":"address"},{"indexed":false,"internalType":"uint256","name":"transactingAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"localAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"nonce","type":"uint256"},{"indexed":false,"internalType":"address","name":"caller","type":"address"}],"name":"XCalled","type":"event"},{"inputs":[],"name":"acceptProposedOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"}],"name":"acceptProposedRouterOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"local","type":"address"}],"name":"addLiquidity","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"local","type":"address"},{"internalType":"address","name":"router","type":"address"}],"name":"addLiquidityFor","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"relayer","type":"address"}],"name":"addRelayer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"}],"name":"addRelayerFees","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"uint32","name":"domain","type":"uint32"},{"internalType":"bytes32","name":"id","type":"bytes32"}],"internalType":"struct BridgeMessage.TokenId","name":"canonical","type":"tuple"},{"internalType":"address","name":"stableSwapPool","type":"address"}],"name":"addStableSwapPool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"adoptedToCanonical","outputs":[{"internalType":"uint32","name":"domain","type":"uint32"},{"internalType":"bytes32","name":"id","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"adoptedToLocalPools","outputs":[{"internalType":"contract IStableSwap","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"approvedAssets","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"approvedRelayers","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_approved","type":"address"}],"name":"approvedRouters","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"assetOwnershipTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bridgeRouter","outputs":[{"internalType":"contract BridgeRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"canonicalToAdopted","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"delay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"domain","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"},{"internalType":"uint32","name":"originDomain","type":"uint32"},{"internalType":"uint32","name":"destinationDomain","type":"uint32"}],"internalType":"struct IConnext.CallParams","name":"params","type":"tuple"},{"internalType":"address","name":"local","type":"address"},{"internalType":"address[]","name":"routers","type":"address[]"},{"internalType":"uint32","name":"feePercentage","type":"uint32"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"bytes","name":"relayerSignature","type":"bytes"},{"internalType":"address","name":"originSender","type":"address"}],"internalType":"struct IConnext.ExecuteArgs","name":"_args","type":"tuple"}],"name":"execute","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"executor","outputs":[{"internalType":"contract IExecutor","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_domain","type":"uint256"},{"internalType":"address payable","name":"_bridgeRouter","type":"address"},{"internalType":"address","name":"_tokenRegistry","type":"address"},{"internalType":"address","name":"_wrappedNative","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isAssetOwnershipRenounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isRouterOwnershipRenounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxRoutersPerTransfer","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nonce","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposeAssetOwnershipRenunciation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newlyProposed","type":"address"}],"name":"proposeNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"proposed","type":"address"}],"name":"proposeRouterOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposeRouterOwnershipRenunciation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposed","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_router","type":"address"}],"name":"proposedRouterOwners","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_router","type":"address"}],"name":"proposedRouterTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposedTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_transferId","type":"bytes32"},{"internalType":"uint32","name":"_origin","type":"uint32"},{"internalType":"address","name":"_local","type":"address"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"reconcile","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"reconciledTransfers","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"canonicalId","type":"bytes32"},{"internalType":"address","name":"adoptedAssetId","type":"address"}],"name":"removeAssetId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"local","type":"address"},{"internalType":"address payable","name":"to","type":"address"}],"name":"removeLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"relayer","type":"address"}],"name":"removeRelayer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address payable","name":"to","type":"address"}],"name":"removeRelayerFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"}],"name":"removeRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceAssetOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceRouterOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"routedTransfers","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"index_0","type":"bytes32"}],"name":"routedTransfersGas","outputs":[{"internalType":"uint256","name":"gasUsed","type":"uint256"},{"internalType":"uint256","name":"gasPrice","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"},{"internalType":"address","name":"index_1","type":"address"}],"name":"routerBalances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_router","type":"address"}],"name":"routerOwners","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"routerOwnershipTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_router","type":"address"}],"name":"routerRecipients","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"routerRelayerFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"newMaxRouters","type":"uint256"}],"name":"setMaxRoutersPerTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"recipient","type":"address"}],"name":"setRouterRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint32","name":"domain","type":"uint32"},{"internalType":"bytes32","name":"id","type":"bytes32"}],"internalType":"struct BridgeMessage.TokenId","name":"canonical","type":"tuple"},{"internalType":"address","name":"adoptedAssetId","type":"address"},{"internalType":"address","name":"stableSwapPool","type":"address"}],"name":"setupAsset","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"router","type":"address"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"recipient","type":"address"}],"name":"setupRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"tokenRegistry","outputs":[{"internalType":"contract TokenRegistry","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"wrapper","outputs":[{"internalType":"contract IWrapped","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"},{"internalType":"uint32","name":"originDomain","type":"uint32"},{"internalType":"uint32","name":"destinationDomain","type":"uint32"}],"internalType":"struct IConnext.CallParams","name":"params","type":"tuple"},{"internalType":"address","name":"transactingAssetId","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct IConnext.XCallArgs","name":"_args","type":"tuple"}],"name":"xcall","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
