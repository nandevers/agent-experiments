import pandas as pd
import numpy as np
import sqlite3
from faker import Faker
from loguru import logger



import pandas as pd
import random
import numpy as np
import sqlite3
from datetime import datetime, timedelta
from faker import Faker
from loguru import logger

# Initialize Faker for Brazil
fake = Faker('pt_BR')

# Borrower Profiles Dataset
def generate_borrower_profiles(num_records):
    logger.info("Generating Borrower Profiles dataset...")
    data = []
    for _ in range(num_records):
        profile = {
            "CPF": fake.cpf(),
            "Name": fake.name(),
            "Age": np.random.randint(18, 70),
            "Income": max(0, np.random.normal(4000, 1500)),  # Mean income ~4000 BRL
            "Credit_Score": np.random.randint(300, 850),
            "Debt_to_Income_Ratio": np.random.uniform(0.1, 0.9),
            "Region": fake.state()
        }
        data.append(profile)
    logger.info("Borrower Profiles dataset generated.")
    return pd.DataFrame(data)

# Loan Products Dataset
def generate_loan_products(num_records):
    logger.info("Generating Loan Products dataset...")
    loan_types = ["Personal Loan", "Mortgage", "Auto Loan", "Credit Card"]
    data = []
    for _ in range(num_records):
        product = {
            "Loan_Type": np.random.choice(loan_types),
            "Interest_Rate": round(np.random.uniform(5, 35), 2),
            "Max_Loan_Amount": round(np.random.uniform(1000, 500000), 2),
            "Repayment_Term_Months": np.random.choice([12, 24, 36, 60, 120, 240]),
            "Origination_Fee": round(np.random.uniform(1, 5), 2)  # Percentage
        }
        data.append(product)
    logger.info("Loan Products dataset generated.")
    return pd.DataFrame(data)

# Default Rates Dataset
def generate_default_rates(num_records):
    logger.info("Generating Default Rates dataset...")
    borrower_classes = ["Prime", "Near-Prime", "Subprime"]
    data = []
    for _ in range(num_records):
        default = {
            "Borrower_Class": np.random.choice(borrower_classes),
            "Default_Rate": round(np.random.uniform(0.01, 0.3), 2),
            "Loss_Given_Default": round(np.random.uniform(0.4, 0.9), 2),
            "Exposure_at_Default": round(np.random.uniform(1000, 50000), 2)
        }
        data.append(default)
    logger.info("Default Rates dataset generated.")
    return pd.DataFrame(data)

# Market Trends Dataset
def generate_market_trends(num_records):
    logger.info("Generating Market Trends dataset...")
    data = []
    for _ in range(num_records):
        trend = {
            "Year": np.random.choice(range(2000, 2025)),
            "Benchmark_Rate": round(np.random.uniform(2, 15), 2),  # E.g., SELIC rate
            "Inflation_Rate": round(np.random.uniform(1, 10), 2),
            "GDP_Growth": round(np.random.uniform(-5, 5), 2)
        }
        data.append(trend)
    logger.info("Market Trends dataset generated.")
    return pd.DataFrame(data)

# Regulatory Data Dataset
def generate_regulatory_data(num_records):
    logger.info("Generating Regulatory Data dataset...")
    regions = ["Norte", "Nordeste", "Sul", "Sudeste", "Centro-Oeste"]
    data = []
    for _ in range(num_records):
        regulation = {
            "Region": np.random.choice(regions),
            "Max_Interest_Rate": round(np.random.uniform(30, 60), 2),
            "Max_Loan_Amount": round(np.random.uniform(50000, 1000000), 2),
            "Compliance_Rule": fake.text(max_nb_chars=50)
        }
        data.append(regulation)
    logger.info("Regulatory Data dataset generated.")
    return pd.DataFrame(data)

# Save Data to SQLite
def save_to_sqlite(df, table_name, conn):
    logger.info(f"Saving {table_name} to SQLite database...")
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    logger.info(f"{table_name} saved to SQLite database.")

# Utility functions
def random_date(start, end):
    if isinstance(start, datetime):
        start = start
    else:
        start = datetime.combine(start, datetime.min.time())

    if isinstance(end, datetime):
        end = end
    else:
        end = datetime.combine(end, datetime.min.time())

    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Data generation functions

def generate_contracts(num_contracts, installments_per_contract):
    contracts = []
    for contract_id in range(1, num_contracts + 1):
        contract_start_date = random_date(datetime(2020, 1, 1), datetime(2024, 1, 1))
        contract_end_date = contract_start_date + timedelta(days=random.randint(365, 1825))
        total_value = random.randint(5000, 50000)
        num_installments = installments_per_contract
        frequency = "Monthly"

        contracts.append({
            "Contract ID": f"C{contract_id:03}",
            "Customer Name": f"Customer {contract_id}",
            "Contract Start Date": contract_start_date.date(),
            "Contract End Date": contract_end_date.date(),
            "Contract Type": random.choice(["Loan", "Lease", "Subscription"]),
            "Total Contract Value": total_value,
            "Number of Installments": num_installments,
            "Frequency of Installments": frequency,
        })
    return pd.DataFrame(contracts)

