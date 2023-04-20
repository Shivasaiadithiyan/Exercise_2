"""
This module provides a class that represents a point object
whiich has  x and y coordinate as members and
Euclidean distance and k-nearest neighbours as
member functions.

This is a part of the exercises given under the 
course UIT2201 (Programming and Data Structures).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Fri Apr 14 2023

Revised on Sat Apr 18 2023

Original Author: S.Shiva sai adithiyan <shivasaiadithiyan2210687@ssn.edu.in>

$Id: 115571315$

"""


class Point:
    """
    A class to represent a Point.
    ...

    Attributes
    ------------
    _x : float
        x coordinate of a point in cartesian system.
    _y : float
        y coordinate of a point in cartesian system.
    
    Methods
    -----------

    distance()
        displays the Euclidean distance between two point objects.

    k_nn()
        displays the first k point objects which are close 
        to a patricular point object.
    
    """


    def __init__(self,coordinate_x=0,coordinate_y=0) -> None:
        self._x=coordinate_x
        self._y=coordinate_y
#end of constructor __init__().


    def distance (self,point2):
        """
        finds and returns the distance between
        two point objects

        self: point object
        point2: point object

        returns float if self and point2 are different
        point objects otherwise returns 0
        
        """
        if self._x != point2._x and self._y != point2._y:
            x_diff=(self._x-point2._x)**2
            y_diff=(self._y-point2._y)**2
            Euclidean_distance=(x_diff+y_diff)**0.5
            return Euclidean_distance

        else:
            return 0
#end of method distance().


    def k_nn(self,k,points_secquence):
        """
        finds and returns the first k nearest neighbours
        which are close to a point.

        self: point object 
        k: integer
        points_secquence: secquence of point objects.

        returns the first k nearest neighbours
        as a list of tuples.

        """
        #dictionary to store the points and their respective
        #distance from the common point object.
        point_distance={}
        for object in points_secquence:
            Euclidean_distance=self.distance(object)
            point_distance[(object._x,object._y)]=Euclidean_distance
        
        #sorting the dictionary accordint to distance
        sorted_distance=sorted(list(point_distance.values())) 
        sorted_coordinates=[]
        for distance in sorted_distance:
            for key in point_distance:
                if point_distance[key]==distance and key not in sorted_coordinates and (self._x,self._y) != key :
                    sorted_coordinates.append(key)
      

        k_nearest_coordinates = sorted_coordinates[0:k]
        return k_nearest_coordinates
#end of method k_nn().



if __name__=="__main__":

    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.
    while True:
        try:
            #secquence_of_points: a secquence to store point objects.
            secquence_of_points=[]

            num_of_points=int(input("Enter the total number of coordinates: "))
            for count in range(num_of_points):
                print("-"*40)
                coord_x=float(input(f"Enter x ordinate of point {count+1}: "))
                coord_y=float(input(f"Enter y ordinate of point {count+1}: "))
                
                my_point=Point(coord_x,coord_y)
                secquence_of_points.append(my_point)

            print("-"*40)
            print()
            number_of_nearest_points=int(input("Enter the number of nearest points to be found: "))
            start_x=float(input("Enter the starting point's x-coordinate: "))
            start_y=float(input("Enter the starting point's y-coordinate: "))
            Pnew=Point(start_x,start_y)
            k_nearest_neighbours=Pnew.k_nn(number_of_nearest_points,secquence_of_points)
            print(f"The {len(k_nearest_neighbours)} nearest neighbours near point {(Pnew._x,Pnew._y)} are ")
            print(f"{k_nearest_neighbours}")
            break

        except ValueError:
            print("Enter a Valid Input.")
            print()