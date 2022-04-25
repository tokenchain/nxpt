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
    aggregate(calls: Array<{target: string;callData: string}>,):Promise<[BN, string[]]>
}



/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class MulticallContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'Multicall';
    private readonly _methodABIIndex: { [name: string]: number } = {};


    public static Instance(): (MulticallContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_Multicall")) {
          // @ts-ignore
          const obj = window.__eth_contract_Multicall
          if (obj instanceof MulticallContract) {
            return (obj) as MulticallContract
          } else {
            return (obj) as MulticallContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<MulticallContract>
    {
        const contractInstance = await new MulticallContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/**  **/];

        if (window && !window.hasOwnProperty("__eth_contract_Multicall")) {
            // @ts-ignore
            window.__eth_contract_Multicall = contractInstance
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
                        name: 'calls',
                        type: 'tuple[]',
                        components: [
                            {
                                name: 'target',
                                type: 'address',
                            },
                            {
                                name: 'callData',
                                type: 'bytes',
                            },
                        ]
                    },
                ],
                name: 'aggregate',
                outputs: [
                    {
                        name: 'blockNumber',
                        type: 'uint256',
                    },
                    {
                        name: 'returnData',
                        type: 'bytes[]',
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

    public async aggregate(calls: Array<{target: string;callData: string}>,): Promise<[BN, string[]]> {
        const self = this as any as MulticallContract;

            assert.isArray('calls', calls);

        const promizz = self._contract.methods.aggregate(
            calls,
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


    public async aggregateGas(calls: Array<{target: string;callData: string}>,): Promise<number>{
        const self = this as any as MulticallContract;
        const gasAmount = await self._contract.methods.aggregate(calls,).estimateGas();
        return gasAmount;
    };




    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('Multicall', MulticallContract.ABI(), address, supportedProvider,ww3);

        MulticallContract.ABI().forEach((item, index) => {
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
