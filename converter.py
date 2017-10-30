import subprocess
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')

infile = sys.argv[1]
outfile = sys.argv[2]

infile=infile.encode('utf-8')
outfile=outfile.encode('utf-8')

print infile
print outfile

subprocess.call(['ffmpeg', '-i', infile, '-codec' ,'copy' ,outfile])
