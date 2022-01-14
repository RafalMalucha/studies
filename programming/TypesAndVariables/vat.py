price = float(input("Podaj kwote:  "))

vat = price * 0.23

print(f"Amount: {'{0:.2f}'.format(price)} zł")
print(f"VAT 23%: {'{0:.2f}'.format(vat)} zł")

input("Press enter to exit ;)")