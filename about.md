# Bookstore Inventory System (MVP and Documentation)

## Motive
I have worked for a bookstore of a ten-day conference twice; in that bookstore, we sell books to participants. The manager of the bookstore has an Excel of all the information of the books in the bookstore. When one buys a book, we manually record the sales in the printed version of the Excel file and charge them with an App called Square. This takes time for assistants to locate the relevant book in the Excel form and also sometimes easily leads to mistakes. This makes me want to have a programe to record the inventory of the bookstore and track the sales during the conference. 

## Difficulties
1. Interface: It is hard to find an appropriate platform to run the program. By platform, I mean I don't know which method/operation is best for me to carry out the functions I wanted. <br />
    (1) I tried csv and DictReader at first, but then I was troubled by the result it produces because I didn't know how to separate each variants in the csv by DictReader or do some searching method according to different categories. <br />
    (2) I also tried tkinter as my interface and sqlite3 as my database for a while, which provide me with a nice interface and strong capacities of storing data. Then I was not sure how to change specific items in the csv (e.g. quantity of a book). It seems that I still need to do it with dictionaries. <br />
    (3) I also tried pandas. It has a nice display of the information. But I think its strength--data analysis--is not the main function I needed here for my project.<br />
    (4) By looking at various models online, I finally decided to go back to the basics. To use Python and run the program in commandline/Git Bash. I also learned how to use DictReader and csv/tsv in the end. <br />

2. Different types of information to process. For example, at first when I use DictReader to import data from csv, I didn't know what the type of results I got (is it a list? a string? a dictionary?). Same problem also occurs when I use panda, sqlite3. Sometimes it takes time to figure out how to convert between different types of data. 

3. The rest are some minor issues. For example, I didn't know to do with Excel and the csv when encountering ISBN. When I opened csv with Excel and I made some changes to the file, it will automatically change the ISBN into an scientific approximation such as '9.7814E+12'. It creates trouble when I run the program in the csv. Another example would be I didn't make the printed version of the book information alighed according to different categories. In cases like these, I usually search online for the answers. As long as I can find the right words/terminologies to ask the question, I can often get what I needed. Patrick also helped me figure out some questions I needed to ask. 

## Learning

In addition to the programming knowledge I learned through the process, I also find the following method/practice helpful in my process of programming:

1. Listing "Must Have," "Should Have," "Could Have" is helpful in establishing a clear, focused goal of the project.

2. Finding the appropriate terms to ask the question.

3. Browsing various related/relevant models, and learning their programming langauge through these models. 

4. It is helpful to talk to Patrick about the project and issues I have in the project, who gave me some valuable specific suggestions in programming; It is also helpful to talk to my partner who has no knowledge of programming, but understands what I want to do and give some refreshing advice from a client's perspective to improve the product from the product's end. 

5. If the syntax of the code is too convoluted, sometimes there is a better simpler way to accomplish the task/goal.

## Next Step (Client Communication)
Although I'm pretty familiar with the needs and wants of the project, I want to talk to the bookstore manager about the project and will confirm with him if he has any further needs and wants. I will have a couple of test runs with him before we finally use this program in the bookstore. 

## Breakdown of the weeks (Process)
### Week 4/7-4/14
1. 2h create final projects file (bookstore), list the details of about.md, create a tentative booklist (csv) for testing. But don't know why in the author's categories, there is a pair of quotation marks. Really excited about this project. 
2. 3.5h Set up a barcode scanner; figuring out how to incorporate csv into a dictionary, how to search under csv.DictReader, but not wroking... Can print out the full list. Still working on the search function.
3. 4h work on the loops for the essential features of the inventory. Not sure if csv is a good idea to save the data. Still trying to figure out a way to mark down the sale without making the syntax too convoluted. 
4. 1.5h Plan to use sqlite3 as my database and tkinter as my interface.  


### Week 4/22-4/28
1. 1h pip install pandas; explore pandas; pandas is a very useful tool for csv. It has a nice display of the information. But the data analysis part is not what I needed here for my project.
2. 1h Study a bookstore inventory program I downloaded. It uses sqlite3 to manage the bookstore inventory
3. 2h learn sqlite3: https://docs.python.org/2/library/sqlite3.html I think sqlite3 will be my frame of the program. 
4. 4h programming with sqlite3, tkinter. Figure out the basics of an inventory system. Don't know if there's an easy way to import the information from csv to db? not sure how to display the data in a better way, like the data from pandas, also including the title line. next time I'll design the sell windows...

