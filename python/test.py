import Adoptor
import numpy as np
import math

#adoptor = Adoptor.MatlabAdoptor()
adoptor = Adoptor.PythonAdoptor()

q = [math.pi/2 for _ in range(7)]

fk     = adoptor.ForwardKinematic(q)
eef    = adoptor.EndEffector(q)
rot    = adoptor.Orientation(q)
J      = adoptor.Jacobian(q)
Jsharp = adoptor.PesudoInverseJacobian(q)

print("finish")