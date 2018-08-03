'''
Created on 23.07.2018

@author: amesagarcia
'''
from logging import getLogger
from os import remove
from os.path import exists
import unittest

from pkgIng.swcIng import cIng as DUT


_log = getLogger(__name__)

data = '''My Lords, I thank the noble Lord, Lord Clement-Jones, for initiating this important debate. I will talk 
briefly about museums, art galleries and commercial art galleries. Some have argued that these are not 
part of the creative industries, but surely exhibitions that bring together installations of art, music, 
video and photography have to be regarded as creative.Museums and galleries play a central part in the 
cultural and creative life of our country and of our cities in particular. The role of culture and creativity 
in the social and economic future of our cities should be recognised and supported across government. 
For our cities throughout the UK to be truly successful, competitive and sustainable, they must be more 
than just hubs of commerce. Culture and creative industries are able to attract highly paid jobs and 
tourism to our cities. As businesses and the workplace become increasingly flexible and mobile, culture 
has a vital role to play in the appeal of a city for both employers and, critically, employees.Culture 
can also support regeneration and development plans, as seen in areas such as London, Manchester and 
Dundee. Making this a reality across the country will require all parts of both the public and private 
sectors to recognise the value that culture and creativity play in the cities of the future. They operate 
in a global marketplace for creative, cultural and research talent. We have museum curators from Europe 
and further afield, and many of our museum and gallery employees have studied in Europe and in other 
parts of the world.The museum sector is well placed to project an image of the country that is open, 
progressive and positively engaged. There is a real opportunity for museums and galleries to shape global 
perceptions of the country and, in doing so, help to encourage inbound tourism, trade and investment, 
as well as supporting the retention of global business. London’s unique collection of world-class museums 
is an essential part of its appeal to mobile and flexible global companies and employers who are choosing 
it as a place to work and live, against competition from other comparable global cities.Of course there 
are uncertain times ahead for museums and art galleries. Leaving the EU could effectively remove the 
UK from the European loan circuit. The loan system as it stands has academic, social, economic ​and political 
advantages. Among many concerns are that costs will go up, and funding down. The Government must take 
note of the possible impact on UK museums and galleries. The laws in place at present are interrelated, 
and these will need to be in place when we leave to regulate such issues as the licensing and movement 
of cultural property, which at present is in EU law.It is vital that museums continue to tour in Europe 
and bring objects, both ancient and modern, in and out of the country, enhancing the UK’s reputation 
abroad and all that they offer to people here in the UK. Now it is more important than ever that they 
continue to look and reach outwards and work with organisations in Europe and beyond, cementing the partnerships 
that have been built up. There is no doubt that our arts, creative and cultural organisations are in 
demand as partners, providers and destinations. As I have said, our creative and cultural strength is 
one of the UK’s trademarks globally.Our departure from the EU will strip the UK of a layer of funding, 
but it need not mean that there should also be an end to culture collaboration. There may be uncertainty 
on the future of funding and free movement, but our creativity, museums and galleries remain vibrant. 
We are world leaders in culture and the arts. Innovative, challenging and exciting arts and culture are 
here to stay. They benefit the economy and attract tourists from all over the world.The British Museum 
has a first-rate international programme that supports the UK’s soft-power capabilities, building networks 
and relationships throughout the world. The museum’s arm’s-length status enables it to continue to engage 
with countries such as Russia and Iran during moments of diplomatic difficulty, maintaining people-to-people 
contact. The museum also regularly receives ministerial and state visits, which emphasise its importance 
as one of the world’s leading attractions and a symbol of the UK’s openness to the world. Of course not 
all museums can operate on that scale, but it is important that museums and the cultural sector as a 
whole continue to engage and build networks, through research, exhibitions and collaboration with partners 
around the world, including throughout Europe.The National Museum Directors’ Council stressed that EU 
funds provide structure and scale that individual member states cannot possibly replicate, and that private 
funding cannot replace public funding. Regional museums and galleries have always been under pressure 
and are particularly vulnerable. They need to rethink their way forward, sharing experience, expertise, 
resources, collections and skills. There must be collaboration with community organisations and connection 
with their local community. Could this be the time to consider a national strategy for museums and galleries? 
I would be interested to know how the Minister might feel about that.I want to spend a couple of minutes 
on commercial galleries. The art market here in the UK is the second largest in the world, attracting 
high-spending individuals to buy and sell here, as well as setting up businesses and homes. They encourage 
and promote many of our artists in all areas of creativity. Commercial art galleries are small businesses 
and, as such, are no different from other businesses trading their wares in Europe and ​further afield. 
I hope that the Government’s industrial strategy will champion them in the same way that it does other 
businesses.Anthony Browne, chairman of the British Art Market Federation, pointed out recently that all 
is not gloom and doom. The freer the trade, the more successful our art market can be. The Brexit vote 
could give London a competitive advantage over rivals in New York, Switzerland and Hong Kong.However, 
there is a caveat. Following Brexit, there is anxiety about freedom of movement and cross-border licensing, 
as well as favourable fiscal advantages to encourage a global market. I am optimistic about the future 
of our museums and galleries. Let us remember that through the use of collections, public programmes 
and community engagement work, museums can connect diverse communities and provide safe civic spaces 
to help us consider and address the changing nature of our society and our relationships with the world. 
Exhibitions such as the British Museum’s “Hajj: Journey to the Heart of Islam” and the Sikh Fortress 
Turban touring exhibition, or the forthcoming South Asia partnership gallery in Manchester, demonstrate 
how collections can be used to engage with local communities and increase levels of understanding and 
tolerance.I look forward to hearing my noble friend’s speech, in which I am sure there will be support 
for museums and galleries in this country.'''

