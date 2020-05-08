# Bookstore Inventory Record

This program records the selling inventory of a bookstore. 

## MUST have
1. The program imports a list of items of books (isbn, title, author, price, quantity, sold).
2. Start to take order.  <br />
*For each order:*
3. The program gets the information from a barcode scanner (or type in isbn), tells the user the relevant information.  
4. Calculate the total amount of the money and show it to the user.
5. Press a button and ask for confirmation.
6. Mark down the number that is sold in the list.   <br />
*End of an order*
7. Would be able to export a new list of updated items of books.

## SHOULD have
1. Can cancel item that is created by mistake.  
2. If the book is taken by the author themselves, the user should mark it down in the "taken" category, instead of "sold" category.
3. instead of using barcode scanner or typing in isbn, user can search for relevant information by typing in key words, because occasionally some items do not have a barcode or isbn.
4. Would be able to record new incoming items brought by authors in categories (isbn, title, author, price, quantity, sold, taken).
5. Would be able to record new quantities of existing items brought by authors.


## COULD have
1. When customers come to buy more than one item, the user can type in the quantity.
2. the program can record the payment method: card/cash/check.
3. Can create a record of each order (with a booklist sold, time, payment method: card/cash/check)
4. Some books are run by the bookstore; some are by consignment. Should be able to mark down these differences as a note for each item.
5. Author's name: Last name, first name.
6. The new added items should follow the previous list in alphabetical order.
7. python -- pandas  data frame
8. Some of the information can be accessed via a public webpage. 
9. Use tkinter interface.  
10. Flask MVC
