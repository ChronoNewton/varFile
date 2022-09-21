import time

from varFile import varFile
import json



keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



#varfile library
start_time = time.perf_counter()#here starts timer


data_varfile = varFile('../benchmark_assets/data.var')
data_varfile.Read_VarFile()

for x in keys:
    data_varfile.Get_Value_ByKey(x)


end_time = time.perf_counter()
duration = (end_time - start_time)
print('\n\nvarFile lib took duration:' + 
        '\n\tNanoSeconds:  ' + str(duration) +
        '\n\tMilliSeconds:  ' + str(duration/pow(10, 6)))#division of pow...to convert from nanoseconds to milliseconds




#json library
start_time = time.perf_counter()#here starts timer


file = open('../benchmark_assets/data.json')
  
json_data = json.load(file)
  
for x in keys:
    json_data[x]
  
file.close()


end_time = time.perf_counter()
duration = (end_time - start_time)
print('\n\nJSON lib took duration:' + 
        '\n\tNanoSeconds:  ' + str(duration) +
        '\n\tMilliSeconds:  ' + str(duration/pow(10, 6)))#division of pow...to convert from nanoseconds to milliseconds
