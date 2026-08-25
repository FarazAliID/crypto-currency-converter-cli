import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd,pkr"

def crypto_currencry_converter():
	try:
		response = requests.get(url)
		data = response.json()
		
		if "bitcoin" and "ethereum" in data:
			bitcoin_usd = data["bitcoin"]["usd"]
			bitcoin_pkr = data["bitcoin"]["pkr"]
			ethereum_usd = data["ethereum"]["usd"]
			ethereum_pkr = data["ethereum"]["pkr"]
			cardano_usd = data["cardano"]["usd"]
			cardano_pkr = data["cardano"]["pkr"]
			
			return bitcoin_usd, bitcoin_pkr, ethereum_usd, ethereum_pkr, cardano_usd, cardano_pkr
			
		else:
			print("Data is not Loading")
			
	except:
		print("Your Internet Is Unstable")



def main():
    bit_usd, bit_pkr, eth_usd, eth_pkr, card_usd, card_pkr = crypto_currencry_converter()

    while True:
        print("\n=== Crypto & Fiat Currency Converter CLI ===")
        print("1. Bitcoin USD & PKR Converter")
        print("2. Ethereum USD & PKR Converter")
        print("3. Cardano USD & PKR Converter")
        print("4. Exit")
        
        choice = input("Select The Option Between (1 & 4) : ")
        
        if choice == "1":
            user = float(input("Put Your Coins To Calculate Bitcoin Currency In USD & PKR: "))
            print(f"Coin Price USD is {bit_usd} X User {user} == {bit_usd * user:,.2f}")
            print(f"Coin Price PKR is {bit_pkr} X User {user} == {bit_pkr * user:,.2f}")
            
        elif choice == "2":
            user = float(input("Put Your Coins To Calculate Ethereum Currency In USD & PKR: "))
            print(f"Coin Price USD is {eth_usd} X User {user} == {eth_usd * user:,.2f}")
            print(f"Coin Price PKR is {eth_pkr} X User {user} == {eth_pkr * user:,.2f}")
            
        elif choice == "3":
            user = float(input("Put Your Coins To Calculate Cardano Currency In USD & PKR: "))
            print(f"Coin Price USD is {card_usd} X User {user} == {card_usd * user:,.2f}")
            print(f"Coin Price PKR is {card_pkr} X User {user} == {card_pkr * user:,.2f}")
            
        elif choice == "4":
            print("Thank you for using Crypto Converter!")
            break
            
        else:
            print("Invalid Option! Please select between 1 and 4.")

main()
