while True:	
	f=open("shift_no.txt","r")
	shift=int(f.readline())

	inp=input("decrypted caesar of: ")
	awaw=list(inp)
	letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	
	for n,letter in enumerate(awaw):
		if letter in letters:
			no=letters.index(letter)
			no=no-shift
			if no<0:
				no=26+no
			awaw[n:n+1]=letters[no]
	
	joined=''.join(awaw)+"\n "
	print(joined)