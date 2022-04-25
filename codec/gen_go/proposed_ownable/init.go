// Code generated - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package proposed_ownable

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

// ProposedOwnableMetaData contains all meta data concerning the ProposedOwnable contract.
var ProposedOwnableMetaData = &bind.MetaData{
	ABI: "[{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"renounced\",\"type\":\"bool\"}],\"name\":\"AssetOwnershipRenounced\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"timestamp\",\"type\":\"uint256\"}],\"name\":\"AssetOwnershipRenunciationProposed\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"proposedOwner\",\"type\":\"address\"}],\"name\":\"OwnershipProposed\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"renounced\",\"type\":\"bool\"}],\"name\":\"RouterOwnershipRenounced\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"timestamp\",\"type\":\"uint256\"}],\"name\":\"RouterOwnershipRenunciationProposed\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"acceptProposedOwner\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"assetOwnershipTimestamp\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"delay\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"isAssetOwnershipRenounced\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"isRouterOwnershipRenounced\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposeAssetOwnershipRenunciation\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newlyProposed\",\"type\":\"address\"}],\"name\":\"proposeNewOwner\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposeRouterOwnershipRenunciation\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposed\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposedTimestamp\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceAssetOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceRouterOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounced\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"routerOwnershipTimestamp\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"}]",
}

// ProposedOwnableABI is the input ABI used to generate the binding from.
// Deprecated: Use ProposedOwnableMetaData.ABI instead.
var ProposedOwnableABI = ProposedOwnableMetaData.ABI

// ProposedOwnable is an auto generated Go binding around an Ethereum contract.
type ProposedOwnable struct {
	ProposedOwnableCaller     // Read-only binding to the contract
	ProposedOwnableTransactor // Write-only binding to the contract
	ProposedOwnableFilterer   // Log filterer for contract events
}

// ProposedOwnableCaller is an auto generated read-only Go binding around an Ethereum contract.
type ProposedOwnableCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// ProposedOwnableTransactor is an auto generated write-only Go binding around an Ethereum contract.
type ProposedOwnableTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// ProposedOwnableFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type ProposedOwnableFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// ProposedOwnableSession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type ProposedOwnableSession struct {
	Contract     *ProposedOwnable  // Generic contract binding to set the session for
	CallOpts     bind.CallOpts     // Call options to use throughout this session
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// ProposedOwnableCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type ProposedOwnableCallerSession struct {
	Contract *ProposedOwnableCaller // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts          // Call options to use throughout this session
}

// ProposedOwnableTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type ProposedOwnableTransactorSession struct {
	Contract     *ProposedOwnableTransactor // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts          // Transaction auth options to use throughout this session
}

// ProposedOwnableRaw is an auto generated low-level Go binding around an Ethereum contract.
type ProposedOwnableRaw struct {
	Contract *ProposedOwnable // Generic contract binding to access the raw methods on
}

// ProposedOwnableCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type ProposedOwnableCallerRaw struct {
	Contract *ProposedOwnableCaller // Generic read-only contract binding to access the raw methods on
}

// ProposedOwnableTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type ProposedOwnableTransactorRaw struct {
	Contract *ProposedOwnableTransactor // Generic write-only contract binding to access the raw methods on
}

