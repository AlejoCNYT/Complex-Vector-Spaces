import unittest
import Libcplx_two as lct
from math import sqrt
#import Libcplx as lc

class TestCplxOperations(unittest.TestCase):

    def test_adVector(self):
        suma = lct.adVector([(1, -2.5), (2, 1)], [(3, 0), (7, -3.8)])
        self.assertEqual(suma, [(4, -2.5), (9, -2.8)])

    def test_invVector(self):
        invAd = lct.invVector([(6, -4), (7, 3)])
        self.assertEqual(invAd, [(-6, 4), (-7, -3)])

    def test_MultEscalarVector(self):
        Msv = lct.MultEscalarVector((3,2),[(6,3),(5,1)])
        self.assertEqual(Msv,[(12,21),(13,13)])

    def test_sumaMatrix(self):
        sumatx = lct.adVector([(1,2),(3,4)],[(4,3),(2,1)])
        self.assertEqual(sumatx,[(5,5),(5,5)])

    def test_invAdMtx(self):
        InvAdM = lct.invAdMtx([[(4, 3), (2, 1)],[(9, 8), (7, 5)]])
        self.assertEqual(InvAdM, [[(-4, -3), (-2, -1)],[(-9, -8), (-7, -5)]])

    def test_MultEscMtx(self):
        MultEscMtx = lct.MultEscMtx((3, 2), [[(6, 3), (5, 1)], [(0, 0), (4, 0)]])
        self.assertEqual(MultEscMtx, [[(12, 21), (13, 13)], [(0, 0), (12, 8)]])

    def test_trMtx(self):
        trMt = lct.trMtx([[(1,0),(2,3)],[(4,5),(1,0)]])
        self.assertEqual(trMt,[[(1,0),(4,5)],[(2,3),(1,0)]])

    def test_conjMtx(self):
        conjM = lct.conjMtx([[(1, 0), (2, 3)], [(4, 5), (1, 0)]])
        self.assertEqual(conjM, [[(1, 0), (2, -3)], [(4, -5), (1, 0)]])

    def test_adjMtx(self):
        HMt = lct.adjMtx([[(6,-3),(2,12),(0,-19)],[(0,0),(5,2.1),(17,0)],[(1,0),(2,5),(3,-4.5)]])
        self.assertEqual(HMt,[[(6,3),(0,0),(1,0)],[(2,-12),(5,-2.1),(2,-5)],[(0,19),(17,0),(3,4.5)]])

    # def test_ProdMtx(self):
    #     PrMtx = lct.ProdMtx([[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]],[[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]])
    #     self.assertEqual(PrMtx,[[(26,-52),(60,24),(26,0)],[(9,7),(1,29),(14,0)],[(48,-21),(15,22),(20,22)]])

    # def MtxVec


    def test_vectorPrInt(self):
        VPI = lct.vectorPrInt([3,1,2])
        self.assertEqual(VPI, 14)

    def test_vectorNorm(self):
        vNorm = lct.vectorNorm([3,5,8,1,1])
        self.assertEqual(vNorm, 10)

    def test_disV(self):
        dv = lct.disV([3,1,2],[2,2,-1])
        self.assertEqual(dv, sqrt(11))

    def test_hermMtx(self):
        hm = lct.hermMtx([[(7,0),(6,5)],[(6,-5),(-3,0)]])
        self.assertEqual(hm, True)

    def vectorTsorProduct(self):
        VTP = lct.vectorTsorProduct([3,4,7],[-1,2])
        self.assertEqual(VTP, [-3,6,-4,8,-7,14])

if __name__ == '__main__':
    unittest.main()