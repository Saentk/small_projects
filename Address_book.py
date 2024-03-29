import csv
import os


# my first code that I wrote after reading the "Byte of Python" book

d = dict()
file_dir = 'C:\\Test'
file_name = file_dir + os.sep + "adress_book.csv"                 # I like csv files, it`s easy to work with them
if not os.path.exists(file_dir):
    os.mkdir(file_dir)
if not os.path.exists(file_name):
    with open(file_name, 'w'):
        pass

def read_file():                                # There is no point to explain what is it)
    with open(file_name) as f:
        reader = csv.reader(f)
        for x in reader:
            if not len(x) == 0:
                a, b = x
                b = int(b)
                d[a] = b

def writer_func():                            # some functions need to re-write file
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        for key, value in d.items():
            l = [key, value]
            writer.writerow(l)

def main(): 
    choice = input('i = info, a = add, c = change, ai = all info, d = delete, y = break : ').lower()    

    if choice == 'i':             # to show info about a certain contact
        name = input('Contact name: ')
        if name in d:
            print(name, ':', d[name])
        else:
            print('there is no contact {}'.format(name))

    elif choice == 'a':                  # to add new contacts
        name = input("Enter a name: ")  
        try:
            number = int(input('Enter a number: '))
        except:
            print('Only integers allowed!')
        else:
            with open(file_name, 'a') as f:
                l = [name, number]
                writer = csv.writer(f)
                writer.writerow(l)
            print('Done! New contact: {}, number: {}'.format(name, number))
            read_file()

    elif choice == 'c':   # to change info about the contact
        name = input("Enter a name: ")
        if name in d:
            try:
                new_number = int(input('Enter a number: '))
            except:
                print('Only integers allowed!')
            else:
                d[name] = new_number
                writer_func()

    elif choice == 'ai':             # to see all contacts and their numbers
        for key, value in d.items():
            print(key, ':', value)
        if d == {}:
            print('there is no contacts yet, add some')
        

    elif choice == 'd':                  # to delete a contact
        name = input('Contact name: ')
        if name in d:
            del d[name]                 
            print('done!')
            writer_func()
        else:
            print('there is no contact {}'.format(name))

    elif choice == 'y':               # to exit
        exit()

    else:
        print('Choose one of options!')


if __name__ == '__main__':
    read_file()
    while True:
        main()

                             # that is my first code) don`t throw rocks at me)
