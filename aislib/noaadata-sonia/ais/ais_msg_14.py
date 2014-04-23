#!/usr/bin/env python

__version__ = '$Revision: 4791 $'.split()[1]
__date__ = '$Date: 2012-10-20 $'.split()[1]
__author__ = 'xmlbinmsg'

__doc__='''

Autogenerated python functions to serialize/deserialize binary messages.

Generated by: ../scripts/aisxmlbinmsg2py.py

Need to then wrap these functions with the outer AIS packet and then
convert the whole binary blob to a NMEA string.  Those functions are
not currently provided in this file.

serialize: python to ais binary
deserialize: ais binary to python

The generated code uses translators.py, binary.py, and aisstring.py
which should be packaged with the resulting files.


@requires: U{epydoc<http://epydoc.sourceforge.net/>} > 3.0alpha3
@requires: U{BitVector<http://cheeseshop.python.org/pypi/BitVector>}

@author: '''+__author__+'''
@version: ''' + __version__ +'''
@var __date__: Date of last svn commit
@undocumented: __version__ __author__ __doc__ parser
@status: under development
@license: Generated code has no license
@todo: FIX: put in a description of the message here with fields and types.
'''

import sys
from decimal import Decimal
from BitVector import BitVector

import binary, aisstring

# FIX: check to see if these will be needed
TrueBV  = BitVector(bitstring="1")
"Why always rebuild the True bit?  This should speed things up a bunch"
FalseBV = BitVector(bitstring="0")
"Why always rebuild the False bit?  This should speed things up a bunch"


fieldList = (
	'MessageID',
	'RepeatIndicator',
	'UserID',
	'Spare2',
)

fieldListPostgres = (
	'MessageID',
	'RepeatIndicator',
	'UserID',
	'Spare2',
)

toPgFields = {
}
'''
Go to the Postgis field names from the straight field name
'''

fromPgFields = {
}
'''
Go from the Postgis field names to the straight field name
'''

pgTypes = {
}
'''
Lookup table for each postgis field name to get its type.
'''

def encode(params, validate=False):
	'''Create a srbm binary message payload to pack into an AIS Msg srbm.

	Fields in params:
	  - MessageID(uint): AIS message number.  Must be 14 (field automatically set to "14")
	  - RepeatIndicator(uint): Indicated how many times a message has been repeated
	  - UserID(uint): Unique ship identification number (MMSI).  Also known as the Source ID
	  - Spare2(uint): Must be 0 (field automatically set to "0")
	@param params: Dictionary of field names/values.  Throws a ValueError exception if required is missing
	@param validate: Set to true to cause checking to occur.  Runs slower.  FIX: not implemented.
	@rtype: BitVector
	@return: encoded binary message (for binary messages, this needs to be wrapped in a msg 8
	@note: The returned bits may not be 6 bit aligned.  It is up to you to pad out the bits.
	'''

	bvList = []
	bvList.append(binary.setBitVectorSize(BitVector(intVal=14),6))
	if 'RepeatIndicator' in params:
		bvList.append(binary.setBitVectorSize(BitVector(intVal=params['RepeatIndicator']),2))
	else:
		bvList.append(binary.setBitVectorSize(BitVector(intVal=0),2))
	bvList.append(binary.setBitVectorSize(BitVector(intVal=params['UserID']),30))
	bvList.append(binary.setBitVectorSize(BitVector(intVal=0),1))

	return binary.joinBV(bvList)

def decode(bv, validate=False):
	'''Unpack a srbm message 

	Fields in params:
	  - MessageID(uint): AIS message number.  Must be 14 (field automatically set to "14")
	  - RepeatIndicator(uint): Indicated how many times a message has been repeated
	  - UserID(uint): Unique ship identification number (MMSI).  Also known as the Source ID
	  - Spare2(uint): Must be 0 (field automatically set to "0")
	@type bv: BitVector
	@param bv: Bits defining a message
	@param validate: Set to true to cause checking to occur.  Runs slower.  FIX: not implemented.
	@rtype: dict
	@return: params
	'''

	#Would be nice to check the bit count here..
	#if validate:
	#	assert (len(bv)==FIX: SOME NUMBER)
	r = {}
	r['MessageID']=14
	r['RepeatIndicator']=int(bv[6:8])
	r['UserID']=int(bv[8:38])
	r['Spare2']=0
	return r

