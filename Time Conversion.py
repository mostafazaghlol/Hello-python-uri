secs=int(input())
hour=int(secs/3600)
rest=secs-(hour*60*60)
mins=int(rest/60)
rest2=rest-(mins*60)
secs=rest2
print("{0:.0f}".format(hour)+':'+"{0:.0f}".format(mins)+':'+"{0:.0f}".format(secs))