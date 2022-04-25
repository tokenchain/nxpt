// Code generated - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package transaction_manager

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

// TransactionManagerMetaData contains all meta data concerning the TransactionManager contract.
var TransactionManagerMetaData = &bind.MetaData{
	ABI: "[{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_chainId\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"addedAssetId\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"AssetAdded\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"renounced\",\"type\":\"bool\"}],\"name\":\"AssetOwnershipRenounced\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"timestamp\",\"type\":\"uint256\"}],\"name\":\"AssetOwnershipRenunciationProposed\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"removedAssetId\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"AssetRemoved\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"LiquidityAdded\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"}],\"name\":\"LiquidityRemoved\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"proposedOwner\",\"type\":\"address\"}],\"name\":\"OwnershipProposed\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"addedRouter\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"RouterAdded\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"renounced\",\"type\":\"bool\"}],\"name\":\"RouterOwnershipRenounced\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"timestamp\",\"type\":\"uint256\"}],\"name\":\"RouterOwnershipRenunciationProposed\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"removedRouter\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"RouterRemoved\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"indexed\":false,\"internalType\":\"structITransactionManager.CancelArgs\",\"name\":\"args\",\"type\":\"tuple\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"TransactionCancelled\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"internalType\":\"uint256\",\"name\":\"relayerFee\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"callData\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"indexed\":false,\"internalType\":\"structITransactionManager.FulfillArgs\",\"name\":\"args\",\"type\":\"tuple\"},{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"success\",\"type\":\"bool\"},{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"isContract\",\"type\":\"bool\"},{\"indexed\":false,\"internalType\":\"bytes\",\"name\":\"returnData\",\"type\":\"bytes\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"}],\"name\":\"TransactionFulfilled\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"indexed\":false,\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"caller\",\"type\":\"address\"},{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"}],\"internalType\":\"structITransactionManager.InvariantTransactionData\",\"name\":\"invariantData\",\"type\":\"tuple\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"encryptedCallData\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedBid\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"bidSignature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"indexed\":false,\"internalType\":\"structITransactionManager.PrepareArgs\",\"name\":\"args\",\"type\":\"tuple\"}],\"name\":\"TransactionPrepared\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"MAX_TIMEOUT\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"MIN_TIMEOUT\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"acceptProposedOwner\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"}],\"name\":\"addAssetId\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"}],\"name\":\"addLiquidity\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"}],\"name\":\"addLiquidityFor\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"}],\"name\":\"addRouter\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"approvedAssets\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"approvedRouters\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"assetOwnershipTimestamp\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"internalType\":\"structITransactionManager.CancelArgs\",\"name\":\"args\",\"type\":\"tuple\"}],\"name\":\"cancel\",\"outputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"delay\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"txData\",\"type\":\"tuple\"},{\"internalType\":\"uint256\",\"name\":\"relayerFee\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"signature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"callData\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"internalType\":\"structITransactionManager.FulfillArgs\",\"name\":\"args\",\"type\":\"tuple\"}],\"name\":\"fulfill\",\"outputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"getChainId\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"_chainId\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"getStoredChainId\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"interpreter\",\"outputs\":[{\"internalType\":\"contractIFulfillInterpreter\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"isAssetOwnershipRenounced\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"isRouterOwnershipRenounced\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"}],\"internalType\":\"structITransactionManager.InvariantTransactionData\",\"name\":\"invariantData\",\"type\":\"tuple\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"encryptedCallData\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedBid\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"bidSignature\",\"type\":\"bytes\"},{\"internalType\":\"bytes\",\"name\":\"encodedMeta\",\"type\":\"bytes\"}],\"internalType\":\"structITransactionManager.PrepareArgs\",\"name\":\"args\",\"type\":\"tuple\"}],\"name\":\"prepare\",\"outputs\":[{\"components\":[{\"internalType\":\"address\",\"name\":\"receivingChainTxManagerAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"user\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"initiator\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAssetId\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"sendingChainFallback\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"receivingAddress\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"callTo\",\"type\":\"address\"},{\"internalType\":\"bytes32\",\"name\":\"callDataHash\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"transactionId\",\"type\":\"bytes32\"},{\"internalType\":\"uint256\",\"name\":\"sendingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"receivingChainId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"expiry\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"preparedBlockNumber\",\"type\":\"uint256\"}],\"internalType\":\"structITransactionManager.TransactionData\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposeAssetOwnershipRenunciation\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newlyProposed\",\"type\":\"address\"}],\"name\":\"proposeNewOwner\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposeRouterOwnershipRenunciation\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposed\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"proposedTimestamp\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"}],\"name\":\"removeAssetId\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"assetId\",\"type\":\"address\"},{\"internalType\":\"addresspayable\",\"name\":\"recipient\",\"type\":\"address\"}],\"name\":\"removeLiquidity\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"router\",\"type\":\"address\"}],\"name\":\"removeRouter\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceAssetOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceRouterOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounced\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"routerBalances\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"routerOwnershipTimestamp\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"variantTransactionData\",\"outputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"stateMutability\":\"view\",\"type\":\"function\"}]",
}

// TransactionManagerABI is the input ABI used to generate the binding from.
// Deprecated: Use TransactionManagerMetaData.ABI instead.
var TransactionManagerABI = TransactionManagerMetaData.ABI

// TransactionManager is an auto generated Go binding around an Ethereum contract.
type TransactionManager struct {
	TransactionManagerCaller     // Read-only binding to the contract
	TransactionManagerTransactor // Write-only binding to the contract
	TransactionManagerFilterer   // Log filterer for contract events
}

// TransactionManagerCaller is an auto generated read-only Go binding around an Ethereum contract.
type TransactionManagerCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// TransactionManagerTransactor is an auto generated write-only Go binding around an Ethereum contract.
type TransactionManagerTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// TransactionManagerFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type TransactionManagerFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// TransactionManagerSession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type TransactionManagerSession struct {
	Contract     *TransactionManager // Generic contract binding to set the session for
	CallOpts     bind.CallOpts       // Call options to use throughout this session
	TransactOpts bind.TransactOpts   // Transaction auth options to use throughout this session
}

// TransactionManagerCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type TransactionManagerCallerSession struct {
	Contract *TransactionManagerCaller // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts             // Call options to use throughout this session
}

// TransactionManagerTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type TransactionManagerTransactorSession struct {
	Contract     *TransactionManagerTransactor // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts             // Transaction auth options to use throughout this session
}

// TransactionManagerRaw is an auto generated low-level Go binding around an Ethereum contract.
type TransactionManagerRaw struct {
	Contract *TransactionManager // Generic contract binding to access the raw methods on
}

// TransactionManagerCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type TransactionManagerCallerRaw struct {
	Contract *TransactionManagerCaller // Generic read-only contract binding to access the raw methods on
}

// TransactionManagerTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type TransactionManagerTransactorRaw struct {
	Contract *TransactionManagerTransactor // Generic write-only contract binding to access the raw methods on
}

// NewTransactionManager creates a new instance of TransactionManager, bound to a specific deployed contract.
func NewTransactionManager(address common.Address, backend bind.ContractBackend) (*TransactionManager, error) {
	contract, err := bindTransactionManager(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &TransactionManager{TransactionManagerCaller: TransactionManagerCaller{contract: contract}, TransactionManagerTransactor: TransactionManagerTransactor{contract: contract}, TransactionManagerFilterer: TransactionManagerFilterer{contract: contract}}, nil
}

// NewTransactionManagerCaller creates a new read-only instance of TransactionManager, bound to a specific deployed contract.
func NewTransactionManagerCaller(address common.Address, caller bind.ContractCaller) (*TransactionManagerCaller, error) {
	contract, err := bindTransactionManager(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerCaller{contract: contract}, nil
}

// NewTransactionManagerTransactor creates a new write-only instance of TransactionManager, bound to a specific deployed contract.
func NewTransactionManagerTransactor(address common.Address, transactor bind.ContractTransactor) (*TransactionManagerTransactor, error) {
	contract, err := bindTransactionManager(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerTransactor{contract: contract}, nil
}

// NewTransactionManagerFilterer creates a new log filterer instance of TransactionManager, bound to a specific deployed contract.
func NewTransactionManagerFilterer(address common.Address, filterer bind.ContractFilterer) (*TransactionManagerFilterer, error) {
	contract, err := bindTransactionManager(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerFilterer{contract: contract}, nil
}

// bindTransactionManager binds a generic wrapper to an already deployed contract.
func bindTransactionManager(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := abi.JSON(strings.NewReader(TransactionManagerABI))
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_TransactionManager *TransactionManagerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _TransactionManager.Contract.TransactionManagerCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_TransactionManager *TransactionManagerRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.Contract.TransactionManagerTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_TransactionManager *TransactionManagerRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _TransactionManager.Contract.TransactionManagerTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_TransactionManager *TransactionManagerCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _TransactionManager.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_TransactionManager *TransactionManagerTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_TransactionManager *TransactionManagerTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _TransactionManager.Contract.contract.Transact(opts, method, params...)
}

// MAXTIMEOUT is a free data retrieval call binding the contract method 0xde38eb3a.
//
// Solidity: function MAX_TIMEOUT() view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) MAXTIMEOUT(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "MAX_TIMEOUT")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// MAXTIMEOUT is a free data retrieval call binding the contract method 0xde38eb3a.
//
// Solidity: function MAX_TIMEOUT() view returns(uint256)
func (_TransactionManager *TransactionManagerSession) MAXTIMEOUT() (*big.Int, error) {
	return _TransactionManager.Contract.MAXTIMEOUT(&_TransactionManager.CallOpts)
}

// MAXTIMEOUT is a free data retrieval call binding the contract method 0xde38eb3a.
//
// Solidity: function MAX_TIMEOUT() view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) MAXTIMEOUT() (*big.Int, error) {
	return _TransactionManager.Contract.MAXTIMEOUT(&_TransactionManager.CallOpts)
}

// MINTIMEOUT is a free data retrieval call binding the contract method 0x543ad1df.
//
// Solidity: function MIN_TIMEOUT() view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) MINTIMEOUT(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "MIN_TIMEOUT")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// MINTIMEOUT is a free data retrieval call binding the contract method 0x543ad1df.
//
// Solidity: function MIN_TIMEOUT() view returns(uint256)
func (_TransactionManager *TransactionManagerSession) MINTIMEOUT() (*big.Int, error) {
	return _TransactionManager.Contract.MINTIMEOUT(&_TransactionManager.CallOpts)
}

// MINTIMEOUT is a free data retrieval call binding the contract method 0x543ad1df.
//
// Solidity: function MIN_TIMEOUT() view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) MINTIMEOUT() (*big.Int, error) {
	return _TransactionManager.Contract.MINTIMEOUT(&_TransactionManager.CallOpts)
}

// ApprovedAssets is a free data retrieval call binding the contract method 0x97eb0088.
//
// Solidity: function approvedAssets(address ) view returns(bool)
func (_TransactionManager *TransactionManagerCaller) ApprovedAssets(opts *bind.CallOpts, arg0 common.Address) (bool, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "approvedAssets", arg0)

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// ApprovedAssets is a free data retrieval call binding the contract method 0x97eb0088.
//
// Solidity: function approvedAssets(address ) view returns(bool)
func (_TransactionManager *TransactionManagerSession) ApprovedAssets(arg0 common.Address) (bool, error) {
	return _TransactionManager.Contract.ApprovedAssets(&_TransactionManager.CallOpts, arg0)
}

// ApprovedAssets is a free data retrieval call binding the contract method 0x97eb0088.
//
// Solidity: function approvedAssets(address ) view returns(bool)
func (_TransactionManager *TransactionManagerCallerSession) ApprovedAssets(arg0 common.Address) (bool, error) {
	return _TransactionManager.Contract.ApprovedAssets(&_TransactionManager.CallOpts, arg0)
}

// ApprovedRouters is a free data retrieval call binding the contract method 0x445b1e4b.
//
// Solidity: function approvedRouters(address ) view returns(bool)
func (_TransactionManager *TransactionManagerCaller) ApprovedRouters(opts *bind.CallOpts, arg0 common.Address) (bool, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "approvedRouters", arg0)

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// ApprovedRouters is a free data retrieval call binding the contract method 0x445b1e4b.
//
// Solidity: function approvedRouters(address ) view returns(bool)
func (_TransactionManager *TransactionManagerSession) ApprovedRouters(arg0 common.Address) (bool, error) {
	return _TransactionManager.Contract.ApprovedRouters(&_TransactionManager.CallOpts, arg0)
}

// ApprovedRouters is a free data retrieval call binding the contract method 0x445b1e4b.
//
// Solidity: function approvedRouters(address ) view returns(bool)
func (_TransactionManager *TransactionManagerCallerSession) ApprovedRouters(arg0 common.Address) (bool, error) {
	return _TransactionManager.Contract.ApprovedRouters(&_TransactionManager.CallOpts, arg0)
}

// AssetOwnershipTimestamp is a free data retrieval call binding the contract method 0x6a41633a.
//
// Solidity: function assetOwnershipTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) AssetOwnershipTimestamp(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "assetOwnershipTimestamp")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// AssetOwnershipTimestamp is a free data retrieval call binding the contract method 0x6a41633a.
//
// Solidity: function assetOwnershipTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerSession) AssetOwnershipTimestamp() (*big.Int, error) {
	return _TransactionManager.Contract.AssetOwnershipTimestamp(&_TransactionManager.CallOpts)
}

// AssetOwnershipTimestamp is a free data retrieval call binding the contract method 0x6a41633a.
//
// Solidity: function assetOwnershipTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) AssetOwnershipTimestamp() (*big.Int, error) {
	return _TransactionManager.Contract.AssetOwnershipTimestamp(&_TransactionManager.CallOpts)
}

