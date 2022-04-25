/* DO NOT EDIT THE BELOW FILE AS THIS IS LIKELY WILL BE GENERATED AGAIN AND REWRITE OVER IT */

// tslint:disable:no-consecutive-blank-lines ordered-imports align trailing-comma enum-naming
// tslint:disable:whitespace no-unbound-method no-trailing-whitespace
// tslint:disable:no-unused-variable

import * as ethers from "ethers"
// eslint-disable-next-line import/named
import {
  assert,
  schemas,
  // eslint-disable-next-line import/named
  SubscriptionManager,
  // eslint-disable-next-line import/named
  BaseContract,
  // eslint-disable-next-line import/named
  EventCallback,
  // eslint-disable-next-line import/named
  IndexedFilterValues,
  // eslint-disable-next-line import/named
  BlockRange,
  // eslint-disable-next-line import/named
  DecodedLogArgs,
  // eslint-disable-next-line import/named
  LogWithDecodedArgs,
  // eslint-disable-next-line import/named
  MethodAbi
} from "vue-blocklink"

import {
  BatchRequest,
  Extension,
  Log,
  PromiEvent,
  provider,
  Providers,
  RLPEncodedTransaction,
  Transaction,
  TransactionConfig,
  TransactionReceipt,
  Common,
  hardfork,
  chain,
  BlockNumber,
  LogsOptions,
  PastLogsOptions
} from "web3-core"

import { Utils, AbiItem } from "web3-utils"
import Web3 from "web3"
import BN from "BN.js"

// tslint:enable:no-unused-variable
export interface ContractInterface {
    MAX_TIMEOUT():Promise<BN>
    MIN_TIMEOUT():Promise<BN>
    acceptProposedOwner():Promise<void>
    addAssetId(assetId: string,):Promise<void>
    addLiquidity(amount: BN,assetId: string,coin: BN):Promise<void>
    addLiquidityFor(amount: BN,assetId: string,router: string,coin: BN):Promise<void>
    addRouter(router: string,):Promise<void>
    approvedAssets(index_0: string,):Promise<boolean>
    approvedRouters(index_0: string,):Promise<boolean>
    assetOwnershipTimestamp():Promise<BN>
    cancel(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};signature: string;encodedMeta: string},):Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}>
    delay():Promise<BN>
    fulfill(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};relayerFee: BN;signature: string;callData: string;encodedMeta: string},):Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}>
    getChainId():Promise<BN>
    getStoredChainId():Promise<BN>
    interpreter():Promise<string>
    isAssetOwnershipRenounced():Promise<boolean>
    isRouterOwnershipRenounced():Promise<boolean>
    owner():Promise<string>
    prepare(args: {invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};amount: BN;expiry: BN;encryptedCallData: string;encodedBid: string;bidSignature: string;encodedMeta: string},coin: BN):Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}>
    proposeAssetOwnershipRenunciation():Promise<void>
    proposeNewOwner(newlyProposed: string,):Promise<void>
    proposeRouterOwnershipRenunciation():Promise<void>
    proposed():Promise<string>
    proposedTimestamp():Promise<BN>
    removeAssetId(assetId: string,):Promise<void>
    removeLiquidity(amount: BN,assetId: string,recipient: string,):Promise<void>
    removeRouter(router: string,):Promise<void>
    renounceAssetOwnership():Promise<void>
    renounceOwnership():Promise<void>
    renounceRouterOwnership():Promise<void>
    renounced():Promise<boolean>
    routerBalances(index_0: string,index_1: string,):Promise<BN>
    routerOwnershipTimestamp():Promise<BN>
    variantTransactionData(index_0: string,):Promise<string>
}





export enum TransactionManagerEvents {
    AssetAdded = 'AssetAdded',
    AssetOwnershipRenounced = 'AssetOwnershipRenounced',
    AssetOwnershipRenunciationProposed = 'AssetOwnershipRenunciationProposed',
    AssetRemoved = 'AssetRemoved',
    LiquidityAdded = 'LiquidityAdded',
    LiquidityRemoved = 'LiquidityRemoved',
    OwnershipProposed = 'OwnershipProposed',
    OwnershipTransferred = 'OwnershipTransferred',
    RouterAdded = 'RouterAdded',
    RouterOwnershipRenounced = 'RouterOwnershipRenounced',
    RouterOwnershipRenunciationProposed = 'RouterOwnershipRenunciationProposed',
    RouterRemoved = 'RouterRemoved',
    TransactionCancelled = 'TransactionCancelled',
    TransactionFulfilled = 'TransactionFulfilled',
    TransactionPrepared = 'TransactionPrepared',
}

