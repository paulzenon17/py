import math

def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

if __name__=="__main__":
    r=input("Enter a radius:")
    r=float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")
    
     **Use this alternative easy code** 
    
    def circle_calc(a):
    area=(22/7)*a*a
    circum=2*(22/7)*a
    dia=2*a
    z1=f'\n{area}\n{round(circum)}\n{dia}'
    z2=print('The Area, Circumference & Diameter of the circle is:',z1)
    return z2
