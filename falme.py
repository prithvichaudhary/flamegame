# function for removing common characters
# with their respective occurrences


def remove_match_char(list1, list2):

	for i in range(len(list1)):
		for j in range(len(list2)):

			# if common character is found
			# then remove that character
			# and return list of concatenated
			# list with True Flag
			if list1[i] == list2[j]:
				c = list1[i]

				# remove character from the list
				list1.remove(c)
				list2.remove(c)

				# concatenation of two list elements with *
				# * is act as border mark here
				list3 = list1 + ["*"] + list2

				# return the concatenated list with True flag
				return [list3, True]

	# no common characters is found
	# return the concatenated list with False flag
	list3 = list1 + ["*"] + list2
	return [list3, False]