// Delay is a free data retrieval call binding the contract method 0x6a42b8f8.
//
// Solidity: function delay() view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) Delay(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "delay")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// Delay is a free data retrieval call binding the contract method 0x6a42b8f8.
//
// Solidity: function delay() view returns(uint256)
func (_TransactionManager *TransactionManagerSession) Delay() (*big.Int, error) {
	return _TransactionManager.Contract.Delay(&_TransactionManager.CallOpts)
}

// Delay is a free data retrieval call binding the contract method 0x6a42b8f8.
//
// Solidity: function delay() view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) Delay() (*big.Int, error) {
	return _TransactionManager.Contract.Delay(&_TransactionManager.CallOpts)
}

// GetChainId is a free data retrieval call binding the contract method 0x3408e470.
//
// Solidity: function getChainId() view returns(uint256 _chainId)
func (_TransactionManager *TransactionManagerCaller) GetChainId(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "getChainId")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// GetChainId is a free data retrieval call binding the contract method 0x3408e470.
//
// Solidity: function getChainId() view returns(uint256 _chainId)
func (_TransactionManager *TransactionManagerSession) GetChainId() (*big.Int, error) {
	return _TransactionManager.Contract.GetChainId(&_TransactionManager.CallOpts)
}

// GetChainId is a free data retrieval call binding the contract method 0x3408e470.
//
// Solidity: function getChainId() view returns(uint256 _chainId)
func (_TransactionManager *TransactionManagerCallerSession) GetChainId() (*big.Int, error) {
	return _TransactionManager.Contract.GetChainId(&_TransactionManager.CallOpts)
}

// GetStoredChainId is a free data retrieval call binding the contract method 0x32a130c9.
//
// Solidity: function getStoredChainId() view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) GetStoredChainId(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "getStoredChainId")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// GetStoredChainId is a free data retrieval call binding the contract method 0x32a130c9.
//
// Solidity: function getStoredChainId() view returns(uint256)
func (_TransactionManager *TransactionManagerSession) GetStoredChainId() (*big.Int, error) {
	return _TransactionManager.Contract.GetStoredChainId(&_TransactionManager.CallOpts)
}

// GetStoredChainId is a free data retrieval call binding the contract method 0x32a130c9.
//
// Solidity: function getStoredChainId() view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) GetStoredChainId() (*big.Int, error) {
	return _TransactionManager.Contract.GetStoredChainId(&_TransactionManager.CallOpts)
}

// Interpreter is a free data retrieval call binding the contract method 0x3a35cf17.
//
// Solidity: function interpreter() view returns(address)
func (_TransactionManager *TransactionManagerCaller) Interpreter(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "interpreter")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Interpreter is a free data retrieval call binding the contract method 0x3a35cf17.
//
// Solidity: function interpreter() view returns(address)
func (_TransactionManager *TransactionManagerSession) Interpreter() (common.Address, error) {
	return _TransactionManager.Contract.Interpreter(&_TransactionManager.CallOpts)
}

// Interpreter is a free data retrieval call binding the contract method 0x3a35cf17.
//
// Solidity: function interpreter() view returns(address)
func (_TransactionManager *TransactionManagerCallerSession) Interpreter() (common.Address, error) {
	return _TransactionManager.Contract.Interpreter(&_TransactionManager.CallOpts)
}

// IsAssetOwnershipRenounced is a free data retrieval call binding the contract method 0xe8be0dfc.
//
// Solidity: function isAssetOwnershipRenounced() view returns(bool)
func (_TransactionManager *TransactionManagerCaller) IsAssetOwnershipRenounced(opts *bind.CallOpts) (bool, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "isAssetOwnershipRenounced")

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// IsAssetOwnershipRenounced is a free data retrieval call binding the contract method 0xe8be0dfc.
//
// Solidity: function isAssetOwnershipRenounced() view returns(bool)
func (_TransactionManager *TransactionManagerSession) IsAssetOwnershipRenounced() (bool, error) {
	return _TransactionManager.Contract.IsAssetOwnershipRenounced(&_TransactionManager.CallOpts)
}

// IsAssetOwnershipRenounced is a free data retrieval call binding the contract method 0xe8be0dfc.
//
// Solidity: function isAssetOwnershipRenounced() view returns(bool)
func (_TransactionManager *TransactionManagerCallerSession) IsAssetOwnershipRenounced() (bool, error) {
	return _TransactionManager.Contract.IsAssetOwnershipRenounced(&_TransactionManager.CallOpts)
}

// IsRouterOwnershipRenounced is a free data retrieval call binding the contract method 0x2004ef45.
//
// Solidity: function isRouterOwnershipRenounced() view returns(bool)
func (_TransactionManager *TransactionManagerCaller) IsRouterOwnershipRenounced(opts *bind.CallOpts) (bool, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "isRouterOwnershipRenounced")

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// IsRouterOwnershipRenounced is a free data retrieval call binding the contract method 0x2004ef45.
//
// Solidity: function isRouterOwnershipRenounced() view returns(bool)
func (_TransactionManager *TransactionManagerSession) IsRouterOwnershipRenounced() (bool, error) {
	return _TransactionManager.Contract.IsRouterOwnershipRenounced(&_TransactionManager.CallOpts)
}

// IsRouterOwnershipRenounced is a free data retrieval call binding the contract method 0x2004ef45.
//
// Solidity: function isRouterOwnershipRenounced() view returns(bool)
func (_TransactionManager *TransactionManagerCallerSession) IsRouterOwnershipRenounced() (bool, error) {
	return _TransactionManager.Contract.IsRouterOwnershipRenounced(&_TransactionManager.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_TransactionManager *TransactionManagerCaller) Owner(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "owner")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_TransactionManager *TransactionManagerSession) Owner() (common.Address, error) {
	return _TransactionManager.Contract.Owner(&_TransactionManager.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_TransactionManager *TransactionManagerCallerSession) Owner() (common.Address, error) {
	return _TransactionManager.Contract.Owner(&_TransactionManager.CallOpts)
}

// Proposed is a free data retrieval call binding the contract method 0xd1851c92.
//
// Solidity: function proposed() view returns(address)
func (_TransactionManager *TransactionManagerCaller) Proposed(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "proposed")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Proposed is a free data retrieval call binding the contract method 0xd1851c92.
//
// Solidity: function proposed() view returns(address)
func (_TransactionManager *TransactionManagerSession) Proposed() (common.Address, error) {
	return _TransactionManager.Contract.Proposed(&_TransactionManager.CallOpts)
}

// Proposed is a free data retrieval call binding the contract method 0xd1851c92.
//
// Solidity: function proposed() view returns(address)
func (_TransactionManager *TransactionManagerCallerSession) Proposed() (common.Address, error) {
	return _TransactionManager.Contract.Proposed(&_TransactionManager.CallOpts)
}

// ProposedTimestamp is a free data retrieval call binding the contract method 0x3cf52ffb.
//
// Solidity: function proposedTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) ProposedTimestamp(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "proposedTimestamp")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// ProposedTimestamp is a free data retrieval call binding the contract method 0x3cf52ffb.
//
// Solidity: function proposedTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerSession) ProposedTimestamp() (*big.Int, error) {
	return _TransactionManager.Contract.ProposedTimestamp(&_TransactionManager.CallOpts)
}

// ProposedTimestamp is a free data retrieval call binding the contract method 0x3cf52ffb.
//
// Solidity: function proposedTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) ProposedTimestamp() (*big.Int, error) {
	return _TransactionManager.Contract.ProposedTimestamp(&_TransactionManager.CallOpts)
}

// Renounced is a free data retrieval call binding the contract method 0xd232c220.
//
// Solidity: function renounced() view returns(bool)
func (_TransactionManager *TransactionManagerCaller) Renounced(opts *bind.CallOpts) (bool, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "renounced")

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// Renounced is a free data retrieval call binding the contract method 0xd232c220.
//
// Solidity: function renounced() view returns(bool)
func (_TransactionManager *TransactionManagerSession) Renounced() (bool, error) {
	return _TransactionManager.Contract.Renounced(&_TransactionManager.CallOpts)
}