def decodeMessageID(bv, validate=False):
	return 14

def decodeRepeatIndicator(bv, validate=False):
	return int(bv[6:8])

def decodeUserID(bv, validate=False):
	return int(bv[8:38])

def decodeSpare2(bv, validate=False):
	return 0


def printHtml(params, out=sys.stdout):
		out.write("<h3>srbm</h3>\n")
		out.write("<table border=\"1\">\n")
		out.write("<tr bgcolor=\"orange\">\n")
		out.write("<th align=\"left\">Field Name</th>\n")
		out.write("<th align=\"left\">Type</th>\n")
		out.write("<th align=\"left\">Value</th>\n")
		out.write("<th align=\"left\">Value in Lookup Table</th>\n")
		out.write("<th align=\"left\">Units</th>\n")
		out.write("</tr>\n")
		out.write("\n")
		out.write("<tr>\n")
		out.write("<td>MessageID</td>\n")
		out.write("<td>uint</td>\n")
		if 'MessageID' in params:
			out.write("	<td>"+str(params['MessageID'])+"</td>\n")
			out.write("	<td>"+str(params['MessageID'])+"</td>\n")
		out.write("</tr>\n")
		out.write("\n")
		out.write("<tr>\n")
		out.write("<td>RepeatIndicator</td>\n")
		out.write("<td>uint</td>\n")
		if 'RepeatIndicator' in params:
			out.write("	<td>"+str(params['RepeatIndicator'])+"</td>\n")
			if str(params['RepeatIndicator']) in RepeatIndicatorDecodeLut:
				out.write("<td>"+RepeatIndicatorDecodeLut[str(params['RepeatIndicator'])]+"</td>")
			else:
				out.write("<td><i>Missing LUT entry</i></td>")
		out.write("</tr>\n")
		out.write("\n")
		out.write("<tr>\n")
		out.write("<td>UserID</td>\n")
		out.write("<td>uint</td>\n")
		if 'UserID' in params:
			out.write("	<td>"+str(params['UserID'])+"</td>\n")
			out.write("	<td>"+str(params['UserID'])+"</td>\n")
		out.write("</tr>\n")
		out.write("\n")
		out.write("<tr>\n")
		out.write("<td>Spare2</td>\n")
		out.write("<td>uint</td>\n")
		if 'Spare2' in params:
			out.write("	<td>"+str(params['Spare2'])+"</td>\n")
			out.write("	<td>"+str(params['Spare2'])+"</td>\n")
		out.write("</tr>\n")
		out.write("</table>\n")

def printFields(params, out=sys.stdout, format='std', fieldList=None, dbType='postgres'):
	'''Print a srbm message to stdout.

	Fields in params:
	  - MessageID(uint): AIS message number.  Must be 14 (field automatically set to "14")
	  - RepeatIndicator(uint): Indicated how many times a message has been repeated
	  - UserID(uint): Unique ship identification number (MMSI).  Also known as the Source ID
	  - Spare2(uint): Must be 0 (field automatically set to "0")
	@param params: Dictionary of field names/values.  
	@param out: File like object to write to
	@rtype: stdout
	@return: text to out
	'''

	if 'std'==format:
		out.write("srbm:\n")
		if 'MessageID' in params: out.write("	MessageID:        "+str(params['MessageID'])+"\n")
		if 'RepeatIndicator' in params: out.write("	RepeatIndicator:  "+str(params['RepeatIndicator'])+"\n")
		if 'UserID' in params: out.write("	UserID:           "+str(params['UserID'])+"\n")
		if 'Spare2' in params: out.write("	Spare2:           "+str(params['Spare2'])+"\n")
	elif 'csv'==format:
		if None == options.fieldList:
			options.fieldList = fieldList
		needComma = False;
		for field in fieldList:
			if needComma: out.write(',')
			needComma = True
			if field in params:
				out.write(str(params[field]))
			# else: leave it empty
		out.write("\n")
	elif 'html'==format:
		printHtml(params,out)
	elif 'sql'==format:
		sqlInsertStr(params,out,dbType=dbType)
	else: 
		print "ERROR: unknown format:",format
		assert False

	return # Nothing to return

