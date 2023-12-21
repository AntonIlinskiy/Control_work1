def warehouse_generator(num_warehouses, total_product):
    avg_product = total_product // num_warehouses
    remainder = total_product % num_warehouses

    for _ in range(num_warehouses - remainder):
        yield avg_product

    for _ in range(remainder):
        yield avg_product + 1


num_warehouses = 5
total_product = 100
warehouses = list(warehouse_generator(num_warehouses, total_product))
print(warehouses)
