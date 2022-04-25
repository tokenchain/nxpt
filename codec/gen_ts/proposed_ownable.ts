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
    acceptProposedOwner():Promise<void>
    assetOwnershipTimestamp():Promise<BN>
    delay():Promise<BN>
    isAssetOwnershipRenounced():Promise<boolean>
    isRouterOwnershipRenounced():Promise<boolean>
    owner():Promise<string>
    proposeAssetOwnershipRenunciation():Promise<void>
    proposeNewOwner(newlyProposed: string,):Promise<void>
    proposeRouterOwnershipRenunciation():Promise<void>
    proposed():Promise<string>
    proposedTimestamp():Promise<BN>
    renounceAssetOwnership():Promise<void>
    renounceOwnership():Promise<void>
    renounceRouterOwnership():Promise<void>
    renounced():Promise<boolean>
    routerOwnershipTimestamp():Promise<BN>
}





export enum ProposedOwnableEvents {
    AssetOwnershipRenounced = 'AssetOwnershipRenounced',
    AssetOwnershipRenunciationProposed = 'AssetOwnershipRenunciationProposed',
    OwnershipProposed = 'OwnershipProposed',
    OwnershipTransferred = 'OwnershipTransferred',
    RouterOwnershipRenounced = 'RouterOwnershipRenounced',
    RouterOwnershipRenunciationProposed = 'RouterOwnershipRenunciationProposed',
}

export interface ProposedOwnableAssetOwnershipRenouncedEventArgs extends DecodedLogArgs {
    renounced: boolean;
}

export interface ProposedOwnableAssetOwnershipRenunciationProposedEventArgs extends DecodedLogArgs {
    timestamp: BN;
}

export interface ProposedOwnableOwnershipProposedEventArgs extends DecodedLogArgs {
    proposedOwner: string;
}

export interface ProposedOwnableOwnershipTransferredEventArgs extends DecodedLogArgs {
    previousOwner: string;
    newOwner: string;
}

export interface ProposedOwnableRouterOwnershipRenouncedEventArgs extends DecodedLogArgs {
    renounced: boolean;
}

export interface ProposedOwnableRouterOwnershipRenunciationProposedEventArgs extends DecodedLogArgs {
    timestamp: BN;
}


export type ProposedOwnableEventArgs =
    | ProposedOwnableAssetOwnershipRenouncedEventArgs
    | ProposedOwnableAssetOwnershipRenunciationProposedEventArgs
    | ProposedOwnableOwnershipProposedEventArgs
    | ProposedOwnableOwnershipTransferredEventArgs
    | ProposedOwnableRouterOwnershipRenouncedEventArgs
    | ProposedOwnableRouterOwnershipRenunciationProposedEventArgs;