// Renounced is a free data retrieval call binding the contract method 0xd232c220.
//
// Solidity: function renounced() view returns(bool)
func (_TransactionManager *TransactionManagerCallerSession) Renounced() (bool, error) {
	return _TransactionManager.Contract.Renounced(&_TransactionManager.CallOpts)
}

// RouterBalances is a free data retrieval call binding the contract method 0x41258b5c.
//
// Solidity: function routerBalances(address , address ) view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) RouterBalances(opts *bind.CallOpts, arg0 common.Address, arg1 common.Address) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "routerBalances", arg0, arg1)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// RouterBalances is a free data retrieval call binding the contract method 0x41258b5c.
//
// Solidity: function routerBalances(address , address ) view returns(uint256)
func (_TransactionManager *TransactionManagerSession) RouterBalances(arg0 common.Address, arg1 common.Address) (*big.Int, error) {
	return _TransactionManager.Contract.RouterBalances(&_TransactionManager.CallOpts, arg0, arg1)
}

// RouterBalances is a free data retrieval call binding the contract method 0x41258b5c.
//
// Solidity: function routerBalances(address , address ) view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) RouterBalances(arg0 common.Address, arg1 common.Address) (*big.Int, error) {
	return _TransactionManager.Contract.RouterBalances(&_TransactionManager.CallOpts, arg0, arg1)
}

// RouterOwnershipTimestamp is a free data retrieval call binding the contract method 0xc1a04959.
//
// Solidity: function routerOwnershipTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerCaller) RouterOwnershipTimestamp(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "routerOwnershipTimestamp")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// RouterOwnershipTimestamp is a free data retrieval call binding the contract method 0xc1a04959.
//
// Solidity: function routerOwnershipTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerSession) RouterOwnershipTimestamp() (*big.Int, error) {
	return _TransactionManager.Contract.RouterOwnershipTimestamp(&_TransactionManager.CallOpts)
}

// RouterOwnershipTimestamp is a free data retrieval call binding the contract method 0xc1a04959.
//
// Solidity: function routerOwnershipTimestamp() view returns(uint256)
func (_TransactionManager *TransactionManagerCallerSession) RouterOwnershipTimestamp() (*big.Int, error) {
	return _TransactionManager.Contract.RouterOwnershipTimestamp(&_TransactionManager.CallOpts)
}

// VariantTransactionData is a free data retrieval call binding the contract method 0x5e679856.
//
// Solidity: function variantTransactionData(bytes32 ) view returns(bytes32)
func (_TransactionManager *TransactionManagerCaller) VariantTransactionData(opts *bind.CallOpts, arg0 [32]byte) ([32]byte, error) {
	var out []interface{}
	err := _TransactionManager.contract.Call(opts, &out, "variantTransactionData", arg0)

	if err != nil {
		return *new([32]byte), err
	}

	out0 := *abi.ConvertType(out[0], new([32]byte)).(*[32]byte)

	return out0, err

}

// VariantTransactionData is a free data retrieval call binding the contract method 0x5e679856.
//
// Solidity: function variantTransactionData(bytes32 ) view returns(bytes32)
func (_TransactionManager *TransactionManagerSession) VariantTransactionData(arg0 [32]byte) ([32]byte, error) {
	return _TransactionManager.Contract.VariantTransactionData(&_TransactionManager.CallOpts, arg0)
}

// VariantTransactionData is a free data retrieval call binding the contract method 0x5e679856.
//
// Solidity: function variantTransactionData(bytes32 ) view returns(bytes32)
func (_TransactionManager *TransactionManagerCallerSession) VariantTransactionData(arg0 [32]byte) ([32]byte, error) {
	return _TransactionManager.Contract.VariantTransactionData(&_TransactionManager.CallOpts, arg0)
}

// AcceptProposedOwner is a paid mutator transaction binding the contract method 0xc5b350df.
//
// Solidity: function acceptProposedOwner() returns()
func (_TransactionManager *TransactionManagerTransactor) AcceptProposedOwner(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "acceptProposedOwner")
}

// AcceptProposedOwner is a paid mutator transaction binding the contract method 0xc5b350df.
//
// Solidity: function acceptProposedOwner() returns()
func (_TransactionManager *TransactionManagerSession) AcceptProposedOwner() (*types.Transaction, error) {
	return _TransactionManager.Contract.AcceptProposedOwner(&_TransactionManager.TransactOpts)
}

// AcceptProposedOwner is a paid mutator transaction binding the contract method 0xc5b350df.
//
// Solidity: function acceptProposedOwner() returns()
func (_TransactionManager *TransactionManagerTransactorSession) AcceptProposedOwner() (*types.Transaction, error) {
	return _TransactionManager.Contract.AcceptProposedOwner(&_TransactionManager.TransactOpts)
}

// AddAssetId is a paid mutator transaction binding the contract method 0x34e9393c.
//
// Solidity: function addAssetId(address assetId) returns()
func (_TransactionManager *TransactionManagerTransactor) AddAssetId(opts *bind.TransactOpts, assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "addAssetId", assetId)
}

// AddAssetId is a paid mutator transaction binding the contract method 0x34e9393c.
//
// Solidity: function addAssetId(address assetId) returns()
func (_TransactionManager *TransactionManagerSession) AddAssetId(assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddAssetId(&_TransactionManager.TransactOpts, assetId)
}

// AddAssetId is a paid mutator transaction binding the contract method 0x34e9393c.
//
// Solidity: function addAssetId(address assetId) returns()
func (_TransactionManager *TransactionManagerTransactorSession) AddAssetId(assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddAssetId(&_TransactionManager.TransactOpts, assetId)
}

// AddLiquidity is a paid mutator transaction binding the contract method 0xc95f9d0e.
//
// Solidity: function addLiquidity(uint256 amount, address assetId) payable returns()
func (_TransactionManager *TransactionManagerTransactor) AddLiquidity(opts *bind.TransactOpts, amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "addLiquidity", amount, assetId)
}

// AddLiquidity is a paid mutator transaction binding the contract method 0xc95f9d0e.
//
// Solidity: function addLiquidity(uint256 amount, address assetId) payable returns()
func (_TransactionManager *TransactionManagerSession) AddLiquidity(amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddLiquidity(&_TransactionManager.TransactOpts, amount, assetId)
}

// AddLiquidity is a paid mutator transaction binding the contract method 0xc95f9d0e.
//
// Solidity: function addLiquidity(uint256 amount, address assetId) payable returns()
func (_TransactionManager *TransactionManagerTransactorSession) AddLiquidity(amount *big.Int, assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddLiquidity(&_TransactionManager.TransactOpts, amount, assetId)
}

// AddLiquidityFor is a paid mutator transaction binding the contract method 0xe070da09.
//
// Solidity: function addLiquidityFor(uint256 amount, address assetId, address router) payable returns()
func (_TransactionManager *TransactionManagerTransactor) AddLiquidityFor(opts *bind.TransactOpts, amount *big.Int, assetId common.Address, router common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "addLiquidityFor", amount, assetId, router)
}

// AddLiquidityFor is a paid mutator transaction binding the contract method 0xe070da09.
//
// Solidity: function addLiquidityFor(uint256 amount, address assetId, address router) payable returns()
func (_TransactionManager *TransactionManagerSession) AddLiquidityFor(amount *big.Int, assetId common.Address, router common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddLiquidityFor(&_TransactionManager.TransactOpts, amount, assetId, router)
}

// AddLiquidityFor is a paid mutator transaction binding the contract method 0xe070da09.
//
// Solidity: function addLiquidityFor(uint256 amount, address assetId, address router) payable returns()
func (_TransactionManager *TransactionManagerTransactorSession) AddLiquidityFor(amount *big.Int, assetId common.Address, router common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddLiquidityFor(&_TransactionManager.TransactOpts, amount, assetId, router)
}

// AddRouter is a paid mutator transaction binding the contract method 0x24ca984e.
//
// Solidity: function addRouter(address router) returns()
func (_TransactionManager *TransactionManagerTransactor) AddRouter(opts *bind.TransactOpts, router common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "addRouter", router)
}

// AddRouter is a paid mutator transaction binding the contract method 0x24ca984e.
//
// Solidity: function addRouter(address router) returns()
func (_TransactionManager *TransactionManagerSession) AddRouter(router common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddRouter(&_TransactionManager.TransactOpts, router)
}

// AddRouter is a paid mutator transaction binding the contract method 0x24ca984e.
//
// Solidity: function addRouter(address router) returns()
func (_TransactionManager *TransactionManagerTransactorSession) AddRouter(router common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.AddRouter(&_TransactionManager.TransactOpts, router)
}

// Cancel is a paid mutator transaction binding the contract method 0xbe91a2ba.
//
// Solidity: function cancel(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerTransactor) Cancel(opts *bind.TransactOpts, args ITransactionManagerCancelArgs) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "cancel", args)
}

// Cancel is a paid mutator transaction binding the contract method 0xbe91a2ba.
//
// Solidity: function cancel(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerSession) Cancel(args ITransactionManagerCancelArgs) (*types.Transaction, error) {
	return _TransactionManager.Contract.Cancel(&_TransactionManager.TransactOpts, args)
}

// Cancel is a paid mutator transaction binding the contract method 0xbe91a2ba.
//
// Solidity: function cancel(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerTransactorSession) Cancel(args ITransactionManagerCancelArgs) (*types.Transaction, error) {
	return _TransactionManager.Contract.Cancel(&_TransactionManager.TransactOpts, args)
}

// Fulfill is a paid mutator transaction binding the contract method 0x9b151a80.
//
// Solidity: function fulfill(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerTransactor) Fulfill(opts *bind.TransactOpts, args ITransactionManagerFulfillArgs) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "fulfill", args)
}

// Fulfill is a paid mutator transaction binding the contract method 0x9b151a80.
//
// Solidity: function fulfill(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerSession) Fulfill(args ITransactionManagerFulfillArgs) (*types.Transaction, error) {
	return _TransactionManager.Contract.Fulfill(&_TransactionManager.TransactOpts, args)
}

// Fulfill is a paid mutator transaction binding the contract method 0x9b151a80.
//
// Solidity: function fulfill(((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args) returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerTransactorSession) Fulfill(args ITransactionManagerFulfillArgs) (*types.Transaction, error) {
	return _TransactionManager.Contract.Fulfill(&_TransactionManager.TransactOpts, args)
}

// Prepare is a paid mutator transaction binding the contract method 0xd9459372.
//
// Solidity: function prepare(((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args) payable returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerTransactor) Prepare(opts *bind.TransactOpts, args ITransactionManagerPrepareArgs) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "prepare", args)
}

// Prepare is a paid mutator transaction binding the contract method 0xd9459372.
//
// Solidity: function prepare(((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args) payable returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerSession) Prepare(args ITransactionManagerPrepareArgs) (*types.Transaction, error) {
	return _TransactionManager.Contract.Prepare(&_TransactionManager.TransactOpts, args)
}

