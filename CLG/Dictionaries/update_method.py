codes = {}
codes.update({"India":'In'})#insert or updates
print(codes)
# Method update can convert keyword arguments into key–value pairs to insert. The
# following call automatically converts the parameter name Australia into the string key
# 'Australia' and associates the value 'ar' with that key:
codes.update(Aus='ar')#it inserts

codes.update(Aus='au')#it updates
print(codes)
#Use update() for bulk updates or merging dictionaries.