export interface TransactionManagerAssetAddedEventArgs extends DecodedLogArgs {
    addedAssetId: string;
    caller: string;
}

export interface TransactionManagerAssetOwnershipRenouncedEventArgs extends DecodedLogArgs {
    renounced: boolean;
}

export interface TransactionManagerAssetOwnershipRenunciationProposedEventArgs extends DecodedLogArgs {
    timestamp: BN;
}

export interface TransactionManagerAssetRemovedEventArgs extends DecodedLogArgs {
    removedAssetId: string;
    caller: string;
}

export interface TransactionManagerLiquidityAddedEventArgs extends DecodedLogArgs {
    router: string;
    assetId: string;
    amount: BN;
    caller: string;
}

export interface TransactionManagerLiquidityRemovedEventArgs extends DecodedLogArgs {
    router: string;
    assetId: string;
    amount: BN;
    recipient: string;
}

export interface TransactionManagerOwnershipProposedEventArgs extends DecodedLogArgs {
    proposedOwner: string;
}

export interface TransactionManagerOwnershipTransferredEventArgs extends DecodedLogArgs {
    previousOwner: string;
    newOwner: string;
}

export interface TransactionManagerRouterAddedEventArgs extends DecodedLogArgs {
    addedRouter: string;
    caller: string;
}

export interface TransactionManagerRouterOwnershipRenouncedEventArgs extends DecodedLogArgs {
    renounced: boolean;
}

export interface TransactionManagerRouterOwnershipRenunciationProposedEventArgs extends DecodedLogArgs {
    timestamp: BN;
}

export interface TransactionManagerRouterRemovedEventArgs extends DecodedLogArgs {
    removedRouter: string;
    caller: string;
}

export interface TransactionManagerTransactionCancelledEventArgs extends DecodedLogArgs {
    user: string;
    router: string;
    transactionId: string;
    args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};signature: string;encodedMeta: string};
    caller: string;
}

export interface TransactionManagerTransactionFulfilledEventArgs extends DecodedLogArgs {
    user: string;
    router: string;
    transactionId: string;
    args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};relayerFee: BN;signature: string;callData: string;encodedMeta: string};
    success: boolean;
    isContract: boolean;
    returnData: string;
    caller: string;
}

export interface TransactionManagerTransactionPreparedEventArgs extends DecodedLogArgs {
    user: string;
    router: string;
    transactionId: string;
    txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};
    caller: string;
    args: {invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};amount: BN;expiry: BN;encryptedCallData: string;encodedBid: string;bidSignature: string;encodedMeta: string};
}


export type TransactionManagerEventArgs =
    | TransactionManagerAssetAddedEventArgs
    | TransactionManagerAssetOwnershipRenouncedEventArgs
    | TransactionManagerAssetOwnershipRenunciationProposedEventArgs
    | TransactionManagerAssetRemovedEventArgs
    | TransactionManagerLiquidityAddedEventArgs
    | TransactionManagerLiquidityRemovedEventArgs
    | TransactionManagerOwnershipProposedEventArgs
    | TransactionManagerOwnershipTransferredEventArgs
    | TransactionManagerRouterAddedEventArgs
    | TransactionManagerRouterOwnershipRenouncedEventArgs
    | TransactionManagerRouterOwnershipRenunciationProposedEventArgs
    | TransactionManagerRouterRemovedEventArgs
    | TransactionManagerTransactionCancelledEventArgs
    | TransactionManagerTransactionFulfilledEventArgs
    | TransactionManagerTransactionPreparedEventArgs;




