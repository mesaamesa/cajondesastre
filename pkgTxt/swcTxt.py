#!/usr/bin/python3
# encoding: utf-8
'''
pkgTxt.swcTxt -- it parses a text file with a integer value inside a range.

pkgTxt.swcTxt it parses the text file 'ifile' searching for a 'pattern' and 
                filtering the line by the 'group' argument that should be within
                the range 'lolimit' and 'hilimit'. 

It defines classes_and_methods

@author:     Tiziano López

@copyright:  2018 organization_name. All rights reserved.

@license:    license

@contact:    mesaamesa@gmail.com
@deffield    updated: Updated
'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from argparse import FileType

from logging import basicConfig
from logging import getLogger
from logging import INFO as logLevel

from re import compile
from re import match

__all__ = []
__version__ = 0.1
__date__ = '2018-09-19'
__updated__ = '2018-09-19'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

log = getLogger(__name__)

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

class txtFilter(object):
    def __init__(self, *args, **kwargs):
        self.__ifile = kwargs['ifile']
        self.__pattern = kwargs['pattern']
        self.__group = kwargs['group']
        self.__lorange = kwargs['lorange']
        self.__hirange = kwargs['hirange']
        self.__rr = ''
        log.debug('{0}:{1}'.format('ifile', self.__ifile))
        log.debug('{0}:{1}'.format('pattern', self.__pattern))
        log.debug('{0}:{1}'.format('group', self.__group))
        log.debug('{0}:{1}'.format('lorange', self.__lorange))
        log.debug('{0}:{1}'.format('hirange', self.__hirange))
        
        
        
    def process(self):
        __pp = compile(self.__pattern)
        
        __ff = open(
            file= self.__ifile.name, 
            mode= self.__ifile.mode,
            encoding= self.__ifile.encoding)
        __nn = 0
        for __ll in __ff.readlines():
            __nn += 1
            __mm = match(__pp, __ll)
            if __mm:
                log.debug('{0}:{1}:{2}'.format('group[0]', __mm.group(0), type(__mm.group(0))))
                log.debug('{0}:{1}:{2}'.format('group[1]', __mm.group(1), type(__mm.group(1))))
                if len(__mm.group(1)):
                    if int(__mm.group(1)) in range(self.__lorange, self.__hirange + 1):
                        self.__rr += '{0}:{1}{2}'.format(__nn, __mm.group(0), '\n')
        __ff.close()

    def show(self):
        log.info('{0}:\n{1}'.format('result', self.__rr))
        

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by tiziano lopez on %s.
  Copyright 2018 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-i", "--ifile", 
                            dest="ifile", 
                            action="store", 
                            type=FileType('r'),
                            default='.',
                            help="input file to analyze [default: %(default)s]")
        parser.add_argument("-p", "--pattern", 
                            dest="pattern", 
                            action="store", 
                            type=str,
                            default='.*',
                            help="regular expression to search for. [default: %(default)s]")
        parser.add_argument("-g", "--group", 
                            dest="group",
                            type=int,
                            default=0, 
                            help="group number in the re pattern[default: %(default)s]")
        parser.add_argument("-l", "--lorange", 
                            dest="lorange", 
                            type=int,
                            default=0,
                            help="filter low limit range. [default: %(default)s]")
        parser.add_argument("-m", "--hirange", 
                            dest="hirange", 
                            type=int,
                            default=0,
                            help="filter high limit range. [default: %(default)s]")

        # Process arguments
        args = parser.parse_args()

        __ff = txtFilter(
            ifile=args.ifile, 
            pattern=args.pattern, 
            group=args.group, 
            lorange=args.lorange, 
            hirange=args.hirange
            )
        __ff.process()
        __ff.show()

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except ValueError as e:
        log.error(e)
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    if DEBUG:
        #sys.argv.append("-h")
        FORMAT = '%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s'
        basicConfig(format=FORMAT)
        log.setLevel(logLevel)
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'pkgTxt.swcTxt_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())