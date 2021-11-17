log_file = open("um-server-01.txt") #we are opening the text file using open() function and assigned it to the variable log_file


# def sales_reports(log_file): #def is used to define a function called sales_reports and the log_file is passed in as an argument.
#     for line in log_file: # iterating line by line thorugh the .txt file object
#         line = line.rstrip()   #rstrip is a method that removes the whitespaces and any trailing characters at the end of  the string from each line
#         day = line[0:3] #calling the line of index 0 to index 3 
#         if day == "Mon": # here condition is given that data from specific day that is say "mon"from index 0 to index 3 should be pulled out.
#             print(line) # print the line of the specified day 


# sales_reports(log_file) #calling the function


def melon_orders(log_file):

    for column in log_file:


        if column[4] > 10:

            print(column)

melon_orders(log_file)


