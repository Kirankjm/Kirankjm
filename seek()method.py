with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())
  
  with open('file.txt','w') as f:
      f.write('oye, tum ho ki nhi')
  
  #with open('file.txt', 'r') as f:
with open('file.txt', 'r') as f:
     data = f.read()
     print(data)
     f.seek(10)  # Move to the 10th byte in the file
     data=f.read(5)   # Read the next 5 bytes
print(data)

with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)
  current_position = f.tell() # Save the current position
  print(f.seek(current_position))   # Seek to the saved position
