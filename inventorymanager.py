import csv
import datetime

#define current time for receipt
now = datetime.datetime.now()

ReceiptUnpack = open("Receipt.txt", "a")

#Dictionaries
ISBN={}
Title={}
Author={}
Price={}
Quantity={}
Sold={}

# Read the tsv file
Unpack = open("booklist.tsv","r")
BooksUnpack = csv.DictReader(Unpack, delimiter = "\t")

# Welcome message
print()
print("Welcome to GMC bookstore inventory system")
print()
print ("In the bookstore, you now have the following books: ")
print()

# Store all the information in separate dictionaries: {ID: xx}. 
totalnumber_items = 0
for book in BooksUnpack:
     totalnumber_items += 1
     ISBN.update({int(book["ID"]):int(book["ISBN"])})
     Title.update({int(book["ID"]):book["Title"]})
     Author.update({int(book["ID"]):book["Author"]})
     Price.update({int(book["ID"]):float(book["Price"])})
     Quantity.update({int(book["ID"]):int(book["Quantity"])})
     Sold.update({int(book["ID"]):int(book["Sold"])})

# Print out current books, restrain the length of each string so that each item will be aligned. 
     print (book["ID"].ljust(3), book["ISBN"].ljust(14), book["Title"].ljust(30)[:30],   \
         book["Author"].ljust(15)[:15], book["Price"].ljust(6), book["Quantity"].ljust(4), (book["Sold"]).ljust(4))

# Close the file; All the changes will be saved in separate dictionaries until the program quits and writes the new info into the file. 
Unpack.close()

print()
print("You can do the following functions by entering relevant letter(s)")
print("A - Add a book to the inventory")
print("R - Remove a book from the inventory")
print("U - Update details of a book")
print("V - View all the books in the inventory")
print("I - Inquire though inventory number")
print("P - Purchase or put your books in the cart")
print("C - Checkout")
print("S - Show all the books in the cart")
print("Re - Remove a book from the cart")
print("RA - Remove all books from the cart/Empty your cart")
print("Q - Quit; any books in the cart will be automatically checked out when you quit")
print("help - See all functions")
print()

# A List to store the items purchased
shoppingcart=[]

r="a" # To keep the while loop running except for the situation of typing "q" or "Q"
total_price = 0 # setup for purchasing
Ifcheckout = 0 #To check if they have checked out

