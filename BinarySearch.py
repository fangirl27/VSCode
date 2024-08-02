import time

start = time.time()
input_str = input("Enter elements of the list separated by space: ")
arr = list(map(int, input_str.split()))  
no = int(input("Enter number to search in the list: "))
l = len(arr)
mid = l//2 #lower term in case of odd number of elements
left_ptr = 0
right_ptr = l-1
if arr[mid] == no:
    print(f"{no} exists at {mid} index")
else:
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr)//2
        if arr[mid] > no: #from index 0 to mid
            right_ptr = mid-1
        elif arr[mid] < no: #from mid+1 to l-1
            #mid = mid + mid//2
            left_ptr = mid + 1
        # if mid == 0 or mid == l-1:
        #     print("Number not in list")
        #     quit()
        if arr[mid] == no:
            print(f"Number found at {mid}")
            break

#print("Number not found")

end = time.time()
print(f"Time taken to binary search is: {end-start} milli-seconds")


