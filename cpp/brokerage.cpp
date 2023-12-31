#include <map>
#include <iostream>
#include <string>

class Brokerage {
	public:
		float cash = 10000.0;
		std::map<std::string, float> holdings;
		void buy(std::string ticker, std::map<std::string, float> ticker_prices, std::string date, float dollar_amount);
		void sell(std::string ticker, std::map<std::string, float> ticker_prices, std::string date, float dollar_amount);
		float Brokerage::account_total(std::map<std::string, std::map<std::string, float>> ticker_prices, std::string date);
};

void Brokerage::buy(std::string ticker, std::map<std::string, float> ticker_prices, std::string date, float dollar_amount) {
	if (dollar_amount > Brokerage::cash)
		throw std::invalid_argument("Not enough cash to buy");

	if (ticker_prices.count(date) == 0)
		throw std::invalid_argument("Invalid date");

	if (Brokerage::holdings.count(ticker) == 0)
		Brokerage::holdings[ticker] = 0;

	float date_price = ticker_prices[date];
	float amount_purchased = dollar_amount / date_price;

	Brokerage::cash -= dollar_amount;
	Brokerage::holdings[ticker] += amount_purchased;

}

void Brokerage::sell(std::string ticker, std::map<std::string, float> ticker_prices, std::string date, float dollar_amount) {
	if (Brokerage::holdings.count(ticker) == 0)
		throw std::invalid_argument("Stock not even owned nerd");
	
	if (ticker_prices.count(date) == 0)
		throw std::invalid_argument("Invalid date");


	float date_price = ticker_prices[date];
	float stock_amount_selling = dollar_amount / date_price;

	if (stock_amount_selling > Brokerage::holdings[ticker])
		throw std::invalid_argument("Trying to sell more than what's in holdings");

	Brokerage::cash += dollar_amount;
	Brokerage::holdings[ticker] -= stock_amount_selling;

}

float Brokerage::account_total(std::map<std::string, std::map<std::string, float>> all_ticker_prices, std::string date){
	float stock_value = 0;
	for (const auto& pair : Brokerage::holdings) {
    	const std::string& ticker = pair.first;
    	float amount = pair.second;

		std::map<std::string, float> ticker_prices = all_ticker_prices[ticker];
		float current_stock_price = ticker_prices[date];
		stock_value += current_stock_price * amount;
	}

	return Brokerage::cash + stock_value;
}


int main() {
	printf("test\n");

	return 0;
}