while(r!= "q" or r!= "Q"): #Unless press "q" or "Q", the loop will continue. 
    r = input("What would you like to do? >>> ")
    
    # the following parts show different functions:

    if(r == "q" or r =="Q"):
        break
        
    elif(r =="a" or r == "A"): #Add a book
        book_number = int(input("Enter inventory number: "))
        book_ISBN = int(input("Enter ISBN: "))
        book_Title = input("Enter title of the book: ")
        book_Author= input("Enter author of the book: ")
        book_Price = float(input("Enter price: "))
        book_Quantity = int(input("Enter quantity of the book: "))
        book_Sold = int(input("Enter the number that has been sold; if none, then enter 0: "))
        
        m = 0
        
        for i in range(0,len(ISBN)):
            if(book_number in ISBN):
                book_number += 1
                m = 1
        if(m == 1):
            print()
            print("That inventory number has already existed, the number will be changed into ", book_number)

        # Store the information in the separate dictionaries        
        ISBN.update({book_number: book_ISBN})
        Title.update({book_number:book_Title})
        Author.update({book_number:book_Author})
        Price.update({book_number:book_Price})
        Quantity.update({book_number:book_Quantity})
        Sold.update({book_number:book_Sold})

        print()
        print("Inventory number: ", book_number)
        print("ISBN: ",ISBN.get(book_number))
        print("Title: ", Title.get(book_number))
        print("Author: ", Author.get(book_number))
        print("Price: ",Price.get(book_number))
        print("Quantity: ",Quantity.get(book_number))
        print("Sold: ", Sold.get(book_number))
        print("The book has been successfully added to the inventory!")
        print()
        

    elif(r == "u" or r == "U"): #Update a book information
        print()
        book_number = int(input("Enter inventory number: "))
        if(book_number in ISBN):
            book_ISBN = int(input("Enter ISBN: "))
            book_Title = input("Enter title of the book: ")
            book_Author= input("Enter author of the book: ")
            book_Price = float(input("Enter price: "))
            book_Quantity = int(input("Enter quantity of the book: "))
            book_Sold = int(input("Enter the number that has been sold; if none, then enter 0: "))

            ISBN.update({book_number: book_ISBN})
            Title.update({book_number:book_Title})
            Author.update({book_number:book_Author})
            Price.update({book_number:book_Price})
            Quantity.update({book_number:book_Quantity})
            Sold.update({book_number:book_Sold})

            print("The information has been successfully updated. The updated information is as followed:")
            print()
            print("Inventory number: ", book_number)
            print("ISBN: ",ISBN.get(book_number))
            print("Title: ", Title.get(book_number))
            print("Author: ", Author.get(book_number))
            print("Price: ",Price.get(book_number))
            print("Quantity: ",Quantity.get(book_number))
            print("Sold: ", Sold.get(book_number))

        else:
            print("That inventory number does not exist, to add a book use A")
        print()

    elif(r == "R" or r == "r"):  # Remove a book 
        print()
        book_number = int(input("Enter inventory number: "))
        if(book_number in ISBN):
            Confirmation = input("Are you sure that you want to remove that item (Enter: y/n)? ")
            if(Confirmation == "y" or Confirmation =="Y"):

                ISBN.pop(book_number)
                Title.pop(book_number)
                Author.pop(book_number)
                Price.pop(book_number)
                Quantity.pop(book_number)
                Sold.pop(book_number)

                print("The book has been successfully removed!")

            print()

        else:
            print("Sorry, we don't have such book in the system!")
            print()

    elif(r == "V" or r == "v"): # View all the books
        print ("ID".ljust(3) + "ISBN".ljust(14) + "Title".ljust(30) + "Author".ljust(15) + "Price".ljust(6) \
             + "Qty".ljust(4) + "Sold".ljust(4))
        for i in range(0, len(ISBN)):
            view_book = (str(i+1).ljust(3) + str(ISBN[i+1]).ljust(14) + str(Title[i+1]).ljust(30)[:30] + \
                str(Author[i+1]).ljust(15)[:15] + str(Price[i+1]).ljust(6) + \
                    str(Quantity[i+1]).ljust(4) + str(Sold[i+1]).ljust(4))
            print (view_book)
        print()

    # Get the information of the book through one of the four methods: inventory number/ISBN/Title/Author
    elif(r == "I" or r == "i"):
        print()
        print("By which one would you like to search for the information:")
        print("1. Inventory number")
        print("2. ISBN")
        print("3. Title")
        print("4. Author")
        print()
        search = int(input("Enter the number: "))
        
        if search == 1:
             book_number = int(input("Enter inventory number: "))
             if(book_number in ISBN):
                  print()
                  print("Here is the information you are looking for: ")
                  print()
                  print("Inventory number: ", book_number)
                  print("ISBN: ",ISBN.get(book_number))
                  print("Title: ", Title.get(book_number))
                  print("Author: ", Author.get(book_number))
                  print("Price: ",Price.get(book_number))
                  print("Quantity: ",Quantity.get(book_number))
                  print("Sold: ", Sold.get(book_number))
                  if(Quantity.get(book_number)<3 and Quantity.get(book_number)!=0):
                       print("Only ",Quantity.get(book_number)," remaining! Hurry!")
                  print()
             else:
                  print("Sorry we don't have such a book!")
                  print()
        if search == 2: 
             ISBN_number = int(input("Enter ISBN number: "))
             for isbns in ISBN.items():  # Through ISBN, search the ID (inventory nubmer) in the dictionary.
                  if isbns[1] == ISBN_number:
                       book_number = isbns[0]
             if(book_number in ISBN):
                  print()
                  print("Here is the information you are looking for: ")
                  print()
                  print("Inventory number: ", book_number)
                  print("ISBN: ",ISBN.get(book_number))
                  print("Title: ", Title.get(book_number))
                  print("Author: ", Author.get(book_number))
                  print("Price: ",Price.get(book_number))
                  print("Quantity: ",Quantity.get(book_number))
                  print("Sold: ", Sold.get(book_number))
                  if(Quantity.get(book_number)<3 and Quantity.get(book_number)!=0):
                       print("Only ",Quantity.get(book_number)," remaining! Hurry!")
                  print()
             else:
                  print("Sorry we don't have such a book!")
                  print()

        if search == 3: # Search the book through part of the title 
             search_book_results = []
             Title_name = input("Enter Title name: ")
             for titles in Title.items():  
                  if Title_name in titles[1]:
                       search_book_results.append(titles[0])  # Can get all results with the titles containing searched text
             if search_book_results != []:
                  print()
                  print("Here is the information you are looking for: ")
             for book_number in search_book_results:  # This runs only when the list is not empty.
                  print()
                  print("Inventory number: ", book_number)
                  print("ISBN: ",ISBN.get(book_number))
                  print("Title: ", Title.get(book_number))
                  print("Author: ", Author.get(book_number))
                  print("Price: ",Price.get(book_number))
                  print("Quantity: ",Quantity.get(book_number))
                  print("Sold: ", Sold.get(book_number))
                  if(Quantity.get(book_number)<3 and Quantity.get(book_number)!=0):
                       print("Only ",Quantity.get(book_number)," remaining! Hurry!")
                  print()
             if search_book_results == []:
                  print()
                  print("Sorry we don't have such a book!")
                  print()

        if search == 4: 
             search_book_results = []
             Author_name = input("Enter Author name: ")
             for authors in Author.items():
                  if Author_name in authors[1]:
                       search_book_results.append(authors[0]) # Can get all results with the titles containing searched text
             if search_book_results != []:
                  print()
                  print("Here is the information you are looking for: ")
             for book_number in search_book_results: # This runs only when the list is not empty.
                  print()
                  print("Inventory number: ", book_number)
                  print("ISBN: ",ISBN.get(book_number))
                  print("Title: ", Title.get(book_number))
                  print("Author: ", Author.get(book_number))
                  print("Price: ",Price.get(book_number))
                  print("Quantity: ",Quantity.get(book_number))
                  print("Sold: ", Sold.get(book_number))
                  if(Quantity.get(book_number)<3 and Quantity.get(book_number)!=0):
                       print("Only ",Quantity.get(book_number)," remaining! Hurry!")
                  print()
             if search_book_results == []:
                  print()
                  print("Sorry we don't have such a book!")
                  print()

    elif(r=="P" or r=="p"): # Purchase a book/ Put a book in a cart
        print()
        book_ISBN_input = int(input("Enter book ISBN: "))
        for isbns in ISBN.items():
            if isbns[1] == book_ISBN_input:
                book_number = isbns[0]
        if(book_number in ISBN):
            if(Ifcheckout == 1):
                Ifcheckout = 0 # Mark the cart is not empty.
            Quantity_current = Quantity.get(book_number)
            if(Quantity_current > 0):
                Quantity_current = Quantity.get(book_number)
                Quantity[book_number] = Quantity_current - 1 # Change the quantity in the record
                Sold_current = Sold.get(book_number)
                Sold[book_number] = Sold_current + 1 # Change the "Sold" in the record
                book_price = Price.get(book_number)
                total_price = total_price + book_price # Calculate the price
                print(Title.get(book_number),"added to your cart: ","$", book_price)
                shoppingcart.append(book_number) # Mark the ID of the book in the cart/put the book in the cart
            else:
                print("Sorry! We don't have the book in the inventory!")
        else:
                print("Sorry! We don't have such a book!")
        print()

    elif(r == "C" or r == "c"):
        print()
        print("The following books are in the cart: ")
        print()
        for books_ID in shoppingcart:  # iterate the book information from the cart
             print(str(ISBN[books_ID]).ljust(14)[:14], Title[books_ID].ljust(30), Author[books_ID].ljust(15)[:15], str(Price[books_ID]).ljust(6))
        print()
        print("Total before tax: $",round(total_price,2))
        tax= round(0.08875 * total_price,2)
        print("Tax is 8.875%: $", tax)
        total = round(total_price + tax,2) 
        print("Grand Total is: $", total)
        print()
        print("You can still purchase books after check out, your cart has been reset. To quit press q")
        print()

        # Record in the receipt
        ReceiptUnpack.write("Receipt. Checkout time: ")
        ReceiptUnpack.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        ReceiptUnpack.write("\n\nItems: \n\n")
        for books_ID in shoppingcart:
             ReceiptUnpack.write(str(ISBN[books_ID]).ljust(14)[:14] + Title[books_ID].ljust(30) \
                  + Author[books_ID].ljust(15)[:15] + str(Price[books_ID]).ljust(6) + "\n")
        ReceiptUnpack.write("\nTotal before tax: $" + str(round(total_price,2)) + "\t" + "Grand Total is: $" + str(total))
        ReceiptUnpack.write("\n=====================================================================\n \n")
        
        # Reset the data
        total_price = 0
        Ifcheckout = 1 # Mark the cart is empty
        shoppingcart = [] #Empty the cart

    elif( r =="help"):
        print()
        print("Help Centre")
        print("Welcome to GMC bookstore inventory system")
        print()
        print()
        print("You can do the following functions by entering relevant letter(s)")
        print("A - Add a book to the inventory")
        print("R - Remove a book from the inventory")
        print("U - Update details of a book")
        print("V - View all the books in the inventory")
        print("I - Inquire though inventory number")
        print("P - Purchase or put your books in the cart")
        print("C - Checkout")
        print("S - Show all the books in the cart")
        print("Re - Remove a book from the cart")
        print("RA - Remove all books from the cart/Empty your cart")
        print("Q - Quit; any books in the cart will be automatically checked out when you quit")
        print()
        print("If you have any other questions or concerns please contact the manager.")
        print()

    elif(r == "re" or r == "Re"):#Remove one item in the cart.
        print()
        print("Now you have following book(s) in your cart:")
        print()
        for books_ID in shoppingcart:
             print(str(ISBN[books_ID]).ljust(14)[:14], Title[books_ID].ljust(30), Author[books_ID].ljust(15)[:15], str(Price[books_ID]).ljust(6))
        print()
        Confirmation = input("Are you sure you want to remove an item from the cart (Enter: y/n)? ")
        if(Confirmation == "y" or Confirmation == "Y"):
            book_number = int(input("Enter inventory number to remove the book from the cart: "))
            if(book_number in shoppingcart):
                Quantity_current = Quantity.get(book_number)
                Quantity[book_number] = Quantity_current + 1
                Sold_current = Sold.get(book_number)
                Sold[book_number] = Sold_current - 1
                book_price = Price.get(book_number)
                total_price = total_price - book_price
                j=0
                for i in range(0,len(shoppingcart)): #To find the index of the part in the list cart
                    if(i == book_number):
                        j=i
                shoppingcart.pop(j)
                print()
                print(Title.get(book_number),"  has been removed from the cart.")
                print()
            else:
                print()
                print("That item is not in your cart!")
                print()

    elif(r == "ra" or r == "Ra" or r == "RA"):#Remove all books in the cart
         shoppingcart=[]

    elif(r == "s" or r =="S"): #Show all the books in the cart 
        print()
        print("You have following books in your cart:")
        print()
        for books_ID in shoppingcart:
             print(str(ISBN[books_ID]).ljust(14)[:14], Title[books_ID].ljust(30), Author[books_ID].ljust(15)[:15], str(Price[books_ID]).ljust(6))
        print()

