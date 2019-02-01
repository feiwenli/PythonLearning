#对字符串进行对齐
d = {
	"lodDist":100.0,
	"SmallCull":0.04,
	"DistCull":500.0,
	"trilinear":40,
	"farclip":477
}

w = max( map (len , d.keys()))
print(w)
for x in d:
	#print(x.center(w),':',d[x])
	print(x.ljust(w),':',d[x])
	