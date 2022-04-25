// Code generated - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package connext_price_oracle

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

// ConnextPriceOracleMetaData contains all meta data concerning the ConnextPriceOracle contract.
var ConnextPriceOracleMetaData = &bind.MetaData{
	ABI: "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_wrapped\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"tokenAddress\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"source\",\"type\":\"address\"}],\"name\":\"AggregatorUpdated\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"token\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"oldPrice\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"newPrice\",\"type\":\"uint256\"}],\"name\":\"DirectPriceUpdated\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"oldAdmin\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"newAdmin\",\"type\":\"address\"}],\"name\":\"NewAdmin\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"token\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"baseToken\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"lpToken\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"_active\",\"type\":\"bool\"}],\"name\":\"PriceRecordUpdated\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"oldAddress\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"newAddress\",\"type\":\"address\"}],\"name\":\"V1PriceOracleUpdated\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"admin\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"aggregators\",\"outputs\":[{\"internalType\":\"contractAggregatorV3Interface\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"assetPrices\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_tokenAddress\",\"type\":\"address\"}],\"name\":\"getPriceFromChainlink\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_tokenAddress\",\"type\":\"address\"}],\"name\":\"getPriceFromDex\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_tokenAddress\",\"type\":\"address\"}],\"name\":\"getPriceFromOracle\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_tokenAddress\",\"type\":\"address\"}],\"name\":\"getTokenPrice\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"isPriceOracle\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"priceRecords\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"baseToken\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"lpToken\",\"type\":\"address\"},{\"internalType\":\"bool\",\"name\":\"active\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newAdmin\",\"type\":\"address\"}],\"name\":\"setAdmin\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address[]\",\"name\":\"tokenAddresses\",\"type\":\"address[]\"},{\"internalType\":\"address[]\",\"name\":\"sources\",\"type\":\"address[]\"}],\"name\":\"setAggregators\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_baseToken\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_lpToken\",\"type\":\"address\"},{\"internalType\":\"bool\",\"name\":\"_active\",\"type\":\"bool\"}],\"name\":\"setDexPriceInfo\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_price\",\"type\":\"uint256\"}],\"name\":\"setDirectPrice\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_v1PriceOracle\",\"type\":\"address\"}],\"name\":\"setV1PriceOracle\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"v1PriceOracle\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"wrapped\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"}]",
}

// ConnextPriceOracleABI is the input ABI used to generate the binding from.
// Deprecated: Use ConnextPriceOracleMetaData.ABI instead.
var ConnextPriceOracleABI = ConnextPriceOracleMetaData.ABI

// ConnextPriceOracle is an auto generated Go binding around an Ethereum contract.
type ConnextPriceOracle struct {
	ConnextPriceOracleCaller     // Read-only binding to the contract
	ConnextPriceOracleTransactor // Write-only binding to the contract
	ConnextPriceOracleFilterer   // Log filterer for contract events
}

// ConnextPriceOracleCaller is an auto generated read-only Go binding around an Ethereum contract.
type ConnextPriceOracleCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// ConnextPriceOracleTransactor is an auto generated write-only Go binding around an Ethereum contract.
type ConnextPriceOracleTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// ConnextPriceOracleFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type ConnextPriceOracleFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// ConnextPriceOracleSession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type ConnextPriceOracleSession struct {
	Contract     *ConnextPriceOracle // Generic contract binding to set the session for
	CallOpts     bind.CallOpts       // Call options to use throughout this session
	TransactOpts bind.TransactOpts   // Transaction auth options to use throughout this session
}

// ConnextPriceOracleCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type ConnextPriceOracleCallerSession struct {
	Contract *ConnextPriceOracleCaller // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts             // Call options to use throughout this session
}

// ConnextPriceOracleTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type ConnextPriceOracleTransactorSession struct {
	Contract     *ConnextPriceOracleTransactor // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts             // Transaction auth options to use throughout this session
}

// ConnextPriceOracleRaw is an auto generated low-level Go binding around an Ethereum contract.
type ConnextPriceOracleRaw struct {
	Contract *ConnextPriceOracle // Generic contract binding to access the raw methods on
}

// ConnextPriceOracleCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type ConnextPriceOracleCallerRaw struct {
	Contract *ConnextPriceOracleCaller // Generic read-only contract binding to access the raw methods on
}

// ConnextPriceOracleTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type ConnextPriceOracleTransactorRaw struct {
	Contract *ConnextPriceOracleTransactor // Generic write-only contract binding to access the raw methods on
}