// NewProposedOwnable creates a new instance of ProposedOwnable, bound to a specific deployed contract.
func NewProposedOwnable(address common.Address, backend bind.ContractBackend) (*ProposedOwnable, error) {
	contract, err := bindProposedOwnable(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &ProposedOwnable{ProposedOwnableCaller: ProposedOwnableCaller{contract: contract}, ProposedOwnableTransactor: ProposedOwnableTransactor{contract: contract}, ProposedOwnableFilterer: ProposedOwnableFilterer{contract: contract}}, nil
}

// NewProposedOwnableCaller creates a new read-only instance of ProposedOwnable, bound to a specific deployed contract.
func NewProposedOwnableCaller(address common.Address, caller bind.ContractCaller) (*ProposedOwnableCaller, error) {
	contract, err := bindProposedOwnable(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableCaller{contract: contract}, nil
}

// NewProposedOwnableTransactor creates a new write-only instance of ProposedOwnable, bound to a specific deployed contract.
func NewProposedOwnableTransactor(address common.Address, transactor bind.ContractTransactor) (*ProposedOwnableTransactor, error) {
	contract, err := bindProposedOwnable(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableTransactor{contract: contract}, nil
}

// NewProposedOwnableFilterer creates a new log filterer instance of ProposedOwnable, bound to a specific deployed contract.
func NewProposedOwnableFilterer(address common.Address, filterer bind.ContractFilterer) (*ProposedOwnableFilterer, error) {
	contract, err := bindProposedOwnable(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableFilterer{contract: contract}, nil
}

// bindProposedOwnable binds a generic wrapper to an already deployed contract.
func bindProposedOwnable(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := abi.JSON(strings.NewReader(ProposedOwnableABI))
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_ProposedOwnable *ProposedOwnableRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _ProposedOwnable.Contract.ProposedOwnableCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_ProposedOwnable *ProposedOwnableRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposedOwnableTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_ProposedOwnable *ProposedOwnableRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposedOwnableTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_ProposedOwnable *ProposedOwnableCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _ProposedOwnable.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_ProposedOwnable *ProposedOwnableTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_ProposedOwnable *ProposedOwnableTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _ProposedOwnable.Contract.contract.Transact(opts, method, params...)
}

// AssetOwnershipTimestamp is a free data retrieval call binding the contract method 0x6a41633a.
//
// Solidity: function assetOwnershipTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCaller) AssetOwnershipTimestamp(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "assetOwnershipTimestamp")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// AssetOwnershipTimestamp is a free data retrieval call binding the contract method 0x6a41633a.
//
// Solidity: function assetOwnershipTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableSession) AssetOwnershipTimestamp() (*big.Int, error) {
	return _ProposedOwnable.Contract.AssetOwnershipTimestamp(&_ProposedOwnable.CallOpts)
}

// AssetOwnershipTimestamp is a free data retrieval call binding the contract method 0x6a41633a.
//
// Solidity: function assetOwnershipTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCallerSession) AssetOwnershipTimestamp() (*big.Int, error) {
	return _ProposedOwnable.Contract.AssetOwnershipTimestamp(&_ProposedOwnable.CallOpts)
}

// Delay is a free data retrieval call binding the contract method 0x6a42b8f8.
//
// Solidity: function delay() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCaller) Delay(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "delay")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// Delay is a free data retrieval call binding the contract method 0x6a42b8f8.
//
// Solidity: function delay() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableSession) Delay() (*big.Int, error) {
	return _ProposedOwnable.Contract.Delay(&_ProposedOwnable.CallOpts)
}

// Delay is a free data retrieval call binding the contract method 0x6a42b8f8.
//
// Solidity: function delay() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCallerSession) Delay() (*big.Int, error) {
	return _ProposedOwnable.Contract.Delay(&_ProposedOwnable.CallOpts)
}

// IsAssetOwnershipRenounced is a free data retrieval call binding the contract method 0xe8be0dfc.
//
// Solidity: function isAssetOwnershipRenounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableCaller) IsAssetOwnershipRenounced(opts *bind.CallOpts) (bool, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "isAssetOwnershipRenounced")

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// IsAssetOwnershipRenounced is a free data retrieval call binding the contract method 0xe8be0dfc.
//
// Solidity: function isAssetOwnershipRenounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableSession) IsAssetOwnershipRenounced() (bool, error) {
	return _ProposedOwnable.Contract.IsAssetOwnershipRenounced(&_ProposedOwnable.CallOpts)
}

// IsAssetOwnershipRenounced is a free data retrieval call binding the contract method 0xe8be0dfc.
//
// Solidity: function isAssetOwnershipRenounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableCallerSession) IsAssetOwnershipRenounced() (bool, error) {
	return _ProposedOwnable.Contract.IsAssetOwnershipRenounced(&_ProposedOwnable.CallOpts)
}

// IsRouterOwnershipRenounced is a free data retrieval call binding the contract method 0x2004ef45.
//
// Solidity: function isRouterOwnershipRenounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableCaller) IsRouterOwnershipRenounced(opts *bind.CallOpts) (bool, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "isRouterOwnershipRenounced")

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// IsRouterOwnershipRenounced is a free data retrieval call binding the contract method 0x2004ef45.
//
// Solidity: function isRouterOwnershipRenounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableSession) IsRouterOwnershipRenounced() (bool, error) {
	return _ProposedOwnable.Contract.IsRouterOwnershipRenounced(&_ProposedOwnable.CallOpts)
}