class Test(unittest.TestCase):


    def setUp(self):
        self.dut = DUT(config='./appIng/config.cfg')

    def tearDown(self):
        del self.dut

    def testConfigFile(self):
        '''
        The class cIng instance uses the configuration file set up by the constructor.
        The class cIng instance uses a default configuration file called 'default.cfg'.
        The configuration file has the following sections, items, items type and defaut value:
            files
                wd:string = .
                original:string = original.txt
                input:string = input.txt
                output:string = output.txt
                result:string = result.txt
            lengths
                maxLine:int = 0
                maxSecretChars:int = 0
                maxSecretWords:int = 0
            chars
                secret:string = *
                correction:string = *
        '''
        _log.info('<testConfigFile')

        self.assertEqual('./appIng', self.dut.wd, 'Error at wd configuration.')
        self.assertEqual('./appIng/test.txt', self.dut.originalfile, 'Error at original file configuration.')
        self.assertEqual('./appIng/itest.txt', self.dut.inputfile, 'Error at input file configuration.')
        self.assertEqual('./appIng/otest.txt', self.dut.outputfile, 'Error at output file configuration.')
        self.assertEqual('./appIng/rtest.txt', self.dut.resultfile, 'Error at result file configuration.')

        self.assertEqual(100, self.dut.maxline, 'Error at max line lengths configuration.')
        self.assertEqual(10, self.dut.maxsecretchars, 'Error at max secret chars lengths configuration.')
        self.assertEqual(2, self.dut.maxsecretwords, 'Error at max secret words lengths configuration.')

        self.assertEqual('*', self.dut.secret, 'Error at secret char configuration.')
        self.assertEqual('?', self.dut.correction, 'Error at correction char configuration.')

        _log.info('testConfigFile>')


    def testFormatFile(self):
        '''
        The class cIng instance reads the original file from section 'package' and item 'originalFile'.
        The class cIng instance generates the input file from the original one, cutting the line length to the a maximum configurated value, but not splitting the words.
        The input file has the same information than the original file.
        The properties 'data' and 'length' from the cIng instance are filled in with the content and length of the 'inputFile'.
        '''
        _log.info('<testFormatFile')

        self.maxDiff = None
        #self.assertFalse(exists('./appIng/itest.txt'), 'Error at input file (it should not exist).')
        self.dut.formatInput()
        self.assertTrue(exists('./appIng/itest.txt'), 'Error at input file (it should exist).')
        self.assertEqual(''.join(self.dut.origdata.splitlines()), ''.join(self.dut.indata.splitlines()), 'Error at input file')
        self.assertEqual(data, self.dut.indata, 'Error at data.')
        self.assertEqual(len(data), len(self.dut.indata), 'Error at data length.')

        _log.info('testFormatFile>')

    def testCalculations(self):
        '''
        The cIng instance gives out a list of integers called 'centers'.
        The 'centers' list size is the number of lines of the 'data' field.
        The cIng instance gives out a list of integers called 'radius'.
        The 'radius' list size is the number of lines of the 'data' field.
        The max value for any element of the radius list is the configuration value 'maxSecretLen'.
        The addition result of one 'centers' list element plus the same indexed element from 'radius' list is lower than the indexed line length.
        '''
        _log.info('<testCalculations')

        self.dut.formatInput()
        self.assertEqual(69, len(self.dut.centers), 'Error at centers list size.')
        self.assertEqual(69, len(self.dut.radius), 'Error at radius list size.')
        for xx in self.dut.radius:
            self.assertGreaterEqual(10, xx, 'Error at radius list element {0}'.format(xx))
        ii = 0
        for ll in data.splitlines():
            _log.debug(ll)
            self.assertGreater(
                len(ll), 
                self.dut.centers[ii] + self.dut.radius[ii], 
                'Error at properties \n(line:{0}, \nlength:{1}, \ncenter:{2}, \nradius:{3})'.format(ll, len(ll), self.dut.centers[ii], self.dut.radius[ii])
            )
            ii += 1

        _log.info('testCalculations>')

    def testOutputFile(self):
        '''
        The cIng instance generates an new output based on the input file, where each line is a copy but the characters between center and radius position are translated to the character '*'.
        The cIng instance writes the output data to the output file indicated in the configuration file.
        '''
        _log.info('<testOutputFile')

        #self.assertFalse(exists('./appIng/otest.txt'), 'Error at ouput file (it should not exist).')
        self.dut.formatInput()
        self.dut.generate()
        self.assertTrue(exists('./appIng/otest.txt'), 'Error at ouput file. (it should exist)')

        ii = 0
        for ll in self.dut.outdata.splitlines():
            _log.debug(ll)
            self.assertEqual(
                '*'*self.dut.radius[ii], 
                ll[self.dut.centers[ii]:(self.dut.centers[ii] + self.dut.radius[ii])], 
                'Error at outpus data \n(line:{0}, \nlength:{1}, \ncenter:{2}, \nradius:{3})'.format(ll, len(ll), self.dut.centers[ii], self.dut.radius[ii])
            )
            ii += 1

        _log.info('testOutputFile>')

    def testResultFile(self):
        '''
        The cIng instance compares the input and the output files and it sets the correction char where they are different.
        '''
        _log.info('<testResultFile')

        self.dut.formatInput()
        self.dut.generate()

        self.dut.compare()
        #input('Continue? [enter]')
        xf = open (
            file = './appIng/itest.txt',
            mode = 'r',
            encoding = 'utf-8',
            )
        yf = self.dut.resdata

        self.maxDiff = None
        self.assertEqual(
            [ xl for xl in xf.readlines() ],
            [ yl for yl in yf ],
            'Error at correction.',
            )

        xf.close()

        _log.info('testResultFile>')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
