# using orfeed price oracle for uniswap
import requests, logging, json, os, time, sys
from web3 import Web3

class uniswapprice:
	def main(source, destination, useramount):
		tokens = json.load(open('abi/kyber_currencies.json', 'r'))["data"]
		tokenarray = {}
		for i in tokens: tokenarray[i["symbol"].lower()] = (Web3.toChecksumAddress(i["address"]), i["decimals"])
		#print(tokenarray)	

		web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/4766db13619a4175aa7cf834d3eeae42'))
		erc20abi = json.load(open('abi/erc20.json', 'r'))
		amount = Web3.toWei(useramount, 'ETHER')
		
		def getuniswapprice(token1, token2, amount):
			expectedreturn = orfeed.functions.getExchangeRate(token1.upper(), token2.upper(), "UNISWAPBYSYMBOLV2", amount).call({'from': baseaccount})
			return expectedreturn

		orfeedbabi= json.load(open('abi/orfeedabi.json', 'r'))
		orfeedcontract = Web3.toChecksumAddress('0x8316b082621cfedab95bf4a44a1d4b64a6ffc336')
		orfeed = web3.eth.contract(abi=orfeedbabi, address=orfeedcontract)

		#for item in dir(orfeed): print(item) # inspect properties and methods of web3 contract object

		ethprovider_url = 'https://mainnet.infura.io/v3/4766db13619a4175aa7cf834d3eeae42' # infura project ID
		baseaccount = Web3.toChecksumAddress('0x2e9f3eb1e287b1081f4bc8ef5adbb80f063ae19e') # pubkey


		afterslippage = getuniswapprice(source, destination, amount)
		output = str(useramount) + " " + source + " after slippage will get " + str(afterslippage) + " " + destination
		return afterslippage























