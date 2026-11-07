import sympy as sp
from sympy.algebras.quaternion import Quaternion as Q
sa,sb=sp.symbols('s_a s_b'); Va=sp.Matrix(sp.symbols('a1:4')); Vb=sp.Matrix(sp.symbols('b1:4'))
ref=Q(sa,*Va)*Q(sb,*Vb)                     # SymPy'nin Hamilton çarpımı
ref_v=sp.Matrix([ref.b,ref.c,ref.d])
ek1_v = sa*Va + sb*Vb + Va.cross(Vb)        # Ek-1'de yazan
std_v = sa*Vb + sb*Va + Va.cross(Vb)        # standart formül
print("skaler kısım eşit mi:", sp.simplify(ref.a-(sa*sb-Va.dot(Vb)))==0)
print("Ek-1 vektör kısmı doğru mu:", sp.simplify(ref_v-ek1_v)==sp.zeros(3,1))
print("Standart formül doğru mu:", sp.simplify(ref_v-std_v)==sp.zeros(3,1))
d=sp.simplify(ref_v-ek1_v).subs({sa:1,sb:0,**dict(zip(Va,[0,0,0])),**dict(zip(Vb,[1,0,0]))})
print("Karşı örnek a=(1,0,0,0), b=(0,1,0,0): fark =", list(d))
# DCM kontrolü: Cbe = Rx Ry Rz, ZYX; MATLAB angle2dcm ile aynı mı + ortogonal mi
ps,th,ph=sp.symbols('psi theta phi',real=True)
Rz=sp.Matrix([[sp.cos(ps),sp.sin(ps),0],[-sp.sin(ps),sp.cos(ps),0],[0,0,1]])
Ry=sp.Matrix([[sp.cos(th),0,-sp.sin(th)],[0,1,0],[sp.sin(th),0,sp.cos(th)]])
Rx=sp.Matrix([[1,0,0],[0,sp.cos(ph),sp.sin(ph)],[0,-sp.sin(ph),sp.cos(ph)]])
C=Rx*Ry*Rz
print("DCM ortogonal (C*C^T=I):", sp.simplify(C*C.T)==sp.eye(3), " det=", sp.simplify(C.det()))
print("θ=90°'de DCM tanımlı ve ortogonal:", sp.simplify((C*C.T).subs(th,sp.pi/2))==sp.eye(3))
print("θ=90°'de C (ψ ve φ ayrı ayrı belirlenemez):", sp.simplify(C.subs(th,sp.pi/2)))
