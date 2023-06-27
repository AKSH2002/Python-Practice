def Remove(tuples):
	tuples = [t for t in tuples if t]
	return tuples

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'radha', '45'), ('',''),()]
print(Remove(tuples))
