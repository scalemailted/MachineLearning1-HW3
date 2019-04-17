""" 
Requires: Weka JAR file, JRE, Python 2.7
Instructions: 
	1. Set the following environmentals: wekaJAR, src, dest
	2. run the script
"""
import time
import os

wekaJAR = '' #BASH command to find your Weka JAR path: find / -name \weka.jar
src = ''     #Source directory of intial Dataset
dest = './'  #Destination directory for output: ARFF file

#Captures Runtime of WEKA dataset conversion into ARFF
def main():
	msBefore = time.time()*1000.0
	getARFF(wekaJAR, src, dest);
	msAfter = time.time()*1000.0
	print str(msAfter - msBefore) + " milliseconds"

#WEKA CLI: convert dataset into ARFF file format 
def getARFF(wekaJAR, src, dest):
	className = 'weka.core.converters.TextDirectoryLoader';
	dest += 'ProcessedData.arff';
	bashCMD = 'java -cp {weka} {className} -dir {src} > {dest}';
	bashCMD = bashCMD.format(weka=wekaJAR, className=className, src=src, dest=dest);
	os.system(bashCMD);

    
if __name__ == '__main__': main()