def generate_installments(num_contracts, installments_per_contract, contracts):
    installments = []
    for _, contract in contracts.iterrows():
        contract_id = contract["Contract ID"]
        contract_start_date = datetime.strptime(str(contract["Contract Start Date"]), '%Y-%m-%d')
        installment_amount = contract["Total Contract Value"] / installments_per_contract

        for installment_id in range(1, installments_per_contract + 1):
            installment_due_date = contract_start_date + timedelta(days=30 * installment_id)
            paid_date_offset = random.choice([0, random.randint(1, 30), None])
            payment_date = (installment_due_date + timedelta(days=paid_date_offset)) if paid_date_offset else None
            days_late = (payment_date - installment_due_date).days if payment_date and payment_date > installment_due_date else 0
            days_outstanding = (datetime.now() - installment_due_date).days if not payment_date and installment_due_date < datetime.now() else 0
            adjusted_amount = installment_amount + days_late * 0.5 + (days_late * 2)

            installments.append({
                "Installment ID": f"I{contract_id.split('C')[-1]:03}-{installment_id:02}",
                "Contract ID": contract_id,
                "Installment Due Date": installment_due_date.date(),
                "Installment Amount (Original)": round(installment_amount, 2),
                "Status": "Paid" if payment_date else "Unpaid",
                "Days Outstanding": days_outstanding,
                "Penalty Charged": days_late > 0,
                "Adjusted Installment Amount": round(adjusted_amount, 2),
            })
    return pd.DataFrame(installments)

def generate_payments(installments):
    payments = []
    for _, installment in installments.iterrows():
        installment_id = installment["Installment ID"]
        payment_date = None
        days_late = 0
        paid_amount = 0
        interest_amount = 0
        penalty_amount = 0
        overpayment_amount = 0

        if installment["Status"] == "Paid":
            payment_date = random_date(datetime.strptime(str(installment["Installment Due Date"]), '%Y-%m-%d'), datetime.now())
            days_late = (payment_date - datetime.strptime(str(installment["Installment Due Date"]), '%Y-%m-%d')).days
            paid_amount = installment["Installment Amount (Original)"] + days_late * 2
            interest_amount = days_late * 0.5
            penalty_amount = days_late * 2
            overpayment_amount = max(0, paid_amount - installment["Installment Amount (Original)"])

        payments.append({
            "Installment ID": installment_id,
            "Payment Date": payment_date.date() if payment_date else None,
            "Installment Amount (Paid)": round(paid_amount, 2),
            "Days Late": days_late,
            "Interest Amount": round(interest_amount, 2),
            "Penalty Amount": penalty_amount,
            "Overpayment Amount": round(overpayment_amount, 2),
            "Payment Method": random.choice(["Credit Card", "Bank Transfer", "Cash"]),
            "Payment Notes": random.choice(["On time", "Late payment", "Pending approval"]),
        })
    return pd.DataFrame(payments)

def save_to_sqlite(df, table_name, conn):
    logger.info(f"Saving {table_name} to SQLite database...")
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    logger.info(f"{table_name} saved to SQLite database.")

# Main function to generate and store data
def main():
    logger.info("Starting dataset generation process...")
    num_records = 10000
    installments_per_contract = 6

    # Generate datasets
    contracts = generate_contracts(num_records, installments_per_contract)
    installments = generate_installments(num_records, installments_per_contract, contracts)
    payments = generate_payments(installments)

    # Save to SQLite database
    conn = sqlite3.connect("synthetic_data.db")
    # Generate Datasets
    logger.info("Starting dataset generation process...")
    borrower_profiles = generate_borrower_profiles(num_records)
    loan_products = generate_loan_products(num_records // 10)  # Fewer loan products
    default_rates = generate_default_rates(num_records // 10)
    market_trends = generate_market_trends(num_records // 100)  # Trends over years
    regulatory_data = generate_regulatory_data(num_records // 100)

    # Save to SQLite Database
    logger.info("Connecting to SQLite database...")
    conn = sqlite3.connect("synthetic_data.db")
    save_to_sqlite(borrower_profiles, "Borrower_Profiles", conn)
    save_to_sqlite(loan_products, "Loan_Products", conn)
    save_to_sqlite(default_rates, "Default_Rates", conn)
    save_to_sqlite(market_trends, "Market_Trends", conn)
    save_to_sqlite(regulatory_data, "Regulatory_Data", conn)
    save_to_sqlite(contracts, "Contracts", conn)
    save_to_sqlite(installments, "Installments", conn)
    save_to_sqlite(payments, "Payments", conn)
    conn.close()
    logger.info("All datasets generated and stored in SQLite database.")

if __name__ == "__main__":
    main()
