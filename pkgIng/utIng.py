'''
Created on 23.07.2018

@author: amesagarcia
'''
import unittest
from pkgIng.swcIng import cIng as DUT
from logging import getLogger
_log = getLogger(__name__)
from os.path import exists
from os import remove

data = '''My Lords, I, too, congratulate my noble friend Lord Clement-Jones on introducing this important debate.Many 
years ago, I was a teacher and I very quickly became disillusioned by participating in a system based 
on the industrial production line model of education.I started to develop ways of catering for the needs 
of individual pupils, not ​least to allow them to develop their own creativity.Later, as an MP and my 
party’s education spokesman, I wrote a book on the importance of developing creativity in education.It 
was not very good and is now out of print.But my passion for the need to insert the power of creativity 
into our education system is undimmed, and it helps explain why I am such a passionate supporter of the 
creative industries.My noble friend Lord Clement-Jones and others have already highlighted the vital 
importance of the creative industries to our economy and our country’s future.I will not repeat all the 
statistics, but it is clear that the creative industries are a huge success story, punching above their 
weight.It is also clear that they have benefited enormously from our membership of the EU.These benefits 
are put at significant risk by the hard Brexit announced by the Prime Minister on Tuesday.Indeed, finding 
some glimmer of Brexit-related light for the creative industries is hard to come by, although I recommend, 
at least for a good laugh, “Brexit the Musical”, which I saw last weekend at the excellent Canal Café 
Theatre.Funny though it was, it intensified my worries about Brexit and Tuesday’s speech by the Prime 
Minister did little to allay them.It is clear that if the creative industries are so important we must, 
at the very least, ensure they have a voice at the top table during negotiations.As Sir John Sorrell 
says, the creative industries are now, “a key driver of wealth and global success”, and imperilling them 
would, he went on, “imperil our wider economy.That is why we need to be at the heart of the … government’s 
industrial strategy and negotiating priorities in coming months”.Yet there is scant evidence that the 
Government are taking the creative industries seriously.As Monday’s Evening Standard said, the creative 
industries do not get much of a look-in—they certainly did not in the Prime Minister’s speech on Tuesday.The 
Government have promised to push hard for trade deals with the EU on the car industry and on the pharmaceutical 
and financial sectors.So far, no such promises have been made for the creative sector, and the DCMS Secretary 
of State is not even on the Government’s main Brexit committee.This does not bode well for the creative 
industries.The negotiations will have to cover many matters, not least employment and skills.The creative 
industries have a higher than average percentage of non-UK EU nationals working for them: 10% of the 
publishing workforce; 25% in visual effects for film; and as high as 30% in computer gaming.All currently 
benefit from being able to attract a skilled workforce from the EU, from their variety and diversity 
and from the collaboration that freedom of movement has enabled.Already, uncertainty over the status 
of EU workers and the lack of clarity around future immigration policy has made it more difficult for 
them to attract the talent they need since the Brexit vote.I continue to believe that the best way to 
resolve the uncertainty is to remain in the single market, but if the Government insist on leaving, they 
must explain how they will resolve the uncertainty.​As the Creative Industries Federation said after 
the Prime Minister’s speech, “the willingness to continue to welcome the ‘brightest and best’ begs the 
question as to how that will be interpreted in future as the UK updates its outdated immigration system”.At 
the very least, we must surely guarantee the status of skilled EU nationals now and in the future.The 
Prime Minister says that she wants to deliver this, but she must do it quickly.Contrary to the comments 
of the noble Lord, Lord Blencathra, uncertainty already means that some are leaving, and it is getting 
harder to attract new talent from other EU countries to fill vacancies and support continued expansion.The 
Government should follow the clear advice of the noble Lord, Lord Puttnam.We also have to address homegrown 
skill shortages.The Prime Minister talked of reforming our schools to achieve this, as if schools had 
not seen reforms enough already.Instead, she should look at funding and at reforming the curriculum.The 
Government have failed to protect funding on a per-pupil basis; it is now predicted to fall by 7.5% by 
2021.Despite the need for creative subjects for a wide range of careers within and beyond the creative 
industries, entries for GCSEs in arts and creative subjects have fallen significantly, not least since 
the Government failed to include them within the EBacc.The EBacc is now interpreted as a signal of what 
matters and what is best for young people, and creative subjects are not a priority.This is leading to 
a mismatch between education policy and industry requirements.We surely need to unleash the creativity 
of pupils.We should learn from the recent writings of the noble Lord, Lord Baker of Dorking, recognise 
the importance of digital skills to the creative industries and take action to tackle the huge shortage 
of such skills.Some good things are happening.There are changes to the IT curriculum to introduce coding.The 
BBC’s “Make it Digital” and micro:bit are helping people to get creative with coding, programming and 
digital technology.Today, on the day it launches its digital marketing strategy with Minister Matt Hancock, 
I especially welcome the efforts of “Do It Digital”, a not-for-profit, business-facing campaign to share, 
signpost and celebrate all things that help small businesses get more out of digital.However, more is 
needed.With 10 million adults lacking basic digital skills, it is simply not a good enough response for 
the Government to announce free adult basic digital skills training but then expect it to be, “funded 
from the existing Adult Education Budget”.Without intervention beyond what is currently scoped, it is 
estimated that there will still be 7.9 million adults without basic digital skills in 2025, and surely—and 
I hope the Minister agrees—additional action to upskill our workforce must be taken before we introduce 
measures to cut the supply of skilled people from the rest of the EU.Without action in this and many 
other areas raised by my noble friend Lord Clement-Jones, the creative industries post-Brexit will be 
in severe difficulty.Sustaining their current position will be hard enough; expecting ​further growth 
will be unrealistic.To ensure that these issues are addressed, the creative industries must be given 
the priority they deserve during the negotiations and a seat at the top table.'''

