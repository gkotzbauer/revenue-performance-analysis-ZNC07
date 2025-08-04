# invoice_benchmark_code_v2.py

import os
import pandas as pd

# === Step 0: Load Invoice-Level Data ===
INVOICE_INPUT = "Invoice_Assigned_To_Benchmark_With_Count.xlsx"
if not os.path.isfile(INVOICE_INPUT):
    raise FileNotFoundError(f"Error: File not found: {INVOICE_INPUT}")

df_inv = pd.read_excel(INVOICE_INPUT, sheet_name='Sheet1')

# === Step 1: Standardize Column Names ===
df_inv = df_inv.rename(columns={
    'Year of Visit Service Date': 'Year',
    'ISO Week of Visit Service Date': 'Week',
    'Primary Financial Class': 'Payer',
    'Chart E/M Code Grouping': 'Group_EM',
    'Chart E/M Code Second Layer': 'Group_EM2',
    'Charge Invoice Number': 'Invoice_Number'
})

# === Step 2: Data Type Conversion ===
df_inv['Year'] = df_inv['Year'].astype(int)
df_inv['Week'] = df_inv['Week'].str.replace('W','').astype(int)

# === Step 3: Define Grouping Keys ===
group_keys = ['Year', 'Week', 'Payer', 'Group_EM', 'Group_EM2']

# === Step 4: Compute Group-Level Benchmarks ===
benchmark_df = (
    df_inv
    .groupby(group_keys)
    .agg(
        Benchmark_Charge_Amount=('Charge Amount', 'mean'),
        Benchmark_Payment_Amount=('Payment Amount*', 'mean'),
        Benchmark_Zero_Balance_Collection_Rate=('Zero Balance Collection Rate', 'mean'),
        Benchmark_Invoice_Count=('Invoice_Number', 'count')
    )
    .reset_index()
)

# === Step 5: Merge Benchmarks Back to Invoice Records ===
df_inv = df_inv.merge(benchmark_df, on=group_keys, how='left')

# === Step 6: Add Metric-Level Root Cause Tags ===
df_inv['Tag_Low_Payment']      = df_inv['Payment Amount*'] < (0.9  * df_inv['Benchmark_Payment_Amount'])
df_inv['Tag_Low_ZB_Collection']= df_inv['Zero Balance Collection Rate'] < (0.9  * df_inv['Benchmark_Zero_Balance_Collection_Rate'])
df_inv['Tag_High_Charge']      = df_inv['Charge Amount'] > (1.1  * df_inv['Benchmark_Charge_Amount'])

# === Step 7: Export Invoice-Level Drill Index ===
OUTPUT_CSV = 'invoice_level_index.csv'
df_inv.to_csv(OUTPUT_CSV, index=False)
print(f"Invoice-level index written to {OUTPUT_CSV}")