RepeatIndicatorEncodeLut = {
	'default':'0',
	'do not repeat any more':'3',
	} #RepeatIndicatorEncodeLut

RepeatIndicatorDecodeLut = {
	'0':'default',
	'3':'do not repeat any more',
	} # RepeatIndicatorEncodeLut

######################################################################
# SQL SUPPORT
######################################################################

dbTableName='srbm'
'Database table name'

def sqlCreateStr(outfile=sys.stdout, fields=None, extraFields=None
		,addCoastGuardFields=True
		,dbType='postgres'
		):
	'''
	Return the SQL CREATE command for this message type
	@param outfile: file like object to print to.
	@param fields: which fields to put in the create.  Defaults to all.
	@param extraFields: A sequence of tuples containing (name,sql type) for additional fields
	@param addCoastGuardFields: Add the extra fields that come after the NMEA check some from the USCG N-AIS format
	@param dbType: Which flavor of database we are using so that the create is tailored ('sqlite' or 'postgres')
	@type addCoastGuardFields: bool
	@return: sql create string
	@rtype: str

	@see: sqlCreate
	'''
	# FIX: should this sqlCreate be the same as in LaTeX (createFuncName) rather than hard coded?
	outfile.write(str(sqlCreate(fields,extraFields,addCoastGuardFields,dbType=dbType)))

def sqlCreate(fields=None, extraFields=None, addCoastGuardFields=True, dbType='postgres'):
	'''
	Return the sqlhelp object to create the table.

	@param fields: which fields to put in the create.  Defaults to all.
	@param extraFields: A sequence of tuples containing (name,sql type) for additional fields
	@param addCoastGuardFields: Add the extra fields that come after the NMEA check some from the USCG N-AIS format
	@type addCoastGuardFields: bool
	@param dbType: Which flavor of database we are using so that the create is tailored ('sqlite' or 'postgres')
	@return: An object that can be used to generate a return
	@rtype: sqlhelp.create
	'''
	if None == fields: fields = fieldList
	import sqlhelp
	c = sqlhelp.create('srbm',dbType=dbType)
	c.addPrimaryKey()
	if 'MessageID' in fields: c.addInt ('MessageID')
	if 'RepeatIndicator' in fields: c.addInt ('RepeatIndicator')
	if 'UserID' in fields: c.addInt ('UserID')
	if 'Spare2' in fields: c.addInt ('Spare2')

	if addCoastGuardFields:
		# c.addInt('cg_s_rssi')     # Relative signal strength indicator
		# c.addInt('cg_d_strength')        # dBm receive strength
		# c.addVarChar('cg_x',10) # Idonno
		c.addInt('cg_t_arrival')        # Receive timestamp from the AIS equipment 'T'
		c.addInt('cg_s_slotnum')        # Slot received in
		c.addVarChar('cg_r',15)   # Receiver station ID  -  should usually be an MMSI, but sometimes is a string
		c.addInt('cg_sec')        # UTC seconds since the epoch

		c.addTimestamp('cg_timestamp') # UTC decoded cg_sec - not actually in the data stream

	return c

