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
    addRelayerFee(amount: BN,assetId: string,coin: BN):Promise<void>
    cancel(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};signature: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,):Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}>
    fulfill(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};relayerFee: BN;signature: string;callData: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,):Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}>
    init(_transactionManager: string,_chainId: BN,_routerSigner: string,_recipient: string,_owner: string,):Promise<void>
    owner():Promise<string>
    prepare(args: {invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};amount: BN;expiry: BN;encryptedCallData: string;encodedBid: string;bidSignature: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,coin: BN):Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}>
    recipient():Promise<string>
    removeLiquidity(amount: BN,assetId: string,routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,):Promise<void>
    removeRelayerFee(amount: BN,assetId: string,):Promise<void>
    renounceOwnership():Promise<void>
    routerFactory():Promise<string>
    routerSigner():Promise<string>
    setRecipient(_recipient: string,):Promise<void>
    setSigner(_routerSigner: string,):Promise<void>
    transactionManager():Promise<string>
    transferOwnership(newOwner: string,):Promise<void>
}





export enum RouterEvents {
    Cancel = 'Cancel',
    Fulfill = 'Fulfill',
    OwnershipTransferred = 'OwnershipTransferred',
    Prepare = 'Prepare',
    RelayerFeeAdded = 'RelayerFeeAdded',
    RelayerFeeRemoved = 'RelayerFeeRemoved',
    RemoveLiquidity = 'RemoveLiquidity',
}

export interface RouterCancelEventArgs extends DecodedLogArgs {
    txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};
    routerRelayerFeeAsset: string;
    routerRelayerFee: BN;
    caller: string;
}

export interface RouterFulfillEventArgs extends DecodedLogArgs {
    txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};
    routerRelayerFeeAsset: string;
    routerRelayerFee: BN;
    caller: string;
}

export interface RouterOwnershipTransferredEventArgs extends DecodedLogArgs {
    previousOwner: string;
    newOwner: string;
}

export interface RouterPrepareEventArgs extends DecodedLogArgs {
    invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};
    routerRelayerFeeAsset: string;
    routerRelayerFee: BN;
    caller: string;
}

export interface RouterRelayerFeeAddedEventArgs extends DecodedLogArgs {
    assetId: string;
    amount: BN;
    caller: string;
}

export interface RouterRelayerFeeRemovedEventArgs extends DecodedLogArgs {
    assetId: string;
    amount: BN;
    caller: string;
}

export interface RouterRemoveLiquidityEventArgs extends DecodedLogArgs {
    amount: BN;
    assetId: string;
    routerRelayerFeeAsset: string;
    routerRelayerFee: BN;
    caller: string;
}


export type RouterEventArgs =
    | RouterCancelEventArgs
    | RouterFulfillEventArgs
    | RouterOwnershipTransferredEventArgs
    | RouterPrepareEventArgs
    | RouterRelayerFeeAddedEventArgs
    | RouterRelayerFeeRemovedEventArgs
    | RouterRemoveLiquidityEventArgs;




