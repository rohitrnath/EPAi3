from math import sin, cos, pi

class Polygon:
    def __init__( self, num_edges:int, circumradius:float):
        
        if num_edges < 3:
            raise ValueError("Polygon require atleast 3 or more edges/vertices!")
        
        self.num_edges = num_edges
        self.circumradius = circumradius

    def __repr__(self):
        return f'Polygon< edges:{self.num_edges}, circumradius:{self.circumradius} >'

    def __eq__( self, other:"Polygon class"):

        if isinstance( other, Polygon):
            return True if self.num_edges == other.num_edges and self.circumradius == other.circumradius else False

        else:
            raise TypeError("Objects must be of type Polygon!")

    def __gt__( self, other:"Polygon class"):

        if isinstance( other, Polygon):
            return True if self.num_edges > other.num_edges else False

        else:
            raise TypeError("Objects must be of type Polygon!")

    @property
    def interior_angle( self):
        return (self.num_edges - 2)*(180/self.num_edges)

    @property
    def edge_length( self):
        return 2*self.circumradius*sin( pi/self.num_edges)

    @property
    def apothem( self):
        return self.circumradius*cos( pi/self.num_edges)

    @property
    def area( self):
        return 0.5*self.num_edges*self.edge_length*self.apothem

    @property
    def perimeter( self):
        return self.num_edges*self.edge_length    
