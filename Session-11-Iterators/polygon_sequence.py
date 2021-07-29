from polygon import Polygon

class Polygon_sequence:

    def __init__( self, largest_num_edges, circumradius):

        if largest_num_edges < 3:
            raise ValueError("Polygon require atleast 3 or more edges/vertices!")

        self.largest_num_edges = largest_num_edges
        self.circumradius = circumradius
        self.sequence = [ Polygon( num_edges, self.circumradius) for num_edges in range( 3, self.largest_num_edges+1)]

    def __repr__( self) -> str:
        
        return f'Polygon sequence< number of polygons:{self.largest_num_edges-2}, largest polygon edges:{self.largest_num_edges}, common circumradius:{self.circumradius} >'

    def __len__( self):

        return self.largest_num_edges-2

    def __getitem__( self, vertex):

        if isinstance( vertex, int):
            if vertex < 3 or vertex > self.largest_num_edges:
                raise IndexError("Vertex index is out of sequence")
            else:
                return self.sequence[ vertex]
        else:
                start, stop, step = vertex.indices(self.largest_num_edges)
                rng = range( start, stop, step)
                return [ self.sequence[i] for i in rng]

    @property
    def max_efficiency(self):

        area_perimeter_ratio = [ p.area/p.perimeter for p in self.sequence]
        max_efficient = max(area_perimeter_ratio)
        vertex = area_perimeter_ratio.index(max_efficient)+3
        return f'Maximum efficint polygon having {vertex} edges and area to perimeter ratio is {max_efficient}'


    
