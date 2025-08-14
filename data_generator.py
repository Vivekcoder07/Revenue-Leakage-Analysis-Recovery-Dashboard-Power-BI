# data_generator.py
# Run: python data_generator.py
import os, random
from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

fake = Faker()
random.seed(42)
np.random.seed(42)

os.makedirs("datasets", exist_ok=True)

# CONFIG
N_CLIENTS = 150
N_EMPLOYEES = 500
N_CONTRACTS = 300
N_TIMESHEET_ROWS = 42000
N_BILLING_ROWS = 8000
N_SLA_ROWS = 2000

# 1) Clients
clients = []
for i in range(N_CLIENTS):
    clients.append({
        "ClientID": f"C{i+1:04}",
        "ClientName": fake.company(),
        "Country": fake.country(),
        "Industry": random.choice(["IT Services","SaaS","Consulting","Infra Support"])
    })
clients_df = pd.DataFrame(clients)
clients_df.to_csv("datasets/clients.csv", index=False)

# 2) Employees
roles = ["Developer","Tester","Project Manager","Consultant","Support Engineer"]
employees = []
for i in range(N_EMPLOYEES):
    employees.append({
        "EmpID": f"E{i+1:05}",
        "EmpName": fake.name(),
        "Role": random.choice(roles),
        "HourlyRate": round(random.uniform(20,120),2)
    })
employees_df = pd.DataFrame(employees)
employees_df.to_csv("datasets/employees.csv", index=False)

# 3) Contracts
contracts = []
start_base = datetime(2023,1,1)
for i in range(N_CONTRACTS):
    client = clients_df.sample(1).iloc[0]
    start = start_base + timedelta(days=random.randint(0, 540))  # between Jan 2023 - Jun 2024
    end = start + timedelta(days=random.randint(180,720))
    contracts.append({
        "ContractID": f"K{i+1:05}",
        "ClientID": client["ClientID"],
        "StartDate": start.date().isoformat(),
        "EndDate": end.date().isoformat(),
        "MonthlyFee": round(random.uniform(2000,20000),2),
        "RateCardHourly": round(random.uniform(30,120),2),
        "SLA_Uptime": random.choice([99.0,99.5,99.9]),
        "RenewalStatus": random.choice(["Renewed","Not Renewed","Pending"])
    })
contracts_df = pd.DataFrame(contracts)
contracts_df.to_csv("datasets/contracts.csv", index=False)

# 4) Timesheets
times = []
for _ in range(N_TIMESHEET_ROWS):
    emp = employees_df.sample(1).iloc[0]
    contract = contracts_df.sample(1).iloc[0]
    s = datetime.fromisoformat(contract["StartDate"])
    e = datetime.fromisoformat(contract["EndDate"])
    if s >= e:
        date = s
    else:
        date = s + timedelta(days=random.randint(0, max(0,(e-s).days)))
    hours_logged = round(random.uniform(1.0,10.0),2)
    r = random.random()
    # 85% fully billed, 10% partially under-billed, 5% not billed
    if r < 0.85:
        hours_billed = hours_logged
    elif r < 0.95:
        hours_billed = max(0, round(hours_logged - random.uniform(0.5,3.0),2))
    else:
        hours_billed = 0.0
    times.append({
        "TimesheetID": f"T{random.randint(1000000,9999999)}",
        "EmpID": emp["EmpID"],
        "ContractID": contract["ContractID"],
        "Date": date.date().isoformat(),
        "HoursLogged": hours_logged,
        "HoursBilled": hours_billed
    })
timesheets_df = pd.DataFrame(times)
timesheets_df.to_csv("datasets/timesheets.csv", index=False)

# 5) Billing invoices
billings = []
for _ in range(N_BILLING_ROWS):
    contract = contracts_df.sample(1).iloc[0]
    start = datetime.fromisoformat(contract["StartDate"])
    end = datetime.fromisoformat(contract["EndDate"])
    inv_date = start + timedelta(days=random.randint(0, max(0,(end-start).days)))
    hours_billed = round(random.uniform(10,200),2)
    # 20% chance billed rate < rate card
    if random.random() < 0.2:
        billed_rate = max(5.0, round(contract["RateCardHourly"] - random.uniform(1,10),2))
    else:
        billed_rate = contract["RateCardHourly"]
    amount_due = round(hours_billed * billed_rate,2)
    if random.random() < 0.12:
        amount_paid = round(amount_due - random.uniform(20, amount_due*0.6),2)
    else:
        amount_paid = amount_due
    billings.append({
        "InvoiceID": f"INV{random.randint(100000,999999)}",
        "ContractID": contract["ContractID"],
        "InvoiceDate": inv_date.date().isoformat(),
        "HoursBilled": hours_billed,
        "HourlyRateBilled": billed_rate,
        "AmountDue": amount_due,
        "AmountPaid": amount_paid
    })
billing_df = pd.DataFrame(billings)
billing_df.to_csv("datasets/billing.csv", index=False)

# 6) SLA logs (breaches & credits)
sla = []
for _ in range(N_SLA_ROWS):
    contract = contracts_df.sample(1).iloc[0]
    s = datetime.fromisoformat(contract["StartDate"])
    e = datetime.fromisoformat(contract["EndDate"])
    breach = s + timedelta(days=random.randint(0, max(0,(e-s).days)))
    downtime = int(abs(np.random.exponential(30))) + 5
    credit_pct = random.choice([0.05,0.1])
    credit_amount = round(contract["MonthlyFee"] * credit_pct, 2)
    claimed = random.random() < 0.45  # 55% unclaimed
    sla.append({
        "SLAEventID": f"SLA{random.randint(100000,999999)}",
        "ContractID": contract["ContractID"],
        "BreachDate": breach.date().isoformat(),
        "DowntimeMinutes": downtime,
        "PotentialCredit": credit_amount,
        "CreditClaimed": credit_amount if claimed else 0.0
    })
sla_df = pd.DataFrame(sla)
sla_df.to_csv("datasets/sla_logs.csv", index=False)

print("✅ Datasets created in ./datasets/")
print("Counts:",
      len(clients_df), len(employees_df), len(contracts_df),
      len(timesheets_df), len(billing_df), len(sla_df))

# Install faker package
os.system("pip install faker")
