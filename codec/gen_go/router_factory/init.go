// Code generated - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package router_factory

import (
	"errors"
	"math/big"
	"strings"

	ethereum "github.com/ethereum/go-ethereum"
	"github.com/ethereum/go-ethereum/accounts/abi"
	"github.com/ethereum/go-ethereum/accounts/abi/bind"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/event"
)

// Reference imports to suppress errors if they are not otherwise used.
var (
	_ = errors.New
	_ = big.NewInt
	_ = strings.NewReader
	_ = ethereum.NotFound
	_ = bind.Bind
	_ = common.Big1
	_ = types.BloomLookup
	_ = event.NewSubscription
)

// RouterFactoryMetaData contains all meta data concerning the RouterFactory contract.
var RouterFactoryMetaData = &bind.MetaData{
	ABI: "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_owner\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"routerSigner\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"transactionManager\",\"type\":\"address\"}],\"name\":\"RouterCreated\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"routerSigner\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"}],\"name\":\"createRouter\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"routerSigner\",\"type\":\"address\"}],\"name\":\"getRouterAddress\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_transactionManager\",\"type\":\"address\"}],\"name\":\"init\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"routerAddresses\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"transactionManager\",\"outputs\":[{\"internalType\":\"contractITransactionManager\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]",
}

// RouterFactoryABI is the input ABI used to generate the binding from.
// Deprecated: Use RouterFactoryMetaData.ABI instead.
var RouterFactoryABI = RouterFactoryMetaData.ABI

// RouterFactory is an auto generated Go binding around an Ethereum contract.
type RouterFactory struct {
	RouterFactoryCaller     // Read-only binding to the contract
	RouterFactoryTransactor // Write-only binding to the contract
	RouterFactoryFilterer   // Log filterer for contract events
}

// RouterFactoryCaller is an auto generated read-only Go binding around an Ethereum contract.
type RouterFactoryCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// RouterFactoryTransactor is an auto generated write-only Go binding around an Ethereum contract.
type RouterFactoryTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// RouterFactoryFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type RouterFactoryFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// RouterFactorySession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type RouterFactorySession struct {
	Contract     *RouterFactory    // Generic contract binding to set the session for
	CallOpts     bind.CallOpts     // Call options to use throughout this session
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// RouterFactoryCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type RouterFactoryCallerSession struct {
	Contract *RouterFactoryCaller // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts        // Call options to use throughout this session
}

// RouterFactoryTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type RouterFactoryTransactorSession struct {
	Contract     *RouterFactoryTransactor // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts        // Transaction auth options to use throughout this session
}

// RouterFactoryRaw is an auto generated low-level Go binding around an Ethereum contract.
type RouterFactoryRaw struct {
	Contract *RouterFactory // Generic contract binding to access the raw methods on
}

// RouterFactoryCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type RouterFactoryCallerRaw struct {
	Contract *RouterFactoryCaller // Generic read-only contract binding to access the raw methods on
}

// RouterFactoryTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type RouterFactoryTransactorRaw struct {
	Contract *RouterFactoryTransactor // Generic write-only contract binding to access the raw methods on
}