// NewConnextPriceOracle creates a new instance of ConnextPriceOracle, bound to a specific deployed contract.
func NewConnextPriceOracle(address common.Address, backend bind.ContractBackend) (*ConnextPriceOracle, error) {
	contract, err := bindConnextPriceOracle(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracle{ConnextPriceOracleCaller: ConnextPriceOracleCaller{contract: contract}, ConnextPriceOracleTransactor: ConnextPriceOracleTransactor{contract: contract}, ConnextPriceOracleFilterer: ConnextPriceOracleFilterer{contract: contract}}, nil
}

// NewConnextPriceOracleCaller creates a new read-only instance of ConnextPriceOracle, bound to a specific deployed contract.
func NewConnextPriceOracleCaller(address common.Address, caller bind.ContractCaller) (*ConnextPriceOracleCaller, error) {
	contract, err := bindConnextPriceOracle(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracleCaller{contract: contract}, nil
}

// NewConnextPriceOracleTransactor creates a new write-only instance of ConnextPriceOracle, bound to a specific deployed contract.
func NewConnextPriceOracleTransactor(address common.Address, transactor bind.ContractTransactor) (*ConnextPriceOracleTransactor, error) {
	contract, err := bindConnextPriceOracle(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracleTransactor{contract: contract}, nil
}

// NewConnextPriceOracleFilterer creates a new log filterer instance of ConnextPriceOracle, bound to a specific deployed contract.
func NewConnextPriceOracleFilterer(address common.Address, filterer bind.ContractFilterer) (*ConnextPriceOracleFilterer, error) {
	contract, err := bindConnextPriceOracle(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracleFilterer{contract: contract}, nil
}

// bindConnextPriceOracle binds a generic wrapper to an already deployed contract.
func bindConnextPriceOracle(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := abi.JSON(strings.NewReader(ConnextPriceOracleABI))
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_ConnextPriceOracle *ConnextPriceOracleRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _ConnextPriceOracle.Contract.ConnextPriceOracleCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_ConnextPriceOracle *ConnextPriceOracleRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.ConnextPriceOracleTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_ConnextPriceOracle *ConnextPriceOracleRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.ConnextPriceOracleTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_ConnextPriceOracle *ConnextPriceOracleCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _ConnextPriceOracle.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_ConnextPriceOracle *ConnextPriceOracleTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_ConnextPriceOracle *ConnextPriceOracleTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.contract.Transact(opts, method, params...)
}

// Admin is a free data retrieval call binding the contract method 0xf851a440.
//
// Solidity: function admin() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) Admin(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "admin")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Admin is a free data retrieval call binding the contract method 0xf851a440.
//
// Solidity: function admin() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleSession) Admin() (common.Address, error) {
	return _ConnextPriceOracle.Contract.Admin(&_ConnextPriceOracle.CallOpts)
}

// Admin is a free data retrieval call binding the contract method 0xf851a440.
//
// Solidity: function admin() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) Admin() (common.Address, error) {
	return _ConnextPriceOracle.Contract.Admin(&_ConnextPriceOracle.CallOpts)
}

// Aggregators is a free data retrieval call binding the contract method 0x112cdab9.
//
// Solidity: function aggregators(address ) view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) Aggregators(opts *bind.CallOpts, arg0 common.Address) (common.Address, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "aggregators", arg0)

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Aggregators is a free data retrieval call binding the contract method 0x112cdab9.
//
// Solidity: function aggregators(address ) view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleSession) Aggregators(arg0 common.Address) (common.Address, error) {
	return _ConnextPriceOracle.Contract.Aggregators(&_ConnextPriceOracle.CallOpts, arg0)
}

// Aggregators is a free data retrieval call binding the contract method 0x112cdab9.
//
// Solidity: function aggregators(address ) view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) Aggregators(arg0 common.Address) (common.Address, error) {
	return _ConnextPriceOracle.Contract.Aggregators(&_ConnextPriceOracle.CallOpts, arg0)
}

// AssetPrices is a free data retrieval call binding the contract method 0x5e9a523c.
//
// Solidity: function assetPrices(address ) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) AssetPrices(opts *bind.CallOpts, arg0 common.Address) (*big.Int, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "assetPrices", arg0)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// AssetPrices is a free data retrieval call binding the contract method 0x5e9a523c.
//
// Solidity: function assetPrices(address ) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleSession) AssetPrices(arg0 common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.AssetPrices(&_ConnextPriceOracle.CallOpts, arg0)
}

// AssetPrices is a free data retrieval call binding the contract method 0x5e9a523c.
//
// Solidity: function assetPrices(address ) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) AssetPrices(arg0 common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.AssetPrices(&_ConnextPriceOracle.CallOpts, arg0)
}

