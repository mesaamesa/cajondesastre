'''
Created on 23.07.2018

@author: amesagarcia
'''

from logging import getLogger
_log = getLogger(__name__)

from configparser import SafeConfigParser as Cfg
from random import randint
from difflib import Differ

class cIng(object):
    '''
    classdocs
    '''


    def __init__(self, *args, **keys):
        '''
        Constructor
        '''
        self.__cfg = Cfg()
        self.__cfg.read(keys['config'])
        _log.debug(self.__cfg.sections())
        self.__originalFile = self.__cfg.get('package', 'originalfile')
        _log.debug(self.__originalFile)
        self.__inputFile = self.__cfg.get('package', 'inputfile')
        _log.debug(self.__inputFile)
        self.__outputFile = self.__cfg.get('package', 'outputfile')
        _log.debug(self.__outputFile)
        self.__resultFile = self.__cfg.get('package', 'resultfile')
        _log.debug(self.__resultFile)
        self.__origdata = open(
            file = self.__originalFile, 
            mode = 'r', 
            encoding = 'utf-8', 
            ).read()
        _log.debug(self.__origdata)
        self.__indata = ''
        self.__outdata = ''
        self.__resdata = ''

    def formatInput(self):
        self.__indata = ''
        ll = ''
        for ww in ''.join(self.__origdata.splitlines()).split(sep = ' '):
            _log.debug('{0}:{1}'.format('ww', ww))
            _log.debug('{0}:{1}'.format('ll', ll))
            _log.debug('{0}:{1}'.format('indata', self.__indata))
            if len(ll) > self.__cfg.getint('package', 'maxLength'):
                self.__indata += ll + '\n'
                ll = ww + ' '
            else:
                ll += ww + ' '
        self.__indata += ll.strip()
        _log.debug(self.__indata)

        self.__lengths = [ len(ll) for ll in self.__indata.splitlines() ]
        _log.debug(self.__lengths)

        self.__centers = [ randint(0, xx - 1) for xx in self.__lengths ]
        _log.debug(self.__centers)
        self.__radius = [ randint(0, self.__lengths[xx] - self.__centers[xx] - 1) for xx in range(len(self.__lengths)) ]
        self.__radius = [ self.__cfg.getint('package', 'maxSecretLen') 
                         if self.__radius[xx] > self.__cfg.getint('package', 'maxSecretLen') 
                         else self.__radius[xx]
                         for xx in range(len(self.__radius)) ] 
        _log.debug(self.__radius)

        ff = open(
            file = self.__inputFile, 
            mode = 'w', 
            encoding = 'utf-8', 
            )
        ff.write(self.__indata)
        ff.close()

    def generate(self):
        ii = 0
        for ll in self.__indata.splitlines():
            self.__outdata += '{0}{1}{2}'.format(
                ll[0:self.__centers[ii]], 
                self.__cfg.get('package', 'secretchar') * self.__radius[ii],
                ll[(self.__centers[ii] + self.__radius[ii]):self.__lengths[ii]]) + '\n'
            ii += 1
        _log.debug(self.__outdata)

        ff = open(
            file = self.__outputFile, 
            mode = 'w', 
            encoding = 'utf-8', 
            )
        ff.write(self.__outdata)
        ff.close()

    def compare(self):
        self.__indata = open (
            file = self.__inputFile, 
            mode = 'r',
            encoding = 'utf-8',
            ).read()
        self.__outdata = open (
            file = self.__outputFile, 
            mode = 'r',
            encoding = 'utf-8',
            ).read()

        dd = Differ()
        rr = list(dd.compare(self.__indata.splitlines(keepends=True), self.__outdata.splitlines(keepends=True)))
        self.__resdata = [ll
                          if ll[0] in ['+', '?'] else ''
                          for ll in rr]
        ff = open(
            file = self.__resultFile, 
            mode = 'w', 
            encoding = 'utf-8', 
            )
        ff.write(''.join(ll for ll in self.__resdata))
        ff.close()

    def get_origdata(self):
        return self.__origdata

    def get_indata(self):
        return self.__indata

    def get_outdata(self):
        return self.__outdata

    def get_input_file(self):
        return self.__inputFile

    def get_original_file(self):
        return self.__originalFile

    def get_centers(self):
        return self.__centers

    def get_radius(self):
        return self.__radius

    def get_cfg(self):
        return self.__cfg.sections()

    def get_resdata(self):
        return self.__resdata

    configFile = property(get_cfg, None, None, None)
    inputFile = property(get_input_file, None, None, None)
    originalFile = property(get_original_file, None, None, None)
    centers = property(get_centers, None, None, None)
    radius = property(get_radius, None, None, None)
    origdata = property(get_origdata, None, None, None)
    indata = property(get_indata, None, None, None)
    outdata = property(get_outdata, None, None, None)
    resdata = property(get_resdata, None, None, None)

