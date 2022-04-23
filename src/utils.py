from csv import writer

def append_list_as_row(file_name, list_of_elem):
<<<<<<< HEAD
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
=======
    with open(file_name, 'a+', newline='') as file:
        for i in list_of_elem:
            if typeof(i) == list:
                for j in i:
                    # file.write(j)
                    input(j)
            file.write(i)
>>>>>>> dec456a (Initial commit)