/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class ProposedOwnableContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'ProposedOwnable';
    private readonly _methodABIIndex: { [name: string]: number } = {};
    //todo: we will come back and fix it later not generic Error @https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
    // @ts-ignore
    private readonly _subscriptionManager: SubscriptionManager<ProposedOwnableEventArgs, ProposedOwnableEvents>;


    public static Instance(): (ProposedOwnableContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_ProposedOwnable")) {
          // @ts-ignore
          const obj = window.__eth_contract_ProposedOwnable
          if (obj instanceof ProposedOwnableContract) {
            return (obj) as ProposedOwnableContract
          } else {
            return (obj) as ProposedOwnableContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<ProposedOwnableContract>
    {
        const contractInstance = await new ProposedOwnableContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/**  **/];

        if (window && !window.hasOwnProperty("__eth_contract_ProposedOwnable")) {
            // @ts-ignore
            window.__eth_contract_ProposedOwnable = contractInstance
        }

        return contractInstance
    }

    /**
     * @returns The contract ABI
     */
    public static ABI(): AbiItem[] {
        const abi = [
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
        ] as AbiItem[];
        return abi;
    }

    /**
     the listed content for the contract functions
    **/

    public async acceptProposedOwner(): Promise<void> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.acceptProposedOwner().estimateGas();
        return gasAmount;
    };


    public async assetOwnershipTimestamp(): Promise<BN> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.assetOwnershipTimestamp().estimateGas();
        return gasAmount;
    };


    public async delay(): Promise<BN> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.delay().estimateGas();
        return gasAmount;
    };


    public async isAssetOwnershipRenounced(): Promise<boolean> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.isAssetOwnershipRenounced().estimateGas();
        return gasAmount;
    };


    public async isRouterOwnershipRenounced(): Promise<boolean> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.isRouterOwnershipRenounced().estimateGas();
        return gasAmount;
    };


    public async owner(): Promise<string> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.owner().estimateGas();
        return gasAmount;
    };


    public async proposeAssetOwnershipRenunciation(): Promise<void> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.proposeAssetOwnershipRenunciation().estimateGas();
        return gasAmount;
    };


    public async proposeNewOwner(newlyProposed: string,): Promise<void> {
        const self = this as any as ProposedOwnableContract;

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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.proposeNewOwner(newlyProposed,).estimateGas();
        return gasAmount;
    };


    public async proposeRouterOwnershipRenunciation(): Promise<void> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.proposeRouterOwnershipRenunciation().estimateGas();
        return gasAmount;
    };


    public async proposed(): Promise<string> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.proposed().estimateGas();
        return gasAmount;
    };


    public async proposedTimestamp(): Promise<BN> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.proposedTimestamp().estimateGas();
        return gasAmount;
    };


    public async renounceAssetOwnership(): Promise<void> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.renounceAssetOwnership().estimateGas();
        return gasAmount;
    };


    public async renounceOwnership(): Promise<void> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.renounceOwnership().estimateGas();
        return gasAmount;
    };


    public async renounceRouterOwnership(): Promise<void> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.renounceRouterOwnership().estimateGas();
        return gasAmount;
    };


    public async renounced(): Promise<boolean> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.renounced().estimateGas();
        return gasAmount;
    };


    public async routerOwnershipTimestamp(): Promise<BN> {
        const self = this as any as ProposedOwnableContract;


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
        const self = this as any as ProposedOwnableContract;
        const gasAmount = await self._contract.methods.routerOwnershipTimestamp().estimateGas();
        return gasAmount;
    };


    /**
     * Subscribe to an event type emitted by the ProposedOwnable contract.
     * @param eventName The ProposedOwnable contract event you would like to subscribe to.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{maker: aUserAddressHex}`
     * @param callback Callback that gets called when a log is added/removed
     * @param isVerbose Enable verbose subscription warnings (e.g recoverable network issues encountered)
     * @return Subscription token used later to unsubscribe
     */
    public subscribe<ArgsType extends ProposedOwnableEventArgs>(
        eventName: ProposedOwnableEvents,
        indexFilterValues: IndexedFilterValues,
        callback: EventCallback<ArgsType>,
        isVerbose: boolean = false,
        blockPollingIntervalMs?: number,
    ): string {
        assert.doesBelongToStringEnum('eventName', eventName, ProposedOwnableEvents);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        assert.isFunction('callback', callback);
        const subscriptionToken = this._subscriptionManager.subscribe<ArgsType>(
            this._address,
            eventName,
            indexFilterValues,
            ProposedOwnableContract.ABI(),
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
     * @param eventName The ProposedOwnable contract event you would like to subscribe to.
     * @param blockRange Block range to get logs from.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{_from: aUserAddressHex}`
     * @return Array of logs that match the parameters
     */
    public async getLogsAsync<ArgsType extends ProposedOwnableEventArgs>(
        eventName: ProposedOwnableEvents,
        blockRange: BlockRange,
        indexFilterValues: IndexedFilterValues,
    ): Promise<Array<LogWithDecodedArgs<ArgsType>>> {
        assert.doesBelongToStringEnum('eventName', eventName, ProposedOwnableEvents);
        assert.doesConformToSchema('blockRange', blockRange, schemas.blockRangeSchema);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        const logs = await this._subscriptionManager.getLogsAsync<ArgsType>(
            this._address,
            eventName,
            blockRange,
            indexFilterValues,
            ProposedOwnableContract.ABI(),
        );
        return logs;
    }

    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('ProposedOwnable', ProposedOwnableContract.ABI(), address, supportedProvider,ww3);
        this._subscriptionManager = new SubscriptionManager(
            ProposedOwnableContract.ABI(),
            supportedProvider,
        );

        ProposedOwnableContract.ABI().forEach((item, index) => {
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
