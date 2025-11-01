def calculate_average(numbers):
    if not numbers:
        return 0
    
    total_sum = sum(numbers)
    return total_sum / len(numbers)

def find_max(numbers):
    if not numbers:
        return None
        
    return max(numbers)