// NewRouterFactory creates a new instance of RouterFactory, bound to a specific deployed contract.
func NewRouterFactory(address common.Address, backend bind.ContractBackend) (*RouterFactory, error) {
	contract, err := bindRouterFactory(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &RouterFactory{RouterFactoryCaller: RouterFactoryCaller{contract: contract}, RouterFactoryTransactor: RouterFactoryTransactor{contract: contract}, RouterFactoryFilterer: RouterFactoryFilterer{contract: contract}}, nil
}

// NewRouterFactoryCaller creates a new read-only instance of RouterFactory, bound to a specific deployed contract.
func NewRouterFactoryCaller(address common.Address, caller bind.ContractCaller) (*RouterFactoryCaller, error) {
	contract, err := bindRouterFactory(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &RouterFactoryCaller{contract: contract}, nil
}

// NewRouterFactoryTransactor creates a new write-only instance of RouterFactory, bound to a specific deployed contract.
func NewRouterFactoryTransactor(address common.Address, transactor bind.ContractTransactor) (*RouterFactoryTransactor, error) {
	contract, err := bindRouterFactory(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &RouterFactoryTransactor{contract: contract}, nil
}

// NewRouterFactoryFilterer creates a new log filterer instance of RouterFactory, bound to a specific deployed contract.
func NewRouterFactoryFilterer(address common.Address, filterer bind.ContractFilterer) (*RouterFactoryFilterer, error) {
	contract, err := bindRouterFactory(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &RouterFactoryFilterer{contract: contract}, nil
}

// bindRouterFactory binds a generic wrapper to an already deployed contract.
func bindRouterFactory(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := abi.JSON(strings.NewReader(RouterFactoryABI))
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_RouterFactory *RouterFactoryRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _RouterFactory.Contract.RouterFactoryCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_RouterFactory *RouterFactoryRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _RouterFactory.Contract.RouterFactoryTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_RouterFactory *RouterFactoryRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _RouterFactory.Contract.RouterFactoryTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_RouterFactory *RouterFactoryCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _RouterFactory.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_RouterFactory *RouterFactoryTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _RouterFactory.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_RouterFactory *RouterFactoryTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _RouterFactory.Contract.contract.Transact(opts, method, params...)
}

// GetRouterAddress is a free data retrieval call binding the contract method 0x463a6176.
//
// Solidity: function getRouterAddress(address routerSigner) view returns(address)
func (_RouterFactory *RouterFactoryCaller) GetRouterAddress(opts *bind.CallOpts, routerSigner common.Address) (common.Address, error) {
	var out []interface{}
	err := _RouterFactory.contract.Call(opts, &out, "getRouterAddress", routerSigner)

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// GetRouterAddress is a free data retrieval call binding the contract method 0x463a6176.
//
// Solidity: function getRouterAddress(address routerSigner) view returns(address)
func (_RouterFactory *RouterFactorySession) GetRouterAddress(routerSigner common.Address) (common.Address, error) {
	return _RouterFactory.Contract.GetRouterAddress(&_RouterFactory.CallOpts, routerSigner)
}

// GetRouterAddress is a free data retrieval call binding the contract method 0x463a6176.
//
// Solidity: function getRouterAddress(address routerSigner) view returns(address)
func (_RouterFactory *RouterFactoryCallerSession) GetRouterAddress(routerSigner common.Address) (common.Address, error) {
	return _RouterFactory.Contract.GetRouterAddress(&_RouterFactory.CallOpts, routerSigner)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_RouterFactory *RouterFactoryCaller) Owner(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _RouterFactory.contract.Call(opts, &out, "owner")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_RouterFactory *RouterFactorySession) Owner() (common.Address, error) {
	return _RouterFactory.Contract.Owner(&_RouterFactory.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_RouterFactory *RouterFactoryCallerSession) Owner() (common.Address, error) {
	return _RouterFactory.Contract.Owner(&_RouterFactory.CallOpts)
}

// RouterAddresses is a free data retrieval call binding the contract method 0x1f16a046.
//
// Solidity: function routerAddresses(address ) view returns(address)
func (_RouterFactory *RouterFactoryCaller) RouterAddresses(opts *bind.CallOpts, arg0 common.Address) (common.Address, error) {
	var out []interface{}
	err := _RouterFactory.contract.Call(opts, &out, "routerAddresses", arg0)

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// RouterAddresses is a free data retrieval call binding the contract method 0x1f16a046.
//
// Solidity: function routerAddresses(address ) view returns(address)
func (_RouterFactory *RouterFactorySession) RouterAddresses(arg0 common.Address) (common.Address, error) {
	return _RouterFactory.Contract.RouterAddresses(&_RouterFactory.CallOpts, arg0)
}

// RouterAddresses is a free data retrieval call binding the contract method 0x1f16a046.
//
// Solidity: function routerAddresses(address ) view returns(address)
func (_RouterFactory *RouterFactoryCallerSession) RouterAddresses(arg0 common.Address) (common.Address, error) {
	return _RouterFactory.Contract.RouterAddresses(&_RouterFactory.CallOpts, arg0)
}

// TransactionManager is a free data retrieval call binding the contract method 0x3b716452.
//
// Solidity: function transactionManager() view returns(address)
func (_RouterFactory *RouterFactoryCaller) TransactionManager(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _RouterFactory.contract.Call(opts, &out, "transactionManager")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// TransactionManager is a free data retrieval call binding the contract method 0x3b716452.
//
// Solidity: function transactionManager() view returns(address)
func (_RouterFactory *RouterFactorySession) TransactionManager() (common.Address, error) {
	return _RouterFactory.Contract.TransactionManager(&_RouterFactory.CallOpts)
}

// TransactionManager is a free data retrieval call binding the contract method 0x3b716452.
//
// Solidity: function transactionManager() view returns(address)
func (_RouterFactory *RouterFactoryCallerSession) TransactionManager() (common.Address, error) {
	return _RouterFactory.Contract.TransactionManager(&_RouterFactory.CallOpts)
}

// CreateRouter is a paid mutator transaction binding the contract method 0x7f629efc.
//
// Solidity: function createRouter(address routerSigner, address recipient) returns(address)
func (_RouterFactory *RouterFactoryTransactor) CreateRouter(opts *bind.TransactOpts, routerSigner common.Address, recipient common.Address) (*types.Transaction, error) {
	return _RouterFactory.contract.Transact(opts, "createRouter", routerSigner, recipient)
}

// CreateRouter is a paid mutator transaction binding the contract method 0x7f629efc.
//
// Solidity: function createRouter(address routerSigner, address recipient) returns(address)
func (_RouterFactory *RouterFactorySession) CreateRouter(routerSigner common.Address, recipient common.Address) (*types.Transaction, error) {
	return _RouterFactory.Contract.CreateRouter(&_RouterFactory.TransactOpts, routerSigner, recipient)
}

// CreateRouter is a paid mutator transaction binding the contract method 0x7f629efc.
//
// Solidity: function createRouter(address routerSigner, address recipient) returns(address)
func (_RouterFactory *RouterFactoryTransactorSession) CreateRouter(routerSigner common.Address, recipient common.Address) (*types.Transaction, error) {
	return _RouterFactory.Contract.CreateRouter(&_RouterFactory.TransactOpts, routerSigner, recipient)
}

// Init is a paid mutator transaction binding the contract method 0x19ab453c.
//
// Solidity: function init(address _transactionManager) returns()
func (_RouterFactory *RouterFactoryTransactor) Init(opts *bind.TransactOpts, _transactionManager common.Address) (*types.Transaction, error) {
	return _RouterFactory.contract.Transact(opts, "init", _transactionManager)
}

// Init is a paid mutator transaction binding the contract method 0x19ab453c.
//
// Solidity: function init(address _transactionManager) returns()
func (_RouterFactory *RouterFactorySession) Init(_transactionManager common.Address) (*types.Transaction, error) {
	return _RouterFactory.Contract.Init(&_RouterFactory.TransactOpts, _transactionManager)
}

// Init is a paid mutator transaction binding the contract method 0x19ab453c.
//
// Solidity: function init(address _transactionManager) returns()
func (_RouterFactory *RouterFactoryTransactorSession) Init(_transactionManager common.Address) (*types.Transaction, error) {
	return _RouterFactory.Contract.Init(&_RouterFactory.TransactOpts, _transactionManager)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_RouterFactory *RouterFactoryTransactor) RenounceOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _RouterFactory.contract.Transact(opts, "renounceOwnership")
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_RouterFactory *RouterFactorySession) RenounceOwnership() (*types.Transaction, error) {
	return _RouterFactory.Contract.RenounceOwnership(&_RouterFactory.TransactOpts)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_RouterFactory *RouterFactoryTransactorSession) RenounceOwnership() (*types.Transaction, error) {
	return _RouterFactory.Contract.RenounceOwnership(&_RouterFactory.TransactOpts)
}

// TransferOwnership is a paid mutator transaction binding the contract method 0xf2fde38b.
//
// Solidity: function transferOwnership(address newOwner) returns()
func (_RouterFactory *RouterFactoryTransactor) TransferOwnership(opts *bind.TransactOpts, newOwner common.Address) (*types.Transaction, error) {
	return _RouterFactory.contract.Transact(opts, "transferOwnership", newOwner)
}

// TransferOwnership is a paid mutator transaction binding the contract method 0xf2fde38b.
//
// Solidity: function transferOwnership(address newOwner) returns()
func (_RouterFactory *RouterFactorySession) TransferOwnership(newOwner common.Address) (*types.Transaction, error) {
	return _RouterFactory.Contract.TransferOwnership(&_RouterFactory.TransactOpts, newOwner)
}

// TransferOwnership is a paid mutator transaction binding the contract method 0xf2fde38b.
//
// Solidity: function transferOwnership(address newOwner) returns()
func (_RouterFactory *RouterFactoryTransactorSession) TransferOwnership(newOwner common.Address) (*types.Transaction, error) {
	return _RouterFactory.Contract.TransferOwnership(&_RouterFactory.TransactOpts, newOwner)
}

// RouterFactoryOwnershipTransferredIterator is returned from FilterOwnershipTransferred and is used to iterate over the raw logs and unpacked data for OwnershipTransferred events raised by the RouterFactory contract.
type RouterFactoryOwnershipTransferredIterator struct {
	Event *RouterFactoryOwnershipTransferred // Event containing the contract specifics and raw log

	contract *bind.BoundContract // Generic contract to use for unpacking event data
	event    string              // Event name to use for unpacking event data

	logs chan types.Log        // Log channel receiving the found contract events
	sub  ethereum.Subscription // Subscription for errors, completion and termination
	done bool                  // Whether the subscription completed delivering logs
	fail error                 // Occurred error to stop iteration
}

// Next advances the iterator to the subsequent event, returning whether there
// are any more events found. In case of a retrieval or parsing error, false is
// returned and Error() can be queried for the exact failure.
func (it *RouterFactoryOwnershipTransferredIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterFactoryOwnershipTransferred)
			if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
				it.fail = err
				return false
			}
			it.Event.Raw = log
			return true

		default:
			return false
		}
	}
	// Iterator still in progress, wait for either a data or an error event
	select {
	case log := <-it.logs:
		it.Event = new(RouterFactoryOwnershipTransferred)
		if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
			it.fail = err
			return false
		}
		it.Event.Raw = log
		return true

	case err := <-it.sub.Err():
		it.done = true
		it.fail = err
		return it.Next()
	}
}

// Error returns any retrieval or parsing error occurred during filtering.
func (it *RouterFactoryOwnershipTransferredIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterFactoryOwnershipTransferredIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterFactoryOwnershipTransferred represents a OwnershipTransferred event raised by the RouterFactory contract.
type RouterFactoryOwnershipTransferred struct {
	PreviousOwner common.Address
	NewOwner      common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterOwnershipTransferred is a free log retrieval operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_RouterFactory *RouterFactoryFilterer) FilterOwnershipTransferred(opts *bind.FilterOpts, previousOwner []common.Address, newOwner []common.Address) (*RouterFactoryOwnershipTransferredIterator, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _RouterFactory.contract.FilterLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return &RouterFactoryOwnershipTransferredIterator{contract: _RouterFactory.contract, event: "OwnershipTransferred", logs: logs, sub: sub}, nil
}

// WatchOwnershipTransferred is a free log subscription operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_RouterFactory *RouterFactoryFilterer) WatchOwnershipTransferred(opts *bind.WatchOpts, sink chan<- *RouterFactoryOwnershipTransferred, previousOwner []common.Address, newOwner []common.Address) (event.Subscription, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _RouterFactory.contract.WatchLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterFactoryOwnershipTransferred)
				if err := _RouterFactory.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
					return err
				}
				event.Raw = log

				select {
				case sink <- event:
				case err := <-sub.Err():
					return err
				case <-quit:
					return nil
				}
			case err := <-sub.Err():
				return err
			case <-quit:
				return nil
			}
		}
	}), nil
}

