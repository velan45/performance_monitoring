import csv
import os
class Writer:

    def writer(self, my_dict, address):
        filename = address[0] + '.csv'
        key_list = my_dict.keys()
        header_list = []
        for item in key_list:
            header_list.append(item.strip())
            if os.path.exists(filename):
                write_option = 'a'
            else:
                write_option = 'w'

        with open(filename,mode=write_option,newline='') as filehandle:
            writing = csv.DictWriter(filehandle,fieldnames=header_list)
            if write_option=='w':
                writing.writeheader()
            else:
                writing.writerow(my_dict)






if __name__ == '__main__':
    my_dict={'name':'velan', 'age':'28'}
    address = ('127.0.0.1', 611253)
    my_writer = Writer()
    print(my_writer.writer(my_dict,address))