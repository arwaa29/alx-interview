def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Starting with the first row

    for i in range(1, n):
        
        # Previous row
        prev_row = triangle[-1]
        
        # Create a new row, starting and ending with 1
        new_row = [1]
        
        # Fill the middle of the new row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        # End the row with 1
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle
