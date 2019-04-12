class Beam_Simple():
    def __init__(self,name,L):
        self.name = name
        self.L = L
        self.loads = []
        self.SFD = []
        self.BMD = []
        self.R_a,self.R_b = 0,0
        self.reactions = [self.R_a,self.R_b]
        
    def unpack_load_position(self,pt_load):
        # P,L,a,b = self.unpack_load_position(self,pt_load)
        P = pt_load['load_value']
        L = self.L
        a = pt_load['distance_from_a']
        b = L-a
        return(P,L,a,b)
        
    def add_point_load(self,P,a):
        self.P = P
        self.a = a
        assert (0.0<=a and a<=self.L),f"Length must be between 0 m and input beam length:{self.L} m"
        load_labels = 'load_type,load_value,distance_from_a'.split(",")
        load_values = ('point',self.P,self.a)
        self.loads.append(dict(zip(load_labels,load_values)))
        
    def cal_reaction(self,pt_load,cumulative=False):
        P,L,a,b = self.unpack_load_position(pt_load)
        R_a, R_b = P*a/L , P*b/L   
        if cumulative:
            self.R_a += R_a
            self.R_b += R_b
            self.reactions = self.R_a , self.R_b
        else:
            print(R_a,R_b)
        
    def cal_all_reactions(self):
        for load in self.loads:
            if load['load_type'] == 'point':
                self.cal_reaction(load,cumulative=True)
    
    def cal_M_max(self,pt_load):
        P,L,a,b = self.unpack_load_position(self,pt_load)     
        M = P*a*b/L
        self.M_max = M
        
    def cal_M_at_x(self,pt_load,x):
        P,L,a,b = self.unpack_load_position(self,pt_load)     
        if a<=x:
            M = P*x*b/L
        else:
            M = P*x*a/L 

    def show_units(self):
        msg = """
        All units in SI
        Load: kN
        Length: meter"""

        print(msg)           
    