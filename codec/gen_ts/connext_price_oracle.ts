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
    admin():Promise<string>
    aggregators(index_0: string,):Promise<string>
    assetPrices(index_0: string,):Promise<BN>
    getPriceFromChainlink(_tokenAddress: string,):Promise<BN>
    getPriceFromDex(_tokenAddress: string,):Promise<BN>
    getPriceFromOracle(_tokenAddress: string,):Promise<BN>
    getTokenPrice(_tokenAddress: string,):Promise<BN>
    isPriceOracle():Promise<boolean>
    priceRecords(index_0: string,):Promise<[string, string, string, boolean]>
    setAdmin(newAdmin: string,):Promise<void>
    setAggregators(tokenAddresses: string[],sources: string[],):Promise<void>
    setDexPriceInfo(_token: string,_baseToken: string,_lpToken: string,_active: boolean,):Promise<void>
    setDirectPrice(_token: string,_price: BN,):Promise<void>
    setV1PriceOracle(_v1PriceOracle: string,):Promise<void>
    v1PriceOracle():Promise<string>
    wrapped():Promise<string>
}





export enum ConnextPriceOracleEvents {
    AggregatorUpdated = 'AggregatorUpdated',
    DirectPriceUpdated = 'DirectPriceUpdated',
    NewAdmin = 'NewAdmin',
    PriceRecordUpdated = 'PriceRecordUpdated',
    V1PriceOracleUpdated = 'V1PriceOracleUpdated',
}

export interface ConnextPriceOracleAggregatorUpdatedEventArgs extends DecodedLogArgs {
    tokenAddress: string;
    source: string;
}

export interface ConnextPriceOracleDirectPriceUpdatedEventArgs extends DecodedLogArgs {
    token: string;
    oldPrice: BN;
    newPrice: BN;
}

export interface ConnextPriceOracleNewAdminEventArgs extends DecodedLogArgs {
    oldAdmin: string;
    newAdmin: string;
}

export interface ConnextPriceOraclePriceRecordUpdatedEventArgs extends DecodedLogArgs {
    token: string;
    baseToken: string;
    lpToken: string;
    _active: boolean;
}

export interface ConnextPriceOracleV1PriceOracleUpdatedEventArgs extends DecodedLogArgs {
    oldAddress: string;
    newAddress: string;
}


export type ConnextPriceOracleEventArgs =
    | ConnextPriceOracleAggregatorUpdatedEventArgs
    | ConnextPriceOracleDirectPriceUpdatedEventArgs
    | ConnextPriceOracleNewAdminEventArgs
    | ConnextPriceOraclePriceRecordUpdatedEventArgs
    | ConnextPriceOracleV1PriceOracleUpdatedEventArgs;




