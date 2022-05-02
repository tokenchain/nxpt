from moody.libeb import MiliDoS

from codec.gen_py.test_erc20 import TestERC20
from codec.gen_py.transaction_manager import TransactionManager


def add_liqudity(j: MiliDoS, router: str, asset_address: str, amount: int, txManager: str):
    # router
    # assetId
    # amount
    tx_manager = TransactionManager(j, txManager)
    erc20 = TestERC20(j, asset_address)
    tx_manager.CallAutoConf(j)
    erc20.CallAutoConf(j)
    mallow = erc20.allowance(router, txManager)
    if amount > mallow:
        approveTx = erc20.approve(txManager, 10 ** 28)
    else:
        print(f"Sufficient allowance: {mallow}")
    approvedRouter = tx_manager.approved_routers(router)
    if not approvedRouter:
        print(f"Router {router} is not approved")
    approvedAsset = tx_manager.approved_assets(asset_address)
    if not approvedAsset:
        print(f"Asset {asset_address} is not approved")

    wei_amount = amount if asset_address == 0x0 else 0

    tx_manager.add_liquidity(amount, asset_address, wei_amount)

    liquidity = tx_manager.router_balances(router, asset_address)

    print(f"liquidity added {liquidity}")


def add_liquidity_anyone(j: MiliDoS, router: str, asset_address: str, amount: int, txManager: str):
    # router
    # assetId
    # amount
    tx_manager = TransactionManager(j, txManager)
    erc20 = TestERC20(j, asset_address)
    tx_manager.CallAutoConf(j)
    erc20.CallAutoConf(j)
    mallow = erc20.allowance(router, txManager)
    if amount > mallow:
        approveTx = erc20.approve(txManager, 10 ** 28)
    else:
        print(f"Sufficient allowance: {mallow}")
    approvedRouter = tx_manager.approved_routers(router)
    if not approvedRouter:
        print(f"Router {router} is not approved")
    approvedAsset = tx_manager.approved_assets(asset_address)
    if not approvedAsset:
        print(f"Asset {asset_address} is not approved")

    wei_amount = amount if asset_address == 0x0 else 0

    tx_manager.add_liquidity_for(amount, asset_address, router, wei_amount)

    liquidity = tx_manager.router_balances(router, asset_address)

    print(f"liquidity added {liquidity}")
