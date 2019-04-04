print('vnesi dve števili in jih bom zdelil med sabo')
print('ko nehate vnašati števila, se deljenje konča')
print('deljenje z ničlo prekine zanko')
while True:
    try:
      a = int(input())
      b = int(input())
      c = a/b
      print(c)
    except:
      print('niste vnesli stevila')
      break
