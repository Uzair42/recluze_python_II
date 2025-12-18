import os 
import shutil
import tempfile
from contextlib import contextmanager   



try:
    

     # Get disk usage for the root directory
    # total, used, free = shutil.disk_usage("/")

    # print(f"Total: {total // (2**30)} GB")
    # print(f"Used: {used // (2**30)} GB")
    # print(f"Free: {free // (2**30)} GB")

    print(tempfile.gettempdir())
    tempDir= tempfile.mkdtemp()
    print("folder just created =",tempDir ,"exists =",os.path.exists(tempDir))

    with open (os.path.join(tempDir,"tempfile.txt"),'w') as f:
        print("temp file has been created , its name is : %s ",f.name)
        f.write("This is a temporary file.")

finally:
    shutil.rmtree (tempDir)
    print("folder removed =",tempDir ,"exists =",os.path.exists(tempDir))



# Example of a context manager using the contextlib.contextmanager decorator
@contextmanager
def managed_file(name, mode):
    try:
        f = open(name, mode)
       
        yield f
    finally:
        f.close()   

for i in range(20):
 with managed_file('example.txt', 'a') as f:
    f.write('Hello, World! \n')  
    print("File written successfully.")
    


with open("example.txt", 'r') as f :
    for line in f:
        print(line)