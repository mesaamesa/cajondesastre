'''
Created on 01.08.2018

@author: amesagarcia
'''
from pkgIng.swcIng import cIng as DUT

GEN = False

if __name__ == '__main__':
    dut = DUT(config='./appIng/example.cfg')
    if GEN:
        dut.formatInput()
        dut.generate()
    dut.compare()
    pass
