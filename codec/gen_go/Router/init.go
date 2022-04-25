// Code generated - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package Router

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

// ITransactionManagerCancelArgs is an auto generated low-level Go binding around an user-defined struct.
type ITransactionManagerCancelArgs struct {
	TxData      ITransactionManagerTransactionData
	Signature   []byte
	EncodedMeta []byte
}

// ITransactionManagerFulfillArgs is an auto generated low-level Go binding around an user-defined struct.
type ITransactionManagerFulfillArgs struct {
	TxData      ITransactionManagerTransactionData
	RelayerFee  *big.Int
	Signature   []byte
	CallData    []byte
	EncodedMeta []byte
}

// ITransactionManagerInvariantTransactionData is an auto generated low-level Go binding around an user-defined struct.
type ITransactionManagerInvariantTransactionData struct {
	ReceivingChainTxManagerAddress common.Address
	User                           common.Address
	Router                         common.Address
	Initiator                      common.Address
	SendingAssetId                 common.Address
	ReceivingAssetId               common.Address
	SendingChainFallback           common.Address
	ReceivingAddress               common.Address
	CallTo                         common.Address
	SendingChainId                 *big.Int
	ReceivingChainId               *big.Int
	CallDataHash                   [32]byte
	TransactionId                  [32]byte
}

// ITransactionManagerPrepareArgs is an auto generated low-level Go binding around an user-defined struct.
type ITransactionManagerPrepareArgs struct {
	InvariantData     ITransactionManagerInvariantTransactionData
	Amount            *big.Int
	Expiry            *big.Int
	EncryptedCallData []byte
	EncodedBid        []byte
	BidSignature      []byte
	EncodedMeta       []byte
}

// ITransactionManagerTransactionData is an auto generated low-level Go binding around an user-defined struct.
type ITransactionManagerTransactionData struct {
	ReceivingChainTxManagerAddress common.Address
	User                           common.Address
	Router                         common.Address
	Initiator                      common.Address
	SendingAssetId                 common.Address
	ReceivingAssetId               common.Address
	SendingChainFallback           common.Address
	ReceivingAddress               common.Address
	CallTo                         common.Address
	CallDataHash                   [32]byte
	TransactionId                  [32]byte
	SendingChainId                 *big.Int
	ReceivingChainId               *big.Int
	Amount                         *big.Int
	Expiry                         *big.Int
	PreparedBlockNumber            *big.Int
}

// RouterMetaData contains all meta data concerning the Router contract.
var RouterMetaData = &bind.MetaData{
	ABI: "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_routerFactory\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"indexed\":false,\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"Cancel\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"indexed\":false,\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"Fulfill\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"}],\"indexed\":false,\"internalType\":\"structITransactionManager.InvariantTransactionData\",\"name\":\"invariantData\",\"type\":\"tuple\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"Prepare\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"RelayerFeeAdded\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"RelayerFeeRemoved\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"RemoveLiquidity\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"}],\"name\":\"addRelayerFee\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"internalType\":\"structITransactionManager.CancelArgs\",\"name\":\"args\",\"type\":\"tuple\"},{\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"}],\"name\":\"cancel\",\"outputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"internalType\":\"uint256\",\"name\":\"relayerFee\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"callData\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"internalType\":\"structITransactionManager.FulfillArgs\",\"name\":\"args\",\"type\":\"tuple\"},{\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"}],\"name\":\"fulfill\",\"outputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_transactionManager\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_chainId\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"_routerSigner\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_recipient\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_owner\",\"type\":\"address\"}],\"name\":\"init\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"}],\"internalType\":\"structITransactionManager.InvariantTransactionData\",\"name\":\"invariantData\",\"type\":\"tuple\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"encryptedCallData\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedBid\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"bidSignature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"internalType\":\"structITransactionManager.PrepareArgs\",\"name\":\"args\",\"type\":\"tuple\"},{\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"}],\"name\":\"prepare\",\"outputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"recipient\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"routerRelayerFeeAsset\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"routerRelayerFee\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"}],\"name\":\"removeLiquidity\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"}],\"name\":\"removeRelayerFee\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"routerFactory\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"routerSigner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_recipient\",\"type\":\"address\"}],\"name\":\"setRecipient\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_routerSigner\",\"type\":\"address\"}],\"name\":\"setSigner\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"transactionManager\",\"outputs\":[{\"internalType\":\"contractITransactionManager\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"stateMutability\":\"payable\",\"type\":\"receive\"}]",
}

// RouterABI is the input ABI used to generate the binding from.
// Deprecated: Use RouterMetaData.ABI instead.
var RouterABI = RouterMetaData.ABI

// Router is an auto generated Go binding around an Ethereum contract.
type Router struct {
	RouterCaller     // Read-only binding to the contract
	RouterTransactor // Write-only binding to the contract
	RouterFilterer   // Log filterer for contract events
}

