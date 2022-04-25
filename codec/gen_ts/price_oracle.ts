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
    getTokenPrice(token: string,):Promise<BN>
    isPriceOracle():Promise<boolean>
}



/* istanbul ignore next */
// tslint:disable:array-type
// tslint:disable:no-parameter-reassignment
// tslint:disable-next-line:class-name
export class PriceOracleContract extends BaseContract implements ContractInterface{
    /**
     * @ignore
     */
public static deployedBytecode: string | undefined;
public static readonly contractName = 'PriceOracle';
    private readonly _methodABIIndex: { [name: string]: number } = {};


    public static Instance(): (PriceOracleContract | any | boolean) {
        if (window && window.hasOwnProperty("__eth_contract_PriceOracle")) {
          // @ts-ignore
          const obj = window.__eth_contract_PriceOracle
          if (obj instanceof PriceOracleContract) {
            return (obj) as PriceOracleContract
          } else {
            return (obj) as PriceOracleContract
          }
        } else {
          return false
        }
    }

    static async init(
        contract_address: string,
        supportedProvider: provider,
        ww3: Web3
        ):Promise<PriceOracleContract>
    {
        const contractInstance = await new PriceOracleContract(
            contract_address,
            supportedProvider,
            ww3
        );

        contractInstance.constructorArgs = [/**  **/];

        if (window && !window.hasOwnProperty("__eth_contract_PriceOracle")) {
            // @ts-ignore
            window.__eth_contract_PriceOracle = contractInstance
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
                        name: 'token',
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
        ] as AbiItem[];
        return abi;
    }

    /**
     the listed content for the contract functions
    **/

    public async getTokenPrice(token: string,): Promise<BN> {
        const self = this as any as PriceOracleContract;

            assert.isString('token', token);

        const promizz = self._contract.methods.getTokenPrice(
            token,
        )

        const _essence = {
            from: this._blockwrap.getAccountAddress(),
            gas: this.gas,
            gasPrice: this.gasPrice
        };


        const result = await promizz.call(_essence);

        return result;
    };


    public async getTokenPriceGas(token: string,): Promise<number>{
        const self = this as any as PriceOracleContract;
        const gasAmount = await self._contract.methods.getTokenPrice(token,).estimateGas();
        return gasAmount;
    };


    public async isPriceOracle(): Promise<boolean> {
        const self = this as any as PriceOracleContract;


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
        const self = this as any as PriceOracleContract;
        const gasAmount = await self._contract.methods.isPriceOracle().estimateGas();
        return gasAmount;
    };




    constructor(
        address: string,
        supportedProvider: provider,
        ww3: Web3
    ) {
        super('PriceOracle', PriceOracleContract.ABI(), address, supportedProvider,ww3);

        PriceOracleContract.ABI().forEach((item, index) => {
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