// GetPriceFromChainlink is a free data retrieval call binding the contract method 0x856d562d.
//
// Solidity: function getPriceFromChainlink(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) GetPriceFromChainlink(opts *bind.CallOpts, _tokenAddress common.Address) (*big.Int, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "getPriceFromChainlink", _tokenAddress)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// GetPriceFromChainlink is a free data retrieval call binding the contract method 0x856d562d.
//
// Solidity: function getPriceFromChainlink(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleSession) GetPriceFromChainlink(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetPriceFromChainlink(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// GetPriceFromChainlink is a free data retrieval call binding the contract method 0x856d562d.
//
// Solidity: function getPriceFromChainlink(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) GetPriceFromChainlink(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetPriceFromChainlink(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// GetPriceFromDex is a free data retrieval call binding the contract method 0x4c8e42a1.
//
// Solidity: function getPriceFromDex(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) GetPriceFromDex(opts *bind.CallOpts, _tokenAddress common.Address) (*big.Int, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "getPriceFromDex", _tokenAddress)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// GetPriceFromDex is a free data retrieval call binding the contract method 0x4c8e42a1.
//
// Solidity: function getPriceFromDex(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleSession) GetPriceFromDex(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetPriceFromDex(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// GetPriceFromDex is a free data retrieval call binding the contract method 0x4c8e42a1.
//
// Solidity: function getPriceFromDex(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) GetPriceFromDex(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetPriceFromDex(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// GetPriceFromOracle is a free data retrieval call binding the contract method 0x538e573c.
//
// Solidity: function getPriceFromOracle(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) GetPriceFromOracle(opts *bind.CallOpts, _tokenAddress common.Address) (*big.Int, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "getPriceFromOracle", _tokenAddress)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// GetPriceFromOracle is a free data retrieval call binding the contract method 0x538e573c.
//
// Solidity: function getPriceFromOracle(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleSession) GetPriceFromOracle(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetPriceFromOracle(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// GetPriceFromOracle is a free data retrieval call binding the contract method 0x538e573c.
//
// Solidity: function getPriceFromOracle(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) GetPriceFromOracle(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetPriceFromOracle(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// GetTokenPrice is a free data retrieval call binding the contract method 0xd02641a0.
//
// Solidity: function getTokenPrice(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) GetTokenPrice(opts *bind.CallOpts, _tokenAddress common.Address) (*big.Int, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "getTokenPrice", _tokenAddress)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// GetTokenPrice is a free data retrieval call binding the contract method 0xd02641a0.
//
// Solidity: function getTokenPrice(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleSession) GetTokenPrice(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetTokenPrice(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// GetTokenPrice is a free data retrieval call binding the contract method 0xd02641a0.
//
// Solidity: function getTokenPrice(address _tokenAddress) view returns(uint256)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) GetTokenPrice(_tokenAddress common.Address) (*big.Int, error) {
	return _ConnextPriceOracle.Contract.GetTokenPrice(&_ConnextPriceOracle.CallOpts, _tokenAddress)
}

// IsPriceOracle is a free data retrieval call binding the contract method 0x66331bba.
//
// Solidity: function isPriceOracle() view returns(bool)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) IsPriceOracle(opts *bind.CallOpts) (bool, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "isPriceOracle")

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// IsPriceOracle is a free data retrieval call binding the contract method 0x66331bba.
//
// Solidity: function isPriceOracle() view returns(bool)
func (_ConnextPriceOracle *ConnextPriceOracleSession) IsPriceOracle() (bool, error) {
	return _ConnextPriceOracle.Contract.IsPriceOracle(&_ConnextPriceOracle.CallOpts)
}

// IsPriceOracle is a free data retrieval call binding the contract method 0x66331bba.
//
// Solidity: function isPriceOracle() view returns(bool)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) IsPriceOracle() (bool, error) {
	return _ConnextPriceOracle.Contract.IsPriceOracle(&_ConnextPriceOracle.CallOpts)
}

// PriceRecords is a free data retrieval call binding the contract method 0xa2a870a9.
//
// Solidity: function priceRecords(address ) view returns(address token, address baseToken, address lpToken, bool active)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) PriceRecords(opts *bind.CallOpts, arg0 common.Address) (struct {
	Token     common.Address
	BaseToken common.Address
	LpToken   common.Address
	Active    bool
}, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "priceRecords", arg0)

	outstruct := new(struct {
		Token     common.Address
		BaseToken common.Address
		LpToken   common.Address
		Active    bool
	})
	if err != nil {
		return *outstruct, err
	}

	outstruct.Token = *abi.ConvertType(out[0], new(common.Address)).(*common.Address)
	outstruct.BaseToken = *abi.ConvertType(out[1], new(common.Address)).(*common.Address)
	outstruct.LpToken = *abi.ConvertType(out[2], new(common.Address)).(*common.Address)
	outstruct.Active = *abi.ConvertType(out[3], new(bool)).(*bool)

	return *outstruct, err

}