/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class ConnextPriceOracleContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'ConnextPriceOracle';
    private readonly _methodABIIndex: { [name: string]: number } = {};
    //todo: we will come back and fix it later not generic Error @https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
    // @ts-ignore
    private readonly _subscriptionManager: SubscriptionManager<ConnextPriceOracleEventArgs, ConnextPriceOracleEvents>;


    public static Instance(): (ConnextPriceOracleContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_ConnextPriceOracle")) {
          // @ts-ignore
          const obj = window.__eth_contract_ConnextPriceOracle
          if (obj instanceof ConnextPriceOracleContract) {
            return (obj) as ConnextPriceOracleContract
          } else {
            return (obj) as ConnextPriceOracleContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<ConnextPriceOracleContract>
    {
        const contractInstance = await new ConnextPriceOracleContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/** "_wrapped"
 **/];

        if (window && !window.hasOwnProperty("__eth_contract_ConnextPriceOracle")) {
            // @ts-ignore
            window.__eth_contract_ConnextPriceOracle = contractInstance
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
                        name: '_wrapped',
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
                        name: 'tokenAddress',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'source',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'AggregatorUpdated',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'token',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'oldPrice',
                        type: 'uint256',
                        indexed: false,
                    },
                    {
                        name: 'newPrice',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'DirectPriceUpdated',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'oldAdmin',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'newAdmin',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'NewAdmin',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'token',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'baseToken',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'lpToken',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: '_active',
                        type: 'bool',
                        indexed: false,
                    },
                ],
                name: 'PriceRecordUpdated',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'oldAddress',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'newAddress',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'V1PriceOracleUpdated',
                outputs: [
                ],
                type: 'event',
            },
            { 
                inputs: [
                ],
                name: 'admin',
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
                        name: 'index_0',
                        type: 'address',
                    },
                ],
                name: 'aggregators',
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
                        name: 'index_0',
                        type: 'address',
                    },
                ],
                name: 'assetPrices',
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
                        name: '_tokenAddress',
                        type: 'address',
                    },
                ],
                name: 'getPriceFromChainlink',
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
                        name: '_tokenAddress',
                        type: 'address',
                    },
                ],
                name: 'getPriceFromDex',
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
                        name: '_tokenAddress',
                        type: 'address',
                    },
                ],
                name: 'getPriceFromOracle',
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
                        name: '_tokenAddress',
                        type: 'address',
                    },
                ],
                name: 'getTokenPrice',
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
                name: 'isPriceOracle',
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
                name: 'priceRecords',
                outputs: [
                    {
                        name: 'token',
                        type: 'address',
                    },
                    {
                        name: 'baseToken',
                        type: 'address',
                    },
                    {
                        name: 'lpToken',
                        type: 'address',
                    },
                    {
                        name: 'active',
                        type: 'bool',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'newAdmin',
                        type: 'address',
                    },
                ],
                name: 'setAdmin',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'tokenAddresses',
                        type: 'address[]',
                    },
                    {
                        name: 'sources',
                        type: 'address[]',
                    },
                ],
                name: 'setAggregators',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_token',
                        type: 'address',
                    },
                    {
                        name: '_baseToken',
                        type: 'address',
                    },
                    {
                        name: '_lpToken',
                        type: 'address',
                    },
                    {
                        name: '_active',
                        type: 'bool',
                    },
                ],
                name: 'setDexPriceInfo',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_token',
                        type: 'address',
                    },
                    {
                        name: '_price',
                        type: 'uint256',
                    },
                ],
                name: 'setDirectPrice',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: '_v1PriceOracle',
                        type: 'address',
                    },
                ],
                name: 'setV1PriceOracle',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'v1PriceOracle',
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
                name: 'wrapped',
                outputs: [
                    {
                        name: '',
                        type: 'address',
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

    public async admin(): Promise<string> {
        const self = this as any as ConnextPriceOracleContract;


        const promizz = self._contract.methods.admin(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async adminGas(): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.admin().estimateGas();
        return gasAmount;
    };


    public async aggregators(index_0: string,): Promise<string> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('index_0', index_0);

        const promizz = self._contract.methods.aggregators(
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


    public async aggregatorsGas(index_0: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.aggregators(index_0,).estimateGas();
        return gasAmount;
    };


    public async assetPrices(index_0: string,): Promise<BN> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('index_0', index_0);

        const promizz = self._contract.methods.assetPrices(
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


    public async assetPricesGas(index_0: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.assetPrices(index_0,).estimateGas();
        return gasAmount;
    };


    public async getPriceFromChainlink(_tokenAddress: string,): Promise<BN> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('_tokenAddress', _tokenAddress);

        const promizz = self._contract.methods.getPriceFromChainlink(
            _tokenAddress,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getPriceFromChainlinkGas(_tokenAddress: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.getPriceFromChainlink(_tokenAddress,).estimateGas();
        return gasAmount;
    };


    public async getPriceFromDex(_tokenAddress: string,): Promise<BN> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('_tokenAddress', _tokenAddress);

        const promizz = self._contract.methods.getPriceFromDex(
            _tokenAddress,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getPriceFromDexGas(_tokenAddress: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.getPriceFromDex(_tokenAddress,).estimateGas();
        return gasAmount;
    };


    public async getPriceFromOracle(_tokenAddress: string,): Promise<BN> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('_tokenAddress', _tokenAddress);

        const promizz = self._contract.methods.getPriceFromOracle(
            _tokenAddress,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getPriceFromOracleGas(_tokenAddress: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.getPriceFromOracle(_tokenAddress,).estimateGas();
        return gasAmount;
    };


    public async getTokenPrice(_tokenAddress: string,): Promise<BN> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('_tokenAddress', _tokenAddress);

        const promizz = self._contract.methods.getTokenPrice(
            _tokenAddress,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getTokenPriceGas(_tokenAddress: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.getTokenPrice(_tokenAddress,).estimateGas();
        return gasAmount;
    };


    public async isPriceOracle(): Promise<boolean> {
        const self = this as any as ConnextPriceOracleContract;


        const promizz = self._contract.methods.isPriceOracle(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async isPriceOracleGas(): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.isPriceOracle().estimateGas();
        return gasAmount;
    };


    public async priceRecords(index_0: string,): Promise<[string, string, string, boolean]> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('index_0', index_0);

        const promizz = self._contract.methods.priceRecords(
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


    public async priceRecordsGas(index_0: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.priceRecords(index_0,).estimateGas();
        return gasAmount;
    };


    public async setAdmin(newAdmin: string,): Promise<void> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('newAdmin', newAdmin);

        const promizz = self._contract.methods.setAdmin(
            newAdmin,
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


    public async setAdminGas(newAdmin: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.setAdmin(newAdmin,).estimateGas();
        return gasAmount;
    };


    public async setAggregators(tokenAddresses: string[],sources: string[],): Promise<void> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isArray('tokenAddresses', tokenAddresses);
            assert.isArray('sources', sources);

        const promizz = self._contract.methods.setAggregators(
            tokenAddresses,
                    sources,
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


    public async setAggregatorsGas(tokenAddresses: string[],sources: string[],): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.setAggregators(tokenAddresses,sources,).estimateGas();
        return gasAmount;
    };


    public async setDexPriceInfo(_token: string,_baseToken: string,_lpToken: string,_active: boolean,): Promise<void> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('_token', _token);
            assert.isString('_baseToken', _baseToken);
            assert.isString('_lpToken', _lpToken);
            assert.isBoolean('_active', _active);

        const promizz = self._contract.methods.setDexPriceInfo(
            _token,
                    _baseToken,
                    _lpToken,
                    _active,
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


    public async setDexPriceInfoGas(_token: string,_baseToken: string,_lpToken: string,_active: boolean,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.setDexPriceInfo(_token,_baseToken,_lpToken,_active,).estimateGas();
        return gasAmount;
    };


    public async setDirectPrice(_token: string,_price: BN,): Promise<void> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('_token', _token);
            assert.isNumberOrBigNumber('_price', _price);

        const promizz = self._contract.methods.setDirectPrice(
            _token,
                    _price,
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


    public async setDirectPriceGas(_token: string,_price: BN,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.setDirectPrice(_token,_price,).estimateGas();
        return gasAmount;
    };


    public async setV1PriceOracle(_v1PriceOracle: string,): Promise<void> {
        const self = this as any as ConnextPriceOracleContract;

            assert.isString('_v1PriceOracle', _v1PriceOracle);

        const promizz = self._contract.methods.setV1PriceOracle(
            _v1PriceOracle,
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


    public async setV1PriceOracleGas(_v1PriceOracle: string,): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.setV1PriceOracle(_v1PriceOracle,).estimateGas();
        return gasAmount;
    };


    public async v1PriceOracle(): Promise<string> {
        const self = this as any as ConnextPriceOracleContract;


        const promizz = self._contract.methods.v1PriceOracle(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async v1PriceOracleGas(): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.v1PriceOracle().estimateGas();
        return gasAmount;
    };


    public async wrapped(): Promise<string> {
        const self = this as any as ConnextPriceOracleContract;


        const promizz = self._contract.methods.wrapped(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async wrappedGas(): Promise<number>{
        const self = this as any as ConnextPriceOracleContract;
        const gasAmount = await self._contract.methods.wrapped().estimateGas();
        return gasAmount;
    };


    /**
     * Subscribe to an event type emitted by the ConnextPriceOracle contract.
     * @param eventName The ConnextPriceOracle contract event you would like to subscribe to.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{maker: aUserAddressHex}`
     * @param callback Callback that gets called when a log is added/removed
     * @param isVerbose Enable verbose subscription warnings (e.g recoverable network issues encountered)
     * @return Subscription token used later to unsubscribe
     */
    public subscribe<ArgsType extends ConnextPriceOracleEventArgs>(
        eventName: ConnextPriceOracleEvents,
        indexFilterValues: IndexedFilterValues,
        callback: EventCallback<ArgsType>,
        isVerbose: boolean = false,
        blockPollingIntervalMs?: number,
    ): string {
        assert.doesBelongToStringEnum('eventName', eventName, ConnextPriceOracleEvents);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        assert.isFunction('callback', callback);
        const subscriptionToken = this._subscriptionManager.subscribe<ArgsType>(
            this._address,
            eventName,
            indexFilterValues,
            ConnextPriceOracleContract.ABI(),
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
     * @param eventName The ConnextPriceOracle contract event you would like to subscribe to.
     * @param blockRange Block range to get logs from.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{_from: aUserAddressHex}`
     * @return Array of logs that match the parameters
     */
    public async getLogsAsync<ArgsType extends ConnextPriceOracleEventArgs>(
        eventName: ConnextPriceOracleEvents,
        blockRange: BlockRange,
        indexFilterValues: IndexedFilterValues,
    ): Promise<Array<LogWithDecodedArgs<ArgsType>>> {
        assert.doesBelongToStringEnum('eventName', eventName, ConnextPriceOracleEvents);
        assert.doesConformToSchema('blockRange', blockRange, schemas.blockRangeSchema);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        const logs = await this._subscriptionManager.getLogsAsync<ArgsType>(
            this._address,
            eventName,
            blockRange,
            indexFilterValues,
            ConnextPriceOracleContract.ABI(),
        );
        return logs;
    }

    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('ConnextPriceOracle', ConnextPriceOracleContract.ABI(), address, supportedProvider,ww3);
        this._subscriptionManager = new SubscriptionManager(
            ConnextPriceOracleContract.ABI(),
            supportedProvider,
        );

        ConnextPriceOracleContract.ABI().forEach((item, index) => {
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
