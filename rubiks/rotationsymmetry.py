""" Rotation and Turn Convension Class """__all__ = ["RotationSymmetry"]import numpy as npfrom .rotation import Turnclass RotationSymmetry:    def __repr__(self):        return f"RotationSymmetry(dim={self.dim}, global={self.global_rot_groups}, plane={self.plane_rot_groups})"        def __init__(self, nx: int, ny: int, nz: int):        """        # Cubic (N = 1)        # 1 x 1 x 1 ==> Global: [Z4 in x-hat, y-hat, z-hat]                # Cubic (N > 1)        # N x N x N ==> Local: [Z4 in x-hat with N layers ; Z4 in y-hat with N layers ; Z4 in z-hat with N layers]                # Cuboid (N > 1)        # N x 1 x 1 ==> Local: [Z4 in x-hat with N layers]  ;  Global: [Z2 in y-hat, z-hat]        # 1 x N x 1 ==> Local: [Z4 in y-hat with N layers]  ;  Global: [Z2 in x-hat, z-hat]        # 1 x 1 x N ==> Local: [Z4 in z-hat with N layers]  ;  Global: [Z2 in x-hat, y-hat]                # Cuboid (N > 1)        # 1 x N x N ==> Local: [Z2 in y-hat with N layers ; Z2 in z-hat with N layers]  ;  Global: [Z4 in x-hat]        # N x 1 x N ==> Local: [Z2 in x-hat with N layers ; Z2 in z-hat with N layers]  ;  Global: [Z4 in y-hat]        # N x N x 1 ==> Local: [Z2 in x-hat with N layers ; Z2 in y-hat with N layers]  ;  Global: [Z4 in z-hat]                # Cuboid (N, M > 1, M != N)        # 1 x N x M ==> Local: [Z2 in y-hat with N layers ; Z2 in z-hat with M layers]  ;  Global: [Z4 in x-hat]        # 1 x M x N ==> Local: [Z2 in y-hat with M layers ; Z2 in z-hat with N layers]  ;  Global: [Z4 in x-hat]        # N x 1 x M ==> Local: [Z2 in x-hat with N layers ; Z2 in z-hat with M layers]  ;  Global: [Z4 in y-hat]        # M x 1 x N ==> Local: [Z2 in x-hat with M layers ; Z2 in z-hat with N layers]  ;  Global: [Z4 in y-hat]        # N x M x 1 ==> Local: [Z2 in x-hat with N layers ; Z2 in y-hat with M layers]  ;  Global: [Z4 in z-hat]        # M x N x 1 ==> Local: [Z2 in x-hat with M layers ; Z2 in y-hat with N layers]  ;  Global: [Z4 in z-hat]                # Cuboid (M != N, M, N > 1)        # M x N x N ==> Local: [Z4 in x-hat with M layers ; Z2 in y-hat with N layers ; Z2 in z-hat with N layers]        # N x M x N ==> Local: [Z2 in x-hat with N layers ; Z4 in y-hat with M layers ; Z2 in z-hat with N layers]        # N x N x M ==> Local: [Z2 in x-hat with N layers ; Z2 in y-hat with N layers ; Z4 in z-hat with M layers]                # Cuboid (M != N != P, M, N, P > 1)        # N x M x P ==> Local: [Z2 in x-hat with N layers ; Z2 in y-hat with M layers ; Z2 in z-hat with P layers]        """        # Determine rotation options        dim = np.array([nx, ny, nz])        dim_freq = np.unique(dim, return_counts=True)        dim_freq = dict(zip(dim_freq[0], dim_freq[1]))                Z1 = []        Z2 = [Turn(2)]        Z4 = [Turn(1), Turn(2), Turn(-1)]        if dim_freq.get(1) == 3 and len(dim_freq) == 1:  # 1 x 1 x 1 Cube            global_rot_groups = ["Z4", "Z4", "Z4"]            plane_rot_groups = ["Z1", "Z1", "Z1"]        elif dim_freq.get(1) == 2 and len(dim_freq) == 2:  # N x 1 x 1 (cyclic)            global_rot_groups = ["Z4" if idx in np.where(dim > 1) else "Z2" for idx in range(len(dim))]            plane_rot_groups = ["Z4" if idx in np.where(dim > 1) else "Z1" for idx in range(len(dim))]        elif dim_freq.get(1) == 1 and len(dim_freq) == 2:  # N x N x 1 (cyclic)            global_rot_groups = ["Z4" if idx in np.where(dim == 1) else "Z2" for idx in range(len(dim))]            plane_rot_groups = ["Z1" if idx in np.where(dim == 1) else "Z2" for idx in range(len(dim))]        elif dim_freq.get(1) == 1 and len(dim_freq) == 3:  # N x M x 1 (cyclic)            global_rot_groups = ["Z4" if idx in np.where(dim == 1) else "Z2" for idx in range(len(dim))]            plane_rot_groups = ["Z1" if idx in np.where(dim == 1) else "Z2" for idx in range(len(dim))]        elif dim_freq.get(1) is None and len(dim_freq) == 1:  # N x N x N (cyclic)            global_rot_groups = ["Z4", "Z4", "Z4"]            plane_rot_groups = ["Z4", "Z4", "Z4"]        elif dim_freq.get(1) is None and len(dim_freq) == 3:  # N x M x P (cyclic)            global_rot_groups = ["Z2", "Z2", "Z2"]            plane_rot_groups = ["Z2", "Z2", "Z2"]        else:            raise ValueError(f"An object with dimension [{dim}] is not currently available: {dim_freq}")        self.dim = dim        self.global_rot_groups = global_rot_groups        self.plane_rot_groups = plane_rot_groups        self.group_rotations = dict(zip(["Z1", "Z2", "Z4"], [Z1, Z2, Z4]))    def get_group_rotations(self, group: str):        rotations = self.group_rotations.get(group)        assert isinstance(rotations, list), f"group [{group}] is not a valid rotation group"        return rotations