// ParseOwnershipTransferred is a log parse operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_RouterFactory *RouterFactoryFilterer) ParseOwnershipTransferred(log types.Log) (*RouterFactoryOwnershipTransferred, error) {
	event := new(RouterFactoryOwnershipTransferred)
	if err := _RouterFactory.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// RouterFactoryRouterCreatedIterator is returned from FilterRouterCreated and is used to iterate over the raw logs and unpacked data for RouterCreated events raised by the RouterFactory contract.
type RouterFactoryRouterCreatedIterator struct {
	Event *RouterFactoryRouterCreated // Event containing the contract specifics and raw log

	contract *bind.BoundContract // Generic contract to use for unpacking event data
	event    string              // Event name to use for unpacking event data

	logs chan types.Log        // Log channel receiving the found contract events
	sub  ethereum.Subscription // Subscription for errors, completion and termination
	done bool                  // Whether the subscription completed delivering logs
	fail error                 // Occurred error to stop iteration
}

// Next advances the iterator to the subsequent event, returning whether there
// are any more events found. In case of a retrieval or parsing error, false is
// returned and Error() can be queried for the exact failure.
func (it *RouterFactoryRouterCreatedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterFactoryRouterCreated)
			if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
				it.fail = err
				return false
			}
			it.Event.Raw = log
			return true

		default:
			return false
		}
	}
	// Iterator still in progress, wait for either a data or an error event
	select {
	case log := <-it.logs:
		it.Event = new(RouterFactoryRouterCreated)
		if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
			it.fail = err
			return false
		}
		it.Event.Raw = log
		return true

	case err := <-it.sub.Err():
		it.done = true
		it.fail = err
		return it.Next()
	}
}

