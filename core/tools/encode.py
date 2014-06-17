#-*- coding: UTF-8 -*-


import codecs
import chardet
import os,sys

BLOCKSIZE = 1024

def convert_to_encoding(infile_name, dest_encoding):
   infile = open(infile_name, 'rb')
   result = chardet.detect(infile.read())
   charenc = result['encoding']
   print 'src file encoding: %s' % charenc
   infile.close()

   infile_rawname, infile_extension = os.path.splitext(infile_name)
   
   # target_file_name = infile_rawname  + '.' + dest_encoding + '.' + infile_extension
   target_file_name = infile_name + '.' + dest_encoding
   with codecs.open(infile_name, 'r', charenc) as infile:
    with codecs.open(target_file_name, "w", dest_encoding) as target_file:
        while(True):
            content = infile.read(BLOCKSIZE)
            if not content:
                break
            target_file.write(content)
            
   
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python encode.py src_filename dest_encoding" 
        exit(0)
    convert_to_encoding(sys.argv[1], sys.argv[2])
