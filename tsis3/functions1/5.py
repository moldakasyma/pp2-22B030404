def permute(s,res):
	if (len(s) == 0):
		print(res,end=" ")
		return

	for i in range(len(s)):
		char= s[i]
		left_substr = s[0:i]
		right_substr = s[i + 1:]
		ans = left_substr + right_substr
		permute(ans, res+char)



res=""
s = input()
permute(s,res)


