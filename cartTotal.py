# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headPhone = "999";
smartWatch = "1599";
PS5 = "1299";
iPad = "599";


productName = input("Enter Product Name: ");

#bug=input("Enter the Quantity of the Product:"),fix=int(input("Enter the Quantity of the Product: "));
quantity = int(input("Enter the Quantity of the Product: "));


if productName == "headPhone":
    totalPrice = (headPhone)*quantity;

elif productName == "smartWatch":
    #bug=totalprice=headphone * quantity;,fix=totalPrice=smartWatch*quantity;
    totalPrice = (smartWatch)*quantity;

elif productName == "PS5":
    #bug=totalprice=headphone * quantity;,fix=totalPrice=PS5*quantity;
    totalPrice = (PS5)*quantity;

elif productName == "iPad":
    #bug=totalprice=headphone * quantity;,fix=totalPrice=iPad*quantity;
    totalPrice = (iPad)*quantity;


print(f"Total Amount To Be Paid: {totalPrice}");