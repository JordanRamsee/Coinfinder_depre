from icons import *
from activate import *
from flask import Flask, request, render_template
from activate import *
from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct
from flask import jsonify
import json

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(""))

# read them from config.json
owner_wallet_address = None
api_key = None
try:
    with open('config.json', 'r') as f:
        config_data = json.load(f)
        owner_wallet_address = config_data.get('owner_wallet_address')
        api_key = config_data.get('api_key_opensea')
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading configuration: {str(e)}")

verified = False
allow = False
verified_message = "Not authenticated"
print(f'initiating:{verified} - {verified_message}')

def retrieve_user_nfts(wallet_address):
    print(f"Fetching NFTs for wallet address: {wallet_address}")
    # Make a GET request to the OpenSea API to fetch the user's NFTs
    url = f"https://api.opensea.io/api/v1/assets?owner={wallet_address}"
    response = requests.get(url, headers={"X-API-KEY": api_key})

    if response.status_code == 200:
        data = response.json()
        # Extract the relevant information from the API response
        user_nfts = data["assets"]
        return user_nfts

    # If the API request fails, return an empty list or handle the error accordingly
    print("Error fetching NFTs from OpenSea API")
    return []

def has_same_nft_with_owner(nfts_user:set, nfts_owners:set):
    # Check if the user has any NFTs that are owned by the specified owner
    # Return True if the user has at least one NFT owned by the specified owner
    # Return False otherwise
    # return tuple, internsection ids and True/False
    return nfts_user.intersection(nfts_owners), len(nfts_user.intersection(nfts_owners)) > 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify_wallet_ownership():
    global verified, verified_message, allow
    data = request.get_json()
    wallet_address = data['account']
    signature = data['signature']
    message = data['message']

    text_message = encode_defunct(text=message)
    recovered_address = w3.eth.account.recover_message(text_message, signature=HexBytes(signature))
    is_verified = recovered_address.lower() == wallet_address.lower()

    if is_verified:
        verified = True
        verified_message = "Authenticated"
        owner_nft_ids = set(nft['token_id'] for nft in retrieve_user_nfts(wallet_address=owner_wallet_address))
        user_nfts = set(nft['token_id'] for nft in retrieve_user_nfts(wallet_address=wallet_address))
        same_nfts, has_same_nft = has_same_nft_with_owner(user_nfts, owner_nft_ids)
        
        result_message = None
        if has_same_nft:
            allow = True
            verified_message = "Authenticated and you own at least one Mintrower NFT"
            result_message = f"Congratulations! You own at least one Mintrower NFT. The ID(s) of your NFT(s) is/are {same_nfts}."
        else:
            verified_message = "Authenticated but you do not own a Mintrower NFT"
            result_message = "Sorry, you do not own a Mintrower NFT."
        
        return jsonify(
            result_message=result_message,
            owner_wallet_address=owner_wallet_address,
            owner_nft_ids=list(owner_nft_ids),
            user_wallet_address=wallet_address,
            user_nft_ids=list(user_nfts),
            same_nfts=list(same_nfts)
        )
    else:
        verified = False
        verified_message = "Not authenticated"
        print(f'authenticated:{verified} - {verified_message}')
        return jsonify(result_message="Sorry, the signature is invalid.")


@app.route('/result')
def show_result():
    result_message = request.args.get('result_message', '')
    owner_wallet_address = request.args.get('owner_wallet_address', '')
    owner_nft_ids = request.args.get('owner_nft_ids', '')
    user_wallet_address = request.args.get('user_wallet_address', '')
    user_nft_ids = request.args.get('user_nft_ids', '')
    same_nfts = request.args.get('same_nfts', '')
    return render_template('result.html', 
                           result_message=result_message,
                            owner_wallet_address=owner_wallet_address,
                            owner_nft_ids=owner_nft_ids,
                            user_wallet_address=user_wallet_address,
                            user_nft_ids=user_nft_ids,
                            same_nfts=same_nfts)
                            