// IsRouterOwnershipRenounced is a free data retrieval call binding the contract method 0x2004ef45.
//
// Solidity: function isRouterOwnershipRenounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableCallerSession) IsRouterOwnershipRenounced() (bool, error) {
	return _ProposedOwnable.Contract.IsRouterOwnershipRenounced(&_ProposedOwnable.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_ProposedOwnable *ProposedOwnableCaller) Owner(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "owner")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_ProposedOwnable *ProposedOwnableSession) Owner() (common.Address, error) {
	return _ProposedOwnable.Contract.Owner(&_ProposedOwnable.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_ProposedOwnable *ProposedOwnableCallerSession) Owner() (common.Address, error) {
	return _ProposedOwnable.Contract.Owner(&_ProposedOwnable.CallOpts)
}

// Proposed is a free data retrieval call binding the contract method 0xd1851c92.
//
// Solidity: function proposed() view returns(address)
func (_ProposedOwnable *ProposedOwnableCaller) Proposed(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "proposed")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Proposed is a free data retrieval call binding the contract method 0xd1851c92.
//
// Solidity: function proposed() view returns(address)
func (_ProposedOwnable *ProposedOwnableSession) Proposed() (common.Address, error) {
	return _ProposedOwnable.Contract.Proposed(&_ProposedOwnable.CallOpts)
}

// Proposed is a free data retrieval call binding the contract method 0xd1851c92.
//
// Solidity: function proposed() view returns(address)
func (_ProposedOwnable *ProposedOwnableCallerSession) Proposed() (common.Address, error) {
	return _ProposedOwnable.Contract.Proposed(&_ProposedOwnable.CallOpts)
}

// ProposedTimestamp is a free data retrieval call binding the contract method 0x3cf52ffb.
//
// Solidity: function proposedTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCaller) ProposedTimestamp(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "proposedTimestamp")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// ProposedTimestamp is a free data retrieval call binding the contract method 0x3cf52ffb.
//
// Solidity: function proposedTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableSession) ProposedTimestamp() (*big.Int, error) {
	return _ProposedOwnable.Contract.ProposedTimestamp(&_ProposedOwnable.CallOpts)
}

// ProposedTimestamp is a free data retrieval call binding the contract method 0x3cf52ffb.
//
// Solidity: function proposedTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCallerSession) ProposedTimestamp() (*big.Int, error) {
	return _ProposedOwnable.Contract.ProposedTimestamp(&_ProposedOwnable.CallOpts)
}

// Renounced is a free data retrieval call binding the contract method 0xd232c220.
//
// Solidity: function renounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableCaller) Renounced(opts *bind.CallOpts) (bool, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "renounced")

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// Renounced is a free data retrieval call binding the contract method 0xd232c220.
//
// Solidity: function renounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableSession) Renounced() (bool, error) {
	return _ProposedOwnable.Contract.Renounced(&_ProposedOwnable.CallOpts)
}

// Renounced is a free data retrieval call binding the contract method 0xd232c220.
//
// Solidity: function renounced() view returns(bool)
func (_ProposedOwnable *ProposedOwnableCallerSession) Renounced() (bool, error) {
	return _ProposedOwnable.Contract.Renounced(&_ProposedOwnable.CallOpts)
}

// RouterOwnershipTimestamp is a free data retrieval call binding the contract method 0xc1a04959.
//
// Solidity: function routerOwnershipTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCaller) RouterOwnershipTimestamp(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _ProposedOwnable.contract.Call(opts, &out, "routerOwnershipTimestamp")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// RouterOwnershipTimestamp is a free data retrieval call binding the contract method 0xc1a04959.
//
// Solidity: function routerOwnershipTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableSession) RouterOwnershipTimestamp() (*big.Int, error) {
	return _ProposedOwnable.Contract.RouterOwnershipTimestamp(&_ProposedOwnable.CallOpts)
}

// RouterOwnershipTimestamp is a free data retrieval call binding the contract method 0xc1a04959.
//
// Solidity: function routerOwnershipTimestamp() view returns(uint256)
func (_ProposedOwnable *ProposedOwnableCallerSession) RouterOwnershipTimestamp() (*big.Int, error) {
	return _ProposedOwnable.Contract.RouterOwnershipTimestamp(&_ProposedOwnable.CallOpts)
}

// AcceptProposedOwner is a paid mutator transaction binding the contract method 0xc5b350df.
//
// Solidity: function acceptProposedOwner() returns()
func (_ProposedOwnable *ProposedOwnableTransactor) AcceptProposedOwner(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.contract.Transact(opts, "acceptProposedOwner")
}

// AcceptProposedOwner is a paid mutator transaction binding the contract method 0xc5b350df.
//
// Solidity: function acceptProposedOwner() returns()
func (_ProposedOwnable *ProposedOwnableSession) AcceptProposedOwner() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.AcceptProposedOwner(&_ProposedOwnable.TransactOpts)
}

// AcceptProposedOwner is a paid mutator transaction binding the contract method 0xc5b350df.
//
// Solidity: function acceptProposedOwner() returns()
func (_ProposedOwnable *ProposedOwnableTransactorSession) AcceptProposedOwner() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.AcceptProposedOwner(&_ProposedOwnable.TransactOpts)
}

// ProposeAssetOwnershipRenunciation is a paid mutator transaction binding the contract method 0x8741eac5.
//
// Solidity: function proposeAssetOwnershipRenunciation() returns()
func (_ProposedOwnable *ProposedOwnableTransactor) ProposeAssetOwnershipRenunciation(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.contract.Transact(opts, "proposeAssetOwnershipRenunciation")
}