class Test(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigFile(self):
        '''
        The class cIng instance uses the configuration file set up by the constructor.
        The class cIng instance uses a default configuration file called 'default.cfg'.
        The configuration file has the following sections, items, items type and defaut value:
            files
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
        dut = DUT(config='config.cfg')
        self.assertEqual('config.cfg', dut.configFile, 'Error at config file.')
        self.assertEqual('test02.txt', dut.files['original'], 'Error at original file configuration.')
        self.assertEqual('itest.txt', dut.files['input'], 'Error at input file configuration.')
        self.assertEqual('otest.txt', dut.files['output'], 'Error at output file configuration.')
        self.assertEqual('rtest.txt', dut.files['result'], 'Error at result file configuration.')
        
        
    def testReq02(self):
        '''
        The class cIng instance reads the original file from section 'package' and item 'originalFile'.
        The class cIng instance generates the input file from the original one, cutting the line length to the a maximum configurated value, but not splitting the words.
        The input file has the same information than the original file.
        '''
        self.maxDiff = None
        self.assertEqual('test01.txt', dut.originalFile, 'Error at original file.')
        self.assertFalse(exists('itest01.txt'), 'Error at input file (it should not exist).')
        dut.formatInput()
        self.assertTrue(exists('itest01.txt'), 'Error at input file (it should exist).')
        self.assertEqual(''.join(dut.origdata.splitlines()), ''.join(dut.indata.splitlines()), 'Error at input file')

    def testReq03(self):
        '''
        The properties 'data' and 'length' from the cIng instance are filled in with the content and length of the 'inputFile'.
        '''
        self.maxDiff = None
        self.assertEqual(data, dut.indata, 'Error at data.')
        self.assertEqual(len(data), len(dut.indata), 'Error at data length.')

    def testReq04(self):
        '''
        The cIng instance gives out a list of integers called 'centers'.
        The 'centers' list size is the number of lines of the 'data' field.
        '''
        self.assertEqual(66, len(dut.centers), 'Error at centers list size.')

    def testReq05(self):
        '''
        The cIng instance gives out a list of integers called 'radius'.
        The 'radius' list size is the number of lines of the 'data' field.
        The max value for any element of the radius list is the configuration value 'maxSecretLen'.
        '''
        self.assertEqual(66, len(dut.radius), 'Error at radius list size.')
        for xx in dut.radius:
            self.assertGreaterEqual(10, xx, 'Error at radius list element {0}'.format(xx))

    def testReq06(self):
        '''
        The addition result of one 'centers' list element plus the same indexed element from 'radius' list is lower than the indexed line length.
        '''
        ii = 0
        for ll in data.splitlines():
            _log.debug(ll)
            self.assertGreater(len(ll), dut.centers[ii] + dut.radius[ii], 'Error at properties (line:{0}, length:{1}, center:{2}, radius:{3})'.format(ll, len(ll), dut.centers[ii], dut.radius[ii]))
            ii += 1

    def testReq07(self):
        '''
        The cIng instance generates an new output based on the input file, where each line is a copy but the characters between center and radius position are translated to the character '*'.
        The cIng instance writes the output data to the output file indicated in the configuration file.
        '''
        self.assertFalse(exists('otest01.txt'), 'Error at ouput file (it should not exist).')
        dut.generate()
        self.assertTrue(exists('otest01.txt'), 'Error at ouput file. (it should exist)')

        ii = 0
        for ll in dut.outdata.splitlines():
            _log.debug(ll)
            self.assertEqual('*'*dut.radius[ii], ll[dut.centers[ii]:(dut.centers[ii] + dut.radius[ii])], 'Error at outpus data (line:{0}, length:{1}, center:{2}, radius:{3})'.format(ll, len(ll), dut.centers[ii], dut.radius[ii]))
            ii += 1

    def testReq08(self):
        '''
        The cIng instance compares the input and the output files and it sets the correction char where they are different.
        '''
        dut.compare()
        input('Continue? [enter]')
        xf = open (
            file = 'itest01.txt', 
            mode = 'r',
            encoding = 'utf-8',
            )
        yf = dut.resdata
        
        self.maxDiff = None
        self.assertEqual(
            [ xl for xl in xf.readlines() ], 
            [ yl for yl in yf.splitlines() ], 
            'Error at correction.',
            )  
        
        xf.close()
        yf.close()

    def testReq99(self):
        '''
        Remove temporary output UT files:
        '''
        input('Continue? [enter]')
        if exists('itest01.txt'): remove('itest01.txt')
        if exists('otest01.txt'): remove('otest01.txt')
        if exists('rtest01.txt'): remove('rtest01.txt')
        self.assertFalse(exists('itest01.txt'), 'Error at input file (it should not exist).')
        self.assertFalse(exists('otest01.txt'), 'Error at output file (it should not exist).')
        self.assertFalse(exists('rtest01.txt'), 'Error at result file (it should not exist).')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()