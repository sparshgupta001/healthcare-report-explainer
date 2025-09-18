from reportlab.pdfgen import canvas

# Create a PDF with two test results
c = canvas.Canvas("sample.pdf")
c.drawString(100, 750, "Hemoglobin: 11.2 g/dL")
c.drawString(100, 730, "Cholesterol: 220 mg/dL")
c.save()

print("✅ sample.pdf created successfully!")
