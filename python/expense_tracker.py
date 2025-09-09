import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = {
            '1': 'Food & Dining',
            '2': 'Transportation',
            '3': 'Shopping',
            '4': 'Entertainment',
            '5': 'Bills & Utilities',
            '6': 'Other'
        }
        
    def display_menu(self):
        print("\n🏦 EXPENSE TRACKER 🏦")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Generate Charts")
        print("4. Exit")
        print("=" * 40)
        
    def display_categories(self):
        print("\n📊 Expense Categories:")
        for key, value in self.categories.items():
            print(f"{key}. {value}")
        
    def add_expense(self):
        print("\n💰 Add New Expense")
        print("-" * 20)
        
        # Get amount
        while True:
            try:
                amount = float(input("Enter expense amount: $"))
                if amount > 0:
                    break
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get category
        self.display_categories()
        while True:
            category_num = input("\nSelect category (1-6): ")
            if category_num in self.categories:
                category = self.categories[category_num]
                break
            else:
                print("Please select a valid category (1-6).")
        
        # Get description
        description = input("Enter description (optional): ").strip()
        if not description:
            description = category
            
        # Add to expenses list
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime("%Y-%m-%d")
        }
        
        self.expenses.append(expense)
        print(f"✅ Added: ${amount:.2f} for {category}")
        
    def view_summary(self):
        if not self.expenses:
            print("\n📭 No expenses recorded yet!")
            return
            
        print("\n📊 EXPENSE SUMMARY")
        print("=" * 50)
        
        df = pd.DataFrame(self.expenses)
        total = df['amount'].sum()
        
        print(f"Total Expenses: ${total:.2f}")
        print(f"Number of Transactions: {len(self.expenses)}")
        print(f"Average Transaction: ${total/len(self.expenses):.2f}")
        
        print("\n💳 By Category:")
        category_totals = df.groupby('category')['amount'].sum().sort_values(ascending=False)
        for category, amount in category_totals.items():
            percentage = (amount / total) * 100
            print(f"  {category}: ${amount:.2f} ({percentage:.1f}%)")
            
        print("\n📋 Recent Transactions:")
        for expense in self.expenses[-5:]:  # Show last 5
            print(f"  ${expense['amount']:.2f} - {expense['category']} - {expense['description']}")
    
    def generate_charts(self):
        if not self.expenses:
            print("\n❌ No expenses to chart! Add some expenses first.")
            return
            
        df = pd.DataFrame(self.expenses)
        
        # Create charts directory if it doesn't exist
        os.makedirs('../public/charts', exist_ok=True)
        
        # Set up the plotting style
        plt.style.use('default')
        
        # 1. Combined Dashboard: Pie Chart + Summary Stats
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        fig.suptitle('Your Expense Analysis Dashboard', fontsize=16, fontweight='bold')
        
        # Pie chart
        category_totals = df.groupby('category')['amount'].sum()
        colors = plt.cm.Set3(np.linspace(0, 1, len(category_totals)))
        
        wedges, texts, autotexts = ax1.pie(category_totals.values, 
                                          labels=category_totals.index,
                                          autopct='%1.1f%%',
                                          colors=colors,
                                          startangle=90)
        
        ax1.set_title('Spending by Category', fontweight='bold', pad=20)
        
        # Make percentage text bold and readable
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        # 2. Summary Statistics as Bar Chart
        stats_data = {
            'Total Spent': df['amount'].sum(),
            'Average per Transaction': df['amount'].mean(),
            'Largest Single Expense': df['amount'].max(),
            'Smallest Single Expense': df['amount'].min()
        }
        
        # Create horizontal bar chart for stats
        categories = list(stats_data.keys())
        values = list(stats_data.values())
        
        bars = ax2.barh(categories, values, 
                       color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
        
        ax2.set_title('Financial Summary Stats', fontweight='bold', pad=20)
        ax2.set_xlabel('Amount ($)')
        
        # Add value labels
        for bar, value in zip(bars, values):
            ax2.text(bar.get_width() + max(values) * 0.01, bar.get_y() + bar.get_height()/2,
                    f'${value:.2f}', va='center', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('../public/charts/expense_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # 2. Detailed Category Breakdown
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        category_totals = df.groupby('category')['amount'].sum().sort_values(ascending=True)
        
        bars = ax.barh(category_totals.index, category_totals.values, 
                      color=plt.cm.viridis(np.linspace(0, 1, len(category_totals))))
        
        ax.set_title('Detailed Spending Breakdown by Category', fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('Amount Spent ($)')
        
        # Add value labels and percentages
        total = category_totals.sum()
        for bar, value in zip(bars, category_totals.values):
            percentage = (value / total) * 100
            ax.text(bar.get_width() + total * 0.01, bar.get_y() + bar.get_height()/2,
                   f'${value:.2f} ({percentage:.1f}%)', va='center', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('../public/charts/expense_stats.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✅ Charts generated successfully!")
        print("📁 Check the /public/charts/ folder for your visualizations")
        print("🌐 You can also view them in the web interface!")
        print("💡 Run 'npm start' then go to /expenses to see your charts on the web!")
        
    def run(self):
        print("🚀 Welcome to your Personal Expense Tracker!")
        print("Let's start tracking your spending and create some awesome charts!")
        
        while True:
            self.display_menu()
            choice = input("\nSelect an option (1-4): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_summary()
            elif choice == '3':
                self.generate_charts()
            elif choice == '4':
                print("\n👋 Thanks for tracking your expenses!")
                print("💡 Remember to commit your charts to GitHub!")
                print("🌐 Don't forget to check out your charts at /expenses!")
                break
            else:
                print("❌ Please select a valid option (1-4)")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()