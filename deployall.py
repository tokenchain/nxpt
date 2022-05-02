# !/usr/bin/env python
# coding: utf-8
# from web3.auto import w3
from datetime import datetime

from moody.libeb import MiliDoS

from codec.gen_py.connext_price_oracle import ConnextPriceOracle
from codec.gen_py.router_factory import RouterFactory
from key import pri, NETWORK, ROOT, pub

# ========================== Of course

j = MiliDoS(NETWORK).withPOA()
j.setWorkspace(ROOT).Auth(pri)
j.OverrideGasConfig(6000000, 2000000000)
# test of all routeres


TEST_ROUTERS = [
    "0x9ADA6aa06eF36977569Dc5b38237809c7DF5082a",  # live testnet router
    "0x0EC26F03e3dBA9bb5162D28fD5a3378A25f168d1",  # rahul test router
    "0xDc150c5Db2cD1d1d8e505F824aBd90aEF887caC6",  # ci/shared router
    "0x627306090abaB3A6e1400e9345bC60c78a8BEf57",  # local router
]
WRAPPED_ETH_MAP = dict()
# mainnet WETH
WRAPPED_ETH_MAP["1"] = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
# rinkeby WETH
WRAPPED_ETH_MAP["4"] = "0xc778417E063141139Fce010982780140Aa0cD5Ab"
# optimism WETH
WRAPPED_ETH_MAP["10"] = "0x4200000000000000000000000000000000000006"
# Binance WETH
WRAPPED_ETH_MAP["56"] = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
# polygon WETH
WRAPPED_ETH_MAP["137"] = "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"
# fantom WETH
WRAPPED_ETH_MAP["250"] = "0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83"
# arbitrum WETH
WRAPPED_ETH_MAP["42161"] = "0x82af49447d8a07e3bd95bd0d56f35241523fbab1"
# avalanche WETH
WRAPPED_ETH_MAP["43114"] = "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7"
# xdai WETH
WRAPPED_ETH_MAP["100"] = "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d"
# moonriver WETH
WRAPPED_ETH_MAP["1285"] = "0x98878B06940aE243284CA214f92Bb71a2b032B8A"
# moonbeam WETH
WRAPPED_ETH_MAP["1284"] = "0xAcc15dC74880C9944775448304B263D191c6077F"
# rsc mainnet WETH
WRAPPED_ETH_MAP["1023"] = "0x516D07Dcf1c448aE5217F845263Ad6CE9149e9Ea"


def deployFunc(chainId: int):
    time_now = int(datetime.now().timestamp())
    future = 55
    start_time = future + time_now
    # j.deploy("TestStakingConf", [])
    if j.hasContractName("TransactionManager") is False:
        j.deploy("TransactionManager", [chainId])

    if j.hasContractName("RouterFactory") is False:
        router_factory_deployer = pub
        j.deploy("RouterFactory", [router_factory_deployer])

    if j.hasContractName("ConnextPriceOracle") is False:
        router_factory_deployer = pub
        j.deploy("ConnextPriceOracle", [WRAPPED_ETH_MAP[str(chainId)]])

    if j.hasContractName("ConnextPriceOracle") is False:
        router_factory_deployer = pub
        j.deploy("ConnextPriceOracle", [WRAPPED_ETH_MAP[str(chainId)]])


def setupRouterFactory():
    if j.hasContractName("RouterFactory") is False:
        print("found no Router Factory contract is deployed")
        exit(11)

    if j.hasContractName("TransactionManager") is False:
        print("found no TransactionManager contract is deployed")
        exit(12)

    if j.hasContractName("ConnextPriceOracle") is False:
        print("found no ConnextPriceOracle contract is deployed")
        exit(13)

    routerfactory = j.getAddr("RouterFactory")
    txmanager = j.getAddr("TransactionManager")
    routerf = RouterFactory(j, routerfactory)
    routerf.CallAutoConf(j)
    # routerf.onSuccssCallback(resultcl)
    routerf.init(txmanager)

    priceoracle = ConnextPriceOracle(j, j.getAddr("ConnextPriceOracle"))
    priceoracle.CallAutoConf(j)
    priceoracle.set_v1_price_oracle(j.getAddr("ConnextPriceOracle"))


def resultcl(f, r):
    print(f"🛤  It is not ok {f}, {r}")


def deployConnext():
    if j.hasContractName("TokenRegistry") is False:
        router_factory_deployer = pub
        j.deploy("TokenRegistry", [])

    if j.hasContractName("BridgeRouter") is False:
        router_factory_deployer = pub
        j.deploy("BridgeRouter", [])

    if j.hasContractName("Connext") is False:
        router_factory_deployer = pub
        registry = j.getAddr("TokenRegistry")
        router = j.getAddr("BridgeRouter")
        domain = 102300
        wrapper_rsc = ""
        j.deploy("Connext", [domain, registry, router, wrapper_rsc])


# RSC mainnet
# deployFunc(1023)
# setupRouterFactory()
deployConnext()
