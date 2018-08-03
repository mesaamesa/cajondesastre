'''
Created on 23.07.2018

@author: amesagarcia
'''

from configparser import ConfigParser as Cfg
from difflib import Differ
from logging import getLogger
from random import randint
from random import sample

_log = getLogger(__name__)


defaultCfg = {
    'files': {
        'wd' : '.',
        'original' : 'original.txt',
        'input' : 'input.txt',
        'output' : 'output.txt',
        'result' : 'result.txt',
        },
    'lengths': {
        'maxLine' : '0',
        'maxSecretChars' : '0',
        'maxSecretWords' : '0',
        },
    'chars': {
        'secret' : '*',
        'correction' : '?',
        },
    }

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
        for ss in self.__cfg.sections() :
            _log.debug('{0}:{1}'.format('section', ss))
            for ii in self.__cfg.items(ss):
                _log.debug('{0}:{1}'.format(ii[0], ii[1]))
        self.__wd = self.__cfg.get('files', 'wd')
        self.__originalFile = '{0}/{1}'.format(
            self.__wd,
            self.__cfg.get('files', 'original')
            )
        _log.debug(self.__originalFile)
        self.__inputFile = '{0}/{1}'.format(
            self.__wd,
            self.__cfg.get('files', 'input')
            )
        _log.debug(self.__inputFile)
        self.__outputFile = '{0}/{1}'.format(
            self.__wd,
            self.__cfg.get('files', 'output')
            )
        _log.debug(self.__outputFile)
        self.__resultFile = '{0}/{1}'.format(
            self.__wd,
            self.__cfg.get('files', 'result')
            )
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
        self.__maxline = self.__cfg.getint('lengths', 'maxLine')
        self.__maxsecretwords = self.__cfg.getint('lengths', 'maxSecretWords')
        self.__maxsecretchars = self.__cfg.getint('lengths', 'maxSecretChars')
        self.__secret = self.__cfg.get('chars', 'secret')
        self.__correction = self.__cfg.get('chars', 'correction')
        self.__centers = list()
        self.__radius = list()
        self.__secretmethod = self.__cfg.getboolean('process', 'secretchars')
        self.__lexicon = self.__cfg.options('lexicon')
        _log.debug(self.__lexicon)
        
    def get_secretmethod(self):
        return self.__secretmethod


    def get_secret(self):
        return self.__secret


    def get_correction(self):
        return self.__correction


    def get_maxsecretwords(self):
        return self.__maxsecretwords


    def get_maxsecretchars(self):
        return self.__maxsecretchars


    def get_maxline(self):
        return self.__maxline


    def get_wd(self):
        return self.__wd


    def formatInput(self):
        self.__indata = ''
        ll = ''
        for ww in ''.join(self.__origdata.splitlines()).split(sep = ' '):
            #_log.debug('{0}:{1}'.format('ww', ww))
            #_log.debug('{0}:{1}'.format('ll', ll))
            #_log.debug('{0}:{1}'.format('indata', self.__indata))
            if len(ll) > self.__cfg.getint('lengths', 'maxline'):
                self.__indata += ll + '\n'
                ll = ww + ' '
            else:
                ll += ww + ' '
        self.__indata += ll.strip()
        _log.debug(self.__indata)

        self.__lengths = [ len(ll)  if self.__secretmethod 
                    else len(ll.split()) 
                    for ll in self.__indata.splitlines() 
                    ]
        _log.debug(self.__lengths)

        self.__radius = [ 
            randint(0, 
                    self.__cfg.getint('lengths', 'maxSecretChars') 
                    if self.__secretmethod 
                    else self.__cfg.getint('lengths', 'maxSecretWords')
                    ) for xx in self.__lengths  
            ]
        _log.debug(self.__radius)

        self.__centers = [ 
            randint(0, 
                    xx - self.__cfg.getint('lengths', 'maxSecretChars') 
                    if self.__secretmethod 
                    else 1
                    ) for xx in self.__lengths 
            ]
        _log.debug(self.__centers)

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
            if self.__secretmethod :
                self.__outdata += '{0}{1}{2}'.format(
                    ll[0:self.__centers[ii]],
                    self.__cfg.get('chars', 'secret') * self.__radius[ii],
                    ll[(self.__centers[ii] + self.__radius[ii]):self.__lengths[ii]]) + '\n'
            else:
                ww = ll.split()
                blind = sample(ww, self.__radius[ii])
                _log.debug('{0}:{1}'.format(ww, blind))
                for jj in range(len(ww)):
                    asterisk = self.__cfg.get('chars', 'secret') * len(ww[jj])
                    self.__outdata +=  asterisk if (ww[jj] in blind) and (ww[jj].lower() not in self.__lexicon) else ww[jj] 
                    self.__outdata += ' '
                    _log.debug('index:{0}:center:{1}:radius:{2}:word:{3}:asterisk:{4}'.format(jj, self.__centers[ii], self.__radius[ii], ww[jj], asterisk))
                self.__outdata += '\n'
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

    def get_output_file(self):
        return self.__outputFile

    def get_result_file(self):
        return self.__resultFile

    def get_centers(self):
        return self.__centers

    def get_radius(self):
        return self.__radius

    def get_resdata(self):
        return self.__resdata

    originalfile = property(get_original_file, None, None, None)
    inputfile = property(get_input_file, None, None, None)
    outputfile = property(get_output_file, None, None, None)
    resultfile = property(get_result_file, None, None, None)

    centers = property(get_centers, None, None, None)
    radius = property(get_radius, None, None, None)
    
    origdata = property(get_origdata, None, None, None)
    indata = property(get_indata, None, None, None)
    outdata = property(get_outdata, None, None, None)
    resdata = property(get_resdata, None, None, None)
    wd = property(get_wd, None, None, None)
    maxline = property(get_maxline, None, None, None)
    maxsecretwords = property(get_maxsecretwords, None, None, None)
    maxsecretchars = property(get_maxsecretchars, None, None, None)
    secret = property(get_secret, None, None, None)
    correction = property(get_correction, None, None, None)
    secretmethod = property(get_secretmethod, None, None, None)
