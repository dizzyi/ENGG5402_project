import Adoptor
import numpy as np

adoptor = Adoptor.MatlabAdoptor()

q = [float(0) for _ in range(7)]

fk     = adoptor.ForwardKinematic(q)
eef    = adoptor.EndEffector(q)
rot    = adoptor.RotationMatrix(q)
J      = adoptor.RobotJacobian(q)
Jsharp = adoptor.PsudoInverseJ(q)

print("finish")