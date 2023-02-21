import re

a = """
https://youtu.be/_q6GJ-MkFsg
https://www.youtube.com/watch?v=oivkC6vS9eM
https://youtu.be/gFHtdYfSENk
https://www.youtube.com/watch?v=Kiyp44wjqmI
https://youtu.be/nZcf3oXfz5https://youtu.be/_q6GJ-MkFsg
https://www.youtube.com/watch?v=oivkC6vS9eM
https://youtu.be/gFHtdYfSENk
https://www.youtube.com/watch?v=Kiyp44wjqmI
https://youtu.be/nZcf3oXfz5k
https://youtu.be/gRkyed5m0o0
https://youtu.be/69EsE-apy1E
https://youtu.be/XeLaiL9tk68
https://youtu.be/_kqQDCxRCzM
https://youtu.be/8ofCZObsnOo
https://youtu.be/VNdHd1asf9s
https://youtu.be/d_HlPboLRL8
https://youtu.be/ifv_ekpVCvk?list=LL
https://youtu.be/jg9uBEUXirA
https://youtu.be/tRAQEpRIcnk
https://youtu.be/RBumgq5yVrA
https://www.youtube.com/watch?v=GWvd_j-Cok0
https://www.youtube.com/watch?v=4O--jfWRQwo
https://youtu.be/i3N0uNoTLZk
https://youtu.be/N7VCLNBNJQs
https://youtu.be/HIF0st2mnCA
""".strip()

pattern = re.compile("http[a-z]://[a-z]+\.[a-z]{2,4}/?.*")


for i in pattern.finditer(a):
    x, b = i.span()
    print(a[a:b])
