import csv

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     for car in csv_reader:
#         # print(car)
#         print(f'{car[1]} {car[2]} costs {car[4]}')


# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     data_list = list(csv_reader)
#     print(data_list)

# with open('cars1.csv') as file:
#     csv_reader = csv.DictReader(file, delimiter=';')
#     # next(csv_reader)
#     for car in csv_reader:
#         # print(car)
#         print(f'{car["Make"]} {car["Model"]} is {car["Length"]} m')


# with open('students.csv', 'w') as file:
#     csv_write = csv.writer(file)
#     csv_write.writerow(['First name', 'Last name', 'Age'])
#     csv_write.writerow(['Jack', 'Black', '24'])
#     csv_write.writerow(['John', 'White', '19'])

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     make_model_list = []
#     for car in csv_reader:
#         make_model = [car[1], car[2]]
#         make_model_list.append(make_model)
#
# print(make_model_list)
#
# with open('cars_make_model.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     for row in make_model_list:
#         csv_writer.writerow(row)

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     with open('cars_make_model.csv', 'w') as file:
#         csv_writer = csv.writer(file)
#         for row in csv_reader:
#             csv_writer.writerow([row[1], row[2]])


with open('cars.csv') as file:
    csv_reader = csv.DictReader(file)
    # next(csv_reader)
    row_list = list(csv_reader)
# print(row_list)
    # for row in csv_reader:
    #     row_list.append(row)
    # # print(row_list)

with open('cars_make_model_dict.csv', 'w') as file2:
    headers_list = ['Make', 'Model']
    csv_writer = csv.DictWriter(file2, fieldnames=row_list[0])
    # csv_writer2 = csv.DictWriter(file2, fieldnames=csv_reader)
    csv_writer.writeheader()
    # print(csv_reader)
    for row in row_list:
        csv_writer.writerow({'Make': row['Make'], 'Model': row['Model']})