/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class TransactionManagerContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'TransactionManager';
    private readonly _methodABIIndex: { [name: string]: number } = {};
    //todo: we will come back and fix it later not generic Error @https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
    // @ts-ignore
    private readonly _subscriptionManager: SubscriptionManager<TransactionManagerEventArgs, TransactionManagerEvents>;


    public static Instance(): (TransactionManagerContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_TransactionManager")) {
          // @ts-ignore
          const obj = window.__eth_contract_TransactionManager
          if (obj instanceof TransactionManagerContract) {
            return (obj) as TransactionManagerContract
          } else {
            return (obj) as TransactionManagerContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<TransactionManagerContract>
    {
        const contractInstance = await new TransactionManagerContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/** "_chainId"
 **/];

        if (window && !window.hasOwnProperty("__eth_contract_TransactionManager")) {
            // @ts-ignore
            window.__eth_contract_TransactionManager = contractInstance
        }

        return contractInstance
    }

    /**
     * @returns The contract ABI
     */
    public static ABI(): AbiItem[] {
        const abi = [
            { 
                inputs: [
                    {
                        name: '_chainId',
                        type: 'uint256',
                    },
                ],
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'constructor',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'addedAssetId',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: true,
                    },
                ],
                name: 'AssetAdded',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'renounced',
                        type: 'bool',
                        indexed: false,
                    },
                ],
                name: 'AssetOwnershipRenounced',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'timestamp',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'AssetOwnershipRenunciationProposed',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'removedAssetId',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: true,
                    },
                ],
                name: 'AssetRemoved',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'router',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'amount',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'LiquidityAdded',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'router',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'amount',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'recipient',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'LiquidityRemoved',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'proposedOwner',
                        type: 'address',
                        indexed: true,
                    },
                ],
                name: 'OwnershipProposed',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'previousOwner',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'newOwner',
                        type: 'address',
                        indexed: true,
                    },
                ],
                name: 'OwnershipTransferred',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'addedRouter',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: true,
                    },
                ],
                name: 'RouterAdded',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'renounced',
                        type: 'bool',
                        indexed: false,
                    },
                ],
                name: 'RouterOwnershipRenounced',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'timestamp',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'RouterOwnershipRenunciationProposed',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'removedRouter',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: true,
                    },
                ],
                name: 'RouterRemoved',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'user',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'router',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'transactionId',
                        type: 'bytes32',
                        indexed: true,
                    },
                    {
                        name: 'args',
                        type: 'tuple',
                        indexed: false,
                        components: [
                            {
                                name: 'txData',
                                type: 'tuple',
                                components: [
                                    {
                                        name: 'receivingChainTxManagerAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'user',
                                        type: 'address',
                                    },
                                    {
                                        name: 'router',
                                        type: 'address',
                                    },
                                    {
                                        name: 'initiator',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainFallback',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callTo',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callDataHash',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'transactionId',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'sendingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'receivingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'amount',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'expiry',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'preparedBlockNumber',
                                        type: 'uint256',
                                    },
                                ]
                            },
                            {
                                name: 'signature',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedMeta',
                                type: 'bytes',
                            },
                        ]
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'TransactionCancelled',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'user',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'router',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'transactionId',
                        type: 'bytes32',
                        indexed: true,
                    },
                    {
                        name: 'args',
                        type: 'tuple',
                        indexed: false,
                        components: [
                            {
                                name: 'txData',
                                type: 'tuple',
                                components: [
                                    {
                                        name: 'receivingChainTxManagerAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'user',
                                        type: 'address',
                                    },
                                    {
                                        name: 'router',
                                        type: 'address',
                                    },
                                    {
                                        name: 'initiator',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainFallback',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callTo',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callDataHash',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'transactionId',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'sendingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'receivingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'amount',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'expiry',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'preparedBlockNumber',
                                        type: 'uint256',
                                    },
                                ]
                            },
                            {
                                name: 'relayerFee',
                                type: 'uint256',
                            },
                            {
                                name: 'signature',
                                type: 'bytes',
                            },
                            {
                                name: 'callData',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedMeta',
                                type: 'bytes',
                            },
                        ]
                    },
                    {
                        name: 'success',
                        type: 'bool',
                        indexed: false,
                    },
                    {
                        name: 'isContract',
                        type: 'bool',
                        indexed: false,
                    },
                    {
                        name: 'returnData',
                        type: 'bytes',
                        indexed: false,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'TransactionFulfilled',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'user',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'router',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'transactionId',
                        type: 'bytes32',
                        indexed: true,
                    },
                    {
                        name: 'txData',
                        type: 'tuple',
                        indexed: false,
                        components: [
                            {
                                name: 'receivingChainTxManagerAddress',
                                type: 'address',
                            },
                            {
                                name: 'user',
                                type: 'address',
                            },
                            {
                                name: 'router',
                                type: 'address',
                            },
                            {
                                name: 'initiator',
                                type: 'address',
                            },
                            {
                                name: 'sendingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'receivingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'sendingChainFallback',
                                type: 'address',
                            },
                            {
                                name: 'receivingAddress',
                                type: 'address',
                            },
                            {
                                name: 'callTo',
                                type: 'address',
                            },
                            {
                                name: 'callDataHash',
                                type: 'bytes32',
                            },
                            {
                                name: 'transactionId',
                                type: 'bytes32',
                            },
                            {
                                name: 'sendingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'receivingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'amount',
                                type: 'uint256',
                            },
                            {
                                name: 'expiry',
                                type: 'uint256',
                            },
                            {
                                name: 'preparedBlockNumber',
                                type: 'uint256',
                            },
                        ]
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'args',
                        type: 'tuple',
                        indexed: false,
                        components: [
                            {
                                name: 'invariantData',
                                type: 'tuple',
                                components: [
                                    {
                                        name: 'receivingChainTxManagerAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'user',
                                        type: 'address',
                                    },
                                    {
                                        name: 'router',
                                        type: 'address',
                                    },
                                    {
                                        name: 'initiator',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainFallback',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callTo',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'receivingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'callDataHash',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'transactionId',
                                        type: 'bytes32',
                                    },
                                ]
                            },
                            {
                                name: 'amount',
                                type: 'uint256',
                            },
                            {
                                name: 'expiry',
                                type: 'uint256',
                            },
                            {
                                name: 'encryptedCallData',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedBid',
                                type: 'bytes',
                            },
                            {
                                name: 'bidSignature',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedMeta',
                                type: 'bytes',
                            },
                        ]
                    },
                ],
                name: 'TransactionPrepared',
                outputs: [
                ],
                type: 'event',
            },
            { 
                inputs: [
                ],
                name: 'MAX_TIMEOUT',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'MIN_TIMEOUT',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'acceptProposedOwner',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'assetId',
                        type: 'address',
                    },
                ],
                name: 'addAssetId',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                    },
                ],
                name: 'addLiquidity',
                outputs: [
                ],
                stateMutability: 'payable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                    },
                    {
                        name: 'router',
                        type: 'address',
                    },
                ],
                name: 'addLiquidityFor',
                outputs: [
                ],
                stateMutability: 'payable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'router',
                        type: 'address',
                    },
                ],
                name: 'addRouter',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'index_0',
                        type: 'address',
                    },
                ],
                name: 'approvedAssets',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'index_0',
                        type: 'address',
                    },
                ],
                name: 'approvedRouters',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'assetOwnershipTimestamp',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'args',
                        type: 'tuple',
                        components: [
                            {
                                name: 'txData',
                                type: 'tuple',
                                components: [
                                    {
                                        name: 'receivingChainTxManagerAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'user',
                                        type: 'address',
                                    },
                                    {
                                        name: 'router',
                                        type: 'address',
                                    },
                                    {
                                        name: 'initiator',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainFallback',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callTo',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callDataHash',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'transactionId',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'sendingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'receivingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'amount',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'expiry',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'preparedBlockNumber',
                                        type: 'uint256',
                                    },
                                ]
                            },
                            {
                                name: 'signature',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedMeta',
                                type: 'bytes',
                            },
                        ]
                    },
                ],
                name: 'cancel',
                outputs: [
                    {
                        name: '',
                        type: 'tuple',
                        components: [
                            {
                                name: 'receivingChainTxManagerAddress',
                                type: 'address',
                            },
                            {
                                name: 'user',
                                type: 'address',
                            },
                            {
                                name: 'router',
                                type: 'address',
                            },
                            {
                                name: 'initiator',
                                type: 'address',
                            },
                            {
                                name: 'sendingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'receivingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'sendingChainFallback',
                                type: 'address',
                            },
                            {
                                name: 'receivingAddress',
                                type: 'address',
                            },
                            {
                                name: 'callTo',
                                type: 'address',
                            },
                            {
                                name: 'callDataHash',
                                type: 'bytes32',
                            },
                            {
                                name: 'transactionId',
                                type: 'bytes32',
                            },
                            {
                                name: 'sendingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'receivingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'amount',
                                type: 'uint256',
                            },
                            {
                                name: 'expiry',
                                type: 'uint256',
                            },
                            {
                                name: 'preparedBlockNumber',
                                type: 'uint256',
                            },
                        ]
                    },
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'delay',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'args',
                        type: 'tuple',
                        components: [
                            {
                                name: 'txData',
                                type: 'tuple',
                                components: [
                                    {
                                        name: 'receivingChainTxManagerAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'user',
                                        type: 'address',
                                    },
                                    {
                                        name: 'router',
                                        type: 'address',
                                    },
                                    {
                                        name: 'initiator',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainFallback',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callTo',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callDataHash',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'transactionId',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'sendingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'receivingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'amount',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'expiry',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'preparedBlockNumber',
                                        type: 'uint256',
                                    },
                                ]
                            },
                            {
                                name: 'relayerFee',
                                type: 'uint256',
                            },
                            {
                                name: 'signature',
                                type: 'bytes',
                            },
                            {
                                name: 'callData',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedMeta',
                                type: 'bytes',
                            },
                        ]
                    },
                ],
                name: 'fulfill',
                outputs: [
                    {
                        name: '',
                        type: 'tuple',
                        components: [
                            {
                                name: 'receivingChainTxManagerAddress',
                                type: 'address',
                            },
                            {
                                name: 'user',
                                type: 'address',
                            },
                            {
                                name: 'router',
                                type: 'address',
                            },
                            {
                                name: 'initiator',
                                type: 'address',
                            },
                            {
                                name: 'sendingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'receivingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'sendingChainFallback',
                                type: 'address',
                            },
                            {
                                name: 'receivingAddress',
                                type: 'address',
                            },
                            {
                                name: 'callTo',
                                type: 'address',
                            },
                            {
                                name: 'callDataHash',
                                type: 'bytes32',
                            },
                            {
                                name: 'transactionId',
                                type: 'bytes32',
                            },
                            {
                                name: 'sendingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'receivingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'amount',
                                type: 'uint256',
                            },
                            {
                                name: 'expiry',
                                type: 'uint256',
                            },
                            {
                                name: 'preparedBlockNumber',
                                type: 'uint256',
                            },
                        ]
                    },
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'getChainId',
                outputs: [
                    {
                        name: '_chainId',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'getStoredChainId',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'interpreter',
                outputs: [
                    {
                        name: '',
                        type: 'address',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'isAssetOwnershipRenounced',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'isRouterOwnershipRenounced',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'owner',
                outputs: [
                    {
                        name: '',
                        type: 'address',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'args',
                        type: 'tuple',
                        components: [
                            {
                                name: 'invariantData',
                                type: 'tuple',
                                components: [
                                    {
                                        name: 'receivingChainTxManagerAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'user',
                                        type: 'address',
                                    },
                                    {
                                        name: 'router',
                                        type: 'address',
                                    },
                                    {
                                        name: 'initiator',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAssetId',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainFallback',
                                        type: 'address',
                                    },
                                    {
                                        name: 'receivingAddress',
                                        type: 'address',
                                    },
                                    {
                                        name: 'callTo',
                                        type: 'address',
                                    },
                                    {
                                        name: 'sendingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'receivingChainId',
                                        type: 'uint256',
                                    },
                                    {
                                        name: 'callDataHash',
                                        type: 'bytes32',
                                    },
                                    {
                                        name: 'transactionId',
                                        type: 'bytes32',
                                    },
                                ]
                            },
                            {
                                name: 'amount',
                                type: 'uint256',
                            },
                            {
                                name: 'expiry',
                                type: 'uint256',
                            },
                            {
                                name: 'encryptedCallData',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedBid',
                                type: 'bytes',
                            },
                            {
                                name: 'bidSignature',
                                type: 'bytes',
                            },
                            {
                                name: 'encodedMeta',
                                type: 'bytes',
                            },
                        ]
                    },
                ],
                name: 'prepare',
                outputs: [
                    {
                        name: '',
                        type: 'tuple',
                        components: [
                            {
                                name: 'receivingChainTxManagerAddress',
                                type: 'address',
                            },
                            {
                                name: 'user',
                                type: 'address',
                            },
                            {
                                name: 'router',
                                type: 'address',
                            },
                            {
                                name: 'initiator',
                                type: 'address',
                            },
                            {
                                name: 'sendingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'receivingAssetId',
                                type: 'address',
                            },
                            {
                                name: 'sendingChainFallback',
                                type: 'address',
                            },
                            {
                                name: 'receivingAddress',
                                type: 'address',
                            },
                            {
                                name: 'callTo',
                                type: 'address',
                            },
                            {
                                name: 'callDataHash',
                                type: 'bytes32',
                            },
                            {
                                name: 'transactionId',
                                type: 'bytes32',
                            },
                            {
                                name: 'sendingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'receivingChainId',
                                type: 'uint256',
                            },
                            {
                                name: 'amount',
                                type: 'uint256',
                            },
                            {
                                name: 'expiry',
                                type: 'uint256',
                            },
                            {
                                name: 'preparedBlockNumber',
                                type: 'uint256',
                            },
                        ]
                    },
                ],
                stateMutability: 'payable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'proposeAssetOwnershipRenunciation',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'newlyProposed',
                        type: 'address',
                    },
                ],
                name: 'proposeNewOwner',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'proposeRouterOwnershipRenunciation',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'proposed',
                outputs: [
                    {
                        name: '',
                        type: 'address',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'proposedTimestamp',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'assetId',
                        type: 'address',
                    },
                ],
                name: 'removeAssetId',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                    },
                    {
                        name: 'recipient',
                        type: 'address',
                    },
                ],
                name: 'removeLiquidity',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'router',
                        type: 'address',
                    },
                ],
                name: 'removeRouter',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'renounceAssetOwnership',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'renounceOwnership',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'renounceRouterOwnership',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'renounced',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'index_0',
                        type: 'address',
                    },
                    {
                        name: 'index_1',
                        type: 'address',
                    },
                ],
                name: 'routerBalances',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'routerOwnershipTimestamp',
                outputs: [
                    {
                        name: '',
                        type: 'uint256',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'index_0',
                        type: 'bytes32',
                    },
                ],
                name: 'variantTransactionData',
                outputs: [
                    {
                        name: '',
                        type: 'bytes32',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
        ] as AbiItem[];
        return abi;
    }

    /**
     the listed content for the contract functions
    **/

    public async MAX_TIMEOUT(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.MAX_TIMEOUT(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async MAX_TIMEOUTGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.MAX_TIMEOUT().estimateGas();
        return gasAmount;
    };


    public async MIN_TIMEOUT(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.MIN_TIMEOUT(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async MIN_TIMEOUTGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.MIN_TIMEOUT().estimateGas();
        return gasAmount;
    };


    public async acceptProposedOwner(): Promise<void> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.acceptProposedOwner(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async acceptProposedOwnerGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.acceptProposedOwner().estimateGas();
        return gasAmount;
    };


    public async addAssetId(assetId: string,): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isString('assetId', assetId);

        const promizz = self._contract.methods.addAssetId(
            assetId,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async addAssetIdGas(assetId: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.addAssetId(assetId,).estimateGas();
        return gasAmount;
    };


    public async addLiquidity(amount: BN,assetId: string,valCoin: BN): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isNumberOrBigNumber('amount', amount);
            assert.isString('assetId', assetId);

        const promizz = self._contract.methods.addLiquidity(
            amount,
                    assetId,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice, value: valCoin
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async addLiquidityGas(amount: BN,assetId: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.addLiquidity(amount,assetId,).estimateGas();
        return gasAmount;
    };


    public async addLiquidityFor(amount: BN,assetId: string,router: string,valCoin: BN): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isNumberOrBigNumber('amount', amount);
            assert.isString('assetId', assetId);
            assert.isString('router', router);

        const promizz = self._contract.methods.addLiquidityFor(
            amount,
                    assetId,
                    router,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice, value: valCoin
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async addLiquidityForGas(amount: BN,assetId: string,router: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.addLiquidityFor(amount,assetId,router,).estimateGas();
        return gasAmount;
    };


    public async addRouter(router: string,): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isString('router', router);

        const promizz = self._contract.methods.addRouter(
            router,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async addRouterGas(router: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.addRouter(router,).estimateGas();
        return gasAmount;
    };


    public async approvedAssets(index_0: string,): Promise<boolean> {
        const self = this as any as TransactionManagerContract;

            assert.isString('index_0', index_0);

        const promizz = self._contract.methods.approvedAssets(
            index_0,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async approvedAssetsGas(index_0: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.approvedAssets(index_0,).estimateGas();
        return gasAmount;
    };


    public async approvedRouters(index_0: string,): Promise<boolean> {
        const self = this as any as TransactionManagerContract;

            assert.isString('index_0', index_0);

        const promizz = self._contract.methods.approvedRouters(
            index_0,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async approvedRoutersGas(index_0: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.approvedRouters(index_0,).estimateGas();
        return gasAmount;
    };


    public async assetOwnershipTimestamp(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.assetOwnershipTimestamp(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async assetOwnershipTimestampGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.assetOwnershipTimestamp().estimateGas();
        return gasAmount;
    };


    public async cancel(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};signature: string;encodedMeta: string},): Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}> {
        const self = this as any as TransactionManagerContract;

            

        const promizz = self._contract.methods.cancel(
            args,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async cancelGas(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};signature: string;encodedMeta: string},): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.cancel(args,).estimateGas();
        return gasAmount;
    };


    public async delay(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.delay(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async delayGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.delay().estimateGas();
        return gasAmount;
    };


    public async fulfill(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};relayerFee: BN;signature: string;callData: string;encodedMeta: string},): Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}> {
        const self = this as any as TransactionManagerContract;

            

        const promizz = self._contract.methods.fulfill(
            args,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async fulfillGas(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};relayerFee: BN;signature: string;callData: string;encodedMeta: string},): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.fulfill(args,).estimateGas();
        return gasAmount;
    };


    public async getChainId(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.getChainId(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getChainIdGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.getChainId().estimateGas();
        return gasAmount;
    };


    public async getStoredChainId(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.getStoredChainId(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getStoredChainIdGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.getStoredChainId().estimateGas();
        return gasAmount;
    };


    public async interpreter(): Promise<string> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.interpreter(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async interpreterGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.interpreter().estimateGas();
        return gasAmount;
    };


    public async isAssetOwnershipRenounced(): Promise<boolean> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.isAssetOwnershipRenounced(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async isAssetOwnershipRenouncedGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.isAssetOwnershipRenounced().estimateGas();
        return gasAmount;
    };


    public async isRouterOwnershipRenounced(): Promise<boolean> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.isRouterOwnershipRenounced(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async isRouterOwnershipRenouncedGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.isRouterOwnershipRenounced().estimateGas();
        return gasAmount;
    };


    public async owner(): Promise<string> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.owner(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async ownerGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.owner().estimateGas();
        return gasAmount;
    };


    public async prepare(args: {invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};amount: BN;expiry: BN;encryptedCallData: string;encodedBid: string;bidSignature: string;encodedMeta: string},valCoin: BN): Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}> {
        const self = this as any as TransactionManagerContract;

            

        const promizz = self._contract.methods.prepare(
            args,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice, value: valCoin
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async prepareGas(args: {invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};amount: BN;expiry: BN;encryptedCallData: string;encodedBid: string;bidSignature: string;encodedMeta: string},): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.prepare(args,).estimateGas();
        return gasAmount;
    };


    public async proposeAssetOwnershipRenunciation(): Promise<void> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.proposeAssetOwnershipRenunciation(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async proposeAssetOwnershipRenunciationGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.proposeAssetOwnershipRenunciation().estimateGas();
        return gasAmount;
    };


    public async proposeNewOwner(newlyProposed: string,): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isString('newlyProposed', newlyProposed);

        const promizz = self._contract.methods.proposeNewOwner(
            newlyProposed,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async proposeNewOwnerGas(newlyProposed: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.proposeNewOwner(newlyProposed,).estimateGas();
        return gasAmount;
    };


    public async proposeRouterOwnershipRenunciation(): Promise<void> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.proposeRouterOwnershipRenunciation(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async proposeRouterOwnershipRenunciationGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.proposeRouterOwnershipRenunciation().estimateGas();
        return gasAmount;
    };


    public async proposed(): Promise<string> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.proposed(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async proposedGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.proposed().estimateGas();
        return gasAmount;
    };


    public async proposedTimestamp(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.proposedTimestamp(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async proposedTimestampGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.proposedTimestamp().estimateGas();
        return gasAmount;
    };


    public async removeAssetId(assetId: string,): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isString('assetId', assetId);

        const promizz = self._contract.methods.removeAssetId(
            assetId,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async removeAssetIdGas(assetId: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.removeAssetId(assetId,).estimateGas();
        return gasAmount;
    };


    public async removeLiquidity(amount: BN,assetId: string,recipient: string,): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isNumberOrBigNumber('amount', amount);
            assert.isString('assetId', assetId);
            assert.isString('recipient', recipient);

        const promizz = self._contract.methods.removeLiquidity(
            amount,
                    assetId,
                    recipient,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async removeLiquidityGas(amount: BN,assetId: string,recipient: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.removeLiquidity(amount,assetId,recipient,).estimateGas();
        return gasAmount;
    };


    public async removeRouter(router: string,): Promise<void> {
        const self = this as any as TransactionManagerContract;

            assert.isString('router', router);

        const promizz = self._contract.methods.removeRouter(
            router,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async removeRouterGas(router: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.removeRouter(router,).estimateGas();
        return gasAmount;
    };


    public async renounceAssetOwnership(): Promise<void> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.renounceAssetOwnership(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async renounceAssetOwnershipGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.renounceAssetOwnership().estimateGas();
        return gasAmount;
    };


    public async renounceOwnership(): Promise<void> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.renounceOwnership(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async renounceOwnershipGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.renounceOwnership().estimateGas();
        return gasAmount;
    };


    public async renounceRouterOwnership(): Promise<void> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.renounceRouterOwnership(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


const result = await promizz.send(_essence)
        .on('transactionHash', (hash) => {
            this.onBroadcast(hash);
        }).on('confirmation', (confirmationNumber, receipt) => {
            this.onConfirmation(receipt);
        }).on('receipt', (r) => {
            this.pushReceiptSuccess(r);
        }).on('error', (error, receipt) => {
            this.onError(receipt, error);
        }).catch((e) => {
            this.catchErro(e)
        });

        return result;
    };


    public async renounceRouterOwnershipGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.renounceRouterOwnership().estimateGas();
        return gasAmount;
    };


    public async renounced(): Promise<boolean> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.renounced(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async renouncedGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.renounced().estimateGas();
        return gasAmount;
    };


    public async routerBalances(index_0: string,index_1: string,): Promise<BN> {
        const self = this as any as TransactionManagerContract;

            assert.isString('index_0', index_0);
            assert.isString('index_1', index_1);

        const promizz = self._contract.methods.routerBalances(
            index_0,
                    index_1,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async routerBalancesGas(index_0: string,index_1: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.routerBalances(index_0,index_1,).estimateGas();
        return gasAmount;
    };


    public async routerOwnershipTimestamp(): Promise<BN> {
        const self = this as any as TransactionManagerContract;


        const promizz = self._contract.methods.routerOwnershipTimestamp(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async routerOwnershipTimestampGas(): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.routerOwnershipTimestamp().estimateGas();
        return gasAmount;
    };


    public async variantTransactionData(index_0: string,): Promise<string> {
        const self = this as any as TransactionManagerContract;

            assert.isString('index_0', index_0);

        const promizz = self._contract.methods.variantTransactionData(
            index_0,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async variantTransactionDataGas(index_0: string,): Promise<number>{
        const self = this as any as TransactionManagerContract;
        const gasAmount = await self._contract.methods.variantTransactionData(index_0,).estimateGas();
        return gasAmount;
    };


    /**
     * Subscribe to an event type emitted by the TransactionManager contract.
     * @param eventName The TransactionManager contract event you would like to subscribe to.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{maker: aUserAddressHex}`
     * @param callback Callback that gets called when a log is added/removed
     * @param isVerbose Enable verbose subscription warnings (e.g recoverable network issues encountered)
     * @return Subscription token used later to unsubscribe
     */
    public subscribe<ArgsType extends TransactionManagerEventArgs>(
        eventName: TransactionManagerEvents,
        indexFilterValues: IndexedFilterValues,
        callback: EventCallback<ArgsType>,
        isVerbose: boolean = false,
        blockPollingIntervalMs?: number,
    ): string {
        assert.doesBelongToStringEnum('eventName', eventName, TransactionManagerEvents);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        assert.isFunction('callback', callback);
        const subscriptionToken = this._subscriptionManager.subscribe<ArgsType>(
            this._address,
            eventName,
            indexFilterValues,
            TransactionManagerContract.ABI(),
            callback,
            isVerbose,
            blockPollingIntervalMs,
        );
        return subscriptionToken;
    }

    /**
     * Cancel a subscription
     * @param subscriptionToken Subscription token returned by `subscribe()`
     */
    public unsubscribe(subscriptionToken: string): void {
        this._subscriptionManager.unsubscribe(subscriptionToken);
    }

    /**
     * Cancels all existing subscriptions
     */
    public unsubscribeAll(): void {
        this._subscriptionManager.unsubscribeAll();
    }


    /**
     * Gets historical logs without creating a subscription
     * @param eventName The TransactionManager contract event you would like to subscribe to.
     * @param blockRange Block range to get logs from.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{_from: aUserAddressHex}`
     * @return Array of logs that match the parameters
     */
    public async getLogsAsync<ArgsType extends TransactionManagerEventArgs>(
        eventName: TransactionManagerEvents,
        blockRange: BlockRange,
        indexFilterValues: IndexedFilterValues,
    ): Promise<Array<LogWithDecodedArgs<ArgsType>>> {
        assert.doesBelongToStringEnum('eventName', eventName, TransactionManagerEvents);
        assert.doesConformToSchema('blockRange', blockRange, schemas.blockRangeSchema);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        const logs = await this._subscriptionManager.getLogsAsync<ArgsType>(
            this._address,
            eventName,
            blockRange,
            indexFilterValues,
            TransactionManagerContract.ABI(),
        );
        return logs;
    }

    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('TransactionManager', TransactionManagerContract.ABI(), address, supportedProvider,ww3);
        this._subscriptionManager = new SubscriptionManager(
            TransactionManagerContract.ABI(),
            supportedProvider,
        );

        TransactionManagerContract.ABI().forEach((item, index) => {
            if (item.type === 'function') {
                const methodAbi = item as MethodAbi;
                this._methodABIIndex[methodAbi.name] = index;
            }
        });


    }
}

// tslint:disable:max-file-line-count
// tslint:enable:no-unbound-method no-parameter-reassignment no-consecutive-blank-lines ordered-imports align
// tslint:enable:trailing-comma whitespace no-trailing-whitespace