// Prepare is a paid mutator transaction binding the contract method 0xd9459372.
//
// Solidity: function prepare(((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args) payable returns((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256))
func (_TransactionManager *TransactionManagerTransactorSession) Prepare(args ITransactionManagerPrepareArgs) (*types.Transaction, error) {
	return _TransactionManager.Contract.Prepare(&_TransactionManager.TransactOpts, args)
}

// ProposeAssetOwnershipRenunciation is a paid mutator transaction binding the contract method 0x8741eac5.
//
// Solidity: function proposeAssetOwnershipRenunciation() returns()
func (_TransactionManager *TransactionManagerTransactor) ProposeAssetOwnershipRenunciation(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "proposeAssetOwnershipRenunciation")
}

// ProposeAssetOwnershipRenunciation is a paid mutator transaction binding the contract method 0x8741eac5.
//
// Solidity: function proposeAssetOwnershipRenunciation() returns()
func (_TransactionManager *TransactionManagerSession) ProposeAssetOwnershipRenunciation() (*types.Transaction, error) {
	return _TransactionManager.Contract.ProposeAssetOwnershipRenunciation(&_TransactionManager.TransactOpts)
}

// ProposeAssetOwnershipRenunciation is a paid mutator transaction binding the contract method 0x8741eac5.
//
// Solidity: function proposeAssetOwnershipRenunciation() returns()
func (_TransactionManager *TransactionManagerTransactorSession) ProposeAssetOwnershipRenunciation() (*types.Transaction, error) {
	return _TransactionManager.Contract.ProposeAssetOwnershipRenunciation(&_TransactionManager.TransactOpts)
}

// ProposeNewOwner is a paid mutator transaction binding the contract method 0xb1f8100d.
//
// Solidity: function proposeNewOwner(address newlyProposed) returns()
func (_TransactionManager *TransactionManagerTransactor) ProposeNewOwner(opts *bind.TransactOpts, newlyProposed common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "proposeNewOwner", newlyProposed)
}

// ProposeNewOwner is a paid mutator transaction binding the contract method 0xb1f8100d.
//
// Solidity: function proposeNewOwner(address newlyProposed) returns()
func (_TransactionManager *TransactionManagerSession) ProposeNewOwner(newlyProposed common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.ProposeNewOwner(&_TransactionManager.TransactOpts, newlyProposed)
}

// ProposeNewOwner is a paid mutator transaction binding the contract method 0xb1f8100d.
//
// Solidity: function proposeNewOwner(address newlyProposed) returns()
func (_TransactionManager *TransactionManagerTransactorSession) ProposeNewOwner(newlyProposed common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.ProposeNewOwner(&_TransactionManager.TransactOpts, newlyProposed)
}

// ProposeRouterOwnershipRenunciation is a paid mutator transaction binding the contract method 0xe47602f7.
//
// Solidity: function proposeRouterOwnershipRenunciation() returns()
func (_TransactionManager *TransactionManagerTransactor) ProposeRouterOwnershipRenunciation(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "proposeRouterOwnershipRenunciation")
}

// ProposeRouterOwnershipRenunciation is a paid mutator transaction binding the contract method 0xe47602f7.
//
// Solidity: function proposeRouterOwnershipRenunciation() returns()
func (_TransactionManager *TransactionManagerSession) ProposeRouterOwnershipRenunciation() (*types.Transaction, error) {
	return _TransactionManager.Contract.ProposeRouterOwnershipRenunciation(&_TransactionManager.TransactOpts)
}

// ProposeRouterOwnershipRenunciation is a paid mutator transaction binding the contract method 0xe47602f7.
//
// Solidity: function proposeRouterOwnershipRenunciation() returns()
func (_TransactionManager *TransactionManagerTransactorSession) ProposeRouterOwnershipRenunciation() (*types.Transaction, error) {
	return _TransactionManager.Contract.ProposeRouterOwnershipRenunciation(&_TransactionManager.TransactOpts)
}

// RemoveAssetId is a paid mutator transaction binding the contract method 0xb1d2618d.
//
// Solidity: function removeAssetId(address assetId) returns()
func (_TransactionManager *TransactionManagerTransactor) RemoveAssetId(opts *bind.TransactOpts, assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "removeAssetId", assetId)
}

// RemoveAssetId is a paid mutator transaction binding the contract method 0xb1d2618d.
//
// Solidity: function removeAssetId(address assetId) returns()
func (_TransactionManager *TransactionManagerSession) RemoveAssetId(assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.RemoveAssetId(&_TransactionManager.TransactOpts, assetId)
}

// RemoveAssetId is a paid mutator transaction binding the contract method 0xb1d2618d.
//
// Solidity: function removeAssetId(address assetId) returns()
func (_TransactionManager *TransactionManagerTransactorSession) RemoveAssetId(assetId common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.RemoveAssetId(&_TransactionManager.TransactOpts, assetId)
}

// RemoveLiquidity is a paid mutator transaction binding the contract method 0xf31abcc4.
//
// Solidity: function removeLiquidity(uint256 amount, address assetId, address recipient) returns()
func (_TransactionManager *TransactionManagerTransactor) RemoveLiquidity(opts *bind.TransactOpts, amount *big.Int, assetId common.Address, recipient common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "removeLiquidity", amount, assetId, recipient)
}

// RemoveLiquidity is a paid mutator transaction binding the contract method 0xf31abcc4.
//
// Solidity: function removeLiquidity(uint256 amount, address assetId, address recipient) returns()
func (_TransactionManager *TransactionManagerSession) RemoveLiquidity(amount *big.Int, assetId common.Address, recipient common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.RemoveLiquidity(&_TransactionManager.TransactOpts, amount, assetId, recipient)
}

// RemoveLiquidity is a paid mutator transaction binding the contract method 0xf31abcc4.
//
// Solidity: function removeLiquidity(uint256 amount, address assetId, address recipient) returns()
func (_TransactionManager *TransactionManagerTransactorSession) RemoveLiquidity(amount *big.Int, assetId common.Address, recipient common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.RemoveLiquidity(&_TransactionManager.TransactOpts, amount, assetId, recipient)
}

// RemoveRouter is a paid mutator transaction binding the contract method 0x6ae0b154.
//
// Solidity: function removeRouter(address router) returns()
func (_TransactionManager *TransactionManagerTransactor) RemoveRouter(opts *bind.TransactOpts, router common.Address) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "removeRouter", router)
}

// RemoveRouter is a paid mutator transaction binding the contract method 0x6ae0b154.
//
// Solidity: function removeRouter(address router) returns()
func (_TransactionManager *TransactionManagerSession) RemoveRouter(router common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.RemoveRouter(&_TransactionManager.TransactOpts, router)
}

// RemoveRouter is a paid mutator transaction binding the contract method 0x6ae0b154.
//
// Solidity: function removeRouter(address router) returns()
func (_TransactionManager *TransactionManagerTransactorSession) RemoveRouter(router common.Address) (*types.Transaction, error) {
	return _TransactionManager.Contract.RemoveRouter(&_TransactionManager.TransactOpts, router)
}

// RenounceAssetOwnership is a paid mutator transaction binding the contract method 0x3855b467.
//
// Solidity: function renounceAssetOwnership() returns()
func (_TransactionManager *TransactionManagerTransactor) RenounceAssetOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "renounceAssetOwnership")
}

// RenounceAssetOwnership is a paid mutator transaction binding the contract method 0x3855b467.
//
// Solidity: function renounceAssetOwnership() returns()
func (_TransactionManager *TransactionManagerSession) RenounceAssetOwnership() (*types.Transaction, error) {
	return _TransactionManager.Contract.RenounceAssetOwnership(&_TransactionManager.TransactOpts)
}

// RenounceAssetOwnership is a paid mutator transaction binding the contract method 0x3855b467.
//
// Solidity: function renounceAssetOwnership() returns()
func (_TransactionManager *TransactionManagerTransactorSession) RenounceAssetOwnership() (*types.Transaction, error) {
	return _TransactionManager.Contract.RenounceAssetOwnership(&_TransactionManager.TransactOpts)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_TransactionManager *TransactionManagerTransactor) RenounceOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "renounceOwnership")
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_TransactionManager *TransactionManagerSession) RenounceOwnership() (*types.Transaction, error) {
	return _TransactionManager.Contract.RenounceOwnership(&_TransactionManager.TransactOpts)
}

// RenounceOwnership is a paid mutator transaction binding the contract method 0x715018a6.
//
// Solidity: function renounceOwnership() returns()
func (_TransactionManager *TransactionManagerTransactorSession) RenounceOwnership() (*types.Transaction, error) {
	return _TransactionManager.Contract.RenounceOwnership(&_TransactionManager.TransactOpts)
}

// RenounceRouterOwnership is a paid mutator transaction binding the contract method 0xc0c17baf.
//
// Solidity: function renounceRouterOwnership() returns()
func (_TransactionManager *TransactionManagerTransactor) RenounceRouterOwnership(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _TransactionManager.contract.Transact(opts, "renounceRouterOwnership")
}

// RenounceRouterOwnership is a paid mutator transaction binding the contract method 0xc0c17baf.
//
// Solidity: function renounceRouterOwnership() returns()
func (_TransactionManager *TransactionManagerSession) RenounceRouterOwnership() (*types.Transaction, error) {
	return _TransactionManager.Contract.RenounceRouterOwnership(&_TransactionManager.TransactOpts)
}

// RenounceRouterOwnership is a paid mutator transaction binding the contract method 0xc0c17baf.
//
// Solidity: function renounceRouterOwnership() returns()
func (_TransactionManager *TransactionManagerTransactorSession) RenounceRouterOwnership() (*types.Transaction, error) {
	return _TransactionManager.Contract.RenounceRouterOwnership(&_TransactionManager.TransactOpts)
}

