markdown = "1. first\n2. second\n3. third"
block_list = markdown.split("\n")
print(block_list)

ol = True
i = 1 
for line in block_list:
    if(not line.startswith(f"{i}. ")):
            ol = False 
            break

    i += 1

if(ol):
    print("ol")
else:
    print("no ol")