def sqlInsertStr(params, outfile=sys.stdout, extraParams=None, dbType='postgres'):
	'''
	Return the SQL INSERT command for this message type
	@param params: dictionary of values keyed by field name
	@param outfile: file like object to print to.
	@param extraParams: A sequence of tuples containing (name,sql type) for additional fields
	@return: sql create string
	@rtype: str

	@see: sqlCreate
	'''
	outfile.write(str(sqlInsert(params,extraParams,dbType=dbType)))


def sqlInsert(params,extraParams=None,dbType='postgres'):
	'''
	Give the SQL INSERT statement
	@param params: dict keyed by field name of values
	@param extraParams: any extra fields that you have created beyond the normal ais message fields
	@rtype: sqlhelp.insert
	@return: insert class instance
	@todo: allow optional type checking of params?
	@warning: this will take invalid keys happily and do what???
	'''
	import sqlhelp
	i = sqlhelp.insert('srbm',dbType=dbType)

	if dbType=='postgres':
		finished = []
		for key in params:
			if key in finished: 
				continue

			if key not in toPgFields and key not in fromPgFields:
				if type(params[key])==Decimal: i.add(key,float(params[key]))
				else: i.add(key,params[key])
			else:
				if key in fromPgFields:
					val = params[key]
				        # Had better be a WKT type like POINT(-88.1 30.321)
					i.addPostGIS(key,val)
					finished.append(key)
				else:
					# Need to construct the type.
					pgName = toPgFields[key]
					#valStr='GeomFromText(\''+pgTypes[pgName]+'('
					valStr=pgTypes[pgName]+'('
					vals = []
					for nonPgKey in fromPgFields[pgName]:
						vals.append(str(params[nonPgKey]))
						finished.append(nonPgKey)
					valStr+=' '.join(vals)+')'
					i.addPostGIS(pgName,valStr)
	else:
		for key in params: 
			if type(params[key])==Decimal: i.add(key,float(params[key]))
			else: i.add(key,params[key])

	if None != extraParams:
		for key in extraParams: 
			i.add(key,extraParams[key])

	return i

######################################################################
# LATEX SUPPORT
######################################################################

def latexDefinitionTable(outfile=sys.stdout
		):
	'''
	Return the LaTeX definition table for this message type
	@param outfile: file like object to print to.
	@type outfile: file obj
	@return: LaTeX table string via the outfile
	@rtype: str

	'''
	o = outfile

	o.write('''
\\begin{table}%[htb]
\\centering
\\begin{tabular}{|l|c|l|}
\\hline
Parameter & Number of bits & Description 
\\\\  \\hline\\hline
MessageID & 6 & AIS message number.  Must be 14 \\\\ \hline 
RepeatIndicator & 2 & Indicated how many times a message has been repeated \\\\ \hline 
UserID & 30 & Unique ship identification number (MMSI).  Also known as the Source ID \\\\ \hline 
Spare2 & 1 & Must be 0\\\\ \\hline \\hline
Total bits & 39 & Appears to take 1 slot with 129 pad bits to fill the last slot \\\\ \\hline
\\end{tabular}
\\caption{AIS message number 14: Safety related broadcast message}
\\label{tab:srbm}
\\end{table}
''')

######################################################################
# Text Definition
######################################################################

def textDefinitionTable(outfile=sys.stdout
		,delim='\t'
		):
	'''
	Return the text definition table for this message type
	@param outfile: file like object to print to.
	@type outfile: file obj
	@return: text table string via the outfile
	@rtype: str

	'''
	o = outfile
	o.write('''Parameter'''+delim+'Number of bits'''+delim+'''Description 
MessageID'''+delim+'''6'''+delim+'''AIS message number.  Must be 14
RepeatIndicator'''+delim+'''2'''+delim+'''Indicated how many times a message has been repeated
UserID'''+delim+'''30'''+delim+'''Unique ship identification number (MMSI).  Also known as the Source ID
Spare2'''+delim+'''1'''+delim+'''Must be 0
Total bits'''+delim+'''39'''+delim+'''Appears to take 1 slot with 129 pad bits to fill the last slot''')