#Outputs total if the user quits without checking out
if(total_price > 0 and Ifcheckout == 0):
    print()
    print("You bought the following books: ")
    for books_ID in shoppingcart:
        print(str(ISBN[books_ID]).ljust(14)[:14], Title[books_ID].ljust(30), Author[books_ID].ljust(15)[:15], str(Price[books_ID]).ljust(6))
        print()
    print("Total before tax: $", round(total_price, 2))
    tax= round(0.08875*total_price,2)
    print("Tax is 8.875%: $", tax)
    total = round(total_price + tax , 2)
    print("Grand total is $", total)

     # Record in the receipt
    ReceiptUnpack.write("Receipt. Checkout time: ")
    ReceiptUnpack.write(now.strftime("%Y-%m-%d %H:%M:%S")) #Record current time
    ReceiptUnpack.write("\n\nItems: \n\n")
    for books_ID in shoppingcart:
         ReceiptUnpack.write(str(ISBN[books_ID]).ljust(14)[:14] + Title[books_ID].ljust(30) \
              + Author[books_ID].ljust(15)[:15] + str(Price[books_ID]).ljust(6) + "\n")
    ReceiptUnpack.write("\nTotal before tax: $" + str(round(total_price,2)) + "\t" + "Grand Total is: $" + str(total))
    ReceiptUnpack.write("\n=====================================================================\n \n")

print()
print("Thank you for using the GMC bookstore inventory system")


#Write the updated inventory to the file
Unpack = open ("booklist.tsv" , "w")
totalnumber_items = len(ISBN)

data_to_save = []
for i in range(0,totalnumber_items):
     data_to_save.append({"ID":str(i+1), "ISBN": str(ISBN[i+1]), "Title": str(Title[i+1]),\
           "Author": str(Author[i+1]), "Price": str(Price[i+1]), \
                "Quantity": str(Quantity[i+1]), "Sold": str(Sold[i+1])})

BooksPack = csv.DictWriter(Unpack, fieldnames = ["ID", "ISBN", "Title", "Author", "Price", "Quantity", "Sold"], delimiter = '\t')
BooksPack.writeheader()
for row in data_to_save:
     BooksPack.writerow(row)

Unpack.close()
ReceiptUnpack.close()






