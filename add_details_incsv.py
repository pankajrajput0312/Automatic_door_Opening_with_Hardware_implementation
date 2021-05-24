from csv import writer


def add_details(Name, unique_id, email_id, phone_no):
    list_of_elem = [unique_id, Name, email_id, phone_no]
    from csv import writer
    # Open file in append mode
    with open("valid_person_data/data.csv", '+a') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        write_obj.close()


def get_date_time():
    import datetime
    x = datetime.datetime.now()
    x = str(x)
    date = x.split(" ")[0]
    time = x.split(" ")[1].split(".")[0]
    return (date, time)


def update_incoming_list(Name, unique_id, email_id, phone_no):
    date, time = get_date_time()
    list_of_elem = [date, time, Name, unique_id, email_id, phone_no]
    with open("./Entry/"+date+".csv", 'a') as write_obj:
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        write_obj.close()


if __name__ == "__main__":
    add_details("anand", "456", "anand_fake_mail@gmail.com", "9876544321")

    # update_incoming_list(
    #     "Pankaj", "312", "pankajrajput020010@gmail.com", 9315630275)