######################################################################
# UNIT TESTING
######################################################################
import unittest
def testParams():
	'''Return a params file base on the testvalue tags.
	@rtype: dict
	@return: params based on testvalue tags
	'''
	params = {}
	params['MessageID'] = 14
	params['RepeatIndicator'] = 1
	params['UserID'] = 1193046
	params['Spare2'] = 0

	return params

class Testsrbm(unittest.TestCase):
	'''Use testvalue tag text from each type to build test case the srbm message'''
	def testEncodeDecode(self):

		params = testParams()
		bits   = encode(params)
		r      = decode(bits)

		# Check that each parameter came through ok.
		self.failUnlessEqual(r['MessageID'],params['MessageID'])
		self.failUnlessEqual(r['RepeatIndicator'],params['RepeatIndicator'])
		self.failUnlessEqual(r['UserID'],params['UserID'])
		self.failUnlessEqual(r['Spare2'],params['Spare2'])

def addMsgOptions(parser):
	parser.add_option('-d','--decode',dest='doDecode',default=False,action='store_true',
		help='decode a "srbm" AIS message')
	parser.add_option('-e','--encode',dest='doEncode',default=False,action='store_true',
		help='encode a "srbm" AIS message')
	parser.add_option('--RepeatIndicator-field', dest='RepeatIndicatorField',default=0,metavar='uint',type='int'
		,help='Field parameter value [default: %default]')
	parser.add_option('--UserID-field', dest='UserIDField',metavar='uint',type='int'
		,help='Field parameter value [default: %default]')

