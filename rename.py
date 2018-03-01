import os
for fileName in os.listdir("."):
    os.rename(fileName, fileName.replace(".mod", ".txt"))
