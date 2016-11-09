import os,time,subprocess,pyautogui

filePath="HappyBirthday.mp3"
waitingTime=3
screenWidth=130
screenHeigth=58
timeskip=.01
cakeWidth=101 # has to be smaller then screenWidth
cakeHeigth=30
candleNum=11 # (candleNum-1) has to divide (cakeWidth-candleNum)

def processString(string):
	result=[""]*universalHeight
	for i in range(universalHeight):
		for character in string:
			result[i]+=alphabet[character][i]
	return result

def processMessage(stringLines):
	result=[]
	maxLength=0
	for line in stringLines:
		maxLength=max(maxLength,len(line))
	for line in stringLines:
		result.append(processString(" "*((maxLength-len(line))//2)+line))
	return result

def getCake(flameState):
	flames=[".  "," . ","  ."]
	cake=["",]
	cake.append((" "*((screenWidth-cakeWidth)//2)+(flames[flameState%3]+" "*((cakeWidth-candleNum)//(candleNum-1)-2))*candleNum)[1:])
	cake.append(" "*((screenWidth-cakeWidth)//2)+("|"+" "*((cakeWidth-candleNum)//(candleNum-1)))*candleNum)
	cake.append(" "*((screenWidth-cakeWidth)//2)+"-"*cakeWidth)
	for i in range(cakeHeigth):
		if i%2==0:
			cake.append(" "*((screenWidth-cakeWidth)//2)+"|"+" "*(cakeWidth-2)+"|")
		else:
			cake.append(" "*((screenWidth-cakeWidth)//2)+"|"*cakeWidth)
	cake.append(" "*((screenWidth-cakeWidth)//2)+"-"*cakeWidth)
	return cake

def display(messageLines,distance):
	maxLength=0
	for bigLine in messageLines:
		for smallLine in bigLine:
			maxLength=max(maxLength,len(smallLine))
	i=0
	direction=1
	while i>=0 and i+maxLength<=screenWidth-1:
		if i==screenWidth-maxLength-1:
			direction*=(-1)
		elif i==0 and direction==-1:
			direction=1
		cake=getCake(i)
		time.sleep(timeskip)
		os.system("cls")
		for line in cake:
			print(line)
		print("\n"*distance)
		for bigLine in messageLines:
			for smallLine in bigLine:
				print(" "*i+smallLine)
		i+=direction

myFile=open("figlet-alphabet.txt")
letterModel=["a","b","c","d","e","f","g","h","i","j","k","l","m",
			 "n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet={" ":["      "]*6}
universalHeight=6
lines=myFile.read().split("\n")
strokeInLine=[]
for line in lines:
	strokeInLine.append(line.split("; "))
for i in range(len(letterModel)):
	alphabet[letterModel[i]]=[]
	for line in strokeInLine:
		alphabet[letterModel[i]].append(line[i])

os.startfile(filePath)
time.sleep(waitingTime)
pyautogui.keyDown("alt")
pyautogui.keyDown("tab")
pyautogui.keyUp("alt")
pyautogui.keyUp("tab")
os.system("mode con:cols="+str(screenWidth)+" lines="+str(screenHeigth))
message=["happy birthday","qwerty"]
result=processMessage(message)
display(result,8)