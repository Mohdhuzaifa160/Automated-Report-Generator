import pandas as pd
from fpdf import FPDF

# Load data
df = pd.read_csv('data.csv')

# Analyze data
average = df['Marks'].mean()
highest = df['Marks'].max()
lowest = df['Marks'].min()

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')
pdf.ln(10)

# Add table
for index, row in df.iterrows():
    pdf.cell(200, 10, txt=f"{row['Name']}: {row['Marks']} Marks", ln=True)

# Add stats
pdf.ln(10)
pdf.cell(200, 10, txt=f"Average Marks: {average}", ln=True)
pdf.cell(200, 10, txt=f"Highest Marks: {highest}", ln=True)
pdf.cell(200, 10, txt=f"Lowest Marks: {lowest}", ln=True)

# Save PDF
pdf.output("sample_report.pdf")
