cart = 0
# if cart != 2:
#     raise Exception("No product in cart")

# assert (cart == 2)

try:
    with open('tesst.txt', 'r') as reader:
        print(reader.read())
except Exception as e:
    print("File not available")
    print(e)
finally:
    print("Finally")
