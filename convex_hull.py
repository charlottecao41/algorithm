from copy import copy
import math
a=(1,2)
b=(3,6)
c=(5,4)
d=(4,4)
e=(1,1.1)

points=[a,b,c,d,e]
#util function to find if a point is on left or right side of a line
def isLeft(a,b,c):
  #0 colinear
  return (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])

#util function to find the edge where all points are at one side, this is O(n^2)
def find_edge(points):
    for i in range(len(points)):
        for j in range(i,len(points)):
            flag=False
            if i!=j:
                points_cp=copy(points)
                del points_cp[i]
                del points_cp[j]
                state=isLeft(points[i],points[j],points_cp[0])>0
                for p in points_cp:
                    if isLeft(points[i],points[j],p)>0==state:
                        pass
                    if isLeft(points[i],points[j],p)==0:
                        pass
                    else:
                        flag=True
                    break
                if flag== False:
                    return points[i],points[j]

#cos theta = A.B/(||A||.||B||)
def cos_inverse(a1,a2,p):
    a=(a1[0]-a2[0],a1[1]-a2[1])
    b=(p[0]-a2[0],p[1]-a2[1])
    return abs((a[0]*b[0]+a[1]*b[1])/math.sqrt(a[0]**2+a[1]**2)/math.sqrt(b[0]**2+b[1]**2))

def chs(points):
    p1,p2=find_edge(points)

    points.remove(p1)
    points.remove(p2)

    sequence=[p1,p2]

    iter=0
    while len(points)>0:
        max_val=0
        max_p=points[0]

        #Find max of angle, draw new line
        for p in points:
            if cos_inverse(p1,p2,p)>max_val:
                max_val=cos_inverse(p1,p2,p)
                max_p=p

        points.remove(max_p)
        sequence.append(max_p)
        p1=p2
        p2=max_p
        if iter==0:
            #Append this at the end
            points.append(sequence[0])

        #Once the line reach back to start, chs found, end program
        if max_p==sequence[0]:
            break
        iter=iter+1

    return sequence

print(f"convex hull perimeter of {points} is {chs(points)}")