from numpy.core.arrayprint import printoptions
import openpyxl
import numpy as np
inv_file = openpyxl.load_workbook(
    "/Users/femitemiola/Documents/gitdoc/.venv/inventory.xlsx")
product_file = inv_file["Sheet1"]

product_per_supplier = {}
print(product_file.max_row)
# exercise 1
# for product_row in range(2, product_file.max_row+1):
#     supplier_name = product_file.cell(product_row, 4).value
#     # calculation of the number of product per supplier
#     if supplier_name in product_per_supplier:
#         # print(supplier_name) : Like if the value is 0 set is 1
#         current_num_product = product_per_supplier.get(supplier_name)
#         print(current_num_product)
#         product_per_supplier[supplier_name] = current_num_product + 1
#     else:
#         # print("adding a new supplier")  Like if the value is 0 set is 1
#         product_per_supplier[supplier_name] = 1
# print(product_per_supplier)
# exercise 2
total_supplier_inv = {}
product_nums = {}
for product_row in range(1, product_file.max_row+1):
    supplier_name = product_file.cell(product_row, 4).value
    # print(supplier_name)
    inventory = product_file.cell(product_row, 2).value
    price = product_file.cell(product_row, 3).value

    # print(supplier_name)
    # print("--")
    # if supplier_name in product_per_supplier:
    # For dictionary to access the key of the dic, you have to first define and
    # print(supplier_name)
    # print("-----")

# #     # print(firstrow)

    if supplier_name in total_supplier_inv:
        current_total_value = total_supplier_inv.get(
            supplier_name)
        print(current_total_value)
        total_supplier_inv[supplier_name] = price * \
            inventory + current_total_value

    else:
        total_supplier_inv[supplier_name] = product_file.cell(
            product_row, 2).value * product_file.cell(product_row, 3).value

print(total_supplier_inv)

# # exercise 3
# for product_row in range(2, product_file.max_row+1):
#     supplier_name = product_file.cell(product_row, 4).value
#     inventory = product_file.cell(product_row, 2).value
#     product_num = product_file.cell(product_row, 1).value
#     # print(supplier_name)
#     # print("--")
#     # if supplier_name in product_per_supplier:
#     # For dictionary to access the key of the dic, you have to first define and
#     # print(supplier_name)
#     # print("-----")

#     # if supplier_name in product_per_supplier:
#     #     product_per_supplier[supplier_name] = product_per_supplier.get(
#     #         supplier_name)
#     if inventory < 10:
#         product_nums[product_num] = inventory
# print(product_nums)


# current_num_product = product_per_supplier.get(supplier_name)
# product_per_supplier[supplier_name] = current_num_product + 1
# else:
#      break
# print("adding a new supplier")s
# # product_per_supplier[supplier_name] = 1
# for product_row in range(2, product_file.max_row+1):
#     supplier_name = product_file.cell(product_row, 4).value
#     inventory = product_file.cell(product_row, 2).value
#     inventory_price = product_file.cell(product_row, 2)
#     price = product_file.cell(product_row, 5).value
#     # print(supplier_name)
#     # print("--")
#     # if supplier_name in product_per_supplier:
#     # For dictionary to access the key of the dic, you have to first define and
#     # print(supplier_name)
#     # print("-----")

#     inventory_price.value = inventory * price
# inv_file.save("invertorywithtotalvalue3.xlsx")
