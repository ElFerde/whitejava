
javalist=[]
while(True):
	i = input("javakod: ")
	if i == "ä":
		break
	javalist.append(i)

ws=[]
while(True):
	i = input("whitespace: ")
	if i == "ä":
		break
	ws.append(i)

wsstring = "\n".join(ws)

for x in range(len(ws)):
	print(".")
	if ws[x] == "\t":
		ws[x] = "ö"

javastring = "".join(javalist)
javalist = javastring.split(" ")
newJava = ""
for j in range(0, len(javalist)):
    newJava += javalist[j]
    newJava += wsstring[j]
for j in range(len(javalist), len(ws)):
	newJava += wsstring[j]
	print("extra ws")
print("")
print("")
print(newJava)
print("")
print("")
print("replace 'ö' with tab")