pin = "0805"
attempt = 0

entered_pin = input("Enter the PIN code: ")

while pin != entered_pin:
    print("Incorrect...")
    attempt += 1
    if attempt > 2:
        print("Sorry, your payment card has been blocked.")
        break
    entered_pin = input("Enter the PIN code: ")
    continue
while pin == entered_pin:
    print("Great success")
    break

    
        
    

    

    
