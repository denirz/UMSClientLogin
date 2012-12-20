'''
Created on Dec 19, 2012

@author: denirz
'''
import optparse    
def ParseOptions():    
    parser=optparse.OptionParser()
    parser.add_option("-n","--name",help="Phone Number in format 92Cxxxyyzz ",default='9262001222')
    parser.add_option("-p","--password",help="password, most porbably it os 6 digits or somethong else",default='000000')
    parser.add_option("-t","--text", help="Text os Short Message to send", default='Short message from UMS Python Library')
    parser.add_option("-f","--flash",help="--flash=1 is Flash SMS --flash=0 - normal SMS",default='0')
#    parser.add_option("-g","--")
    (args,additional_args)=parser.parse_args()
    return (args,additional_args)