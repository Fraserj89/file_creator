# File Creator
# This is my File Creation Project
# The idea is to create as many files or defined size as you like in a specified path.
import time
import os

# Define the number of files to create
n = 100000
for i in range (n):
# Define the size of file in Bytes e.g. 1024 * 1024 = 1MB
    size = 1024
# Create file in directory with name "i", which is the number of the file.
# Then append the file with an extension e.g. '.txt' then write the file.
    with open('C:/Users/Fraserj89/Documents/' + str(i) + '.txt', 'w') as fout:
# Now write the file with random data to the size defined above.
        fout.write(os.urandom(size))
# Define time to wait before creating the next file in seconds
    time.sleep(3)
# Print to console the name of the file created
    print (str(i) + ".txt created")
