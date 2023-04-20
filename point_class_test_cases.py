from point_class import Point
"""
Importing the user defined point class from
module point_class.

"""


import random
if __name__=="__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.


    secquence_of_points=[]
    num_of_points=random.randint(1,10)
    #getting a random number of points using random module.
    for count in range(num_of_points):
        coord_x=random.randint(-100,+100)
        coord_y=random.randint(-100,100)
        my_point=Point(coord_x,coord_y)
        secquence_of_points.append(my_point)
    

    print(f"The {num_of_points} random points are :")
    print("---------------------------------------------------------------------------------------")
    for object in secquence_of_points:
        print((object._x,object._y))
    print("---------------------------------------------------------------------------------------")

    number_of_nearest_neighbours=random.randint(1,10)
    _x_=random.randint(-100,100)
    _y_=random.randint(-100,100)
    Pnew=Point(_x_,_y_)
    k_nearest_neighbours=Pnew.k_nn(number_of_nearest_neighbours,secquence_of_points)
    print()
    print(f"The {len(k_nearest_neighbours)} nearest neighbours of point {(Pnew._x,Pnew._y)} are ")
    print("---------------------------------------------------------------------------------------")
    for object in k_nearest_neighbours:
        print(object)
    print()
    print("---------------------------------------------------------------------------------------")

   