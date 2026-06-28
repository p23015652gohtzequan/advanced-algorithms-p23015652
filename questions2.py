import time
class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    def __str__(self):
        return f"ID: {self.transaction_id} | {self.customer_name} | {self.product_name} | RM{self.amount} | {self.transaction_date}"

# Requirement 3: Dataset of 10 unsorted transactions
transactions = [
    Transaction(502, "Alice", "Laptop", 3500.00, "2023-10-01"),
    Transaction(105, "Bob", "Mouse", 50.00, "2023-10-02"),
    Transaction(999, "Charlie", "Keyboard", 150.00, "2023-10-03"),
    Transaction(234, "Diana", "Monitor", 600.00, "2023-10-04"),
    Transaction(876, "Eve", "USB Drive", 30.00, "2023-10-05"),
    Transaction(345, "Frank", "Webcam", 120.00, "2023-10-06"),
    Transaction(765, "Grace", "Headphones", 200.00, "2023-10-07"),
    Transaction(456, "Heidi", "Desk Mat", 40.00, "2023-10-08"),
    Transaction(654, "Ivan", "Chair", 450.00, "2023-10-09"),
    Transaction(111, "Judy", "Router", 180.00, "2023-10-10")
]


#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j <len(right):
        if left[i].transaction_id <= right[j].transaction_id:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j +=1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

#binary search
def binary_search(arr,target_id):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid =(low + high) //2
        if arr[mid].transaction_id == target_id:
            return mid
        elif arr[mid].transaction_id < target_id:
            low = mid+1
        else:
            high = mid-1
    return None

#linear search
def linear_search(arr,target_id):
    for item in arr:
        if item.transaction_id == target_id:
            return item
    return None


if  __name__ == '__main__':
    current_data =  transactions
    is_sorted = False
    while True:
        print("Transaction management system ")
        print("1. Display All Transactions")
        print("2. Sort Inventory (Merge Sort)")
        print("3. Search by ID (Binary Search)")
        print("4. Search by ID (Linear Search)")
        print("5. Exit System")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current  transactions: ")
            for t in current_data:
                print(t)
        elif choice == 2:
            start_t = time.perf_counter()
            current_data = merge_sort(current_data)
            end_t = time.perf_counter()

            is_sorted = True
            print("Sorted after Transactions: ")
            for t in current_data:
                print(t.transaction_id,end=" ")

            print(f"time: {end_t - start_t:.8f} second")

        #require use merge sort frist
        elif choice == 3:
            search_target = int(input("Enter transaction ID: "))
            start_t = time.perf_counter()
            found_record = binary_search(current_data,search_target)
            end_t = time.perf_counter()

            print("Binary Search time: ")
            if found_record :
                print("Target",search_target,"found at index",found_record)
            else:
                print("No such transaction")
            print(f"time: {end_t - start_t:.8f} second")

        elif choice == 4:
            search_target = int(input("Enter transaction ID: "))
            start_t = time.perf_counter()
            found_record = linear_search(current_data, search_target)
            end_t = time.perf_counter()

            print("Linear Search time: ")
            if found_record:
                print("Target", search_target, "found at index", found_record)
            else:
                print("No such transaction")
            print(f"time: {end_t - start_t:.8f} second")

        elif choice == 5:
            print("Exiting System")
            break
        else:
            print("Invalid Choice,PLease try again")