// Error returns any retrieval or parsing error occurred during filtering.
func (it *RouterFactoryRouterCreatedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterFactoryRouterCreatedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterFactoryRouterCreated represents a RouterCreated event raised by the RouterFactory contract.
type RouterFactoryRouterCreated struct {
	Router             common.Address
	RouterSigner       common.Address
	Recipient          common.Address
	TransactionManager common.Address
	Raw                types.Log // Blockchain specific contextual infos
}

// FilterRouterCreated is a free log retrieval operation binding the contract event 0xe8e811674d167b407a67a22f592a226ade5e34b608e7d56721f82422f3b98197.
//
// Solidity: event RouterCreated(address router, address routerSigner, address recipient, address transactionManager)
func (_RouterFactory *RouterFactoryFilterer) FilterRouterCreated(opts *bind.FilterOpts) (*RouterFactoryRouterCreatedIterator, error) {

	logs, sub, err := _RouterFactory.contract.FilterLogs(opts, "RouterCreated")
	if err != nil {
		return nil, err
	}
	return &RouterFactoryRouterCreatedIterator{contract: _RouterFactory.contract, event: "RouterCreated", logs: logs, sub: sub}, nil
}

// WatchRouterCreated is a free log subscription operation binding the contract event 0xe8e811674d167b407a67a22f592a226ade5e34b608e7d56721f82422f3b98197.
//
// Solidity: event RouterCreated(address router, address routerSigner, address recipient, address transactionManager)
func (_RouterFactory *RouterFactoryFilterer) WatchRouterCreated(opts *bind.WatchOpts, sink chan<- *RouterFactoryRouterCreated) (event.Subscription, error) {

	logs, sub, err := _RouterFactory.contract.WatchLogs(opts, "RouterCreated")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterFactoryRouterCreated)
				if err := _RouterFactory.contract.UnpackLog(event, "RouterCreated", log); err != nil {
					return err
				}
				event.Raw = log

				select {
				case sink <- event:
				case err := <-sub.Err():
					return err
				case <-quit:
					return nil
				}
			case err := <-sub.Err():
				return err
			case <-quit:
				return nil
			}
		}
	}), nil
}

// ParseRouterCreated is a log parse operation binding the contract event 0xe8e811674d167b407a67a22f592a226ade5e34b608e7d56721f82422f3b98197.
//
// Solidity: event RouterCreated(address router, address routerSigner, address recipient, address transactionManager)
func (_RouterFactory *RouterFactoryFilterer) ParseRouterCreated(log types.Log) (*RouterFactoryRouterCreated, error) {
	event := new(RouterFactoryRouterCreated)
	if err := _RouterFactory.contract.UnpackLog(event, "RouterCreated", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}
