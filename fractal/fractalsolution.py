import math
cases = int(input())

for _ in range(cases):
    points=[]
    n = int(input())
    for i in range(n):
        x,y = map(int, input().split())
        points.append(complex(x,y))

    d= int(input())
    f= float(input())

    # save segment data
    segments = []
    segmentFractions = []
    totalLength = 0
    directionfixer=(points[-1]-points[0]).conjugate()
    totalspan = abs(directionfixer)
    directionfixer=directionfixer/totalspan

    for i in range(n-1):
        c = points[i+1]-points[i]
        segments.append(c)
        segmentFractions.append(abs(c))
        totalLength+=abs(c)
    segmentFractions = [x/totalLength for x in segmentFractions]
    #print(segments, segmentFractions)
    #traverse the fractal
    fmissing=f
    position = points[0]

    ffactor= 1
    pfactor= 1
    
    for depth in range(d):
        for i in range(n-1):
            #print(fmissing, segmentFractions[i]*ffactor)
            #print(depth,i,position,segments[i]*pfactor)
            #print(ffactor)
            if fmissing > segmentFractions[i]*ffactor:
                fmissing -=segmentFractions[i]*ffactor
                position += segments[i]*pfactor
                #print(depth, position)
            elif depth < d-1:
                #print(depth,"landed on",i)
                ffactor *=segmentFractions[i]
                pfactor *=segments[i]/totalspan*directionfixer
                break
            else:
                position += fmissing *segments[i]*pfactor/(segmentFractions[i]*ffactor)
                break
    print(position.real, position.imag)