// PriceRecords is a free data retrieval call binding the contract method 0xa2a870a9.
//
// Solidity: function priceRecords(address ) view returns(address token, address baseToken, address lpToken, bool active)
func (_ConnextPriceOracle *ConnextPriceOracleSession) PriceRecords(arg0 common.Address) (struct {
	Token     common.Address
	BaseToken common.Address
	LpToken   common.Address
	Active    bool
}, error) {
	return _ConnextPriceOracle.Contract.PriceRecords(&_ConnextPriceOracle.CallOpts, arg0)
}

// PriceRecords is a free data retrieval call binding the contract method 0xa2a870a9.
//
// Solidity: function priceRecords(address ) view returns(address token, address baseToken, address lpToken, bool active)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) PriceRecords(arg0 common.Address) (struct {
	Token     common.Address
	BaseToken common.Address
	LpToken   common.Address
	Active    bool
}, error) {
	return _ConnextPriceOracle.Contract.PriceRecords(&_ConnextPriceOracle.CallOpts, arg0)
}

// V1PriceOracle is a free data retrieval call binding the contract method 0xfe10c98d.
//
// Solidity: function v1PriceOracle() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) V1PriceOracle(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "v1PriceOracle")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// V1PriceOracle is a free data retrieval call binding the contract method 0xfe10c98d.
//
// Solidity: function v1PriceOracle() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleSession) V1PriceOracle() (common.Address, error) {
	return _ConnextPriceOracle.Contract.V1PriceOracle(&_ConnextPriceOracle.CallOpts)
}

// V1PriceOracle is a free data retrieval call binding the contract method 0xfe10c98d.
//
// Solidity: function v1PriceOracle() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) V1PriceOracle() (common.Address, error) {
	return _ConnextPriceOracle.Contract.V1PriceOracle(&_ConnextPriceOracle.CallOpts)
}

// Wrapped is a free data retrieval call binding the contract method 0x50e70d48.
//
// Solidity: function wrapped() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCaller) Wrapped(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _ConnextPriceOracle.contract.Call(opts, &out, "wrapped")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Wrapped is a free data retrieval call binding the contract method 0x50e70d48.
//
// Solidity: function wrapped() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleSession) Wrapped() (common.Address, error) {
	return _ConnextPriceOracle.Contract.Wrapped(&_ConnextPriceOracle.CallOpts)
}

// Wrapped is a free data retrieval call binding the contract method 0x50e70d48.
//
// Solidity: function wrapped() view returns(address)
func (_ConnextPriceOracle *ConnextPriceOracleCallerSession) Wrapped() (common.Address, error) {
	return _ConnextPriceOracle.Contract.Wrapped(&_ConnextPriceOracle.CallOpts)
}

// SetAdmin is a paid mutator transaction binding the contract method 0x704b6c02.
//
// Solidity: function setAdmin(address newAdmin) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactor) SetAdmin(opts *bind.TransactOpts, newAdmin common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.contract.Transact(opts, "setAdmin", newAdmin)
}

// SetAdmin is a paid mutator transaction binding the contract method 0x704b6c02.
//
// Solidity: function setAdmin(address newAdmin) returns()
func (_ConnextPriceOracle *ConnextPriceOracleSession) SetAdmin(newAdmin common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetAdmin(&_ConnextPriceOracle.TransactOpts, newAdmin)
}

// SetAdmin is a paid mutator transaction binding the contract method 0x704b6c02.
//
// Solidity: function setAdmin(address newAdmin) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactorSession) SetAdmin(newAdmin common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetAdmin(&_ConnextPriceOracle.TransactOpts, newAdmin)
}

// SetAggregators is a paid mutator transaction binding the contract method 0x3f9fb505.
//
// Solidity: function setAggregators(address[] tokenAddresses, address[] sources) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactor) SetAggregators(opts *bind.TransactOpts, tokenAddresses []common.Address, sources []common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.contract.Transact(opts, "setAggregators", tokenAddresses, sources)
}

// SetAggregators is a paid mutator transaction binding the contract method 0x3f9fb505.
//
// Solidity: function setAggregators(address[] tokenAddresses, address[] sources) returns()
func (_ConnextPriceOracle *ConnextPriceOracleSession) SetAggregators(tokenAddresses []common.Address, sources []common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetAggregators(&_ConnextPriceOracle.TransactOpts, tokenAddresses, sources)
}

// SetAggregators is a paid mutator transaction binding the contract method 0x3f9fb505.
//
// Solidity: function setAggregators(address[] tokenAddresses, address[] sources) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactorSession) SetAggregators(tokenAddresses []common.Address, sources []common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetAggregators(&_ConnextPriceOracle.TransactOpts, tokenAddresses, sources)
}