/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class RouterContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'Router';
    private readonly _methodABIIndex: { [name: string]: number } = {};
    //todo: we will come back and fix it later not generic Error @https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
    // @ts-ignore
    private readonly _subscriptionManager: SubscriptionManager<RouterEventArgs, RouterEvents>;


    public static Instance(): (RouterContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_Router")) {
          // @ts-ignore
          const obj = window.__eth_contract_Router
          if (obj instanceof RouterContract) {
            return (obj) as RouterContract
          } else {
            return (obj) as RouterContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<RouterContract>
    {
        const contractInstance = await new RouterContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/** "_routerFactory"
 **/];

        if (window && !window.hasOwnProperty("__eth_contract_Router")) {
            // @ts-ignore
            window.__eth_contract_Router = contractInstance
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
                        name: '_routerFactory',
                        type: 'address',
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
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'Cancel',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
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
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'Fulfill',
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
                        name: 'invariantData',
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
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'Prepare',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'assetId',
                        type: 'address',
                        indexed: false,
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
                name: 'RelayerFeeAdded',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'assetId',
                        type: 'address',
                        indexed: false,
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
                name: 'RelayerFeeRemoved',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'amount',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'caller',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'RemoveLiquidity',
                outputs: [
                ],
                type: 'event',
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
                name: 'addRelayerFee',
                outputs: [
                ],
                stateMutability: 'payable',
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
                    {
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                    },
                    {
                        name: 'signature',
                        type: 'bytes',
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
                    {
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                    },
                    {
                        name: 'signature',
                        type: 'bytes',
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
                    {
                        name: '_transactionManager',
                        type: 'address',
                    },
                    {
                        name: '_chainId',
                        type: 'uint256',
                    },
                    {
                        name: '_routerSigner',
                        type: 'address',
                    },
                    {
                        name: '_recipient',
                        type: 'address',
                    },
                    {
                        name: '_owner',
                        type: 'address',
                    },
                ],
                name: 'init',
                outputs: [
                ],
                stateMutability: 'nonpayable',
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
                    {
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                    },
                    {
                        name: 'signature',
                        type: 'bytes',
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
                name: 'recipient',
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
                        name: 'amount',
                        type: 'uint256',
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                    },
                    {
                        name: 'routerRelayerFeeAsset',
                        type: 'address',
                    },
                    {
                        name: 'routerRelayerFee',
                        type: 'uint256',
                    },
                    {
                        name: 'signature',
                        type: 'bytes',
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
                        name: 'amount',
                        type: 'uint256',
                    },
                    {
                        name: 'assetId',
                        type: 'address',
                    },
                ],
                name: 'removeRelayerFee',
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
                name: 'routerFactory',
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
                name: 'routerSigner',
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
                        name: '_recipient',
                        type: 'address',
                    },
                ],
                name: 'setRecipient',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_routerSigner',
                        type: 'address',
                    },
                ],
                name: 'setSigner',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'transactionManager',
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
                        name: 'newOwner',
                        type: 'address',
                    },
                ],
                name: 'transferOwnership',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                outputs: [
                ],
                stateMutability: 'payable',
                type: 'receive',
            },
        ] as AbiItem[];
        return abi;
    }

    /**
     the listed content for the contract functions
    **/

    public async addRelayerFee(amount: BN,assetId: string,valCoin: BN): Promise<void> {
        const self = this as any as RouterContract;

            assert.isNumberOrBigNumber('amount', amount);
            assert.isString('assetId', assetId);

        const promizz = self._contract.methods.addRelayerFee(
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


    public async addRelayerFeeGas(amount: BN,assetId: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.addRelayerFee(amount,assetId,).estimateGas();
        return gasAmount;
    };


    public async cancel(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};signature: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,): Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}> {
        const self = this as any as RouterContract;

            
            assert.isString('routerRelayerFeeAsset', routerRelayerFeeAsset);
            assert.isNumberOrBigNumber('routerRelayerFee', routerRelayerFee);
            assert.isString('signature', signature);

        const promizz = self._contract.methods.cancel(
            args,
                    routerRelayerFeeAsset,
                    routerRelayerFee,
                    signature,
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


    public async cancelGas(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};signature: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.cancel(args,routerRelayerFeeAsset,routerRelayerFee,signature,).estimateGas();
        return gasAmount;
    };


    public async fulfill(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};relayerFee: BN;signature: string;callData: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,): Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}> {
        const self = this as any as RouterContract;

            
            assert.isString('routerRelayerFeeAsset', routerRelayerFeeAsset);
            assert.isNumberOrBigNumber('routerRelayerFee', routerRelayerFee);
            assert.isString('signature', signature);

        const promizz = self._contract.methods.fulfill(
            args,
                    routerRelayerFeeAsset,
                    routerRelayerFee,
                    signature,
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


    public async fulfillGas(args: {txData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN};relayerFee: BN;signature: string;callData: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.fulfill(args,routerRelayerFeeAsset,routerRelayerFee,signature,).estimateGas();
        return gasAmount;
    };


    public async init(_transactionManager: string,_chainId: BN,_routerSigner: string,_recipient: string,_owner: string,): Promise<void> {
        const self = this as any as RouterContract;

            assert.isString('_transactionManager', _transactionManager);
            assert.isNumberOrBigNumber('_chainId', _chainId);
            assert.isString('_routerSigner', _routerSigner);
            assert.isString('_recipient', _recipient);
            assert.isString('_owner', _owner);

        const promizz = self._contract.methods.init(
            _transactionManager,
                    _chainId,
                    _routerSigner,
                    _recipient,
                    _owner,
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


    public async initGas(_transactionManager: string,_chainId: BN,_routerSigner: string,_recipient: string,_owner: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.init(_transactionManager,_chainId,_routerSigner,_recipient,_owner,).estimateGas();
        return gasAmount;
    };


    public async owner(): Promise<string> {
        const self = this as any as RouterContract;


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
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.owner().estimateGas();
        return gasAmount;
    };


    public async prepare(args: {invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};amount: BN;expiry: BN;encryptedCallData: string;encodedBid: string;bidSignature: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,valCoin: BN): Promise<{receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;callDataHash: string;transactionId: string;sendingChainId: BN;receivingChainId: BN;amount: BN;expiry: BN;preparedBlockNumber: BN}> {
        const self = this as any as RouterContract;

            
            assert.isString('routerRelayerFeeAsset', routerRelayerFeeAsset);
            assert.isNumberOrBigNumber('routerRelayerFee', routerRelayerFee);
            assert.isString('signature', signature);

        const promizz = self._contract.methods.prepare(
            args,
                    routerRelayerFeeAsset,
                    routerRelayerFee,
                    signature,
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


    public async prepareGas(args: {invariantData: {receivingChainTxManagerAddress: string;user: string;router: string;initiator: string;sendingAssetId: string;receivingAssetId: string;sendingChainFallback: string;receivingAddress: string;callTo: string;sendingChainId: BN;receivingChainId: BN;callDataHash: string;transactionId: string};amount: BN;expiry: BN;encryptedCallData: string;encodedBid: string;bidSignature: string;encodedMeta: string},routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.prepare(args,routerRelayerFeeAsset,routerRelayerFee,signature,).estimateGas();
        return gasAmount;
    };


    public async recipient(): Promise<string> {
        const self = this as any as RouterContract;


        const promizz = self._contract.methods.recipient(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async recipientGas(): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.recipient().estimateGas();
        return gasAmount;
    };


    public async removeLiquidity(amount: BN,assetId: string,routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,): Promise<void> {
        const self = this as any as RouterContract;

            assert.isNumberOrBigNumber('amount', amount);
            assert.isString('assetId', assetId);
            assert.isString('routerRelayerFeeAsset', routerRelayerFeeAsset);
            assert.isNumberOrBigNumber('routerRelayerFee', routerRelayerFee);
            assert.isString('signature', signature);

        const promizz = self._contract.methods.removeLiquidity(
            amount,
                    assetId,
                    routerRelayerFeeAsset,
                    routerRelayerFee,
                    signature,
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


    public async removeLiquidityGas(amount: BN,assetId: string,routerRelayerFeeAsset: string,routerRelayerFee: BN,signature: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.removeLiquidity(amount,assetId,routerRelayerFeeAsset,routerRelayerFee,signature,).estimateGas();
        return gasAmount;
    };


    public async removeRelayerFee(amount: BN,assetId: string,): Promise<void> {
        const self = this as any as RouterContract;

            assert.isNumberOrBigNumber('amount', amount);
            assert.isString('assetId', assetId);

        const promizz = self._contract.methods.removeRelayerFee(
            amount,
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


    public async removeRelayerFeeGas(amount: BN,assetId: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.removeRelayerFee(amount,assetId,).estimateGas();
        return gasAmount;
    };


    public async renounceOwnership(): Promise<void> {
        const self = this as any as RouterContract;


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
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.renounceOwnership().estimateGas();
        return gasAmount;
    };


    public async routerFactory(): Promise<string> {
        const self = this as any as RouterContract;


        const promizz = self._contract.methods.routerFactory(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async routerFactoryGas(): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.routerFactory().estimateGas();
        return gasAmount;
    };


    public async routerSigner(): Promise<string> {
        const self = this as any as RouterContract;


        const promizz = self._contract.methods.routerSigner(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async routerSignerGas(): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.routerSigner().estimateGas();
        return gasAmount;
    };


    public async setRecipient(_recipient: string,): Promise<void> {
        const self = this as any as RouterContract;

            assert.isString('_recipient', _recipient);

        const promizz = self._contract.methods.setRecipient(
            _recipient,
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


    public async setRecipientGas(_recipient: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.setRecipient(_recipient,).estimateGas();
        return gasAmount;
    };


    public async setSigner(_routerSigner: string,): Promise<void> {
        const self = this as any as RouterContract;

            assert.isString('_routerSigner', _routerSigner);

        const promizz = self._contract.methods.setSigner(
            _routerSigner,
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


    public async setSignerGas(_routerSigner: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.setSigner(_routerSigner,).estimateGas();
        return gasAmount;
    };


    public async transactionManager(): Promise<string> {
        const self = this as any as RouterContract;


        const promizz = self._contract.methods.transactionManager(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async transactionManagerGas(): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.transactionManager().estimateGas();
        return gasAmount;
    };


    public async transferOwnership(newOwner: string,): Promise<void> {
        const self = this as any as RouterContract;

            assert.isString('newOwner', newOwner);

        const promizz = self._contract.methods.transferOwnership(
            newOwner,
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


    public async transferOwnershipGas(newOwner: string,): Promise<number>{
        const self = this as any as RouterContract;
        const gasAmount = await self._contract.methods.transferOwnership(newOwner,).estimateGas();
        return gasAmount;
    };


    /**
     * Subscribe to an event type emitted by the Router contract.
     * @param eventName The Router contract event you would like to subscribe to.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{maker: aUserAddressHex}`
     * @param callback Callback that gets called when a log is added/removed
     * @param isVerbose Enable verbose subscription warnings (e.g recoverable network issues encountered)
     * @return Subscription token used later to unsubscribe
     */
    public subscribe<ArgsType extends RouterEventArgs>(
        eventName: RouterEvents,
        indexFilterValues: IndexedFilterValues,
        callback: EventCallback<ArgsType>,
        isVerbose: boolean = false,
        blockPollingIntervalMs?: number,
    ): string {
        assert.doesBelongToStringEnum('eventName', eventName, RouterEvents);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        assert.isFunction('callback', callback);
        const subscriptionToken = this._subscriptionManager.subscribe<ArgsType>(
            this._address,
            eventName,
            indexFilterValues,
            RouterContract.ABI(),
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
     * @param eventName The Router contract event you would like to subscribe to.
     * @param blockRange Block range to get logs from.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{_from: aUserAddressHex}`
     * @return Array of logs that match the parameters
     */
    public async getLogsAsync<ArgsType extends RouterEventArgs>(
        eventName: RouterEvents,
        blockRange: BlockRange,
        indexFilterValues: IndexedFilterValues,
    ): Promise<Array<LogWithDecodedArgs<ArgsType>>> {
        assert.doesBelongToStringEnum('eventName', eventName, RouterEvents);
        assert.doesConformToSchema('blockRange', blockRange, schemas.blockRangeSchema);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        const logs = await this._subscriptionManager.getLogsAsync<ArgsType>(
            this._address,
            eventName,
            blockRange,
            indexFilterValues,
            RouterContract.ABI(),
        );
        return logs;
    }

    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('Router', RouterContract.ABI(), address, supportedProvider,ww3);
        this._subscriptionManager = new SubscriptionManager(
            RouterContract.ABI(),
            supportedProvider,
        );

        RouterContract.ABI().forEach((item, index) => {
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
