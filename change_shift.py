while True:
	shift=open("shift_no.txt","r")
	cur=shift.readline()

	inp=input("change shift into(current is "+cur+"): ")
	
	shiftw=open("shift_no.txt","w")
	shiftw.write(inp)
	shiftw.close()
	