// SetDexPriceInfo is a paid mutator transaction binding the contract method 0x1994b4fd.
//
// Solidity: function setDexPriceInfo(address _token, address _baseToken, address _lpToken, bool _active) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactor) SetDexPriceInfo(opts *bind.TransactOpts, _token common.Address, _baseToken common.Address, _lpToken common.Address, _active bool) (*types.Transaction, error) {
	return _ConnextPriceOracle.contract.Transact(opts, "setDexPriceInfo", _token, _baseToken, _lpToken, _active)
}

// SetDexPriceInfo is a paid mutator transaction binding the contract method 0x1994b4fd.
//
// Solidity: function setDexPriceInfo(address _token, address _baseToken, address _lpToken, bool _active) returns()
func (_ConnextPriceOracle *ConnextPriceOracleSession) SetDexPriceInfo(_token common.Address, _baseToken common.Address, _lpToken common.Address, _active bool) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetDexPriceInfo(&_ConnextPriceOracle.TransactOpts, _token, _baseToken, _lpToken, _active)
}

// SetDexPriceInfo is a paid mutator transaction binding the contract method 0x1994b4fd.
//
// Solidity: function setDexPriceInfo(address _token, address _baseToken, address _lpToken, bool _active) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactorSession) SetDexPriceInfo(_token common.Address, _baseToken common.Address, _lpToken common.Address, _active bool) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetDexPriceInfo(&_ConnextPriceOracle.TransactOpts, _token, _baseToken, _lpToken, _active)
}

// SetDirectPrice is a paid mutator transaction binding the contract method 0x09a8acb0.
//
// Solidity: function setDirectPrice(address _token, uint256 _price) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactor) SetDirectPrice(opts *bind.TransactOpts, _token common.Address, _price *big.Int) (*types.Transaction, error) {
	return _ConnextPriceOracle.contract.Transact(opts, "setDirectPrice", _token, _price)
}

// SetDirectPrice is a paid mutator transaction binding the contract method 0x09a8acb0.
//
// Solidity: function setDirectPrice(address _token, uint256 _price) returns()
func (_ConnextPriceOracle *ConnextPriceOracleSession) SetDirectPrice(_token common.Address, _price *big.Int) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetDirectPrice(&_ConnextPriceOracle.TransactOpts, _token, _price)
}

// SetDirectPrice is a paid mutator transaction binding the contract method 0x09a8acb0.
//
// Solidity: function setDirectPrice(address _token, uint256 _price) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactorSession) SetDirectPrice(_token common.Address, _price *big.Int) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetDirectPrice(&_ConnextPriceOracle.TransactOpts, _token, _price)
}

// SetV1PriceOracle is a paid mutator transaction binding the contract method 0xcb45c4f2.
//
// Solidity: function setV1PriceOracle(address _v1PriceOracle) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactor) SetV1PriceOracle(opts *bind.TransactOpts, _v1PriceOracle common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.contract.Transact(opts, "setV1PriceOracle", _v1PriceOracle)
}

// SetV1PriceOracle is a paid mutator transaction binding the contract method 0xcb45c4f2.
//
// Solidity: function setV1PriceOracle(address _v1PriceOracle) returns()
func (_ConnextPriceOracle *ConnextPriceOracleSession) SetV1PriceOracle(_v1PriceOracle common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetV1PriceOracle(&_ConnextPriceOracle.TransactOpts, _v1PriceOracle)
}

// SetV1PriceOracle is a paid mutator transaction binding the contract method 0xcb45c4f2.
//
// Solidity: function setV1PriceOracle(address _v1PriceOracle) returns()
func (_ConnextPriceOracle *ConnextPriceOracleTransactorSession) SetV1PriceOracle(_v1PriceOracle common.Address) (*types.Transaction, error) {
	return _ConnextPriceOracle.Contract.SetV1PriceOracle(&_ConnextPriceOracle.TransactOpts, _v1PriceOracle)
}