// ProposeAssetOwnershipRenunciation is a paid mutator transaction binding the contract method 0x8741eac5.
//
// Solidity: function proposeAssetOwnershipRenunciation() returns()
func (_ProposedOwnable *ProposedOwnableSession) ProposeAssetOwnershipRenunciation() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposeAssetOwnershipRenunciation(&_ProposedOwnable.TransactOpts)
}

// ProposeAssetOwnershipRenunciation is a paid mutator transaction binding the contract method 0x8741eac5.
//
// Solidity: function proposeAssetOwnershipRenunciation() returns()
func (_ProposedOwnable *ProposedOwnableTransactorSession) ProposeAssetOwnershipRenunciation() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposeAssetOwnershipRenunciation(&_ProposedOwnable.TransactOpts)
}

// ProposeNewOwner is a paid mutator transaction binding the contract method 0xb1f8100d.
//
// Solidity: function proposeNewOwner(address newlyProposed) returns()
func (_ProposedOwnable *ProposedOwnableTransactor) ProposeNewOwner(opts *bind.TransactOpts, newlyProposed common.Address) (*types.Transaction, error) {
	return _ProposedOwnable.contract.Transact(opts, "proposeNewOwner", newlyProposed)
}

// ProposeNewOwner is a paid mutator transaction binding the contract method 0xb1f8100d.
//
// Solidity: function proposeNewOwner(address newlyProposed) returns()
func (_ProposedOwnable *ProposedOwnableSession) ProposeNewOwner(newlyProposed common.Address) (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposeNewOwner(&_ProposedOwnable.TransactOpts, newlyProposed)
}

// ProposeNewOwner is a paid mutator transaction binding the contract method 0xb1f8100d.
//
// Solidity: function proposeNewOwner(address newlyProposed) returns()
func (_ProposedOwnable *ProposedOwnableTransactorSession) ProposeNewOwner(newlyProposed common.Address) (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposeNewOwner(&_ProposedOwnable.TransactOpts, newlyProposed)
}

// ProposeRouterOwnershipRenunciation is a paid mutator transaction binding the contract method 0xe47602f7.
//
// Solidity: function proposeRouterOwnershipRenunciation() returns()
func (_ProposedOwnable *ProposedOwnableTransactor) ProposeRouterOwnershipRenunciation(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.contract.Transact(opts, "proposeRouterOwnershipRenunciation")
}

// ProposeRouterOwnershipRenunciation is a paid mutator transaction binding the contract method 0xe47602f7.
//
// Solidity: function proposeRouterOwnershipRenunciation() returns()
func (_ProposedOwnable *ProposedOwnableSession) ProposeRouterOwnershipRenunciation() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposeRouterOwnershipRenunciation(&_ProposedOwnable.TransactOpts)
}

// ProposeRouterOwnershipRenunciation is a paid mutator transaction binding the contract method 0xe47602f7.
//
// Solidity: function proposeRouterOwnershipRenunciation() returns()
func (_ProposedOwnable *ProposedOwnableTransactorSession) ProposeRouterOwnershipRenunciation() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.ProposeRouterOwnershipRenunciation(&_ProposedOwnable.TransactOpts)
}

// RenounceAssetOwnership is a paid mutator transaction binding the contract method 0x3855b467.
//
// Solidity: function renounceAssetOwnership() returns()
func (_ProposedOwnable *ProposedOwnableTransactor) RenounceAssetOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.contract.Transact(opts, "renounceAssetOwnership")
}

// RenounceAssetOwnership is a paid mutator transaction binding the contract method 0x3855b467.
//
// Solidity: function renounceAssetOwnership() returns()
func (_ProposedOwnable *ProposedOwnableSession) RenounceAssetOwnership() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.RenounceAssetOwnership(&_ProposedOwnable.TransactOpts)
}

// RenounceAssetOwnership is a paid mutator transaction binding the contract method 0x3855b467.
//
// Solidity: function renounceAssetOwnership() returns()
func (_ProposedOwnable *ProposedOwnableTransactorSession) RenounceAssetOwnership() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.RenounceAssetOwnership(&_ProposedOwnable.TransactOpts)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_ProposedOwnable *ProposedOwnableTransactor) RenounceOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.contract.Transact(opts, "renounceOwnership")
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_ProposedOwnable *ProposedOwnableSession) RenounceOwnership() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.RenounceOwnership(&_ProposedOwnable.TransactOpts)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_ProposedOwnable *ProposedOwnableTransactorSession) RenounceOwnership() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.RenounceOwnership(&_ProposedOwnable.TransactOpts)
}

// RenounceRouterOwnership is a paid mutator transaction binding the contract method 0xc0c17baf.
//
// Solidity: function renounceRouterOwnership() returns()
func (_ProposedOwnable *ProposedOwnableTransactor) RenounceRouterOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ProposedOwnable.contract.Transact(opts, "renounceRouterOwnership")
}

