pragma solidity ^0.5.10;

import "./IERC20.sol";

/**
 * @dev Optional functions from the ERC20 standard. also works for TRC20
 */
contract ERC20Detailed is IERC20 {
    string private _name;
    string private _symbol;
    uint8 private _decimals;

    string public tokenName;
    string public tokenSymbol;

    string public name;
    string public symbol;
    uint8 public decimals;

    constructor (string memory __name, string memory __symbol, uint8 __decimals) public {
        _name = __name;
        name = __name;
        tokenName = __name;
        symbol = __symbol;
        _symbol = __symbol;
        tokenSymbol = __symbol;
        decimals = __decimals;
        _decimals = __decimals;
    }

    /*   function name() public view returns (string memory) {
           return _name;
       }

       function symbol() public view returns (string memory) {
           return _symbol;
       }

    function decimals() public view returns (uint8) {
        return _decimals;
    }

      */
    function getDecimals() external view returns (uint8){
        return _decimals;
    }
}
