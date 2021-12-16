import matlab.engine
import os
import numpy as np

class MatlabAdoptor:
    def __init__(self):
        self.eng = matlab.engine.start_matlab()

        GEN_CODE_PATH = os.path.join(os.getcwd(),"matlab","gen")

        self.eng.cd(GEN_CODE_PATH)

        print("Matlab Code Adoptor Ready")
    
    def ForwardKinematic(self,q):
        return np.asarray(self.eng.fk(*q))

    def RobotJacobian(self,q):
        return np.asarray(self.eng.Rjacobian(*q))

    def RotationMatrix(self,q):
        return np.asarray(self.eng.rot(*q))

    def EndEffector(self,q):
        return np.asarray(self.eng.eef(*q))

    def PsudoInverseJ(self,q):
        J = self.RobotJacobian(q)
        JT = J.transpose()

        JJT = np.matmul(J,JT)

        invJJT = np.linalg.inv(JJT)

        return np.matmul(JT,invJJT)