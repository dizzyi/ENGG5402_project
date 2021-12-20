import os
from  abc import ABC
import numpy as np
import matlab.engine

from symbolic import Get_functions

class SymbolicAdoptor(ABC):
    def ForwardKinematic(self,q):
        return np.asarray(self.fk(*q))

    def EndEffector(self,q):
        return np.asarray(self.eef(*q))
    
    def Orientation(self,q):
        return np.asarray(self.rot(*q))
    
    def Jacobian(self,q):
        return np.asarray(self.j(*q))
    
    def PesudoInverseJacobian(self,q):
        J = self.Jacobian(q)
        JT = J.transpose()

        JJT = np.matmul(J,JT)

        invJJT = np.linalg.inv(JJT)

        return np.matmul(JT,invJJT)
    

class MatlabAdoptor(SymbolicAdoptor):
    def __init__(self):
        self.eng = matlab.engine.start_matlab()

        GEN_CODE_PATH = os.path.join(os.getcwd(),"matlab","gen")

        self.eng.cd(GEN_CODE_PATH)
        
        print("Matlab Code Adoptor Ready")
        self.fk = self.eng.fk
        self.eef = self.eng.eef
        self.rot = self.eng.rot
        self.j = self.eng.Rjacobian

    

class PythonAdoptor(SymbolicAdoptor):
    def __init__(self):
        fk, eef, rot, j = Get_functions()
        self.fk  = fk
        self.eef = eef
        self.rot = rot
        self.j   = j

        
        print("Python Code Adoptor Ready")

    