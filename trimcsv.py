import csv

file_handler = open('./ExcelTest.csv','r')
file_handler_write = open('./ExcelTest_New.csv','w')

csv_reader = csv.reader(file_handler,delimiter=',')
csv_writer = csv.writer(file_handler_write,delimiter=',')


twitter_handle_col = 2 # set the twitter handle column here

for line in csv_reader:
    del line[twitter_handle_col]
    csv_writer.writerow(line)

file_handler_write.close()
file_handler.close()