// RouterCaller is an auto generated read-only Go binding around an Ethereum contract.
type RouterCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// RouterTransactor is an auto generated write-only Go binding around an Ethereum contract.
type RouterTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// RouterFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type RouterFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// RouterSession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type RouterSession struct {
	Contract     *Router           // Generic contract binding to set the session for
	CallOpts     bind.CallOpts     // Call options to use throughout this session
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// RouterCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type RouterCallerSession struct {
	Contract *RouterCaller // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts // Call options to use throughout this session
}

// RouterTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type RouterTransactorSession struct {
	Contract     *RouterTransactor // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// RouterRaw is an auto generated low-level Go binding around an Ethereum contract.
type RouterRaw struct {
	Contract *Router // Generic contract binding to access the raw methods on
}

// RouterCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type RouterCallerRaw struct {
	Contract *RouterCaller // Generic read-only contract binding to access the raw methods on
}

// RouterTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type RouterTransactorRaw struct {
	Contract *RouterTransactor // Generic write-only contract binding to access the raw methods on
}

// NewRouter creates a new instance of Router, bound to a specific deployed contract.
func NewRouter(address common.Address, backend bind.ContractBackend) (*Router, error) {
	contract, err := bindRouter(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &Router{RouterCaller: RouterCaller{contract: contract}, RouterTransactor: RouterTransactor{contract: contract}, RouterFilterer: RouterFilterer{contract: contract}}, nil
}

// NewRouterCaller creates a new read-only instance of Router, bound to a specific deployed contract.
func NewRouterCaller(address common.Address, caller bind.ContractCaller) (*RouterCaller, error) {
	contract, err := bindRouter(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &RouterCaller{contract: contract}, nil
}

// NewRouterTransactor creates a new write-only instance of Router, bound to a specific deployed contract.
func NewRouterTransactor(address common.Address, transactor bind.ContractTransactor) (*RouterTransactor, error) {
	contract, err := bindRouter(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &RouterTransactor{contract: contract}, nil
}

// NewRouterFilterer creates a new log filterer instance of Router, bound to a specific deployed contract.
func NewRouterFilterer(address common.Address, filterer bind.ContractFilterer) (*RouterFilterer, error) {
	contract, err := bindRouter(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &RouterFilterer{contract: contract}, nil
}

// bindRouter binds a generic wrapper to an already deployed contract.
func bindRouter(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := abi.JSON(strings.NewReader(RouterABI))
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_Router *RouterRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _Router.Contract.RouterCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_Router *RouterRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _Router.Contract.RouterTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_Router *RouterRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _Router.Contract.RouterTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_Router *RouterCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _Router.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_Router *RouterTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _Router.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_Router *RouterTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _Router.Contract.contract.Transact(opts, method, params...)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_Router *RouterCaller) Owner(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _Router.contract.Call(opts, &out, "owner")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_Router *RouterSession) Owner() (common.Address, error) {
	return _Router.Contract.Owner(&_Router.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_Router *RouterCallerSession) Owner() (common.Address, error) {
	return _Router.Contract.Owner(&_Router.CallOpts)
}

// Recipient is a free data retrieval call binding the contract method 0x66d003ac.
//
// Solidity: function recipient() view returns(address)
func (_Router *RouterCaller) Recipient(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _Router.contract.Call(opts, &out, "recipient")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Recipient is a free data retrieval call binding the contract method 0x66d003ac.
//
// Solidity: function recipient() view returns(address)
func (_Router *RouterSession) Recipient() (common.Address, error) {
	return _Router.Contract.Recipient(&_Router.CallOpts)
}

// Recipient is a free data retrieval call binding the contract method 0x66d003ac.
//
// Solidity: function recipient() view returns(address)
func (_Router *RouterCallerSession) Recipient() (common.Address, error) {
	return _Router.Contract.Recipient(&_Router.CallOpts)
}

// RouterFactory is a free data retrieval call binding the contract method 0x4ba51437.
//
// Solidity: function routerFactory() view returns(address)
func (_Router *RouterCaller) RouterFactory(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _Router.contract.Call(opts, &out, "routerFactory")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// RouterFactory is a free data retrieval call binding the contract method 0x4ba51437.
//
// Solidity: function routerFactory() view returns(address)
func (_Router *RouterSession) RouterFactory() (common.Address, error) {
	return _Router.Contract.RouterFactory(&_Router.CallOpts)
}

// RouterFactory is a free data retrieval call binding the contract method 0x4ba51437.
//
// Solidity: function routerFactory() view returns(address)
func (_Router *RouterCallerSession) RouterFactory() (common.Address, error) {
	return _Router.Contract.RouterFactory(&_Router.CallOpts)
}

// RouterSigner is a free data retrieval call binding the contract method 0x3411dbdc.
//
// Solidity: function routerSigner() view returns(address)
func (_Router *RouterCaller) RouterSigner(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _Router.contract.Call(opts, &out, "routerSigner")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// RouterSigner is a free data retrieval call binding the contract method 0x3411dbdc.
//
// Solidity: function routerSigner() view returns(address)
func (_Router *RouterSession) RouterSigner() (common.Address, error) {
	return _Router.Contract.RouterSigner(&_Router.CallOpts)
}

// RouterSigner is a free data retrieval call binding the contract method 0x3411dbdc.
//
// Solidity: function routerSigner() view returns(address)
func (_Router *RouterCallerSession) RouterSigner() (common.Address, error) {
	return _Router.Contract.RouterSigner(&_Router.CallOpts)
}

// TransactionManager is a free data retrieval call binding the contract method 0x3b716452.
//
// Solidity: function transactionManager() view returns(address)
func (_Router *RouterCaller) TransactionManager(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _Router.contract.Call(opts, &out, "transactionManager")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// TransactionManager is a free data retrieval call binding the contract method 0x3b716452.
//
// Solidity: function transactionManager() view returns(address)
func (_Router *RouterSession) TransactionManager() (common.Address, error) {
	return _Router.Contract.TransactionManager(&_Router.CallOpts)
}

// TransactionManager is a free data retrieval call binding the contract method 0x3b716452.
//
// Solidity: function transactionManager() view returns(address)
func (_Router *RouterCallerSession) TransactionManager() (common.Address, error) {
	return _Router.Contract.TransactionManager(&_Router.CallOpts)
}

// AddRelayerFee is a paid mutator transaction binding the contract method 0xfc6bee13.
//
// Solidity: function addRelayerFee(uint256 amount, address assetId) payable returns()
func (_Router *RouterTransactor) AddRelayerFee(opts *bind.TransactOpts, amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "addRelayerFee", amount, assetId)
}

// AddRelayerFee is a paid mutator transaction binding the contract method 0xfc6bee13.
//
// Solidity: function addRelayerFee(uint256 amount, address assetId) payable returns()
func (_Router *RouterSession) AddRelayerFee(amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _Router.Contract.AddRelayerFee(&_Router.TransactOpts, amount, assetId)
}

// AddRelayerFee is a paid mutator transaction binding the contract method 0xfc6bee13.
//
// Solidity: function addRelayerFee(uint256 amount, address assetId) payable returns()
func (_Router *RouterTransactorSession) AddRelayerFee(amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _Router.Contract.AddRelayerFee(&_Router.TransactOpts, amount, assetId)
}

// Cancel is a paid mutator transaction binding the contract method 0xd42030ed.
//
// Solidity: function cancel(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterTransactor) Cancel(opts *bind.TransactOpts, args ITransactionManagerCancelArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "cancel", args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Cancel is a paid mutator transaction binding the contract method 0xd42030ed.
//
// Solidity: function cancel(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterSession) Cancel(args ITransactionManagerCancelArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.Cancel(&_Router.TransactOpts, args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Cancel is a paid mutator transaction binding the contract method 0xd42030ed.
//
// Solidity: function cancel(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterTransactorSession) Cancel(args ITransactionManagerCancelArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.Cancel(&_Router.TransactOpts, args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Fulfill is a paid mutator transaction binding the contract method 0x6e2054a9.
//
// Solidity: function fulfill(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterTransactor) Fulfill(opts *bind.TransactOpts, args ITransactionManagerFulfillArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "fulfill", args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Fulfill is a paid mutator transaction binding the contract method 0x6e2054a9.
//
// Solidity: function fulfill(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterSession) Fulfill(args ITransactionManagerFulfillArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.Fulfill(&_Router.TransactOpts, args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Fulfill is a paid mutator transaction binding the contract method 0x6e2054a9.
//
// Solidity: function fulfill(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterTransactorSession) Fulfill(args ITransactionManagerFulfillArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.Fulfill(&_Router.TransactOpts, args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Init is a paid mutator transaction binding the contract method 0x44bd3765.
//
// Solidity: function init(address _transactionManager, uint256 _chainId, address _routerSigner, address _recipient, address _owner) returns()
func (_Router *RouterTransactor) Init(opts *bind.TransactOpts, _transactionManager common.Address, _chainId *big.Int, _routerSigner common.Address, _recipient common.Address, _owner common.Address) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "init", _transactionManager, _chainId, _routerSigner, _recipient, _owner)
}

// Init is a paid mutator transaction binding the contract method 0x44bd3765.
//
// Solidity: function init(address _transactionManager, uint256 _chainId, address _routerSigner, address _recipient, address _owner) returns()
func (_Router *RouterSession) Init(_transactionManager common.Address, _chainId *big.Int, _routerSigner common.Address, _recipient common.Address, _owner common.Address) (*types.Transaction, error) {
	return _Router.Contract.Init(&_Router.TransactOpts, _transactionManager, _chainId, _routerSigner, _recipient, _owner)
}

// Init is a paid mutator transaction binding the contract method 0x44bd3765.
//
// Solidity: function init(address _transactionManager, uint256 _chainId, address _routerSigner, address _recipient, address _owner) returns()
func (_Router *RouterTransactorSession) Init(_transactionManager common.Address, _chainId *big.Int, _routerSigner common.Address, _recipient common.Address, _owner common.Address) (*types.Transaction, error) {
	return _Router.Contract.Init(&_Router.TransactOpts, _transactionManager, _chainId, _routerSigner, _recipient, _owner)
}

// Prepare is a paid mutator transaction binding the contract method 0xce976539.
//
// Solidity: function prepare(((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) payable returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterTransactor) Prepare(opts *bind.TransactOpts, args ITransactionManagerPrepareArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "prepare", args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Prepare is a paid mutator transaction binding the contract method 0xce976539.
//
// Solidity: function prepare(((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) payable returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterSession) Prepare(args ITransactionManagerPrepareArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.Prepare(&_Router.TransactOpts, args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// Prepare is a paid mutator transaction binding the contract method 0xce976539.
//
// Solidity: function prepare(((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) payable returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_Router *RouterTransactorSession) Prepare(args ITransactionManagerPrepareArgs, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.Prepare(&_Router.TransactOpts, args, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// RemoveLiquidity is a paid mutator transaction binding the contract method 0x82977466.
//
// Solidity: function removeLiquidity(uint256 amount, address assetId, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns()
func (_Router *RouterTransactor) RemoveLiquidity(opts *bind.TransactOpts, amount *big.Int, assetId common.Address, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "removeLiquidity", amount, assetId, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// RemoveLiquidity is a paid mutator transaction binding the contract method 0x82977466.
//
// Solidity: function removeLiquidity(uint256 amount, address assetId, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns()
func (_Router *RouterSession) RemoveLiquidity(amount *big.Int, assetId common.Address, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.RemoveLiquidity(&_Router.TransactOpts, amount, assetId, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// RemoveLiquidity is a paid mutator transaction binding the contract method 0x82977466.
//
// Solidity: function removeLiquidity(uint256 amount, address assetId, address routerRelayerFeeAsset, uint256 routerRelayerFee, bytes signature) returns()
func (_Router *RouterTransactorSession) RemoveLiquidity(amount *big.Int, assetId common.Address, routerRelayerFeeAsset common.Address, routerRelayerFee *big.Int, signature []byte) (*types.Transaction, error) {
	return _Router.Contract.RemoveLiquidity(&_Router.TransactOpts, amount, assetId, routerRelayerFeeAsset, routerRelayerFee, signature)
}

// RemoveRelayerFee is a paid mutator transaction binding the contract method 0x4f64cfc5.
//
// Solidity: function removeRelayerFee(uint256 amount, address assetId) returns()
func (_Router *RouterTransactor) RemoveRelayerFee(opts *bind.TransactOpts, amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "removeRelayerFee", amount, assetId)
}

// RemoveRelayerFee is a paid mutator transaction binding the contract method 0x4f64cfc5.
//
// Solidity: function removeRelayerFee(uint256 amount, address assetId) returns()
func (_Router *RouterSession) RemoveRelayerFee(amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _Router.Contract.RemoveRelayerFee(&_Router.TransactOpts, amount, assetId)
}

// RemoveRelayerFee is a paid mutator transaction binding the contract method 0x4f64cfc5.
//
// Solidity: function removeRelayerFee(uint256 amount, address assetId) returns()
func (_Router *RouterTransactorSession) RemoveRelayerFee(amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _Router.Contract.RemoveRelayerFee(&_Router.TransactOpts, amount, assetId)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_Router *RouterTransactor) RenounceOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "renounceOwnership")
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_Router *RouterSession) RenounceOwnership() (*types.Transaction, error) {
	return _Router.Contract.RenounceOwnership(&_Router.TransactOpts)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_Router *RouterTransactorSession) RenounceOwnership() (*types.Transaction, error) {
	return _Router.Contract.RenounceOwnership(&_Router.TransactOpts)
}

// SetRecipient is a paid mutator transaction binding the contract method 0x3bbed4a0.
//
// Solidity: function setRecipient(address _recipient) returns()
func (_Router *RouterTransactor) SetRecipient(opts *bind.TransactOpts, _recipient common.Address) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "setRecipient", _recipient)
}

// SetRecipient is a paid mutator transaction binding the contract method 0x3bbed4a0.
//
// Solidity: function setRecipient(address _recipient) returns()
func (_Router *RouterSession) SetRecipient(_recipient common.Address) (*types.Transaction, error) {
	return _Router.Contract.SetRecipient(&_Router.TransactOpts, _recipient)
}

// SetRecipient is a paid mutator transaction binding the contract method 0x3bbed4a0.
//
// Solidity: function setRecipient(address _recipient) returns()
func (_Router *RouterTransactorSession) SetRecipient(_recipient common.Address) (*types.Transaction, error) {
	return _Router.Contract.SetRecipient(&_Router.TransactOpts, _recipient)
}

// SetSigner is a paid mutator transaction binding the contract method 0x6c19e783.
//
// Solidity: function setSigner(address _routerSigner) returns()
func (_Router *RouterTransactor) SetSigner(opts *bind.TransactOpts, _routerSigner common.Address) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "setSigner", _routerSigner)
}

// SetSigner is a paid mutator transaction binding the contract method 0x6c19e783.
//
// Solidity: function setSigner(address _routerSigner) returns()
func (_Router *RouterSession) SetSigner(_routerSigner common.Address) (*types.Transaction, error) {
	return _Router.Contract.SetSigner(&_Router.TransactOpts, _routerSigner)
}

// SetSigner is a paid mutator transaction binding the contract method 0x6c19e783.
//
// Solidity: function setSigner(address _routerSigner) returns()
func (_Router *RouterTransactorSession) SetSigner(_routerSigner common.Address) (*types.Transaction, error) {
	return _Router.Contract.SetSigner(&_Router.TransactOpts, _routerSigner)
}

// TransferOwnership is a paid mutator transaction binding the contract method 0xf2fde38b.
//
// Solidity: function transferOwnership(address newOwner) returns()
func (_Router *RouterTransactor) TransferOwnership(opts *bind.TransactOpts, newOwner common.Address) (*types.Transaction, error) {
	return _Router.contract.Transact(opts, "transferOwnership", newOwner)
}

// TransferOwnership is a paid mutator transaction binding the contract method 0xf2fde38b.
//
// Solidity: function transferOwnership(address newOwner) returns()
func (_Router *RouterSession) TransferOwnership(newOwner common.Address) (*types.Transaction, error) {
	return _Router.Contract.TransferOwnership(&_Router.TransactOpts, newOwner)
}

// TransferOwnership is a paid mutator transaction binding the contract method 0xf2fde38b.
//
// Solidity: function transferOwnership(address newOwner) returns()
func (_Router *RouterTransactorSession) TransferOwnership(newOwner common.Address) (*types.Transaction, error) {
	return _Router.Contract.TransferOwnership(&_Router.TransactOpts, newOwner)
}

// Receive is a paid mutator transaction binding the contract receive function.
//
// Solidity: receive() payable returns()
func (_Router *RouterTransactor) Receive(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _Router.contract.RawTransact(opts, nil) // calldata is disallowed for receive function
}

// Receive is a paid mutator transaction binding the contract receive function.
//
// Solidity: receive() payable returns()
func (_Router *RouterSession) Receive() (*types.Transaction, error) {
	return _Router.Contract.Receive(&_Router.TransactOpts)
}

// Receive is a paid mutator transaction binding the contract receive function.
//
// Solidity: receive() payable returns()
func (_Router *RouterTransactorSession) Receive() (*types.Transaction, error) {
	return _Router.Contract.Receive(&_Router.TransactOpts)
}

// RouterCancelIterator is returned from FilterCancel and is used to iterate over the raw logs and unpacked data for Cancel events raised by the Router contract.
type RouterCancelIterator struct {
	Event *RouterCancel // Event containing the contract specifics and raw log

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
func (it *RouterCancelIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterCancel)
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
		it.Event = new(RouterCancel)
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
func (it *RouterCancelIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterCancelIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterCancel represents a Cancel event raised by the Router contract.
type RouterCancel struct {
	TxData                ITransactionManagerTransactionData
	RouterRelayerFeeAsset common.Address
	RouterRelayerFee      *big.Int
	Caller                common.Address
	Raw                   types.Log // Blockchain specific contextual infos
}

// FilterCancel is a free log retrieval operation binding the contract event 0xdb26fb99c342114246dbc5580bb4d02519f9250cacf10aafc127b24f755d4e3f.
//
// Solidity: event Cancel((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) FilterCancel(opts *bind.FilterOpts) (*RouterCancelIterator, error) {

	logs, sub, err := _Router.contract.FilterLogs(opts, "Cancel")
	if err != nil {
		return nil, err
	}
	return &RouterCancelIterator{contract: _Router.contract, event: "Cancel", logs: logs, sub: sub}, nil
}

// WatchCancel is a free log subscription operation binding the contract event 0xdb26fb99c342114246dbc5580bb4d02519f9250cacf10aafc127b24f755d4e3f.
//
// Solidity: event Cancel((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) WatchCancel(opts *bind.WatchOpts, sink chan<- *RouterCancel) (event.Subscription, error) {

	logs, sub, err := _Router.contract.WatchLogs(opts, "Cancel")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterCancel)
				if err := _Router.contract.UnpackLog(event, "Cancel", log); err != nil {
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

// ParseCancel is a log parse operation binding the contract event 0xdb26fb99c342114246dbc5580bb4d02519f9250cacf10aafc127b24f755d4e3f.
//
// Solidity: event Cancel((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) ParseCancel(log types.Log) (*RouterCancel, error) {
	event := new(RouterCancel)
	if err := _Router.contract.UnpackLog(event, "Cancel", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// RouterFulfillIterator is returned from FilterFulfill and is used to iterate over the raw logs and unpacked data for Fulfill events raised by the Router contract.
type RouterFulfillIterator struct {
	Event *RouterFulfill // Event containing the contract specifics and raw log

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
func (it *RouterFulfillIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterFulfill)
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
		it.Event = new(RouterFulfill)
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
func (it *RouterFulfillIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterFulfillIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterFulfill represents a Fulfill event raised by the Router contract.
type RouterFulfill struct {
	TxData                ITransactionManagerTransactionData
	RouterRelayerFeeAsset common.Address
	RouterRelayerFee      *big.Int
	Caller                common.Address
	Raw                   types.Log // Blockchain specific contextual infos
}

// FilterFulfill is a free log retrieval operation binding the contract event 0xbd58fe74fd3111b8d37f5a35a025b9cec45d1f01f329eb4e1b86a1428d5d3337.
//
// Solidity: event Fulfill((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) FilterFulfill(opts *bind.FilterOpts) (*RouterFulfillIterator, error) {

	logs, sub, err := _Router.contract.FilterLogs(opts, "Fulfill")
	if err != nil {
		return nil, err
	}
	return &RouterFulfillIterator{contract: _Router.contract, event: "Fulfill", logs: logs, sub: sub}, nil
}

// WatchFulfill is a free log subscription operation binding the contract event 0xbd58fe74fd3111b8d37f5a35a025b9cec45d1f01f329eb4e1b86a1428d5d3337.
//
// Solidity: event Fulfill((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) WatchFulfill(opts *bind.WatchOpts, sink chan<- *RouterFulfill) (event.Subscription, error) {

	logs, sub, err := _Router.contract.WatchLogs(opts, "Fulfill")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterFulfill)
				if err := _Router.contract.UnpackLog(event, "Fulfill", log); err != nil {
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

// ParseFulfill is a log parse operation binding the contract event 0xbd58fe74fd3111b8d37f5a35a025b9cec45d1f01f329eb4e1b86a1428d5d3337.
//
// Solidity: event Fulfill((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) ParseFulfill(log types.Log) (*RouterFulfill, error) {
	event := new(RouterFulfill)
	if err := _Router.contract.UnpackLog(event, "Fulfill", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// RouterOwnershipTransferredIterator is returned from FilterOwnershipTransferred and is used to iterate over the raw logs and unpacked data for OwnershipTransferred events raised by the Router contract.
type RouterOwnershipTransferredIterator struct {
	Event *RouterOwnershipTransferred // Event containing the contract specifics and raw log

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
func (it *RouterOwnershipTransferredIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterOwnershipTransferred)
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
		it.Event = new(RouterOwnershipTransferred)
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
func (it *RouterOwnershipTransferredIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterOwnershipTransferredIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterOwnershipTransferred represents a OwnershipTransferred event raised by the Router contract.
type RouterOwnershipTransferred struct {
	PreviousOwner common.Address
	NewOwner      common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterOwnershipTransferred is a free log retrieval operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_Router *RouterFilterer) FilterOwnershipTransferred(opts *bind.FilterOpts, previousOwner []common.Address, newOwner []common.Address) (*RouterOwnershipTransferredIterator, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _Router.contract.FilterLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return &RouterOwnershipTransferredIterator{contract: _Router.contract, event: "OwnershipTransferred", logs: logs, sub: sub}, nil
}

// WatchOwnershipTransferred is a free log subscription operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_Router *RouterFilterer) WatchOwnershipTransferred(opts *bind.WatchOpts, sink chan<- *RouterOwnershipTransferred, previousOwner []common.Address, newOwner []common.Address) (event.Subscription, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _Router.contract.WatchLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterOwnershipTransferred)
				if err := _Router.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
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
func (_Router *RouterFilterer) ParseOwnershipTransferred(log types.Log) (*RouterOwnershipTransferred, error) {
	event := new(RouterOwnershipTransferred)
	if err := _Router.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// RouterPrepareIterator is returned from FilterPrepare and is used to iterate over the raw logs and unpacked data for Prepare events raised by the Router contract.
type RouterPrepareIterator struct {
	Event *RouterPrepare // Event containing the contract specifics and raw log

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
func (it *RouterPrepareIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterPrepare)
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
		it.Event = new(RouterPrepare)
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
func (it *RouterPrepareIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterPrepareIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterPrepare represents a Prepare event raised by the Router contract.
type RouterPrepare struct {
	InvariantData         ITransactionManagerInvariantTransactionData
	RouterRelayerFeeAsset common.Address
	RouterRelayerFee      *big.Int
	Caller                common.Address
	Raw                   types.Log // Blockchain specific contextual infos
}

// FilterPrepare is a free log retrieval operation binding the contract event 0x583ad731037599752e477b0d462b10b6067dab73e63227960e20403a8ee7f7f0.
//
// Solidity: event Prepare((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32) invariantData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) FilterPrepare(opts *bind.FilterOpts) (*RouterPrepareIterator, error) {

	logs, sub, err := _Router.contract.FilterLogs(opts, "Prepare")
	if err != nil {
		return nil, err
	}
	return &RouterPrepareIterator{contract: _Router.contract, event: "Prepare", logs: logs, sub: sub}, nil
}

// WatchPrepare is a free log subscription operation binding the contract event 0x583ad731037599752e477b0d462b10b6067dab73e63227960e20403a8ee7f7f0.
//
// Solidity: event Prepare((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32) invariantData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) WatchPrepare(opts *bind.WatchOpts, sink chan<- *RouterPrepare) (event.Subscription, error) {

	logs, sub, err := _Router.contract.WatchLogs(opts, "Prepare")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterPrepare)
				if err := _Router.contract.UnpackLog(event, "Prepare", log); err != nil {
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

// ParsePrepare is a log parse operation binding the contract event 0x583ad731037599752e477b0d462b10b6067dab73e63227960e20403a8ee7f7f0.
//
// Solidity: event Prepare((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32) invariantData, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) ParsePrepare(log types.Log) (*RouterPrepare, error) {
	event := new(RouterPrepare)
	if err := _Router.contract.UnpackLog(event, "Prepare", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// RouterRelayerFeeAddedIterator is returned from FilterRelayerFeeAdded and is used to iterate over the raw logs and unpacked data for RelayerFeeAdded events raised by the Router contract.
type RouterRelayerFeeAddedIterator struct {
	Event *RouterRelayerFeeAdded // Event containing the contract specifics and raw log

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
func (it *RouterRelayerFeeAddedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterRelayerFeeAdded)
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
		it.Event = new(RouterRelayerFeeAdded)
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
func (it *RouterRelayerFeeAddedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterRelayerFeeAddedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterRelayerFeeAdded represents a RelayerFeeAdded event raised by the Router contract.
type RouterRelayerFeeAdded struct {
	AssetId common.Address
	Amount  *big.Int
	Caller  common.Address
	Raw     types.Log // Blockchain specific contextual infos
}

// FilterRelayerFeeAdded is a free log retrieval operation binding the contract event 0x1104e763408245681528382e9b9fcd4d8f1b4bce2e83f5ce2be8d1a5ec8323a0.
//
// Solidity: event RelayerFeeAdded(address assetId, uint256 amount, address caller)
func (_Router *RouterFilterer) FilterRelayerFeeAdded(opts *bind.FilterOpts) (*RouterRelayerFeeAddedIterator, error) {

	logs, sub, err := _Router.contract.FilterLogs(opts, "RelayerFeeAdded")
	if err != nil {
		return nil, err
	}
	return &RouterRelayerFeeAddedIterator{contract: _Router.contract, event: "RelayerFeeAdded", logs: logs, sub: sub}, nil
}

// WatchRelayerFeeAdded is a free log subscription operation binding the contract event 0x1104e763408245681528382e9b9fcd4d8f1b4bce2e83f5ce2be8d1a5ec8323a0.
//
// Solidity: event RelayerFeeAdded(address assetId, uint256 amount, address caller)
func (_Router *RouterFilterer) WatchRelayerFeeAdded(opts *bind.WatchOpts, sink chan<- *RouterRelayerFeeAdded) (event.Subscription, error) {

	logs, sub, err := _Router.contract.WatchLogs(opts, "RelayerFeeAdded")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterRelayerFeeAdded)
				if err := _Router.contract.UnpackLog(event, "RelayerFeeAdded", log); err != nil {
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

// ParseRelayerFeeAdded is a log parse operation binding the contract event 0x1104e763408245681528382e9b9fcd4d8f1b4bce2e83f5ce2be8d1a5ec8323a0.
//
// Solidity: event RelayerFeeAdded(address assetId, uint256 amount, address caller)
func (_Router *RouterFilterer) ParseRelayerFeeAdded(log types.Log) (*RouterRelayerFeeAdded, error) {
	event := new(RouterRelayerFeeAdded)
	if err := _Router.contract.UnpackLog(event, "RelayerFeeAdded", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// RouterRelayerFeeRemovedIterator is returned from FilterRelayerFeeRemoved and is used to iterate over the raw logs and unpacked data for RelayerFeeRemoved events raised by the Router contract.
type RouterRelayerFeeRemovedIterator struct {
	Event *RouterRelayerFeeRemoved // Event containing the contract specifics and raw log

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
func (it *RouterRelayerFeeRemovedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterRelayerFeeRemoved)
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
		it.Event = new(RouterRelayerFeeRemoved)
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
func (it *RouterRelayerFeeRemovedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterRelayerFeeRemovedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterRelayerFeeRemoved represents a RelayerFeeRemoved event raised by the Router contract.
type RouterRelayerFeeRemoved struct {
	AssetId common.Address
	Amount  *big.Int
	Caller  common.Address
	Raw     types.Log // Blockchain specific contextual infos
}

// FilterRelayerFeeRemoved is a free log retrieval operation binding the contract event 0x5d760a2d1cc0892ddaea1748093916f51d345b37724db0f69b41574a92adc06f.
//
// Solidity: event RelayerFeeRemoved(address assetId, uint256 amount, address caller)
func (_Router *RouterFilterer) FilterRelayerFeeRemoved(opts *bind.FilterOpts) (*RouterRelayerFeeRemovedIterator, error) {

	logs, sub, err := _Router.contract.FilterLogs(opts, "RelayerFeeRemoved")
	if err != nil {
		return nil, err
	}
	return &RouterRelayerFeeRemovedIterator{contract: _Router.contract, event: "RelayerFeeRemoved", logs: logs, sub: sub}, nil
}

// WatchRelayerFeeRemoved is a free log subscription operation binding the contract event 0x5d760a2d1cc0892ddaea1748093916f51d345b37724db0f69b41574a92adc06f.
//
// Solidity: event RelayerFeeRemoved(address assetId, uint256 amount, address caller)
func (_Router *RouterFilterer) WatchRelayerFeeRemoved(opts *bind.WatchOpts, sink chan<- *RouterRelayerFeeRemoved) (event.Subscription, error) {

	logs, sub, err := _Router.contract.WatchLogs(opts, "RelayerFeeRemoved")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterRelayerFeeRemoved)
				if err := _Router.contract.UnpackLog(event, "RelayerFeeRemoved", log); err != nil {
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

// ParseRelayerFeeRemoved is a log parse operation binding the contract event 0x5d760a2d1cc0892ddaea1748093916f51d345b37724db0f69b41574a92adc06f.
//
// Solidity: event RelayerFeeRemoved(address assetId, uint256 amount, address caller)
func (_Router *RouterFilterer) ParseRelayerFeeRemoved(log types.Log) (*RouterRelayerFeeRemoved, error) {
	event := new(RouterRelayerFeeRemoved)
	if err := _Router.contract.UnpackLog(event, "RelayerFeeRemoved", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// RouterRemoveLiquidityIterator is returned from FilterRemoveLiquidity and is used to iterate over the raw logs and unpacked data for RemoveLiquidity events raised by the Router contract.
type RouterRemoveLiquidityIterator struct {
	Event *RouterRemoveLiquidity // Event containing the contract specifics and raw log

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
func (it *RouterRemoveLiquidityIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(RouterRemoveLiquidity)
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
		it.Event = new(RouterRemoveLiquidity)
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
func (it *RouterRemoveLiquidityIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *RouterRemoveLiquidityIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// RouterRemoveLiquidity represents a RemoveLiquidity event raised by the Router contract.
type RouterRemoveLiquidity struct {
	Amount                *big.Int
	AssetId               common.Address
	RouterRelayerFeeAsset common.Address
	RouterRelayerFee      *big.Int
	Caller                common.Address
	Raw                   types.Log // Blockchain specific contextual infos
}

// FilterRemoveLiquidity is a free log retrieval operation binding the contract event 0x964a82560b2c071ffde7bc11cc169cfbef31770b4457ff7fa561d5e2bfb51543.
//
// Solidity: event RemoveLiquidity(uint256 amount, address assetId, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) FilterRemoveLiquidity(opts *bind.FilterOpts) (*RouterRemoveLiquidityIterator, error) {

	logs, sub, err := _Router.contract.FilterLogs(opts, "RemoveLiquidity")
	if err != nil {
		return nil, err
	}
	return &RouterRemoveLiquidityIterator{contract: _Router.contract, event: "RemoveLiquidity", logs: logs, sub: sub}, nil
}

// WatchRemoveLiquidity is a free log subscription operation binding the contract event 0x964a82560b2c071ffde7bc11cc169cfbef31770b4457ff7fa561d5e2bfb51543.
//
// Solidity: event RemoveLiquidity(uint256 amount, address assetId, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) WatchRemoveLiquidity(opts *bind.WatchOpts, sink chan<- *RouterRemoveLiquidity) (event.Subscription, error) {

	logs, sub, err := _Router.contract.WatchLogs(opts, "RemoveLiquidity")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(RouterRemoveLiquidity)
				if err := _Router.contract.UnpackLog(event, "RemoveLiquidity", log); err != nil {
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

// ParseRemoveLiquidity is a log parse operation binding the contract event 0x964a82560b2c071ffde7bc11cc169cfbef31770b4457ff7fa561d5e2bfb51543.
//
// Solidity: event RemoveLiquidity(uint256 amount, address assetId, address routerRelayerFeeAsset, uint256 routerRelayerFee, address caller)
func (_Router *RouterFilterer) ParseRemoveLiquidity(log types.Log) (*RouterRemoveLiquidity, error) {
	event := new(RouterRemoveLiquidity)
	if err := _Router.contract.UnpackLog(event, "RemoveLiquidity", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}
