from moody.libeb import MiliDoS

from codec.gen_py.transaction_manager import TransactionManager


def add_asset(j: MiliDoS, asset_address: str, tx_manager_address: str):
    # router
    # assetId
    # amount
    tx_manager = TransactionManager(j, tx_manager_address)
    tx_manager.CallAutoConf(j)
    approved = tx_manager.approved_assets(asset_address)
    if approved is True:
        print(f"asset {asset_address} is already approved. no need to continue")
        return
    tx_manager.add_asset_id(asset_address)

    approved = tx_manager.approved_assets(asset_address)
    print(f"is asset approved for {asset_address}? {approved}")
