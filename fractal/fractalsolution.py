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

    for i in range(n-1):
        c = points[i+1]-points[i]
        segments.append(c)
        segmentFractions.append(abs(c))
        totalLength+=abs(c)
    segmentFractions = [x/totalLength for x in segmentFractions]

    #tools to account for the distance the fractal spans and the angle of the fractal as a whole
    directionfixer=(points[-1]-points[0]).conjugate()
    totalspan = abs(directionfixer)
    directionfixer=directionfixer/totalspan

    #traverse the fractal
    fmissing=f
    position = points[0]

    ffactor= 1
    pfactor= 1
    
    for depth in range(d):
        for i in range(n-1):
            #check if the next segment overshoots where we want to go and if not go the whole segment
            if fmissing > segmentFractions[i]*ffactor:
                fmissing -=segmentFractions[i]*ffactor
                position += segments[i]*pfactor
            #if we cannot go a full segment more and it is not the final iteration jump to the next layer of depth
            elif depth < d-1:
                ffactor *=segmentFractions[i]
                pfactor *=segments[i]/totalspan*directionfixer
                break
            #at the end go the remaining fraction out along the current segment
            else:
                position += fmissing *segments[i]*pfactor/(segmentFractions[i]*ffactor)
                break
    print(position.real, position.imag)