// ConnextPriceOracleAggregatorUpdatedIterator is returned from FilterAggregatorUpdated and is used to iterate over the raw logs and unpacked data for AggregatorUpdated events raised by the ConnextPriceOracle contract.
type ConnextPriceOracleAggregatorUpdatedIterator struct {
	Event *ConnextPriceOracleAggregatorUpdated // Event containing the contract specifics and raw log

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
func (it *ConnextPriceOracleAggregatorUpdatedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ConnextPriceOracleAggregatorUpdated)
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
		it.Event = new(ConnextPriceOracleAggregatorUpdated)
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
func (it *ConnextPriceOracleAggregatorUpdatedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ConnextPriceOracleAggregatorUpdatedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ConnextPriceOracleAggregatorUpdated represents a AggregatorUpdated event raised by the ConnextPriceOracle contract.
type ConnextPriceOracleAggregatorUpdated struct {
	TokenAddress common.Address
	Source       common.Address
	Raw          types.Log // Blockchain specific contextual infos
}

// FilterAggregatorUpdated is a free log retrieval operation binding the contract event 0x89baabef7dfd0683c0ac16fd2a8431c51b49fbe654c3f7b5ef19763e2ccd88f2.
//
// Solidity: event AggregatorUpdated(address tokenAddress, address source)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) FilterAggregatorUpdated(opts *bind.FilterOpts) (*ConnextPriceOracleAggregatorUpdatedIterator, error) {

	logs, sub, err := _ConnextPriceOracle.contract.FilterLogs(opts, "AggregatorUpdated")
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracleAggregatorUpdatedIterator{contract: _ConnextPriceOracle.contract, event: "AggregatorUpdated", logs: logs, sub: sub}, nil
}

// WatchAggregatorUpdated is a free log subscription operation binding the contract event 0x89baabef7dfd0683c0ac16fd2a8431c51b49fbe654c3f7b5ef19763e2ccd88f2.
//
// Solidity: event AggregatorUpdated(address tokenAddress, address source)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) WatchAggregatorUpdated(opts *bind.WatchOpts, sink chan<- *ConnextPriceOracleAggregatorUpdated) (event.Subscription, error) {

	logs, sub, err := _ConnextPriceOracle.contract.WatchLogs(opts, "AggregatorUpdated")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ConnextPriceOracleAggregatorUpdated)
				if err := _ConnextPriceOracle.contract.UnpackLog(event, "AggregatorUpdated", log); err != nil {
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

// ParseAggregatorUpdated is a log parse operation binding the contract event 0x89baabef7dfd0683c0ac16fd2a8431c51b49fbe654c3f7b5ef19763e2ccd88f2.
//
// Solidity: event AggregatorUpdated(address tokenAddress, address source)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) ParseAggregatorUpdated(log types.Log) (*ConnextPriceOracleAggregatorUpdated, error) {
	event := new(ConnextPriceOracleAggregatorUpdated)
	if err := _ConnextPriceOracle.contract.UnpackLog(event, "AggregatorUpdated", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ConnextPriceOracleDirectPriceUpdatedIterator is returned from FilterDirectPriceUpdated and is used to iterate over the raw logs and unpacked data for DirectPriceUpdated events raised by the ConnextPriceOracle contract.
type ConnextPriceOracleDirectPriceUpdatedIterator struct {
	Event *ConnextPriceOracleDirectPriceUpdated // Event containing the contract specifics and raw log

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
func (it *ConnextPriceOracleDirectPriceUpdatedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ConnextPriceOracleDirectPriceUpdated)
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
		it.Event = new(ConnextPriceOracleDirectPriceUpdated)
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
func (it *ConnextPriceOracleDirectPriceUpdatedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ConnextPriceOracleDirectPriceUpdatedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ConnextPriceOracleDirectPriceUpdated represents a DirectPriceUpdated event raised by the ConnextPriceOracle contract.
type ConnextPriceOracleDirectPriceUpdated struct {
	Token    common.Address
	OldPrice *big.Int
	NewPrice *big.Int
	Raw      types.Log // Blockchain specific contextual infos
}

// FilterDirectPriceUpdated is a free log retrieval operation binding the contract event 0xe2c8fb681c257e4e8df5ef1c464cff10ce6b072837628c9b6de5e7239a483e5d.
//
// Solidity: event DirectPriceUpdated(address token, uint256 oldPrice, uint256 newPrice)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) FilterDirectPriceUpdated(opts *bind.FilterOpts) (*ConnextPriceOracleDirectPriceUpdatedIterator, error) {

	logs, sub, err := _ConnextPriceOracle.contract.FilterLogs(opts, "DirectPriceUpdated")
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracleDirectPriceUpdatedIterator{contract: _ConnextPriceOracle.contract, event: "DirectPriceUpdated", logs: logs, sub: sub}, nil
}

// WatchDirectPriceUpdated is a free log subscription operation binding the contract event 0xe2c8fb681c257e4e8df5ef1c464cff10ce6b072837628c9b6de5e7239a483e5d.
//
// Solidity: event DirectPriceUpdated(address token, uint256 oldPrice, uint256 newPrice)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) WatchDirectPriceUpdated(opts *bind.WatchOpts, sink chan<- *ConnextPriceOracleDirectPriceUpdated) (event.Subscription, error) {

	logs, sub, err := _ConnextPriceOracle.contract.WatchLogs(opts, "DirectPriceUpdated")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ConnextPriceOracleDirectPriceUpdated)
				if err := _ConnextPriceOracle.contract.UnpackLog(event, "DirectPriceUpdated", log); err != nil {
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

// ParseDirectPriceUpdated is a log parse operation binding the contract event 0xe2c8fb681c257e4e8df5ef1c464cff10ce6b072837628c9b6de5e7239a483e5d.
//
// Solidity: event DirectPriceUpdated(address token, uint256 oldPrice, uint256 newPrice)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) ParseDirectPriceUpdated(log types.Log) (*ConnextPriceOracleDirectPriceUpdated, error) {
	event := new(ConnextPriceOracleDirectPriceUpdated)
	if err := _ConnextPriceOracle.contract.UnpackLog(event, "DirectPriceUpdated", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ConnextPriceOracleNewAdminIterator is returned from FilterNewAdmin and is used to iterate over the raw logs and unpacked data for NewAdmin events raised by the ConnextPriceOracle contract.
type ConnextPriceOracleNewAdminIterator struct {
	Event *ConnextPriceOracleNewAdmin // Event containing the contract specifics and raw log

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
func (it *ConnextPriceOracleNewAdminIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ConnextPriceOracleNewAdmin)
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
		it.Event = new(ConnextPriceOracleNewAdmin)
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
func (it *ConnextPriceOracleNewAdminIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ConnextPriceOracleNewAdminIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ConnextPriceOracleNewAdmin represents a NewAdmin event raised by the ConnextPriceOracle contract.
type ConnextPriceOracleNewAdmin struct {
	OldAdmin common.Address
	NewAdmin common.Address
	Raw      types.Log // Blockchain specific contextual infos
}

// FilterNewAdmin is a free log retrieval operation binding the contract event 0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc.
//
// Solidity: event NewAdmin(address oldAdmin, address newAdmin)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) FilterNewAdmin(opts *bind.FilterOpts) (*ConnextPriceOracleNewAdminIterator, error) {

	logs, sub, err := _ConnextPriceOracle.contract.FilterLogs(opts, "NewAdmin")
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracleNewAdminIterator{contract: _ConnextPriceOracle.contract, event: "NewAdmin", logs: logs, sub: sub}, nil
}

// WatchNewAdmin is a free log subscription operation binding the contract event 0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc.
//
// Solidity: event NewAdmin(address oldAdmin, address newAdmin)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) WatchNewAdmin(opts *bind.WatchOpts, sink chan<- *ConnextPriceOracleNewAdmin) (event.Subscription, error) {

	logs, sub, err := _ConnextPriceOracle.contract.WatchLogs(opts, "NewAdmin")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ConnextPriceOracleNewAdmin)
				if err := _ConnextPriceOracle.contract.UnpackLog(event, "NewAdmin", log); err != nil {
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

// ParseNewAdmin is a log parse operation binding the contract event 0xf9ffabca9c8276e99321725bcb43fb076a6c66a54b7f21c4e8146d8519b417dc.
//
// Solidity: event NewAdmin(address oldAdmin, address newAdmin)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) ParseNewAdmin(log types.Log) (*ConnextPriceOracleNewAdmin, error) {
	event := new(ConnextPriceOracleNewAdmin)
	if err := _ConnextPriceOracle.contract.UnpackLog(event, "NewAdmin", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ConnextPriceOraclePriceRecordUpdatedIterator is returned from FilterPriceRecordUpdated and is used to iterate over the raw logs and unpacked data for PriceRecordUpdated events raised by the ConnextPriceOracle contract.
type ConnextPriceOraclePriceRecordUpdatedIterator struct {
	Event *ConnextPriceOraclePriceRecordUpdated // Event containing the contract specifics and raw log

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
func (it *ConnextPriceOraclePriceRecordUpdatedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ConnextPriceOraclePriceRecordUpdated)
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
		it.Event = new(ConnextPriceOraclePriceRecordUpdated)
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
func (it *ConnextPriceOraclePriceRecordUpdatedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ConnextPriceOraclePriceRecordUpdatedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ConnextPriceOraclePriceRecordUpdated represents a PriceRecordUpdated event raised by the ConnextPriceOracle contract.
type ConnextPriceOraclePriceRecordUpdated struct {
	Token     common.Address
	BaseToken common.Address
	LpToken   common.Address
	Active    bool
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterPriceRecordUpdated is a free log retrieval operation binding the contract event 0x896c992bf7fd70df3a83c741812b6b20c1da89e5efeaefa1fde40987c7e91a12.
//
// Solidity: event PriceRecordUpdated(address token, address baseToken, address lpToken, bool _active)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) FilterPriceRecordUpdated(opts *bind.FilterOpts) (*ConnextPriceOraclePriceRecordUpdatedIterator, error) {

	logs, sub, err := _ConnextPriceOracle.contract.FilterLogs(opts, "PriceRecordUpdated")
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOraclePriceRecordUpdatedIterator{contract: _ConnextPriceOracle.contract, event: "PriceRecordUpdated", logs: logs, sub: sub}, nil
}

// WatchPriceRecordUpdated is a free log subscription operation binding the contract event 0x896c992bf7fd70df3a83c741812b6b20c1da89e5efeaefa1fde40987c7e91a12.
//
// Solidity: event PriceRecordUpdated(address token, address baseToken, address lpToken, bool _active)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) WatchPriceRecordUpdated(opts *bind.WatchOpts, sink chan<- *ConnextPriceOraclePriceRecordUpdated) (event.Subscription, error) {

	logs, sub, err := _ConnextPriceOracle.contract.WatchLogs(opts, "PriceRecordUpdated")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ConnextPriceOraclePriceRecordUpdated)
				if err := _ConnextPriceOracle.contract.UnpackLog(event, "PriceRecordUpdated", log); err != nil {
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

// ParsePriceRecordUpdated is a log parse operation binding the contract event 0x896c992bf7fd70df3a83c741812b6b20c1da89e5efeaefa1fde40987c7e91a12.
//
// Solidity: event PriceRecordUpdated(address token, address baseToken, address lpToken, bool _active)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) ParsePriceRecordUpdated(log types.Log) (*ConnextPriceOraclePriceRecordUpdated, error) {
	event := new(ConnextPriceOraclePriceRecordUpdated)
	if err := _ConnextPriceOracle.contract.UnpackLog(event, "PriceRecordUpdated", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// ConnextPriceOracleV1PriceOracleUpdatedIterator is returned from FilterV1PriceOracleUpdated and is used to iterate over the raw logs and unpacked data for V1PriceOracleUpdated events raised by the ConnextPriceOracle contract.
type ConnextPriceOracleV1PriceOracleUpdatedIterator struct {
	Event *ConnextPriceOracleV1PriceOracleUpdated // Event containing the contract specifics and raw log

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
func (it *ConnextPriceOracleV1PriceOracleUpdatedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(ConnextPriceOracleV1PriceOracleUpdated)
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
		it.Event = new(ConnextPriceOracleV1PriceOracleUpdated)
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
func (it *ConnextPriceOracleV1PriceOracleUpdatedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *ConnextPriceOracleV1PriceOracleUpdatedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// ConnextPriceOracleV1PriceOracleUpdated represents a V1PriceOracleUpdated event raised by the ConnextPriceOracle contract.
type ConnextPriceOracleV1PriceOracleUpdated struct {
	OldAddress common.Address
	NewAddress common.Address
	Raw        types.Log // Blockchain specific contextual infos
}

// FilterV1PriceOracleUpdated is a free log retrieval operation binding the contract event 0x42e2900b37aa23ca681e13d6efc8018181fa216ca6676cf2b983e00e056afc2c.
//
// Solidity: event V1PriceOracleUpdated(address oldAddress, address newAddress)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) FilterV1PriceOracleUpdated(opts *bind.FilterOpts) (*ConnextPriceOracleV1PriceOracleUpdatedIterator, error) {

	logs, sub, err := _ConnextPriceOracle.contract.FilterLogs(opts, "V1PriceOracleUpdated")
	if err != nil {
		return nil, err
	}
	return &ConnextPriceOracleV1PriceOracleUpdatedIterator{contract: _ConnextPriceOracle.contract, event: "V1PriceOracleUpdated", logs: logs, sub: sub}, nil
}

// WatchV1PriceOracleUpdated is a free log subscription operation binding the contract event 0x42e2900b37aa23ca681e13d6efc8018181fa216ca6676cf2b983e00e056afc2c.
//
// Solidity: event V1PriceOracleUpdated(address oldAddress, address newAddress)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) WatchV1PriceOracleUpdated(opts *bind.WatchOpts, sink chan<- *ConnextPriceOracleV1PriceOracleUpdated) (event.Subscription, error) {

	logs, sub, err := _ConnextPriceOracle.contract.WatchLogs(opts, "V1PriceOracleUpdated")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(ConnextPriceOracleV1PriceOracleUpdated)
				if err := _ConnextPriceOracle.contract.UnpackLog(event, "V1PriceOracleUpdated", log); err != nil {
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

// ParseV1PriceOracleUpdated is a log parse operation binding the contract event 0x42e2900b37aa23ca681e13d6efc8018181fa216ca6676cf2b983e00e056afc2c.
//
// Solidity: event V1PriceOracleUpdated(address oldAddress, address newAddress)
func (_ConnextPriceOracle *ConnextPriceOracleFilterer) ParseV1PriceOracleUpdated(log types.Log) (*ConnextPriceOracleV1PriceOracleUpdated, error) {
	event := new(ConnextPriceOracleV1PriceOracleUpdated)
	if err := _ConnextPriceOracle.contract.UnpackLog(event, "V1PriceOracleUpdated", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}
