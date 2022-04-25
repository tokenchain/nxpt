"""Generated wrapper for Counter Solidity contract."""

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
# constructor for Counter below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        CounterValidator,
    )
except ImportError:

    class CounterValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class CountMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the count method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("count")



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

                self._on_receipt_handle("count", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: count")
            message = f"Error {er}: count"
            self._on_fail("count", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, count: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, count. Reason: Unknown")

            self._on_fail("count", message)

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

class IncrementMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the increment method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("increment")



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

                self._on_receipt_handle("increment", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: increment")
            message = f"Error {er}: increment"
            self._on_fail("increment", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, increment: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, increment. Reason: Unknown")

            self._on_fail("increment", message)

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

class IncrementAndSendMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the incrementAndSend method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("incrementAndSend")

    def validate_and_normalize_inputs(self, asset_id: str, recipient: str, amount: int)->any:
        """Validate the inputs to the incrementAndSend method."""
        self.validator.assert_valid(
            method_name='incrementAndSend',
            parameter_name='assetId',
            argument_value=asset_id,
        )
        asset_id = self.validate_and_checksum_address(asset_id)
        self.validator.assert_valid(
            method_name='incrementAndSend',
            parameter_name='recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        self.validator.assert_valid(
            method_name='incrementAndSend',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (asset_id, recipient, amount)



    def block_send(self, asset_id: str, recipient: str, amount: int,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(asset_id, recipient, amount)
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

                self._on_receipt_handle("increment_and_send", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: increment_and_send")
            message = f"Error {er}: increment_and_send"
            self._on_fail("increment_and_send", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, increment_and_send: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, increment_and_send. Reason: Unknown")

            self._on_fail("increment_and_send", message)

    def send_transaction(self, asset_id: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (asset_id, recipient, amount) = self.validate_and_normalize_inputs(asset_id, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id, recipient, amount).transact(tx_params.as_dict())

    def build_transaction(self, asset_id: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (asset_id, recipient, amount) = self.validate_and_normalize_inputs(asset_id, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id, recipient, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, asset_id: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (asset_id, recipient, amount) = self.validate_and_normalize_inputs(asset_id, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(asset_id, recipient, amount).estimateGas(tx_params.as_dict())

class SetShouldRevertMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setShouldRevert method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setShouldRevert")

    def validate_and_normalize_inputs(self, value: bool)->any:
        """Validate the inputs to the setShouldRevert method."""
        self.validator.assert_valid(
            method_name='setShouldRevert',
            parameter_name='value',
            argument_value=value,
        )
        return (value)



    def block_send(self, value: bool,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(value)
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

                self._on_receipt_handle("set_should_revert", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_should_revert")
            message = f"Error {er}: set_should_revert"
            self._on_fail("set_should_revert", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_should_revert: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_should_revert. Reason: Unknown")

            self._on_fail("set_should_revert", message)

    def send_transaction(self, value: bool, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(value).transact(tx_params.as_dict())

    def build_transaction(self, value: bool, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(value).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, value: bool, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(value).estimateGas(tx_params.as_dict())

class ShouldRevertMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the shouldRevert method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("shouldRevert")



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

                self._on_receipt_handle("should_revert", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: should_revert")
            message = f"Error {er}: should_revert"
            self._on_fail("should_revert", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, should_revert: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, should_revert. Reason: Unknown")

            self._on_fail("should_revert", message)

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

    def count(self) -> str:
        return self._function_signatures["count"]
    def increment(self) -> str:
        return self._function_signatures["increment"]
    def increment_and_send(self) -> str:
        return self._function_signatures["incrementAndSend"]
    def set_should_revert(self) -> str:
        return self._function_signatures["setShouldRevert"]
    def should_revert(self) -> str:
        return self._function_signatures["shouldRevert"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class Counter(ContractBase):
    """Wrapper class for Counter Solidity contract."""
    _fn_count: CountMethod
    """Constructor-initialized instance of
    :class:`CountMethod`.
    """

    _fn_increment: IncrementMethod
    """Constructor-initialized instance of
    :class:`IncrementMethod`.
    """

    _fn_increment_and_send: IncrementAndSendMethod
    """Constructor-initialized instance of
    :class:`IncrementAndSendMethod`.
    """

    _fn_set_should_revert: SetShouldRevertMethod
    """Constructor-initialized instance of
    :class:`SetShouldRevertMethod`.
    """

    _fn_should_revert: ShouldRevertMethod
    """Constructor-initialized instance of
    :class:`ShouldRevertMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: CounterValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, Counter.abi())
        web3 = core_lib.w3

        if not validator:
            validator = CounterValidator(web3, contract_address)




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
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=Counter.abi()).functions
        self._signatures = SignatureGenerator(Counter.abi())
        validator.bindSignatures(self._signatures)

        self._fn_count = CountMethod(core_lib, contract_address, functions.count, validator)
        self._fn_increment = IncrementMethod(core_lib, contract_address, functions.increment, validator)
        self._fn_increment_and_send = IncrementAndSendMethod(core_lib, contract_address, functions.incrementAndSend, validator)
        self._fn_set_should_revert = SetShouldRevertMethod(core_lib, contract_address, functions.setShouldRevert, validator)
        self._fn_should_revert = ShouldRevertMethod(core_lib, contract_address, functions.shouldRevert, validator)


    
    
    
    def count(self) -> int:
        """
        Implementation of count in contract Counter
        Method of the function
    
        """
    
        self._fn_count.callback_onfail = self._callback_onfail
        self._fn_count.callback_onsuccess = self._callback_onsuccess
        self._fn_count.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_count.gas_limit = self.call_contract_fee_amount
        self._fn_count.gas_price_wei = self.call_contract_fee_price
        self._fn_count.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_count.block_call()
    
    
    
    def increment(self) -> None:
        """
        Implementation of increment in contract Counter
        Method of the function
    
        """
    
        self._fn_increment.callback_onfail = self._callback_onfail
        self._fn_increment.callback_onsuccess = self._callback_onsuccess
        self._fn_increment.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_increment.gas_limit = self.call_contract_fee_amount
        self._fn_increment.gas_price_wei = self.call_contract_fee_price
        self._fn_increment.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_increment.block_send()
    
    
    
    
    
    
    
    def increment_and_send(self, asset_id: str, recipient: str, amount: int, wei:int=0) -> None:
        """
        Implementation of increment_and_send in contract Counter
        Method of the function
    
        """
    
        self._fn_increment_and_send.callback_onfail = self._callback_onfail
        self._fn_increment_and_send.callback_onsuccess = self._callback_onsuccess
        self._fn_increment_and_send.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_increment_and_send.gas_limit = self.call_contract_fee_amount
        self._fn_increment_and_send.gas_price_wei = self.call_contract_fee_price
        self._fn_increment_and_send.debug_method = self.call_contract_debug_flag
    
        self._fn_increment_and_send.wei_value = wei
    
    
        return self._fn_increment_and_send.block_send(asset_id, recipient, amount, wei)
    
    
    
    
    
    
    def set_should_revert(self, value: bool) -> None:
        """
        Implementation of set_should_revert in contract Counter
        Method of the function
    
        """
    
        self._fn_set_should_revert.callback_onfail = self._callback_onfail
        self._fn_set_should_revert.callback_onsuccess = self._callback_onsuccess
        self._fn_set_should_revert.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_should_revert.gas_limit = self.call_contract_fee_amount
        self._fn_set_should_revert.gas_price_wei = self.call_contract_fee_price
        self._fn_set_should_revert.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_should_revert.block_send(value)
    
    
    
    
    
    
    
    def should_revert(self) -> bool:
        """
        Implementation of should_revert in contract Counter
        Method of the function
    
        """
    
        self._fn_should_revert.callback_onfail = self._callback_onfail
        self._fn_should_revert.callback_onsuccess = self._callback_onsuccess
        self._fn_should_revert.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_should_revert.gas_limit = self.call_contract_fee_amount
        self._fn_should_revert.gas_price_wei = self.call_contract_fee_price
        self._fn_should_revert.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_should_revert.block_call()

    def CallContractWait(self, t_long:int)-> "Counter":
        self._fn_count.setWait(t_long)
        self._fn_increment.setWait(t_long)
        self._fn_increment_and_send.setWait(t_long)
        self._fn_set_should_revert.setWait(t_long)
        self._fn_should_revert.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"count","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"increment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"assetId","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"incrementAndSend","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bool","name":"value","type":"bool"}],"name":"setShouldRevert","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"shouldRevert","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