// RenounceRouterOwnership is a paid mutator transaction binding the contract method 0xc0c17baf.
//
// Solidity: function renounceRouterOwnership() returns()
func (_ProposedOwnable *ProposedOwnableSession) RenounceRouterOwnership() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.RenounceRouterOwnership(&_ProposedOwnable.TransactOpts)
}

// RenounceRouterOwnership is a paid mutator transaction binding the contract method 0xc0c17baf.
//
// Solidity: function renounceRouterOwnership() returns()
func (_ProposedOwnable *ProposedOwnableTransactorSession) RenounceRouterOwnership() (*types.Transaction, error) {
	return _ProposedOwnable.Contract.RenounceRouterOwnership(&_ProposedOwnable.TransactOpts)
}

// ProposedOwnableAssetOwnershipRenouncedIterator is returned from FilterAssetOwnershipRenounced and is used to iterate over the raw logs and unpacked data for AssetOwnershipRenounced events raised by the ProposedOwnable contract.
type ProposedOwnableAssetOwnershipRenouncedIterator struct {
	Event *ProposedOwnableAssetOwnershipRenounced // Event containing the contract specifics and raw log

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
func (it *ProposedOwnableAssetOwnershipRenouncedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ProposedOwnableAssetOwnershipRenounced)
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
		it.Event = new(ProposedOwnableAssetOwnershipRenounced)
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
func (it *ProposedOwnableAssetOwnershipRenouncedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ProposedOwnableAssetOwnershipRenouncedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ProposedOwnableAssetOwnershipRenounced represents a AssetOwnershipRenounced event raised by the ProposedOwnable contract.
type ProposedOwnableAssetOwnershipRenounced struct {
	Renounced bool
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterAssetOwnershipRenounced is a free log retrieval operation binding the contract event 0x868d89ead22a5d10f456845ac0014901d9af7203e71cf0892d70d9dc262c2fb9.
//
// Solidity: event AssetOwnershipRenounced(bool renounced)
func (_ProposedOwnable *ProposedOwnableFilterer) FilterAssetOwnershipRenounced(opts *bind.FilterOpts) (*ProposedOwnableAssetOwnershipRenouncedIterator, error) {

	logs, sub, err := _ProposedOwnable.contract.FilterLogs(opts, "AssetOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableAssetOwnershipRenouncedIterator{contract: _ProposedOwnable.contract, event: "AssetOwnershipRenounced", logs: logs, sub: sub}, nil
}

// WatchAssetOwnershipRenounced is a free log subscription operation binding the contract event 0x868d89ead22a5d10f456845ac0014901d9af7203e71cf0892d70d9dc262c2fb9.
//
// Solidity: event AssetOwnershipRenounced(bool renounced)
func (_ProposedOwnable *ProposedOwnableFilterer) WatchAssetOwnershipRenounced(opts *bind.WatchOpts, sink chan<- *ProposedOwnableAssetOwnershipRenounced) (event.Subscription, error) {

	logs, sub, err := _ProposedOwnable.contract.WatchLogs(opts, "AssetOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ProposedOwnableAssetOwnershipRenounced)
				if err := _ProposedOwnable.contract.UnpackLog(event, "AssetOwnershipRenounced", log); err != nil {
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

// ParseAssetOwnershipRenounced is a log parse operation binding the contract event 0x868d89ead22a5d10f456845ac0014901d9af7203e71cf0892d70d9dc262c2fb9.
//
// Solidity: event AssetOwnershipRenounced(bool renounced)
func (_ProposedOwnable *ProposedOwnableFilterer) ParseAssetOwnershipRenounced(log types.Log) (*ProposedOwnableAssetOwnershipRenounced, error) {
	event := new(ProposedOwnableAssetOwnershipRenounced)
	if err := _ProposedOwnable.contract.UnpackLog(event, "AssetOwnershipRenounced", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ProposedOwnableAssetOwnershipRenunciationProposedIterator is returned from FilterAssetOwnershipRenunciationProposed and is used to iterate over the raw logs and unpacked data for AssetOwnershipRenunciationProposed events raised by the ProposedOwnable contract.
type ProposedOwnableAssetOwnershipRenunciationProposedIterator struct {
	Event *ProposedOwnableAssetOwnershipRenunciationProposed // Event containing the contract specifics and raw log

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
func (it *ProposedOwnableAssetOwnershipRenunciationProposedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ProposedOwnableAssetOwnershipRenunciationProposed)
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
		it.Event = new(ProposedOwnableAssetOwnershipRenunciationProposed)
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
func (it *ProposedOwnableAssetOwnershipRenunciationProposedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ProposedOwnableAssetOwnershipRenunciationProposedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ProposedOwnableAssetOwnershipRenunciationProposed represents a AssetOwnershipRenunciationProposed event raised by the ProposedOwnable contract.
type ProposedOwnableAssetOwnershipRenunciationProposed struct {
	Timestamp *big.Int
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterAssetOwnershipRenunciationProposed is a free log retrieval operation binding the contract event 0xa78fdca214e4619ef34a695316d423f5b0d8274bc919d29733bf8f92ec8cbb7a.
//
// Solidity: event AssetOwnershipRenunciationProposed(uint256 timestamp)
func (_ProposedOwnable *ProposedOwnableFilterer) FilterAssetOwnershipRenunciationProposed(opts *bind.FilterOpts) (*ProposedOwnableAssetOwnershipRenunciationProposedIterator, error) {

	logs, sub, err := _ProposedOwnable.contract.FilterLogs(opts, "AssetOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableAssetOwnershipRenunciationProposedIterator{contract: _ProposedOwnable.contract, event: "AssetOwnershipRenunciationProposed", logs: logs, sub: sub}, nil
}

// WatchAssetOwnershipRenunciationProposed is a free log subscription operation binding the contract event 0xa78fdca214e4619ef34a695316d423f5b0d8274bc919d29733bf8f92ec8cbb7a.
//
// Solidity: event AssetOwnershipRenunciationProposed(uint256 timestamp)
func (_ProposedOwnable *ProposedOwnableFilterer) WatchAssetOwnershipRenunciationProposed(opts *bind.WatchOpts, sink chan<- *ProposedOwnableAssetOwnershipRenunciationProposed) (event.Subscription, error) {

	logs, sub, err := _ProposedOwnable.contract.WatchLogs(opts, "AssetOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ProposedOwnableAssetOwnershipRenunciationProposed)
				if err := _ProposedOwnable.contract.UnpackLog(event, "AssetOwnershipRenunciationProposed", log); err != nil {
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

// ParseAssetOwnershipRenunciationProposed is a log parse operation binding the contract event 0xa78fdca214e4619ef34a695316d423f5b0d8274bc919d29733bf8f92ec8cbb7a.
//
// Solidity: event AssetOwnershipRenunciationProposed(uint256 timestamp)
func (_ProposedOwnable *ProposedOwnableFilterer) ParseAssetOwnershipRenunciationProposed(log types.Log) (*ProposedOwnableAssetOwnershipRenunciationProposed, error) {
	event := new(ProposedOwnableAssetOwnershipRenunciationProposed)
	if err := _ProposedOwnable.contract.UnpackLog(event, "AssetOwnershipRenunciationProposed", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ProposedOwnableOwnershipProposedIterator is returned from FilterOwnershipProposed and is used to iterate over the raw logs and unpacked data for OwnershipProposed events raised by the ProposedOwnable contract.
type ProposedOwnableOwnershipProposedIterator struct {
	Event *ProposedOwnableOwnershipProposed // Event containing the contract specifics and raw log

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
func (it *ProposedOwnableOwnershipProposedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ProposedOwnableOwnershipProposed)
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
		it.Event = new(ProposedOwnableOwnershipProposed)
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
func (it *ProposedOwnableOwnershipProposedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ProposedOwnableOwnershipProposedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ProposedOwnableOwnershipProposed represents a OwnershipProposed event raised by the ProposedOwnable contract.
type ProposedOwnableOwnershipProposed struct {
	ProposedOwner common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterOwnershipProposed is a free log retrieval operation binding the contract event 0x6ab4d119f23076e8ad491bc65ce85f017fb0591dce08755ba8591059cc51737a.
//
// Solidity: event OwnershipProposed(address indexed proposedOwner)
func (_ProposedOwnable *ProposedOwnableFilterer) FilterOwnershipProposed(opts *bind.FilterOpts, proposedOwner []common.Address) (*ProposedOwnableOwnershipProposedIterator, error) {

	var proposedOwnerRule []interface{}
	for _, proposedOwnerItem := range proposedOwner {
		proposedOwnerRule = append(proposedOwnerRule, proposedOwnerItem)
	}

	logs, sub, err := _ProposedOwnable.contract.FilterLogs(opts, "OwnershipProposed", proposedOwnerRule)
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableOwnershipProposedIterator{contract: _ProposedOwnable.contract, event: "OwnershipProposed", logs: logs, sub: sub}, nil
}

// WatchOwnershipProposed is a free log subscription operation binding the contract event 0x6ab4d119f23076e8ad491bc65ce85f017fb0591dce08755ba8591059cc51737a.
//
// Solidity: event OwnershipProposed(address indexed proposedOwner)
func (_ProposedOwnable *ProposedOwnableFilterer) WatchOwnershipProposed(opts *bind.WatchOpts, sink chan<- *ProposedOwnableOwnershipProposed, proposedOwner []common.Address) (event.Subscription, error) {

	var proposedOwnerRule []interface{}
	for _, proposedOwnerItem := range proposedOwner {
		proposedOwnerRule = append(proposedOwnerRule, proposedOwnerItem)
	}

	logs, sub, err := _ProposedOwnable.contract.WatchLogs(opts, "OwnershipProposed", proposedOwnerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ProposedOwnableOwnershipProposed)
				if err := _ProposedOwnable.contract.UnpackLog(event, "OwnershipProposed", log); err != nil {
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

// ParseOwnershipProposed is a log parse operation binding the contract event 0x6ab4d119f23076e8ad491bc65ce85f017fb0591dce08755ba8591059cc51737a.
//
// Solidity: event OwnershipProposed(address indexed proposedOwner)
func (_ProposedOwnable *ProposedOwnableFilterer) ParseOwnershipProposed(log types.Log) (*ProposedOwnableOwnershipProposed, error) {
	event := new(ProposedOwnableOwnershipProposed)
	if err := _ProposedOwnable.contract.UnpackLog(event, "OwnershipProposed", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ProposedOwnableOwnershipTransferredIterator is returned from FilterOwnershipTransferred and is used to iterate over the raw logs and unpacked data for OwnershipTransferred events raised by the ProposedOwnable contract.
type ProposedOwnableOwnershipTransferredIterator struct {
	Event *ProposedOwnableOwnershipTransferred // Event containing the contract specifics and raw log

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
func (it *ProposedOwnableOwnershipTransferredIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ProposedOwnableOwnershipTransferred)
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
		it.Event = new(ProposedOwnableOwnershipTransferred)
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
func (it *ProposedOwnableOwnershipTransferredIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ProposedOwnableOwnershipTransferredIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ProposedOwnableOwnershipTransferred represents a OwnershipTransferred event raised by the ProposedOwnable contract.
type ProposedOwnableOwnershipTransferred struct {
	PreviousOwner common.Address
	NewOwner      common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterOwnershipTransferred is a free log retrieval operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_ProposedOwnable *ProposedOwnableFilterer) FilterOwnershipTransferred(opts *bind.FilterOpts, previousOwner []common.Address, newOwner []common.Address) (*ProposedOwnableOwnershipTransferredIterator, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _ProposedOwnable.contract.FilterLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableOwnershipTransferredIterator{contract: _ProposedOwnable.contract, event: "OwnershipTransferred", logs: logs, sub: sub}, nil
}

// WatchOwnershipTransferred is a free log subscription operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_ProposedOwnable *ProposedOwnableFilterer) WatchOwnershipTransferred(opts *bind.WatchOpts, sink chan<- *ProposedOwnableOwnershipTransferred, previousOwner []common.Address, newOwner []common.Address) (event.Subscription, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _ProposedOwnable.contract.WatchLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ProposedOwnableOwnershipTransferred)
				if err := _ProposedOwnable.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
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
func (_ProposedOwnable *ProposedOwnableFilterer) ParseOwnershipTransferred(log types.Log) (*ProposedOwnableOwnershipTransferred, error) {
	event := new(ProposedOwnableOwnershipTransferred)
	if err := _ProposedOwnable.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ProposedOwnableRouterOwnershipRenouncedIterator is returned from FilterRouterOwnershipRenounced and is used to iterate over the raw logs and unpacked data for RouterOwnershipRenounced events raised by the ProposedOwnable contract.
type ProposedOwnableRouterOwnershipRenouncedIterator struct {
	Event *ProposedOwnableRouterOwnershipRenounced // Event containing the contract specifics and raw log

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
func (it *ProposedOwnableRouterOwnershipRenouncedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ProposedOwnableRouterOwnershipRenounced)
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
		it.Event = new(ProposedOwnableRouterOwnershipRenounced)
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
func (it *ProposedOwnableRouterOwnershipRenouncedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ProposedOwnableRouterOwnershipRenouncedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ProposedOwnableRouterOwnershipRenounced represents a RouterOwnershipRenounced event raised by the ProposedOwnable contract.
type ProposedOwnableRouterOwnershipRenounced struct {
	Renounced bool
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterRouterOwnershipRenounced is a free log retrieval operation binding the contract event 0x243ebbb2f905234bbf0556bb38e1f7c23b09ffd2e441a16e58b844eb2ab7a397.
//
// Solidity: event RouterOwnershipRenounced(bool renounced)
func (_ProposedOwnable *ProposedOwnableFilterer) FilterRouterOwnershipRenounced(opts *bind.FilterOpts) (*ProposedOwnableRouterOwnershipRenouncedIterator, error) {

	logs, sub, err := _ProposedOwnable.contract.FilterLogs(opts, "RouterOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableRouterOwnershipRenouncedIterator{contract: _ProposedOwnable.contract, event: "RouterOwnershipRenounced", logs: logs, sub: sub}, nil
}

// WatchRouterOwnershipRenounced is a free log subscription operation binding the contract event 0x243ebbb2f905234bbf0556bb38e1f7c23b09ffd2e441a16e58b844eb2ab7a397.
//
// Solidity: event RouterOwnershipRenounced(bool renounced)
func (_ProposedOwnable *ProposedOwnableFilterer) WatchRouterOwnershipRenounced(opts *bind.WatchOpts, sink chan<- *ProposedOwnableRouterOwnershipRenounced) (event.Subscription, error) {

	logs, sub, err := _ProposedOwnable.contract.WatchLogs(opts, "RouterOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ProposedOwnableRouterOwnershipRenounced)
				if err := _ProposedOwnable.contract.UnpackLog(event, "RouterOwnershipRenounced", log); err != nil {
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

// ParseRouterOwnershipRenounced is a log parse operation binding the contract event 0x243ebbb2f905234bbf0556bb38e1f7c23b09ffd2e441a16e58b844eb2ab7a397.
//
// Solidity: event RouterOwnershipRenounced(bool renounced)
func (_ProposedOwnable *ProposedOwnableFilterer) ParseRouterOwnershipRenounced(log types.Log) (*ProposedOwnableRouterOwnershipRenounced, error) {
	event := new(ProposedOwnableRouterOwnershipRenounced)
	if err := _ProposedOwnable.contract.UnpackLog(event, "RouterOwnershipRenounced", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ProposedOwnableRouterOwnershipRenunciationProposedIterator is returned from FilterRouterOwnershipRenunciationProposed and is used to iterate over the raw logs and unpacked data for RouterOwnershipRenunciationProposed events raised by the ProposedOwnable contract.
type ProposedOwnableRouterOwnershipRenunciationProposedIterator struct {
	Event *ProposedOwnableRouterOwnershipRenunciationProposed // Event containing the contract specifics and raw log

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
func (it *ProposedOwnableRouterOwnershipRenunciationProposedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ProposedOwnableRouterOwnershipRenunciationProposed)
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
		it.Event = new(ProposedOwnableRouterOwnershipRenunciationProposed)
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
func (it *ProposedOwnableRouterOwnershipRenunciationProposedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ProposedOwnableRouterOwnershipRenunciationProposedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ProposedOwnableRouterOwnershipRenunciationProposed represents a RouterOwnershipRenunciationProposed event raised by the ProposedOwnable contract.
type ProposedOwnableRouterOwnershipRenunciationProposed struct {
	Timestamp *big.Int
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterRouterOwnershipRenunciationProposed is a free log retrieval operation binding the contract event 0xa52048c5f468d21a62e4644ac4db19bcaa1a20f0cf37d163ba49c7217d35feb8.
//
// Solidity: event RouterOwnershipRenunciationProposed(uint256 timestamp)
func (_ProposedOwnable *ProposedOwnableFilterer) FilterRouterOwnershipRenunciationProposed(opts *bind.FilterOpts) (*ProposedOwnableRouterOwnershipRenunciationProposedIterator, error) {

	logs, sub, err := _ProposedOwnable.contract.FilterLogs(opts, "RouterOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return &ProposedOwnableRouterOwnershipRenunciationProposedIterator{contract: _ProposedOwnable.contract, event: "RouterOwnershipRenunciationProposed", logs: logs, sub: sub}, nil
}

// WatchRouterOwnershipRenunciationProposed is a free log subscription operation binding the contract event 0xa52048c5f468d21a62e4644ac4db19bcaa1a20f0cf37d163ba49c7217d35feb8.
//
// Solidity: event RouterOwnershipRenunciationProposed(uint256 timestamp)
func (_ProposedOwnable *ProposedOwnableFilterer) WatchRouterOwnershipRenunciationProposed(opts *bind.WatchOpts, sink chan<- *ProposedOwnableRouterOwnershipRenunciationProposed) (event.Subscription, error) {

	logs, sub, err := _ProposedOwnable.contract.WatchLogs(opts, "RouterOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ProposedOwnableRouterOwnershipRenunciationProposed)
				if err := _ProposedOwnable.contract.UnpackLog(event, "RouterOwnershipRenunciationProposed", log); err != nil {
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

// ParseRouterOwnershipRenunciationProposed is a log parse operation binding the contract event 0xa52048c5f468d21a62e4644ac4db19bcaa1a20f0cf37d163ba49c7217d35feb8.
//
// Solidity: event RouterOwnershipRenunciationProposed(uint256 timestamp)
func (_ProposedOwnable *ProposedOwnableFilterer) ParseRouterOwnershipRenunciationProposed(log types.Log) (*ProposedOwnableRouterOwnershipRenunciationProposed, error) {
	event := new(ProposedOwnableRouterOwnershipRenunciationProposed)
	if err := _ProposedOwnable.contract.UnpackLog(event, "RouterOwnershipRenunciationProposed", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}
