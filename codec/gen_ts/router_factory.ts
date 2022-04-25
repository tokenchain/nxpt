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
    createRouter(routerSigner: string,recipient: string,):Promise<string>
    getRouterAddress(routerSigner: string,):Promise<string>
    init(_transactionManager: string,):Promise<void>
    owner():Promise<string>
    renounceOwnership():Promise<void>
    routerAddresses(index_0: string,):Promise<string>
    transactionManager():Promise<string>
    transferOwnership(newOwner: string,):Promise<void>
}





export enum RouterFactoryEvents {
    OwnershipTransferred = 'OwnershipTransferred',
    RouterCreated = 'RouterCreated',
}

export interface RouterFactoryOwnershipTransferredEventArgs extends DecodedLogArgs {
    previousOwner: string;
    newOwner: string;
}

export interface RouterFactoryRouterCreatedEventArgs extends DecodedLogArgs {
    router: string;
    routerSigner: string;
    recipient: string;
    transactionManager: string;
}


export type RouterFactoryEventArgs =
    | RouterFactoryOwnershipTransferredEventArgs
    | RouterFactoryRouterCreatedEventArgs;




/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class RouterFactoryContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'RouterFactory';
    private readonly _methodABIIndex: { [name: string]: number } = {};
    //todo: we will come back and fix it later not generic Error @https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
    // @ts-ignore
    private readonly _subscriptionManager: SubscriptionManager<RouterFactoryEventArgs, RouterFactoryEvents>;


    public static Instance(): (RouterFactoryContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_RouterFactory")) {
          // @ts-ignore
          const obj = window.__eth_contract_RouterFactory
          if (obj instanceof RouterFactoryContract) {
            return (obj) as RouterFactoryContract
          } else {
            return (obj) as RouterFactoryContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<RouterFactoryContract>
    {
        const contractInstance = await new RouterFactoryContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/** "_owner"
 **/];

        if (window && !window.hasOwnProperty("__eth_contract_RouterFactory")) {
            // @ts-ignore
            window.__eth_contract_RouterFactory = contractInstance
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
                        name: '_owner',
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
                        name: 'router',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'routerSigner',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'recipient',
                        type: 'address',
                        indexed: false,
                    },
                    {
                        name: 'transactionManager',
                        type: 'address',
                        indexed: false,
                    },
                ],
                name: 'RouterCreated',
                outputs: [
                ],
                type: 'event',
            },
            { 
                inputs: [
                    {
                        name: 'routerSigner',
                        type: 'address',
                    },
                    {
                        name: 'recipient',
                        type: 'address',
                    },
                ],
                name: 'createRouter',
                outputs: [
                    {
                        name: '',
                        type: 'address',
                    },
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'routerSigner',
                        type: 'address',
                    },
                ],
                name: 'getRouterAddress',
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
                        name: '_transactionManager',
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
                ],
                name: 'renounceOwnership',
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
                name: 'routerAddresses',
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
        ] as AbiItem[];
        return abi;
    }

    /**
     the listed content for the contract functions
    **/

    public async createRouter(routerSigner: string,recipient: string,): Promise<string> {
        const self = this as any as RouterFactoryContract;

            assert.isString('routerSigner', routerSigner);
            assert.isString('recipient', recipient);

        const promizz = self._contract.methods.createRouter(
            routerSigner,
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


    public async createRouterGas(routerSigner: string,recipient: string,): Promise<number>{
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.createRouter(routerSigner,recipient,).estimateGas();
        return gasAmount;
    };


    public async getRouterAddress(routerSigner: string,): Promise<string> {
        const self = this as any as RouterFactoryContract;

            assert.isString('routerSigner', routerSigner);

        const promizz = self._contract.methods.getRouterAddress(
            routerSigner,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getRouterAddressGas(routerSigner: string,): Promise<number>{
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.getRouterAddress(routerSigner,).estimateGas();
        return gasAmount;
    };


    public async init(_transactionManager: string,): Promise<void> {
        const self = this as any as RouterFactoryContract;

            assert.isString('_transactionManager', _transactionManager);

        const promizz = self._contract.methods.init(
            _transactionManager,
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


    public async initGas(_transactionManager: string,): Promise<number>{
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.init(_transactionManager,).estimateGas();
        return gasAmount;
    };


    public async owner(): Promise<string> {
        const self = this as any as RouterFactoryContract;


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
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.owner().estimateGas();
        return gasAmount;
    };


    public async renounceOwnership(): Promise<void> {
        const self = this as any as RouterFactoryContract;


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
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.renounceOwnership().estimateGas();
        return gasAmount;
    };


    public async routerAddresses(index_0: string,): Promise<string> {
        const self = this as any as RouterFactoryContract;

            assert.isString('index_0', index_0);

        const promizz = self._contract.methods.routerAddresses(
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


    public async routerAddressesGas(index_0: string,): Promise<number>{
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.routerAddresses(index_0,).estimateGas();
        return gasAmount;
    };


    public async transactionManager(): Promise<string> {
        const self = this as any as RouterFactoryContract;


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
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.transactionManager().estimateGas();
        return gasAmount;
    };


    public async transferOwnership(newOwner: string,): Promise<void> {
        const self = this as any as RouterFactoryContract;

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
        const self = this as any as RouterFactoryContract;
        const gasAmount = await self._contract.methods.transferOwnership(newOwner,).estimateGas();
        return gasAmount;
    };


    /**
     * Subscribe to an event type emitted by the RouterFactory contract.
     * @param eventName The RouterFactory contract event you would like to subscribe to.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{maker: aUserAddressHex}`
     * @param callback Callback that gets called when a log is added/removed
     * @param isVerbose Enable verbose subscription warnings (e.g recoverable network issues encountered)
     * @return Subscription token used later to unsubscribe
     */
    public subscribe<ArgsType extends RouterFactoryEventArgs>(
        eventName: RouterFactoryEvents,
        indexFilterValues: IndexedFilterValues,
        callback: EventCallback<ArgsType>,
        isVerbose: boolean = false,
        blockPollingIntervalMs?: number,
    ): string {
        assert.doesBelongToStringEnum('eventName', eventName, RouterFactoryEvents);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        assert.isFunction('callback', callback);
        const subscriptionToken = this._subscriptionManager.subscribe<ArgsType>(
            this._address,
            eventName,
            indexFilterValues,
            RouterFactoryContract.ABI(),
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
     * @param eventName The RouterFactory contract event you would like to subscribe to.
     * @param blockRange Block range to get logs from.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{_from: aUserAddressHex}`
     * @return Array of logs that match the parameters
     */
    public async getLogsAsync<ArgsType extends RouterFactoryEventArgs>(
        eventName: RouterFactoryEvents,
        blockRange: BlockRange,
        indexFilterValues: IndexedFilterValues,
    ): Promise<Array<LogWithDecodedArgs<ArgsType>>> {
        assert.doesBelongToStringEnum('eventName', eventName, RouterFactoryEvents);
        assert.doesConformToSchema('blockRange', blockRange, schemas.blockRangeSchema);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        const logs = await this._subscriptionManager.getLogsAsync<ArgsType>(
            this._address,
            eventName,
            blockRange,
            indexFilterValues,
            RouterFactoryContract.ABI(),
        );
        return logs;
    }

    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('RouterFactory', RouterFactoryContract.ABI(), address, supportedProvider,ww3);
        this._subscriptionManager = new SubscriptionManager(
            RouterFactoryContract.ABI(),
            supportedProvider,
        );

        RouterFactoryContract.ABI().forEach((item, index) => {
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