### Week 4/29 - 5/5
1. 1h Fix isbn search ... Title search / Author serach not working ...
2. 2.5h Build up an "Taking Order" pop-up window.
3. 1.5h Stuck in how to build up "Total price" // extracting information from the list(?) database?

### Week 5/6 - 5/12
1. 1.5h Testing how to convert csv to db, how to convert db into the dictionary format. trying to figure out a way to save the rows into a new data
2. 10h Back to basic Python, dictionary,  list. adjust and tune the program ...

### Week 5/13-5/19
1. 5h Adjust the program
    Question-1: when I open "tsv" with Excel, sometimes ISBN is changed into "9.7814E+12". Then it will authomatically be changed into approximation "9781000000000," which also causes error when I run the python file. "ValueError: invalid literal for int() with base 10: '9.7814E+12'"
    I found the question online: https://stackoverflow.com/questions/22647042/how-to-save-excel-columns-with-long-numbers-into-csv
    I tried the method of putting in "=9780998829036"; it works as long as I don't make any other changes in the file. If I directly edit the file, the problem occurs again. (Which was the reason why I favor the txt file at first.)

    It seems that the most doable method is:
    Excel is trying to "help" you by formatting the input values. To avoid this, **do not double-click the file to open it**. Instead, open the Data tab and in the Get External Data section, click on From Text. Tell to transform the column of ISBN as text, instead of number.

    If editing in the Excel (tsv file), one needs to save it as (txt, tab delimited) (then changes it into tsv file).
    Question-1 solved.

    Question-2:  how to store all the results in the for loop? If I get search for the two books by the same author. 
    Solution: Store the results in a list. Then run a for loop to iterate the elements in the list.
    Question-2 solved.

2. 3h Can print out all the receipts when one checks out and all the receipts are stored in the file. 

3. 1h Currently I want to work on a daily report. In a txt file, that presents the total number books sold; Grand Total gains. It also presents books sold by day (May 14, 15, 16, ...): number of books sold in total; total gain/income by day; Details of the book sold by day. I think it relates to the time. But I don't know how to do that. Especially, that is to say, for example, today's current total, etc. It seems to relate to a period of time. 
The form would be something like this:
Total number of books that are sold:
Grand Total: $

May 14, 2020
Number of books that are sold in total:
Total: $
Details of books sold:
Title of the book, daily sold number

May 15, 2020
Number of books that are sold in total:
Total: $
Details of books sold:
Title of the book, daily sold number



## Criteria

This program records the selling inventory of a bookstore. 

### MUST have
1. (Achieved) The program imports a list of items of books (isbn, title, author, price, quantity, sold).
2. (Achieved) Start to take order.  <br />
*For each order:*
3. (Achieved) The program gets the information from a barcode scanner (or type in isbn), tells the user the relevant information.  
4. (Achieved) Calculate the total amount of the money and show it to the user.
5. (Achieved) Press a button and ask for confirmation.
6. (Achieved) Mark down the number that is sold in the list.   <br />
*End of an order*
7. (Achieved) Would be able to export a new list of updated items of books.

### SHOULD have
1. (Achieved) Can cancel item that is created by mistake.  
2. (will include this function in the future) If the book is taken by the author themselves, the user should mark it down in the "taken" category, instead of "sold" category.
3. (Achieved) instead of using barcode scanner or typing in isbn, user can search for relevant information by typing in key words, because occasionally some items do not have a barcode or isbn.
4. (Achieved) Would be able to record new incoming items brought by authors in categories (isbn, title, author, price, quantity, sold).
5. (Achieved) Would be able to record new quantities of existing items brought by authors.
6. **(Working on)** Would be able to present the daily total and the daily sales of the books, and also the grand total. 


### COULD have
1. (Will include in the future) When customers come to buy more than one item, the user can type in the quantity.
2. (Will include in the future) the program can record the payment method: card/cash/check.
3. (Achieved) Can create a record of each order (with a booklist sold, time, (this part will be included in the future) payment method: card/cash/check)
4. (will include in the future) Some books are run by the bookstore; some are by consignment. Should be able to mark down these differences as a note for each item.
5. (It seems not an important goal at this moment) Author's name: Last name, first name.
6. (will see if this function is needed) The new added items should follow the previous list in alphabetical order.
7. (Not needed for now) python -- pandas  data frame
8. (To be determined if it is needed; need to talk to the real manager) Some of the information can be accessed via a public webpage. 
9. (Not needed for now) Use tkinter interface.  
10. (Not needed for now) Flask MVC
