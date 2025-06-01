"""
CryptoWise Advisor Chatbot - A rule-based cryptocurrency investment advisor.
Provides investment advice based on profitability and sustainability metrics.
"""

import sys
from colorama import init, Fore, Style
from tabulate import tabulate
from crypto_data import (
    crypto_db, get_trending_cryptos, get_sustainable_cryptos,
    get_profitable_cryptos, calculate_sustainability_score, get_crypto_info
)

# Initialize colorama for cross-platform colored output
init()

class CryptoWiseAdvisor:
    def __init__(self):
        self.name = "CryptoWise"
        self.version = "1.0"
        self.disclaimer = (
            f"{Fore.YELLOW}⚠️  DISCLAIMER: Cryptocurrency investments are inherently risky. "
            "This advice is based on predefined rules and data. "
            "Always conduct your own research and consult with financial advisors "
            "before making investment decisions.{Style.RESET_ALL}"
        )
        
    def print_welcome(self):
        """Display welcome message and introduction."""
        welcome_msg = f"""
{Fore.CYAN}🌟 Welcome to {self.name} - Your Smart Crypto Investment Guide! 🌟{Style.RESET_ALL}

I'm here to help you make informed cryptocurrency investment decisions based on:
• Profitability metrics (price trends, market cap)
• Sustainability factors (energy efficiency, project viability)

{Fore.GREEN}How can I assist you today?{Style.RESET_ALL}
You can ask me about:
• Trending cryptocurrencies
• Sustainable investment options
• Specific cryptocurrency information
• General investment advice

Type 'help' for more options or 'exit' to quit.
"""
        print(welcome_msg)
        print(self.disclaimer)
        print("\n" + "="*80 + "\n")

    def print_help(self):
        """Display help message with available commands."""
        help_msg = f"""
{Fore.CYAN}Available Commands:{Style.RESET_ALL}

1. Trending & Profitability:
   • "Which crypto is trending up?"
   • "What are the profitable coins?"
   • "Show me trending cryptos"

2. Sustainability:
   • "What's the most sustainable coin?"
   • "Show sustainable options"
   • "Which crypto is most eco-friendly?"

3. Specific Information:
   • "Tell me about [cryptocurrency]"
   • "What is [cryptocurrency]?"
   • "Info on [cryptocurrency]"

4. General:
   • "help" - Show this help message
   • "exit" - Quit the chatbot
   • "disclaimer" - Show investment disclaimer
"""
        print(help_msg)

    def format_crypto_table(self, crypto_dict, title):
        """Format cryptocurrency data into a table."""
        if not crypto_dict:
            return f"No cryptocurrencies found matching the criteria for {title}."
        
        table_data = []
        for name, data in crypto_dict.items():
            table_data.append([
                name,
                data["symbol"],
                data["price_trend"].title(),
                data["market_cap"].title(),
                f"{data['sustainability_score']}/10",
                data["energy_use"].title()
            ])
        
        headers = ["Name", "Symbol", "Price Trend", "Market Cap", "Sustainability", "Energy Use"]
        return f"\n{Fore.CYAN}{title}{Style.RESET_ALL}\n" + tabulate(table_data, headers=headers, tablefmt="grid")

    def handle_trending_query(self):
        """Handle queries about trending cryptocurrencies."""
        trending = get_trending_cryptos()
        return self.format_crypto_table(trending, "📈 Trending Cryptocurrencies")

    def handle_sustainability_query(self):
        """Handle queries about sustainable cryptocurrencies."""
        sustainable = get_sustainable_cryptos()
        return self.format_crypto_table(sustainable, "🌱 Sustainable Cryptocurrencies")

    def handle_profitability_query(self):
        """Handle queries about profitable cryptocurrencies."""
        profitable = get_profitable_cryptos()
        return self.format_crypto_table(profitable, "💰 Profitable Cryptocurrencies")

    def handle_crypto_info_query(self, crypto_name):
        """Handle queries about specific cryptocurrency information."""
        info = get_crypto_info(crypto_name)
        if not info:
            return f"{Fore.RED}Sorry, I don't have information about {crypto_name}.{Style.RESET_ALL}"
        
        response = f"""
{Fore.CYAN}📊 {crypto_name.title()} ({info['symbol']}) Information{Style.RESET_ALL}

Description: {info['description']}
Price Trend: {info['price_trend'].title()}
Market Cap: {info['market_cap'].title()}
Energy Use: {info['energy_use'].title()}
Sustainability Score: {info['sustainability_score']}/10
Project Viability: {info['project_viability'].title()}

{Fore.YELLOW}Investment Consideration:{Style.RESET_ALL}
"""
        if info['price_trend'] == 'rising' and info['market_cap'] == 'high':
            response += "• Strong profitability potential due to rising price trend and high market cap"
        elif info['energy_use'] == 'low' and info['sustainability_score'] >= 7:
            response += "• Strong sustainability profile with low energy use and high sustainability score"
        else:
            response += "• Mixed profile - consider both profitability and sustainability factors"
        
        return response

    def process_query(self, query):
        """Process user query and return appropriate response."""
        query = query.lower().strip()
        
        # Exit command
        if query in ['exit', 'quit', 'bye']:
            print(f"\n{Fore.GREEN}Thank you for using {self.name}! Stay crypto-wise! 👋{Style.RESET_ALL}\n")
            sys.exit(0)
        
        # Help command
        if query == 'help':
            self.print_help()
            return None
        
        # Disclaimer command
        if query == 'disclaimer':
            print(self.disclaimer)
            return None
        
        # Trending queries
        if any(phrase in query for phrase in ['trending', 'trend', 'going up', 'rising']):
            return self.handle_trending_query()
        
        # Sustainability queries
        if any(phrase in query for phrase in ['sustainable', 'sustainability', 'eco', 'green', 'environment']):
            return self.handle_sustainability_query()
        
        # Profitability queries
        if any(phrase in query for phrase in ['profitable', 'profit', 'investment', 'invest']):
            return self.handle_profitability_query()
        
        # Specific crypto information
        if query.startswith(('tell me about', 'what is', 'info on', 'information about')):
            crypto_name = query.split()[-1]
            return self.handle_crypto_info_query(crypto_name)
        
        # Default response for unrecognized queries
        return f"""
{Fore.YELLOW}I'm not sure I understand. Here are some things you can ask me:{Style.RESET_ALL}
• "Which crypto is trending up?"
• "What's the most sustainable coin?"
• "Tell me about Bitcoin"
• Type 'help' for more options
"""

def main():
    """Main function to run the chatbot."""
    advisor = CryptoWiseAdvisor()
    advisor.print_welcome()
    
    while True:
        try:
            query = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
            if not query:
                continue
                
            response = advisor.process_query(query)
            if response:
                print(f"\n{Fore.BLUE}CryptoWise: {Style.RESET_ALL}{response}\n")
                print(advisor.disclaimer)
                print("\n" + "="*80 + "\n")
                
        except KeyboardInterrupt:
            print(f"\n\n{Fore.GREEN}Thank you for using {advisor.name}! Stay crypto-wise! 👋{Style.RESET_ALL}\n")
            sys.exit(0)
        except Exception as e:
            print(f"\n{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
            print("Please try again or type 'help' for available commands.\n")

if __name__ == "__main__":
    main() 