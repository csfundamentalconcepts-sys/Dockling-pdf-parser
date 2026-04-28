from parser import unlock_pdf

input_pdf = "app\VAPT1.pdf"
password = "Bpcl#111225"

try:
    unlocked = unlock_pdf(input_pdf, password)
    print("Unlocked file created at:", unlocked)
except Exception as e:
    print("Error:", e)