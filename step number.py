def is_step_number(num_str):
    return all(abs(int(num_str[i]) - int(num_str[i + 1])) == 1 for i in range(len(num_str) - 1))
    

def convert_and_find_step_numbers(N):
    step_numbers = []
    
    
    for base in range(2, 11):  # Convert N to bases 2 to 10
        converted = ""
        
        temp = N
        while temp > 0:
            converted = str(temp % base) + converted
            temp //= base
            print("converted is:",converted)
        
        if is_step_number(converted):
            step_numbers.append(converted)
    
    if step_numbers:
        for num in step_numbers:
            print(num)
    else:
        print(-1)
      
        


N = int(input().strip())

convert_and_find_step_numbers(N)