def main():
	from optparse import OptionParser
	parser = OptionParser(usage="%prog [options]",
		version="%prog "+__version__)

	parser.add_option('--doc-test',dest='doctest',default=False,action='store_true',
		help='run the documentation tests')
	parser.add_option('--unit-test',dest='unittest',default=False,action='store_true',
		help='run the unit tests')
	parser.add_option('-v','--verbose',dest='verbose',default=False,action='store_true',
		help='Make the test output verbose')

	# FIX: remove nmea from binary messages.  No way to build the whole packet?
	# FIX: or build the surrounding msg 8 for a broadcast?
	typeChoices = ('binary','nmeapayload','nmea') # FIX: what about a USCG type message?
	parser.add_option('-t','--type',choices=typeChoices,type='choice',dest='ioType'
		,default='nmeapayload'
		,help='What kind of string to write for encoding ('+', '.join(typeChoices)+') [default: %default]')


	outputChoices = ('std','html','csv','sql' )
	parser.add_option('-T','--output-type',choices=outputChoices,type='choice',dest='outputType'
		,default='std'
		,help='What kind of string to output ('+', '.join(outputChoices)+') [default: %default]')

	parser.add_option('-o','--output',dest='outputFileName',default=None,
			  help='Name of the python file to write [default: stdout]')

	parser.add_option('-f','--fields',dest='fieldList',default=None, action='append',
			  choices=fieldList,
			  help='Which fields to include in the output.  Currently only for csv output [default: all]')

	parser.add_option('-p','--print-csv-field-list',dest='printCsvfieldList',default=False,action='store_true',
			  help='Print the field name for csv')

	parser.add_option('-c','--sql-create',dest='sqlCreate',default=False,action='store_true',
			  help='Print out an sql create command for the table.')

	parser.add_option('--latex-table',dest='latexDefinitionTable',default=False,action='store_true',
			  help='Print a LaTeX table of the type')

	parser.add_option('--text-table',dest='textDefinitionTable',default=False,action='store_true',
			  help='Print delimited table of the type (for Word table importing)')
	parser.add_option('--delimt-text-table',dest='delimTextDefinitionTable',default='\t'
			  ,help='Delimiter for text table [default: \'%default\'](for Word table importing)')


	dbChoices = ('sqlite','postgres')
	parser.add_option('-D','--db-type',dest='dbType',default='postgres'
			  ,choices=dbChoices,type='choice'
			  ,help='What kind of database ('+', '.join(dbChoices)+') [default: %default]')

	addMsgOptions(parser)

	(options,args) = parser.parse_args()
	success=True

	if options.doctest:
		import os; print os.path.basename(sys.argv[0]), 'doctests ...',
		sys.argv= [sys.argv[0]]
		if options.verbose: sys.argv.append('-v')
		import doctest
		numfail,numtests=doctest.testmod()
		if numfail==0: print 'ok'
		else: 
			print 'FAILED'
			success=False

	if not success: sys.exit('Something Failed')
	del success # Hide success from epydoc

	if options.unittest:
		sys.argv = [sys.argv[0]]
		if options.verbose: sys.argv.append('-v')
		unittest.main()

	outfile = sys.stdout
	if None!=options.outputFileName:
		outfile = file(options.outputFileName,'w')


	if options.doEncode:
		# First make sure all non required options are specified
		if None==options.RepeatIndicatorField: parser.error("missing value for RepeatIndicatorField")
		if None==options.UserIDField: parser.error("missing value for UserIDField")
		msgDict={
			'MessageID': '14',
			'RepeatIndicator': options.RepeatIndicatorField,
			'UserID': options.UserIDField,
			'Spare2': '0',
		}

		bits = encode(msgDict)
		if 'binary'==options.ioType: print str(bits)
		elif 'nmeapayload'==options.ioType:
		    # FIX: figure out if this might be necessary at compile time
		    #print "bitLen",len(bits)
		    bitLen=len(bits)
		    if bitLen%6!=0:
			bits = bits + BitVector(size=(6 - (bitLen%6)))  # Pad out to multiple of 6
		    #print "result:",binary.bitvectoais6(bits)[0]
		    print binary.bitvectoais6(bits)[0]


		# FIX: Do not emit this option for the binary message payloads.  Does not make sense.
		elif 'nmea'==options.ioType: 
		    #bitLen=len(bits)
                    #if bitLen%6!=0:
		    #	bits = bits + BitVector(size=(6 - (bitLen%6)))  # Pad out to multiple of 6
                    import aisutils.uscg as uscg
                    nmea = uscg.create_nmea(bits)
                    print nmea
                    #
                    #


                    #sys.exit("FIX: need to implement creating nmea capability")
		else: sys.exit('ERROR: unknown ioType.  Help!')


	if options.sqlCreate:
		sqlCreateStr(outfile,options.fieldList,dbType=options.dbType)

	if options.latexDefinitionTable:
		latexDefinitionTable(outfile)

	# For conversion to word tables
	if options.textDefinitionTable:
		textDefinitionTable(outfile,options.delimTextDefinitionTable)

	if options.printCsvfieldList:
		# Make a csv separated list of fields that will be displayed for csv
		if None == options.fieldList: options.fieldList = fieldList
		import StringIO
		buf = StringIO.StringIO()
		for field in options.fieldList:
			buf.write(field+',')
		result = buf.getvalue()
		if result[-1] == ',': print result[:-1]
		else: print result

	if options.doDecode:
		if len(args)==0: args = sys.stdin
		for msg in args:
			bv = None

			if msg[0] in ('$','!') and msg[3:6] in ('VDM','VDO'):
				# Found nmea
				# FIX: do checksum
				bv = binary.ais6tobitvec(msg.split(',')[5])
			else: # either binary or nmeapayload... expect mostly nmeapayloads
				# assumes that an all 0 and 1 string can not be a nmeapayload
				binaryMsg=True
				for c in msg:
					if c not in ('0','1'):
						binaryMsg=False
						break
				if binaryMsg:
					bv = BitVector(bitstring=msg)
				else: # nmeapayload
					bv = binary.ais6tobitvec(msg)

			printFields(decode(bv)
				    ,out=outfile
				    ,format=options.outputType
				    ,fieldList=options.fieldList
				    ,dbType=options.dbType
				    )

############################################################
if __name__=='__main__':
    main()
