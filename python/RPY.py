from math import *
from sympy import *
from symbolic import Rotx, Roty, Rotz
########################################################################
# Roll Pitch Yaw Tool box

# Usage 
# desireOmega = DesireOmega(Rcurrent, Rtarget)

def DesireOmega(Rcurrent, RTarget):
    current = RPY(Rcurrent)
    target = RPY(RTarget)

    error = target - current

    return current.RPYomegaMatrix() * error.toMatrix()

def RPY2RM(roll, pitch, yaw):
  return Rotz(yaw) * Roty(pitch) * Rotx(roll)

def RM2RPY(R):
  beta = atan2(-R[3 - 1,1 - 1],sqrt( R[3 - 1,2 - 1] ** 2 + R[3 - 1,3 - 1] ** 2 ))

  alpha = atan2( R[3 - 1,2 - 1]/cos(beta),  R[3 - 1,3 - 1]/cos(beta) )

  gamma = atan2( R[2 - 1,1 - 1]/cos(beta), -R[1 - 1,1 - 1]/cos(beta) )

  return alpha, beta, gamma


class RPY:
    def __init__(self,R = None,r=None,p=None,y=None):
        if(R is not None):
            self.r, self.p, self.y = RM2RPY(R)
        else:
            self.r = r
            self.p = p
            self.y = y

    def __sub__(self,other):
        return RPY(
            None,
            self.r - other.r,
            self.p - other.p,
            self.y - other.y)
    
    def RPYomegaMatrix(self):
        beta = self.p
        gamma = self.y
        C1 = Rotz(gamma)* Roty(beta) * Matrix([[1],[0],[0]])
        C2 = Rotz(gamma) * Matrix([[0],[1],[0]])
        C3 = Matrix([[0],[0],[1]])

        return C1.row_join(C2).row_join(C3)
    
    def toMatrix(self):
        return Matrix([[self.r],[self.p],[self.y]])