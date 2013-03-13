#Takes codex and converts to a transition factor
def LinExt(codex):
	ListCode = list(codex)
	if len(ListCode) != 7:
		return False
	elif len(ListCode) == 7:
		pass
		
	op = 0
	if ListCode[1] == 'a':
		op = ''
	elif ListCode[1] == 's':
		op = '-'
	else:
		return False
	
	tranTemp = op + str(ListCode[2]) + str(ListCode[5])
	tran = int(tranTemp)
	return tran