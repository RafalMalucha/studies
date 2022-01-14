meat = open("MeatAndFish.txt", "r")
meat_content = meat.read()
grain = open("GrainsAndBread.txt", "r")
grain_content = grain.read()
shoppinglist = open("shoppinglist.txt", "w")

shoppinglist.write(meat_content)
shoppinglist.write("\n")
shoppinglist.write(grain_content)

meat.close()
grain.close()
shoppinglist.close()