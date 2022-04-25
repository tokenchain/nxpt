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
    allowance(owner: string,spender: string,):Promise<BN>
    approve(spender: string,amount: BN,):Promise<boolean>
    balanceOf(account: string,):Promise<BN>
    burn(account: string,amount: BN,):Promise<void>
    decimals():Promise<BN>
    decreaseAllowance(spender: string,subtractedValue: BN,):Promise<boolean>
    increaseAllowance(spender: string,addedValue: BN,):Promise<boolean>
    mint(account: string,amount: BN,):Promise<void>
    name():Promise<string>
    symbol():Promise<string>
    totalSupply():Promise<BN>
    transfer(recipient: string,amount: BN,):Promise<boolean>
    transferFrom(sender: string,recipient: string,amount: BN,):Promise<boolean>
}





export enum TestERC20Events {
    Approval = 'Approval',
    Transfer = 'Transfer',
}

export interface TestERC20ApprovalEventArgs extends DecodedLogArgs {
    owner: string;
    spender: string;
    value: BN;
}

export interface TestERC20TransferEventArgs extends DecodedLogArgs {
    from: string;
    to: string;
    value: BN;
}


export type TestERC20EventArgs =
    | TestERC20ApprovalEventArgs
    | TestERC20TransferEventArgs;




/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class TestERC20Contract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'TestERC20';
    private readonly _methodABIIndex: { [name: string]: number } = {};
    //todo: we will come back and fix it later not generic Error @https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
    // @ts-ignore
    private readonly _subscriptionManager: SubscriptionManager<TestERC20EventArgs, TestERC20Events>;


    public static Instance(): (TestERC20Contract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_TestERC20")) {
          // @ts-ignore
          const obj = window.__eth_contract_TestERC20
          if (obj instanceof TestERC20Contract) {
            return (obj) as TestERC20Contract
          } else {
            return (obj) as TestERC20Contract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<TestERC20Contract>
    {
        const contractInstance = await new TestERC20Contract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/**  **/];

        if (window && !window.hasOwnProperty("__eth_contract_TestERC20")) {
            // @ts-ignore
            window.__eth_contract_TestERC20 = contractInstance
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
                        name: 'owner',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'spender',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'value',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'Approval',
                outputs: [
                ],
                type: 'event',
            },
            { 
                anonymous: false,
                inputs: [
                    {
                        name: 'from',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'to',
                        type: 'address',
                        indexed: true,
                    },
                    {
                        name: 'value',
                        type: 'uint256',
                        indexed: false,
                    },
                ],
                name: 'Transfer',
                outputs: [
                ],
                type: 'event',
            },
            { 
                inputs: [
                    {
                        name: 'owner',
                        type: 'address',
                    },
                    {
                        name: 'spender',
                        type: 'address',
                    },
                ],
                name: 'allowance',
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
                        name: 'spender',
                        type: 'address',
                    },
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                ],
                name: 'approve',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'account',
                        type: 'address',
                    },
                ],
                name: 'balanceOf',
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
                        name: 'account',
                        type: 'address',
                    },
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                ],
                name: 'burn',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'decimals',
                outputs: [
                    {
                        name: '',
                        type: 'uint8',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'spender',
                        type: 'address',
                    },
                    {
                        name: 'subtractedValue',
                        type: 'uint256',
                    },
                ],
                name: 'decreaseAllowance',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'spender',
                        type: 'address',
                    },
                    {
                        name: 'addedValue',
                        type: 'uint256',
                    },
                ],
                name: 'increaseAllowance',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'account',
                        type: 'address',
                    },
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                ],
                name: 'mint',
                outputs: [
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'name',
                outputs: [
                    {
                        name: '',
                        type: 'string',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'symbol',
                outputs: [
                    {
                        name: '',
                        type: 'string',
                    },
                ],
                stateMutability: 'view',
                type: 'function',
            },
            { 
                inputs: [
                ],
                name: 'totalSupply',
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
                        name: 'recipient',
                        type: 'address',
                    },
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                ],
                name: 'transfer',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
                ],
                stateMutability: 'nonpayable',
                type: 'function',
            },
            { 
                inputs: [
                    {
                        name: 'sender',
                        type: 'address',
                    },
                    {
                        name: 'recipient',
                        type: 'address',
                    },
                    {
                        name: 'amount',
                        type: 'uint256',
                    },
                ],
                name: 'transferFrom',
                outputs: [
                    {
                        name: '',
                        type: 'bool',
                    },
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

    public async allowance(owner: string,spender: string,): Promise<BN> {
        const self = this as any as TestERC20Contract;

            assert.isString('owner', owner);
            assert.isString('spender', spender);

        const promizz = self._contract.methods.allowance(
            owner,
                    spender,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async allowanceGas(owner: string,spender: string,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.allowance(owner,spender,).estimateGas();
        return gasAmount;
    };


    public async approve(spender: string,amount: BN,): Promise<boolean> {
        const self = this as any as TestERC20Contract;

            assert.isString('spender', spender);
            assert.isNumberOrBigNumber('amount', amount);

        const promizz = self._contract.methods.approve(
            spender,
                    amount,
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


    public async approveGas(spender: string,amount: BN,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.approve(spender,amount,).estimateGas();
        return gasAmount;
    };


    public async balanceOf(account: string,): Promise<BN> {
        const self = this as any as TestERC20Contract;

            assert.isString('account', account);

        const promizz = self._contract.methods.balanceOf(
            account,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async balanceOfGas(account: string,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.balanceOf(account,).estimateGas();
        return gasAmount;
    };


    public async burn(account: string,amount: BN,): Promise<void> {
        const self = this as any as TestERC20Contract;

            assert.isString('account', account);
            assert.isNumberOrBigNumber('amount', amount);

        const promizz = self._contract.methods.burn(
            account,
                    amount,
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


    public async burnGas(account: string,amount: BN,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.burn(account,amount,).estimateGas();
        return gasAmount;
    };


    public async decimals(): Promise<BN> {
        const self = this as any as TestERC20Contract;


        const promizz = self._contract.methods.decimals(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async decimalsGas(): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.decimals().estimateGas();
        return gasAmount;
    };


    public async decreaseAllowance(spender: string,subtractedValue: BN,): Promise<boolean> {
        const self = this as any as TestERC20Contract;

            assert.isString('spender', spender);
            assert.isNumberOrBigNumber('subtractedValue', subtractedValue);

        const promizz = self._contract.methods.decreaseAllowance(
            spender,
                    subtractedValue,
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


    public async decreaseAllowanceGas(spender: string,subtractedValue: BN,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.decreaseAllowance(spender,subtractedValue,).estimateGas();
        return gasAmount;
    };


    public async increaseAllowance(spender: string,addedValue: BN,): Promise<boolean> {
        const self = this as any as TestERC20Contract;

            assert.isString('spender', spender);
            assert.isNumberOrBigNumber('addedValue', addedValue);

        const promizz = self._contract.methods.increaseAllowance(
            spender,
                    addedValue,
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


    public async increaseAllowanceGas(spender: string,addedValue: BN,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.increaseAllowance(spender,addedValue,).estimateGas();
        return gasAmount;
    };


    public async mint(account: string,amount: BN,): Promise<void> {
        const self = this as any as TestERC20Contract;

            assert.isString('account', account);
            assert.isNumberOrBigNumber('amount', amount);

        const promizz = self._contract.methods.mint(
            account,
                    amount,
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


    public async mintGas(account: string,amount: BN,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.mint(account,amount,).estimateGas();
        return gasAmount;
    };


    public async name(): Promise<string> {
        const self = this as any as TestERC20Contract;


        const promizz = self._contract.methods.name(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async nameGas(): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.name().estimateGas();
        return gasAmount;
    };


    public async symbol(): Promise<string> {
        const self = this as any as TestERC20Contract;


        const promizz = self._contract.methods.symbol(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async symbolGas(): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.symbol().estimateGas();
        return gasAmount;
    };


    public async totalSupply(): Promise<BN> {
        const self = this as any as TestERC20Contract;


        const promizz = self._contract.methods.totalSupply(
)

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async totalSupplyGas(): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.totalSupply().estimateGas();
        return gasAmount;
    };


    public async transfer(recipient: string,amount: BN,): Promise<boolean> {
        const self = this as any as TestERC20Contract;

            assert.isString('recipient', recipient);
            assert.isNumberOrBigNumber('amount', amount);

        const promizz = self._contract.methods.transfer(
            recipient,
                    amount,
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


    public async transferGas(recipient: string,amount: BN,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.transfer(recipient,amount,).estimateGas();
        return gasAmount;
    };


    public async transferFrom(sender: string,recipient: string,amount: BN,): Promise<boolean> {
        const self = this as any as TestERC20Contract;

            assert.isString('sender', sender);
            assert.isString('recipient', recipient);
            assert.isNumberOrBigNumber('amount', amount);

        const promizz = self._contract.methods.transferFrom(
            sender,
                    recipient,
                    amount,
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


    public async transferFromGas(sender: string,recipient: string,amount: BN,): Promise<number>{
        const self = this as any as TestERC20Contract;
        const gasAmount = await self._contract.methods.transferFrom(sender,recipient,amount,).estimateGas();
        return gasAmount;
    };


    /**
     * Subscribe to an event type emitted by the TestERC20 contract.
     * @param eventName The TestERC20 contract event you would like to subscribe to.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{maker: aUserAddressHex}`
     * @param callback Callback that gets called when a log is added/removed
     * @param isVerbose Enable verbose subscription warnings (e.g recoverable network issues encountered)
     * @return Subscription token used later to unsubscribe
     */
    public subscribe<ArgsType extends TestERC20EventArgs>(
        eventName: TestERC20Events,
        indexFilterValues: IndexedFilterValues,
        callback: EventCallback<ArgsType>,
        isVerbose: boolean = false,
        blockPollingIntervalMs?: number,
    ): string {
        assert.doesBelongToStringEnum('eventName', eventName, TestERC20Events);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        assert.isFunction('callback', callback);
        const subscriptionToken = this._subscriptionManager.subscribe<ArgsType>(
            this._address,
            eventName,
            indexFilterValues,
            TestERC20Contract.ABI(),
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
     * @param eventName The TestERC20 contract event you would like to subscribe to.
     * @param blockRange Block range to get logs from.
     * @param indexFilterValues An object where the keys are indexed args returned by the event and
     * the value is the value you are interested in. E.g `{_from: aUserAddressHex}`
     * @return Array of logs that match the parameters
     */
    public async getLogsAsync<ArgsType extends TestERC20EventArgs>(
        eventName: TestERC20Events,
        blockRange: BlockRange,
        indexFilterValues: IndexedFilterValues,
    ): Promise<Array<LogWithDecodedArgs<ArgsType>>> {
        assert.doesBelongToStringEnum('eventName', eventName, TestERC20Events);
        assert.doesConformToSchema('blockRange', blockRange, schemas.blockRangeSchema);
        assert.doesConformToSchema('indexFilterValues', indexFilterValues, schemas.indexFilterValuesSchema);
        const logs = await this._subscriptionManager.getLogsAsync<ArgsType>(
            this._address,
            eventName,
            blockRange,
            indexFilterValues,
            TestERC20Contract.ABI(),
        );
        return logs;
    }

    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('TestERC20', TestERC20Contract.ABI(), address, supportedProvider,ww3);
        this._subscriptionManager = new SubscriptionManager(
            TestERC20Contract.ABI(),
            supportedProvider,
        );

        TestERC20Contract.ABI().forEach((item, index) => {
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
