import os

def read_half_of_large_file(file_path):
    with open(file_path, 'r') as file:
        file_size = os.path.getsize(file_path)
        chunk_size = int((file_size)/2)-5
        half_content = file.read(chunk_size)
        return half_content

# Example usage
file_path = 'numbers.txt'  # Replace with the actual file path
half_content = read_half_of_large_file(file_path)

# Print or do something with half of the content
print(half_content)
