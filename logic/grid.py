class Grid():
    def __init__(self,N,M):
        
        self.N=N
        self.M=M
        self.map={}
        
    
        """GETTERS"""
    def get_N(self):
        return self.N
    def get_M(self):
        return self.M
    
    """SETTERS"""
    def set_N(self,nv_N):
        self.N = nv_N
    def set_M(self,nv_M):
        self.M = nv_M
    
        """ la fonction scan_around retourne les places possibles ou le bob peut se deplacer ( donne une vision )

        """

    def scan_around(self,position, distance):
        
        x, y = position
        positions_disponibles = []
        if distance == 1:
            for i, j in [(0, -1), (-1, 0), (1, 0), (0, 1)]: #la liste des coordonnees sert a donner des cordonnes qui sont pas en diagonale
                new_x = x + i
                new_y = y + j
                if 0 <= new_x < self.N and 0 <= new_y < self.N : 
                        
                        positions_disponibles.append((new_x, new_y))

        
        else:
            for i in range(-distance, distance + 1):
                for j in range(-distance, distance + 1):
                    new_x = x + i
                    new_y = y + j

                    # Vérification que la nouvelle position est à l'intérieur de la grille
                    # et que x et y diffèrent, excluant ainsi la diagonale lorsque la distance vaut 1
                    if 0 <= new_x < self.N and 0 <= new_y < self.N :
                        positions_disponibles.append((new_x, new_y))

        return positions_disponibles
    
    
        """ la fonction get_position permet de donner la position dans la grille d'un objet passe en parametres
        """
    def get_position(self,obj):
        
        for key, itms in self.map.items():
            for itm in itms:
                if id(itm) == id(obj):
                    return key  # Retourne les coordonnées (x, y) d'objet recherché
        return None  # Retourne None si l'objet n'est pas trouvé

        """
        #Retourne la liste des objets à la clé (x, y), ou une liste vide s'il n'y a pas d'objet à cet endroit
        """
    
    def get_items(self,x,y):
        position = (x, y)
        return self.map[position]  
       
        