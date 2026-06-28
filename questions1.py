import time

class Product:
    def __init__(self,med_id,name,price,item_type):
        self.med_id = med_id
        self.name = name
        self.price = price
        self.item_type = item_type

    def __str__(self):
        return f'{self.med_id},{self.name},{self.price},{self.item_type}'



class HashTable:
    #Requirement 1 Hash Table using Linear Probing
    def __init__(self,size):
        self.size = size
        self.table = [None]*size

    def hash_function(self,key):
        #hashing integer med_id
        return key % self.size

    def insert(self,item):
        key = item.med_id #med id like 101
        index = self.hash_function(key) #index array
        #variable is backup the index variablethi
        original_index = index

        #Linear Porbing for collision resolution
        while self.table[index] is not None:
            #if med_id is inside the slot == key
            if self.table[index].med_id == key:
                self.table[index] = item
                return

            #move to next slot
            index = (index+1)%self.size
            #if looping all,the table
            if index == original_index:
                print("Error: Hash table is full")
                return
        self.table[index] = item

    def search(self,key):
        index = self.hash_function(key)
        original_index = index

        #Proble to find the item
        while self.table[index] is not None:
            if self.table[index].med_id ==key:
                return self.table[index]

            index =(index +1)% self.size
            if index == original_index:
                break
        return None # Item not found

    def display(self):
        print("Current Hash Table")
        for i,item in enumerate(self.table):
            if item is None:
                print(f"{i} Empty")
            else:
                print(f"[{i} {item}]")
"""
#Questions 2
my_inventory = HashTable(5)

med1 = Product(101,"Panadol",12.50,"tablets")
med2 = Product(205,"Cough Syrup", 15.00,"syrup")
med3 = Product(211,'panadol plus',11,"tablets")
med4 = Product(212,'Vitamin B',11,"supplements ")
med5 = Product(213,'fish oil plus',11,"supplements ")
med6 = Product(104,"Vitamin C",12.50,"supplements ")

my_inventory.insert(med1)
my_inventory.insert(med2)
my_inventory.insert(med3)
my_inventory.insert(med4)
my_inventory.insert(med5)
my_inventory.insert(med6)

my_inventory.display()


#Questions 3 Command_line

while True:
    print("Select an option:")
    print("1 Display Product")
    print("2 Insert Product")
    print("3 Search Product")
    choice = input("Enter choice:")

    if choice == '1':
        my_inventory.display()
    elif choice == '2':
        new_id = int(input("Enter new id:"))
        new_name = input("Enter name:")
        new_price = float(input("Enter new price:"))
        new_item = input("Enter new item (tablets , syrup or supplements):")

        new_product = Product(new_id,new_name,new_price,new_item)
        my_inventory.insert(new_product)
        print("successful")

    elif choice == '3':
        search_id = int(input("Enter id"))

        found_item = my_inventory.search(search_id)

        if found_item is not None:
            print(found_item)
        else:
            print("No Item Found")

"""
#Question 4
my_inventory = HashTable(10000)
my_array = []

#insert data
for i in range(5000):
    new_product = Product(med_id = i, name=f"Medical_{i}", price =11 , item_type="tablets")
    my_inventory.insert(new_product)
    my_array.append(new_product)

#search  existing and non existing
target_existing = 4999
target_missing =9999

#Hash
start_time = time.perf_counter()
my_inventory.search(target_existing)
end_time =  time.perf_counter()
hash_time_exist =end_time - start_time
print(f"Hash Table found it in: {hash_time_exist:.8f} seconds")

start_time = time.perf_counter()
for item in my_array:
    if item.med_id == target_existing:
        break
end_time = time.perf_counter()
array_time_exist = end_time - start_time
print(f"1D Array found it in:   {array_time_exist:.8f} seconds")