// TransactionManagerAssetAddedIterator is returned from FilterAssetAdded and is used to iterate over the raw logs and unpacked data for AssetAdded events raised by the TransactionManager contract.
type TransactionManagerAssetAddedIterator struct {
	Event *TransactionManagerAssetAdded // Event containing the contract specifics and raw log

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
func (it *TransactionManagerAssetAddedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerAssetAdded)
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
		it.Event = new(TransactionManagerAssetAdded)
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
func (it *TransactionManagerAssetAddedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerAssetAddedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerAssetAdded represents a AssetAdded event raised by the TransactionManager contract.
type TransactionManagerAssetAdded struct {
	AddedAssetId common.Address
	Caller       common.Address
	Raw          types.Log // Blockchain specific contextual infos
}

// FilterAssetAdded is a free log retrieval operation binding the contract event 0x0bb5715f0f217c2fe9a0c877ea87d474380c641102f3440ee2a4c8b9d9790918.
//
// Solidity: event AssetAdded(address indexed addedAssetId, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) FilterAssetAdded(opts *bind.FilterOpts, addedAssetId []common.Address, caller []common.Address) (*TransactionManagerAssetAddedIterator, error) {

	var addedAssetIdRule []interface{}
	for _, addedAssetIdItem := range addedAssetId {
		addedAssetIdRule = append(addedAssetIdRule, addedAssetIdItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "AssetAdded", addedAssetIdRule, callerRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerAssetAddedIterator{contract: _TransactionManager.contract, event: "AssetAdded", logs: logs, sub: sub}, nil
}

// WatchAssetAdded is a free log subscription operation binding the contract event 0x0bb5715f0f217c2fe9a0c877ea87d474380c641102f3440ee2a4c8b9d9790918.
//
// Solidity: event AssetAdded(address indexed addedAssetId, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) WatchAssetAdded(opts *bind.WatchOpts, sink chan<- *TransactionManagerAssetAdded, addedAssetId []common.Address, caller []common.Address) (event.Subscription, error) {

	var addedAssetIdRule []interface{}
	for _, addedAssetIdItem := range addedAssetId {
		addedAssetIdRule = append(addedAssetIdRule, addedAssetIdItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "AssetAdded", addedAssetIdRule, callerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerAssetAdded)
				if err := _TransactionManager.contract.UnpackLog(event, "AssetAdded", log); err != nil {
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

// ParseAssetAdded is a log parse operation binding the contract event 0x0bb5715f0f217c2fe9a0c877ea87d474380c641102f3440ee2a4c8b9d9790918.
//
// Solidity: event AssetAdded(address indexed addedAssetId, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) ParseAssetAdded(log types.Log) (*TransactionManagerAssetAdded, error) {
	event := new(TransactionManagerAssetAdded)
	if err := _TransactionManager.contract.UnpackLog(event, "AssetAdded", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerAssetOwnershipRenouncedIterator is returned from FilterAssetOwnershipRenounced and is used to iterate over the raw logs and unpacked data for AssetOwnershipRenounced events raised by the TransactionManager contract.
type TransactionManagerAssetOwnershipRenouncedIterator struct {
	Event *TransactionManagerAssetOwnershipRenounced // Event containing the contract specifics and raw log

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
func (it *TransactionManagerAssetOwnershipRenouncedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerAssetOwnershipRenounced)
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
		it.Event = new(TransactionManagerAssetOwnershipRenounced)
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
func (it *TransactionManagerAssetOwnershipRenouncedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerAssetOwnershipRenouncedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerAssetOwnershipRenounced represents a AssetOwnershipRenounced event raised by the TransactionManager contract.
type TransactionManagerAssetOwnershipRenounced struct {
	Renounced bool
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterAssetOwnershipRenounced is a free log retrieval operation binding the contract event 0x868d89ead22a5d10f456845ac0014901d9af7203e71cf0892d70d9dc262c2fb9.
//
// Solidity: event AssetOwnershipRenounced(bool renounced)
func (_TransactionManager *TransactionManagerFilterer) FilterAssetOwnershipRenounced(opts *bind.FilterOpts) (*TransactionManagerAssetOwnershipRenouncedIterator, error) {

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "AssetOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return &TransactionManagerAssetOwnershipRenouncedIterator{contract: _TransactionManager.contract, event: "AssetOwnershipRenounced", logs: logs, sub: sub}, nil
}

// WatchAssetOwnershipRenounced is a free log subscription operation binding the contract event 0x868d89ead22a5d10f456845ac0014901d9af7203e71cf0892d70d9dc262c2fb9.
//
// Solidity: event AssetOwnershipRenounced(bool renounced)
func (_TransactionManager *TransactionManagerFilterer) WatchAssetOwnershipRenounced(opts *bind.WatchOpts, sink chan<- *TransactionManagerAssetOwnershipRenounced) (event.Subscription, error) {

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "AssetOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerAssetOwnershipRenounced)
				if err := _TransactionManager.contract.UnpackLog(event, "AssetOwnershipRenounced", log); err != nil {
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
func (_TransactionManager *TransactionManagerFilterer) ParseAssetOwnershipRenounced(log types.Log) (*TransactionManagerAssetOwnershipRenounced, error) {
	event := new(TransactionManagerAssetOwnershipRenounced)
	if err := _TransactionManager.contract.UnpackLog(event, "AssetOwnershipRenounced", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerAssetOwnershipRenunciationProposedIterator is returned from FilterAssetOwnershipRenunciationProposed and is used to iterate over the raw logs and unpacked data for AssetOwnershipRenunciationProposed events raised by the TransactionManager contract.
type TransactionManagerAssetOwnershipRenunciationProposedIterator struct {
	Event *TransactionManagerAssetOwnershipRenunciationProposed // Event containing the contract specifics and raw log

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
func (it *TransactionManagerAssetOwnershipRenunciationProposedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerAssetOwnershipRenunciationProposed)
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
		it.Event = new(TransactionManagerAssetOwnershipRenunciationProposed)
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
func (it *TransactionManagerAssetOwnershipRenunciationProposedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerAssetOwnershipRenunciationProposedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerAssetOwnershipRenunciationProposed represents a AssetOwnershipRenunciationProposed event raised by the TransactionManager contract.
type TransactionManagerAssetOwnershipRenunciationProposed struct {
	Timestamp *big.Int
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterAssetOwnershipRenunciationProposed is a free log retrieval operation binding the contract event 0xa78fdca214e4619ef34a695316d423f5b0d8274bc919d29733bf8f92ec8cbb7a.
//
// Solidity: event AssetOwnershipRenunciationProposed(uint256 timestamp)
func (_TransactionManager *TransactionManagerFilterer) FilterAssetOwnershipRenunciationProposed(opts *bind.FilterOpts) (*TransactionManagerAssetOwnershipRenunciationProposedIterator, error) {

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "AssetOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return &TransactionManagerAssetOwnershipRenunciationProposedIterator{contract: _TransactionManager.contract, event: "AssetOwnershipRenunciationProposed", logs: logs, sub: sub}, nil
}

// WatchAssetOwnershipRenunciationProposed is a free log subscription operation binding the contract event 0xa78fdca214e4619ef34a695316d423f5b0d8274bc919d29733bf8f92ec8cbb7a.
//
// Solidity: event AssetOwnershipRenunciationProposed(uint256 timestamp)
func (_TransactionManager *TransactionManagerFilterer) WatchAssetOwnershipRenunciationProposed(opts *bind.WatchOpts, sink chan<- *TransactionManagerAssetOwnershipRenunciationProposed) (event.Subscription, error) {

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "AssetOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerAssetOwnershipRenunciationProposed)
				if err := _TransactionManager.contract.UnpackLog(event, "AssetOwnershipRenunciationProposed", log); err != nil {
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
func (_TransactionManager *TransactionManagerFilterer) ParseAssetOwnershipRenunciationProposed(log types.Log) (*TransactionManagerAssetOwnershipRenunciationProposed, error) {
	event := new(TransactionManagerAssetOwnershipRenunciationProposed)
	if err := _TransactionManager.contract.UnpackLog(event, "AssetOwnershipRenunciationProposed", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerAssetRemovedIterator is returned from FilterAssetRemoved and is used to iterate over the raw logs and unpacked data for AssetRemoved events raised by the TransactionManager contract.
type TransactionManagerAssetRemovedIterator struct {
	Event *TransactionManagerAssetRemoved // Event containing the contract specifics and raw log

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
func (it *TransactionManagerAssetRemovedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerAssetRemoved)
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
		it.Event = new(TransactionManagerAssetRemoved)
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
func (it *TransactionManagerAssetRemovedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerAssetRemovedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerAssetRemoved represents a AssetRemoved event raised by the TransactionManager contract.
type TransactionManagerAssetRemoved struct {
	RemovedAssetId common.Address
	Caller         common.Address
	Raw            types.Log // Blockchain specific contextual infos
}

// FilterAssetRemoved is a free log retrieval operation binding the contract event 0x0fa1e4606af435f32f05b3804033d2933e691fab32ee74d2db6fa82d2741f1ea.
//
// Solidity: event AssetRemoved(address indexed removedAssetId, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) FilterAssetRemoved(opts *bind.FilterOpts, removedAssetId []common.Address, caller []common.Address) (*TransactionManagerAssetRemovedIterator, error) {

	var removedAssetIdRule []interface{}
	for _, removedAssetIdItem := range removedAssetId {
		removedAssetIdRule = append(removedAssetIdRule, removedAssetIdItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "AssetRemoved", removedAssetIdRule, callerRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerAssetRemovedIterator{contract: _TransactionManager.contract, event: "AssetRemoved", logs: logs, sub: sub}, nil
}

// WatchAssetRemoved is a free log subscription operation binding the contract event 0x0fa1e4606af435f32f05b3804033d2933e691fab32ee74d2db6fa82d2741f1ea.
//
// Solidity: event AssetRemoved(address indexed removedAssetId, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) WatchAssetRemoved(opts *bind.WatchOpts, sink chan<- *TransactionManagerAssetRemoved, removedAssetId []common.Address, caller []common.Address) (event.Subscription, error) {

	var removedAssetIdRule []interface{}
	for _, removedAssetIdItem := range removedAssetId {
		removedAssetIdRule = append(removedAssetIdRule, removedAssetIdItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "AssetRemoved", removedAssetIdRule, callerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerAssetRemoved)
				if err := _TransactionManager.contract.UnpackLog(event, "AssetRemoved", log); err != nil {
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

// ParseAssetRemoved is a log parse operation binding the contract event 0x0fa1e4606af435f32f05b3804033d2933e691fab32ee74d2db6fa82d2741f1ea.
//
// Solidity: event AssetRemoved(address indexed removedAssetId, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) ParseAssetRemoved(log types.Log) (*TransactionManagerAssetRemoved, error) {
	event := new(TransactionManagerAssetRemoved)
	if err := _TransactionManager.contract.UnpackLog(event, "AssetRemoved", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerLiquidityAddedIterator is returned from FilterLiquidityAdded and is used to iterate over the raw logs and unpacked data for LiquidityAdded events raised by the TransactionManager contract.
type TransactionManagerLiquidityAddedIterator struct {
	Event *TransactionManagerLiquidityAdded // Event containing the contract specifics and raw log

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
func (it *TransactionManagerLiquidityAddedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerLiquidityAdded)
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
		it.Event = new(TransactionManagerLiquidityAdded)
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
func (it *TransactionManagerLiquidityAddedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerLiquidityAddedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerLiquidityAdded represents a LiquidityAdded event raised by the TransactionManager contract.
type TransactionManagerLiquidityAdded struct {
	Router  common.Address
	AssetId common.Address
	Amount  *big.Int
	Caller  common.Address
	Raw     types.Log // Blockchain specific contextual infos
}

// FilterLiquidityAdded is a free log retrieval operation binding the contract event 0x4bd28ccd068c4853d24d35f727ef2a3fea11ce55e8d93461e45f785818e1e139.
//
// Solidity: event LiquidityAdded(address indexed router, address indexed assetId, uint256 amount, address caller)
func (_TransactionManager *TransactionManagerFilterer) FilterLiquidityAdded(opts *bind.FilterOpts, router []common.Address, assetId []common.Address) (*TransactionManagerLiquidityAddedIterator, error) {

	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var assetIdRule []interface{}
	for _, assetIdItem := range assetId {
		assetIdRule = append(assetIdRule, assetIdItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "LiquidityAdded", routerRule, assetIdRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerLiquidityAddedIterator{contract: _TransactionManager.contract, event: "LiquidityAdded", logs: logs, sub: sub}, nil
}

// WatchLiquidityAdded is a free log subscription operation binding the contract event 0x4bd28ccd068c4853d24d35f727ef2a3fea11ce55e8d93461e45f785818e1e139.
//
// Solidity: event LiquidityAdded(address indexed router, address indexed assetId, uint256 amount, address caller)
func (_TransactionManager *TransactionManagerFilterer) WatchLiquidityAdded(opts *bind.WatchOpts, sink chan<- *TransactionManagerLiquidityAdded, router []common.Address, assetId []common.Address) (event.Subscription, error) {

	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var assetIdRule []interface{}
	for _, assetIdItem := range assetId {
		assetIdRule = append(assetIdRule, assetIdItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "LiquidityAdded", routerRule, assetIdRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerLiquidityAdded)
				if err := _TransactionManager.contract.UnpackLog(event, "LiquidityAdded", log); err != nil {
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

// ParseLiquidityAdded is a log parse operation binding the contract event 0x4bd28ccd068c4853d24d35f727ef2a3fea11ce55e8d93461e45f785818e1e139.
//
// Solidity: event LiquidityAdded(address indexed router, address indexed assetId, uint256 amount, address caller)
func (_TransactionManager *TransactionManagerFilterer) ParseLiquidityAdded(log types.Log) (*TransactionManagerLiquidityAdded, error) {
	event := new(TransactionManagerLiquidityAdded)
	if err := _TransactionManager.contract.UnpackLog(event, "LiquidityAdded", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerLiquidityRemovedIterator is returned from FilterLiquidityRemoved and is used to iterate over the raw logs and unpacked data for LiquidityRemoved events raised by the TransactionManager contract.
type TransactionManagerLiquidityRemovedIterator struct {
	Event *TransactionManagerLiquidityRemoved // Event containing the contract specifics and raw log

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
func (it *TransactionManagerLiquidityRemovedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerLiquidityRemoved)
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
		it.Event = new(TransactionManagerLiquidityRemoved)
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
func (it *TransactionManagerLiquidityRemovedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerLiquidityRemovedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerLiquidityRemoved represents a LiquidityRemoved event raised by the TransactionManager contract.
type TransactionManagerLiquidityRemoved struct {
	Router    common.Address
	AssetId   common.Address
	Amount    *big.Int
	Recipient common.Address
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterLiquidityRemoved is a free log retrieval operation binding the contract event 0x7da12116be8cb7af4b2d9e9b4a2ca2c3a3243ddd6fd3a94411902367b8eed568.
//
// Solidity: event LiquidityRemoved(address indexed router, address indexed assetId, uint256 amount, address recipient)
func (_TransactionManager *TransactionManagerFilterer) FilterLiquidityRemoved(opts *bind.FilterOpts, router []common.Address, assetId []common.Address) (*TransactionManagerLiquidityRemovedIterator, error) {

	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var assetIdRule []interface{}
	for _, assetIdItem := range assetId {
		assetIdRule = append(assetIdRule, assetIdItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "LiquidityRemoved", routerRule, assetIdRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerLiquidityRemovedIterator{contract: _TransactionManager.contract, event: "LiquidityRemoved", logs: logs, sub: sub}, nil
}

// WatchLiquidityRemoved is a free log subscription operation binding the contract event 0x7da12116be8cb7af4b2d9e9b4a2ca2c3a3243ddd6fd3a94411902367b8eed568.
//
// Solidity: event LiquidityRemoved(address indexed router, address indexed assetId, uint256 amount, address recipient)
func (_TransactionManager *TransactionManagerFilterer) WatchLiquidityRemoved(opts *bind.WatchOpts, sink chan<- *TransactionManagerLiquidityRemoved, router []common.Address, assetId []common.Address) (event.Subscription, error) {

	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var assetIdRule []interface{}
	for _, assetIdItem := range assetId {
		assetIdRule = append(assetIdRule, assetIdItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "LiquidityRemoved", routerRule, assetIdRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerLiquidityRemoved)
				if err := _TransactionManager.contract.UnpackLog(event, "LiquidityRemoved", log); err != nil {
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

// ParseLiquidityRemoved is a log parse operation binding the contract event 0x7da12116be8cb7af4b2d9e9b4a2ca2c3a3243ddd6fd3a94411902367b8eed568.
//
// Solidity: event LiquidityRemoved(address indexed router, address indexed assetId, uint256 amount, address recipient)
func (_TransactionManager *TransactionManagerFilterer) ParseLiquidityRemoved(log types.Log) (*TransactionManagerLiquidityRemoved, error) {
	event := new(TransactionManagerLiquidityRemoved)
	if err := _TransactionManager.contract.UnpackLog(event, "LiquidityRemoved", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerOwnershipProposedIterator is returned from FilterOwnershipProposed and is used to iterate over the raw logs and unpacked data for OwnershipProposed events raised by the TransactionManager contract.
type TransactionManagerOwnershipProposedIterator struct {
	Event *TransactionManagerOwnershipProposed // Event containing the contract specifics and raw log

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
func (it *TransactionManagerOwnershipProposedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerOwnershipProposed)
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
		it.Event = new(TransactionManagerOwnershipProposed)
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
func (it *TransactionManagerOwnershipProposedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerOwnershipProposedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerOwnershipProposed represents a OwnershipProposed event raised by the TransactionManager contract.
type TransactionManagerOwnershipProposed struct {
	ProposedOwner common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterOwnershipProposed is a free log retrieval operation binding the contract event 0x6ab4d119f23076e8ad491bc65ce85f017fb0591dce08755ba8591059cc51737a.
//
// Solidity: event OwnershipProposed(address indexed proposedOwner)
func (_TransactionManager *TransactionManagerFilterer) FilterOwnershipProposed(opts *bind.FilterOpts, proposedOwner []common.Address) (*TransactionManagerOwnershipProposedIterator, error) {

	var proposedOwnerRule []interface{}
	for _, proposedOwnerItem := range proposedOwner {
		proposedOwnerRule = append(proposedOwnerRule, proposedOwnerItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "OwnershipProposed", proposedOwnerRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerOwnershipProposedIterator{contract: _TransactionManager.contract, event: "OwnershipProposed", logs: logs, sub: sub}, nil
}

// WatchOwnershipProposed is a free log subscription operation binding the contract event 0x6ab4d119f23076e8ad491bc65ce85f017fb0591dce08755ba8591059cc51737a.
//
// Solidity: event OwnershipProposed(address indexed proposedOwner)
func (_TransactionManager *TransactionManagerFilterer) WatchOwnershipProposed(opts *bind.WatchOpts, sink chan<- *TransactionManagerOwnershipProposed, proposedOwner []common.Address) (event.Subscription, error) {

	var proposedOwnerRule []interface{}
	for _, proposedOwnerItem := range proposedOwner {
		proposedOwnerRule = append(proposedOwnerRule, proposedOwnerItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "OwnershipProposed", proposedOwnerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerOwnershipProposed)
				if err := _TransactionManager.contract.UnpackLog(event, "OwnershipProposed", log); err != nil {
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
func (_TransactionManager *TransactionManagerFilterer) ParseOwnershipProposed(log types.Log) (*TransactionManagerOwnershipProposed, error) {
	event := new(TransactionManagerOwnershipProposed)
	if err := _TransactionManager.contract.UnpackLog(event, "OwnershipProposed", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerOwnershipTransferredIterator is returned from FilterOwnershipTransferred and is used to iterate over the raw logs and unpacked data for OwnershipTransferred events raised by the TransactionManager contract.
type TransactionManagerOwnershipTransferredIterator struct {
	Event *TransactionManagerOwnershipTransferred // Event containing the contract specifics and raw log

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
func (it *TransactionManagerOwnershipTransferredIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerOwnershipTransferred)
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
		it.Event = new(TransactionManagerOwnershipTransferred)
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
func (it *TransactionManagerOwnershipTransferredIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerOwnershipTransferredIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerOwnershipTransferred represents a OwnershipTransferred event raised by the TransactionManager contract.
type TransactionManagerOwnershipTransferred struct {
	PreviousOwner common.Address
	NewOwner      common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterOwnershipTransferred is a free log retrieval operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_TransactionManager *TransactionManagerFilterer) FilterOwnershipTransferred(opts *bind.FilterOpts, previousOwner []common.Address, newOwner []common.Address) (*TransactionManagerOwnershipTransferredIterator, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerOwnershipTransferredIterator{contract: _TransactionManager.contract, event: "OwnershipTransferred", logs: logs, sub: sub}, nil
}

// WatchOwnershipTransferred is a free log subscription operation binding the contract event 0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0.
//
// Solidity: event OwnershipTransferred(address indexed previousOwner, address indexed newOwner)
func (_TransactionManager *TransactionManagerFilterer) WatchOwnershipTransferred(opts *bind.WatchOpts, sink chan<- *TransactionManagerOwnershipTransferred, previousOwner []common.Address, newOwner []common.Address) (event.Subscription, error) {

	var previousOwnerRule []interface{}
	for _, previousOwnerItem := range previousOwner {
		previousOwnerRule = append(previousOwnerRule, previousOwnerItem)
	}
	var newOwnerRule []interface{}
	for _, newOwnerItem := range newOwner {
		newOwnerRule = append(newOwnerRule, newOwnerItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "OwnershipTransferred", previousOwnerRule, newOwnerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerOwnershipTransferred)
				if err := _TransactionManager.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
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
func (_TransactionManager *TransactionManagerFilterer) ParseOwnershipTransferred(log types.Log) (*TransactionManagerOwnershipTransferred, error) {
	event := new(TransactionManagerOwnershipTransferred)
	if err := _TransactionManager.contract.UnpackLog(event, "OwnershipTransferred", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerRouterAddedIterator is returned from FilterRouterAdded and is used to iterate over the raw logs and unpacked data for RouterAdded events raised by the TransactionManager contract.
type TransactionManagerRouterAddedIterator struct {
	Event *TransactionManagerRouterAdded // Event containing the contract specifics and raw log

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
func (it *TransactionManagerRouterAddedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerRouterAdded)
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
		it.Event = new(TransactionManagerRouterAdded)
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
func (it *TransactionManagerRouterAddedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerRouterAddedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerRouterAdded represents a RouterAdded event raised by the TransactionManager contract.
type TransactionManagerRouterAdded struct {
	AddedRouter common.Address
	Caller      common.Address
	Raw         types.Log // Blockchain specific contextual infos
}

// FilterRouterAdded is a free log retrieval operation binding the contract event 0xbc68405e644da2aaf25623ce2199da82c6dfd2e1de102b400eba6a091704d4f4.
//
// Solidity: event RouterAdded(address indexed addedRouter, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) FilterRouterAdded(opts *bind.FilterOpts, addedRouter []common.Address, caller []common.Address) (*TransactionManagerRouterAddedIterator, error) {

	var addedRouterRule []interface{}
	for _, addedRouterItem := range addedRouter {
		addedRouterRule = append(addedRouterRule, addedRouterItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "RouterAdded", addedRouterRule, callerRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerRouterAddedIterator{contract: _TransactionManager.contract, event: "RouterAdded", logs: logs, sub: sub}, nil
}

// WatchRouterAdded is a free log subscription operation binding the contract event 0xbc68405e644da2aaf25623ce2199da82c6dfd2e1de102b400eba6a091704d4f4.
//
// Solidity: event RouterAdded(address indexed addedRouter, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) WatchRouterAdded(opts *bind.WatchOpts, sink chan<- *TransactionManagerRouterAdded, addedRouter []common.Address, caller []common.Address) (event.Subscription, error) {

	var addedRouterRule []interface{}
	for _, addedRouterItem := range addedRouter {
		addedRouterRule = append(addedRouterRule, addedRouterItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "RouterAdded", addedRouterRule, callerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerRouterAdded)
				if err := _TransactionManager.contract.UnpackLog(event, "RouterAdded", log); err != nil {
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

// ParseRouterAdded is a log parse operation binding the contract event 0xbc68405e644da2aaf25623ce2199da82c6dfd2e1de102b400eba6a091704d4f4.
//
// Solidity: event RouterAdded(address indexed addedRouter, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) ParseRouterAdded(log types.Log) (*TransactionManagerRouterAdded, error) {
	event := new(TransactionManagerRouterAdded)
	if err := _TransactionManager.contract.UnpackLog(event, "RouterAdded", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerRouterOwnershipRenouncedIterator is returned from FilterRouterOwnershipRenounced and is used to iterate over the raw logs and unpacked data for RouterOwnershipRenounced events raised by the TransactionManager contract.
type TransactionManagerRouterOwnershipRenouncedIterator struct {
	Event *TransactionManagerRouterOwnershipRenounced // Event containing the contract specifics and raw log

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
func (it *TransactionManagerRouterOwnershipRenouncedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerRouterOwnershipRenounced)
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
		it.Event = new(TransactionManagerRouterOwnershipRenounced)
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
func (it *TransactionManagerRouterOwnershipRenouncedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerRouterOwnershipRenouncedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerRouterOwnershipRenounced represents a RouterOwnershipRenounced event raised by the TransactionManager contract.
type TransactionManagerRouterOwnershipRenounced struct {
	Renounced bool
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterRouterOwnershipRenounced is a free log retrieval operation binding the contract event 0x243ebbb2f905234bbf0556bb38e1f7c23b09ffd2e441a16e58b844eb2ab7a397.
//
// Solidity: event RouterOwnershipRenounced(bool renounced)
func (_TransactionManager *TransactionManagerFilterer) FilterRouterOwnershipRenounced(opts *bind.FilterOpts) (*TransactionManagerRouterOwnershipRenouncedIterator, error) {

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "RouterOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return &TransactionManagerRouterOwnershipRenouncedIterator{contract: _TransactionManager.contract, event: "RouterOwnershipRenounced", logs: logs, sub: sub}, nil
}

// WatchRouterOwnershipRenounced is a free log subscription operation binding the contract event 0x243ebbb2f905234bbf0556bb38e1f7c23b09ffd2e441a16e58b844eb2ab7a397.
//
// Solidity: event RouterOwnershipRenounced(bool renounced)
func (_TransactionManager *TransactionManagerFilterer) WatchRouterOwnershipRenounced(opts *bind.WatchOpts, sink chan<- *TransactionManagerRouterOwnershipRenounced) (event.Subscription, error) {

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "RouterOwnershipRenounced")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerRouterOwnershipRenounced)
				if err := _TransactionManager.contract.UnpackLog(event, "RouterOwnershipRenounced", log); err != nil {
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
func (_TransactionManager *TransactionManagerFilterer) ParseRouterOwnershipRenounced(log types.Log) (*TransactionManagerRouterOwnershipRenounced, error) {
	event := new(TransactionManagerRouterOwnershipRenounced)
	if err := _TransactionManager.contract.UnpackLog(event, "RouterOwnershipRenounced", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerRouterOwnershipRenunciationProposedIterator is returned from FilterRouterOwnershipRenunciationProposed and is used to iterate over the raw logs and unpacked data for RouterOwnershipRenunciationProposed events raised by the TransactionManager contract.
type TransactionManagerRouterOwnershipRenunciationProposedIterator struct {
	Event *TransactionManagerRouterOwnershipRenunciationProposed // Event containing the contract specifics and raw log

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
func (it *TransactionManagerRouterOwnershipRenunciationProposedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerRouterOwnershipRenunciationProposed)
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
		it.Event = new(TransactionManagerRouterOwnershipRenunciationProposed)
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
func (it *TransactionManagerRouterOwnershipRenunciationProposedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerRouterOwnershipRenunciationProposedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerRouterOwnershipRenunciationProposed represents a RouterOwnershipRenunciationProposed event raised by the TransactionManager contract.
type TransactionManagerRouterOwnershipRenunciationProposed struct {
	Timestamp *big.Int
	Raw       types.Log // Blockchain specific contextual infos
}

// FilterRouterOwnershipRenunciationProposed is a free log retrieval operation binding the contract event 0xa52048c5f468d21a62e4644ac4db19bcaa1a20f0cf37d163ba49c7217d35feb8.
//
// Solidity: event RouterOwnershipRenunciationProposed(uint256 timestamp)
func (_TransactionManager *TransactionManagerFilterer) FilterRouterOwnershipRenunciationProposed(opts *bind.FilterOpts) (*TransactionManagerRouterOwnershipRenunciationProposedIterator, error) {

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "RouterOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return &TransactionManagerRouterOwnershipRenunciationProposedIterator{contract: _TransactionManager.contract, event: "RouterOwnershipRenunciationProposed", logs: logs, sub: sub}, nil
}

// WatchRouterOwnershipRenunciationProposed is a free log subscription operation binding the contract event 0xa52048c5f468d21a62e4644ac4db19bcaa1a20f0cf37d163ba49c7217d35feb8.
//
// Solidity: event RouterOwnershipRenunciationProposed(uint256 timestamp)
func (_TransactionManager *TransactionManagerFilterer) WatchRouterOwnershipRenunciationProposed(opts *bind.WatchOpts, sink chan<- *TransactionManagerRouterOwnershipRenunciationProposed) (event.Subscription, error) {

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "RouterOwnershipRenunciationProposed")
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerRouterOwnershipRenunciationProposed)
				if err := _TransactionManager.contract.UnpackLog(event, "RouterOwnershipRenunciationProposed", log); err != nil {
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
func (_TransactionManager *TransactionManagerFilterer) ParseRouterOwnershipRenunciationProposed(log types.Log) (*TransactionManagerRouterOwnershipRenunciationProposed, error) {
	event := new(TransactionManagerRouterOwnershipRenunciationProposed)
	if err := _TransactionManager.contract.UnpackLog(event, "RouterOwnershipRenunciationProposed", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerRouterRemovedIterator is returned from FilterRouterRemoved and is used to iterate over the raw logs and unpacked data for RouterRemoved events raised by the TransactionManager contract.
type TransactionManagerRouterRemovedIterator struct {
	Event *TransactionManagerRouterRemoved // Event containing the contract specifics and raw log

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
func (it *TransactionManagerRouterRemovedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerRouterRemoved)
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
		it.Event = new(TransactionManagerRouterRemoved)
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
func (it *TransactionManagerRouterRemovedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerRouterRemovedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerRouterRemoved represents a RouterRemoved event raised by the TransactionManager contract.
type TransactionManagerRouterRemoved struct {
	RemovedRouter common.Address
	Caller        common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterRouterRemoved is a free log retrieval operation binding the contract event 0xbee3e974bb6a6f44f20096ede047c191eef60322e65e4ee4bd3392230a8716d5.
//
// Solidity: event RouterRemoved(address indexed removedRouter, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) FilterRouterRemoved(opts *bind.FilterOpts, removedRouter []common.Address, caller []common.Address) (*TransactionManagerRouterRemovedIterator, error) {

	var removedRouterRule []interface{}
	for _, removedRouterItem := range removedRouter {
		removedRouterRule = append(removedRouterRule, removedRouterItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "RouterRemoved", removedRouterRule, callerRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerRouterRemovedIterator{contract: _TransactionManager.contract, event: "RouterRemoved", logs: logs, sub: sub}, nil
}

// WatchRouterRemoved is a free log subscription operation binding the contract event 0xbee3e974bb6a6f44f20096ede047c191eef60322e65e4ee4bd3392230a8716d5.
//
// Solidity: event RouterRemoved(address indexed removedRouter, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) WatchRouterRemoved(opts *bind.WatchOpts, sink chan<- *TransactionManagerRouterRemoved, removedRouter []common.Address, caller []common.Address) (event.Subscription, error) {

	var removedRouterRule []interface{}
	for _, removedRouterItem := range removedRouter {
		removedRouterRule = append(removedRouterRule, removedRouterItem)
	}
	var callerRule []interface{}
	for _, callerItem := range caller {
		callerRule = append(callerRule, callerItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "RouterRemoved", removedRouterRule, callerRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerRouterRemoved)
				if err := _TransactionManager.contract.UnpackLog(event, "RouterRemoved", log); err != nil {
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

// ParseRouterRemoved is a log parse operation binding the contract event 0xbee3e974bb6a6f44f20096ede047c191eef60322e65e4ee4bd3392230a8716d5.
//
// Solidity: event RouterRemoved(address indexed removedRouter, address indexed caller)
func (_TransactionManager *TransactionManagerFilterer) ParseRouterRemoved(log types.Log) (*TransactionManagerRouterRemoved, error) {
	event := new(TransactionManagerRouterRemoved)
	if err := _TransactionManager.contract.UnpackLog(event, "RouterRemoved", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerTransactionCancelledIterator is returned from FilterTransactionCancelled and is used to iterate over the raw logs and unpacked data for TransactionCancelled events raised by the TransactionManager contract.
type TransactionManagerTransactionCancelledIterator struct {
	Event *TransactionManagerTransactionCancelled // Event containing the contract specifics and raw log

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
func (it *TransactionManagerTransactionCancelledIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerTransactionCancelled)
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
		it.Event = new(TransactionManagerTransactionCancelled)
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
func (it *TransactionManagerTransactionCancelledIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerTransactionCancelledIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerTransactionCancelled represents a TransactionCancelled event raised by the TransactionManager contract.
type TransactionManagerTransactionCancelled struct {
	User          common.Address
	Router        common.Address
	TransactionId [32]byte
	Args          ITransactionManagerCancelArgs
	Caller        common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterTransactionCancelled is a free log retrieval operation binding the contract event 0x56a92405e111173b950d90846413f755ca35bb7631d49a4a564778b21affe287.
//
// Solidity: event TransactionCancelled(address indexed user, address indexed router, bytes32 indexed transactionId, ((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args, address caller)
func (_TransactionManager *TransactionManagerFilterer) FilterTransactionCancelled(opts *bind.FilterOpts, user []common.Address, router []common.Address, transactionId [][32]byte) (*TransactionManagerTransactionCancelledIterator, error) {

	var userRule []interface{}
	for _, userItem := range user {
		userRule = append(userRule, userItem)
	}
	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var transactionIdRule []interface{}
	for _, transactionIdItem := range transactionId {
		transactionIdRule = append(transactionIdRule, transactionIdItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "TransactionCancelled", userRule, routerRule, transactionIdRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerTransactionCancelledIterator{contract: _TransactionManager.contract, event: "TransactionCancelled", logs: logs, sub: sub}, nil
}

// WatchTransactionCancelled is a free log subscription operation binding the contract event 0x56a92405e111173b950d90846413f755ca35bb7631d49a4a564778b21affe287.
//
// Solidity: event TransactionCancelled(address indexed user, address indexed router, bytes32 indexed transactionId, ((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args, address caller)
func (_TransactionManager *TransactionManagerFilterer) WatchTransactionCancelled(opts *bind.WatchOpts, sink chan<- *TransactionManagerTransactionCancelled, user []common.Address, router []common.Address, transactionId [][32]byte) (event.Subscription, error) {

	var userRule []interface{}
	for _, userItem := range user {
		userRule = append(userRule, userItem)
	}
	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var transactionIdRule []interface{}
	for _, transactionIdItem := range transactionId {
		transactionIdRule = append(transactionIdRule, transactionIdItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "TransactionCancelled", userRule, routerRule, transactionIdRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerTransactionCancelled)
				if err := _TransactionManager.contract.UnpackLog(event, "TransactionCancelled", log); err != nil {
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

// ParseTransactionCancelled is a log parse operation binding the contract event 0x56a92405e111173b950d90846413f755ca35bb7631d49a4a564778b21affe287.
//
// Solidity: event TransactionCancelled(address indexed user, address indexed router, bytes32 indexed transactionId, ((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),bytes,bytes) args, address caller)
func (_TransactionManager *TransactionManagerFilterer) ParseTransactionCancelled(log types.Log) (*TransactionManagerTransactionCancelled, error) {
	event := new(TransactionManagerTransactionCancelled)
	if err := _TransactionManager.contract.UnpackLog(event, "TransactionCancelled", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerTransactionFulfilledIterator is returned from FilterTransactionFulfilled and is used to iterate over the raw logs and unpacked data for TransactionFulfilled events raised by the TransactionManager contract.
type TransactionManagerTransactionFulfilledIterator struct {
	Event *TransactionManagerTransactionFulfilled // Event containing the contract specifics and raw log

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
func (it *TransactionManagerTransactionFulfilledIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerTransactionFulfilled)
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
		it.Event = new(TransactionManagerTransactionFulfilled)
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
func (it *TransactionManagerTransactionFulfilledIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerTransactionFulfilledIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerTransactionFulfilled represents a TransactionFulfilled event raised by the TransactionManager contract.
type TransactionManagerTransactionFulfilled struct {
	User          common.Address
	Router        common.Address
	TransactionId [32]byte
	Args          ITransactionManagerFulfillArgs
	Success       bool
	IsContract    bool
	ReturnData    []byte
	Caller        common.Address
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterTransactionFulfilled is a free log retrieval operation binding the contract event 0x8e5df24f8b9ac0e3455417a1d7060762388ce3c1d4941aa49dc1b61943031d32.
//
// Solidity: event TransactionFulfilled(address indexed user, address indexed router, bytes32 indexed transactionId, ((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args, bool success, bool isContract, bytes returnData, address caller)
func (_TransactionManager *TransactionManagerFilterer) FilterTransactionFulfilled(opts *bind.FilterOpts, user []common.Address, router []common.Address, transactionId [][32]byte) (*TransactionManagerTransactionFulfilledIterator, error) {

	var userRule []interface{}
	for _, userItem := range user {
		userRule = append(userRule, userItem)
	}
	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var transactionIdRule []interface{}
	for _, transactionIdItem := range transactionId {
		transactionIdRule = append(transactionIdRule, transactionIdItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "TransactionFulfilled", userRule, routerRule, transactionIdRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerTransactionFulfilledIterator{contract: _TransactionManager.contract, event: "TransactionFulfilled", logs: logs, sub: sub}, nil
}

// WatchTransactionFulfilled is a free log subscription operation binding the contract event 0x8e5df24f8b9ac0e3455417a1d7060762388ce3c1d4941aa49dc1b61943031d32.
//
// Solidity: event TransactionFulfilled(address indexed user, address indexed router, bytes32 indexed transactionId, ((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args, bool success, bool isContract, bytes returnData, address caller)
func (_TransactionManager *TransactionManagerFilterer) WatchTransactionFulfilled(opts *bind.WatchOpts, sink chan<- *TransactionManagerTransactionFulfilled, user []common.Address, router []common.Address, transactionId [][32]byte) (event.Subscription, error) {

	var userRule []interface{}
	for _, userItem := range user {
		userRule = append(userRule, userItem)
	}
	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var transactionIdRule []interface{}
	for _, transactionIdItem := range transactionId {
		transactionIdRule = append(transactionIdRule, transactionIdItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "TransactionFulfilled", userRule, routerRule, transactionIdRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerTransactionFulfilled)
				if err := _TransactionManager.contract.UnpackLog(event, "TransactionFulfilled", log); err != nil {
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

// ParseTransactionFulfilled is a log parse operation binding the contract event 0x8e5df24f8b9ac0e3455417a1d7060762388ce3c1d4941aa49dc1b61943031d32.
//
// Solidity: event TransactionFulfilled(address indexed user, address indexed router, bytes32 indexed transactionId, ((address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256),uint256,bytes,bytes,bytes) args, bool success, bool isContract, bytes returnData, address caller)
func (_TransactionManager *TransactionManagerFilterer) ParseTransactionFulfilled(log types.Log) (*TransactionManagerTransactionFulfilled, error) {
	event := new(TransactionManagerTransactionFulfilled)
	if err := _TransactionManager.contract.UnpackLog(event, "TransactionFulfilled", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// TransactionManagerTransactionPreparedIterator is returned from FilterTransactionPrepared and is used to iterate over the raw logs and unpacked data for TransactionPrepared events raised by the TransactionManager contract.
type TransactionManagerTransactionPreparedIterator struct {
	Event *TransactionManagerTransactionPrepared // Event containing the contract specifics and raw log

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
func (it *TransactionManagerTransactionPreparedIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(TransactionManagerTransactionPrepared)
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
		it.Event = new(TransactionManagerTransactionPrepared)
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
func (it *TransactionManagerTransactionPreparedIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *TransactionManagerTransactionPreparedIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// TransactionManagerTransactionPrepared represents a TransactionPrepared event raised by the TransactionManager contract.
type TransactionManagerTransactionPrepared struct {
	User          common.Address
	Router        common.Address
	TransactionId [32]byte
	TxData        ITransactionManagerTransactionData
	Caller        common.Address
	Args          ITransactionManagerPrepareArgs
	Raw           types.Log // Blockchain specific contextual infos
}

// FilterTransactionPrepared is a free log retrieval operation binding the contract event 0x88fbf1dbc326c404155bad4643bd0ddadd23f0636929c66442f0433208b2c905.
//
// Solidity: event TransactionPrepared(address indexed user, address indexed router, bytes32 indexed transactionId, (address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address caller, ((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args)
func (_TransactionManager *TransactionManagerFilterer) FilterTransactionPrepared(opts *bind.FilterOpts, user []common.Address, router []common.Address, transactionId [][32]byte) (*TransactionManagerTransactionPreparedIterator, error) {

	var userRule []interface{}
	for _, userItem := range user {
		userRule = append(userRule, userItem)
	}
	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var transactionIdRule []interface{}
	for _, transactionIdItem := range transactionId {
		transactionIdRule = append(transactionIdRule, transactionIdItem)
	}

	logs, sub, err := _TransactionManager.contract.FilterLogs(opts, "TransactionPrepared", userRule, routerRule, transactionIdRule)
	if err != nil {
		return nil, err
	}
	return &TransactionManagerTransactionPreparedIterator{contract: _TransactionManager.contract, event: "TransactionPrepared", logs: logs, sub: sub}, nil
}

// WatchTransactionPrepared is a free log subscription operation binding the contract event 0x88fbf1dbc326c404155bad4643bd0ddadd23f0636929c66442f0433208b2c905.
//
// Solidity: event TransactionPrepared(address indexed user, address indexed router, bytes32 indexed transactionId, (address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address caller, ((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args)
func (_TransactionManager *TransactionManagerFilterer) WatchTransactionPrepared(opts *bind.WatchOpts, sink chan<- *TransactionManagerTransactionPrepared, user []common.Address, router []common.Address, transactionId [][32]byte) (event.Subscription, error) {

	var userRule []interface{}
	for _, userItem := range user {
		userRule = append(userRule, userItem)
	}
	var routerRule []interface{}
	for _, routerItem := range router {
		routerRule = append(routerRule, routerItem)
	}
	var transactionIdRule []interface{}
	for _, transactionIdItem := range transactionId {
		transactionIdRule = append(transactionIdRule, transactionIdItem)
	}

	logs, sub, err := _TransactionManager.contract.WatchLogs(opts, "TransactionPrepared", userRule, routerRule, transactionIdRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(TransactionManagerTransactionPrepared)
				if err := _TransactionManager.contract.UnpackLog(event, "TransactionPrepared", log); err != nil {
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

// ParseTransactionPrepared is a log parse operation binding the contract event 0x88fbf1dbc326c404155bad4643bd0ddadd23f0636929c66442f0433208b2c905.
//
// Solidity: event TransactionPrepared(address indexed user, address indexed router, bytes32 indexed transactionId, (address,address,address,address,address,address,address,address,address,bytes32,bytes32,uint256,uint256,uint256,uint256,uint256) txData, address caller, ((address,address,address,address,address,address,address,address,address,uint256,uint256,bytes32,bytes32),uint256,uint256,bytes,bytes,bytes,bytes) args)
func (_TransactionManager *TransactionManagerFilterer) ParseTransactionPrepared(log types.Log) (*TransactionManagerTransactionPrepared, error) {
	event := new(TransactionManagerTransactionPrepared)
	if err := _TransactionManager.contract.UnpackLog(event, "TransactionPrepared", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}
