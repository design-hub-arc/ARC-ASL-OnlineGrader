#!/usr/local/bin/python3.8
import zipfile, subprocess, sys, os, shutil
import cgi, os
import sys
import cgitb; cgitb.enable()
import coversheet # amending coversheet pdf to the outputted pdf results of the ASL-Net

print("Content-Type: text/html\n")
fPrefix = '/path/to/submissions' # path on server for user submissions

try:
    tf = open(fPrefix+'blah.txt', 'w+')
except OSError as err:
    print('<p>OSError:</p>') # +format(err)+'</p>')
except IOError as err:
    print('<p>IOError:') # +format(err)+'</p>')
    print(err)
    print(sys.exc_type)
    print('</p>')
except:
    print('<p>unknown error:</p>') # +sys.exc_info()[0]+'</p>')


name = ''
id_num = ''
assignment = ''
with open('/tmp/db.log','w') as f:
    form = cgi.FieldStorage()

    # Get student info and assignment info
    if 'name' in form and 'id' in form and 'assignment' in form:

        name = str(form.getvalue('name'))
        id_num = str(form.getvalue('id'))
        assignment = str(form.getvalue('assignment'))
        if name == '' or id_num == '' or assignment == '':
            print('Please go back and enter student or assignment data for the report.')
            exit()
    else:
        print('error parsing student/assignment info from form')
        exit()

    # Get filename here.
    if 'filename' in form:
        fileitem = form['filename']

        # Test if the file was uploaded
        if fileitem.filename:
            # strip leading path from file name to avoid directory traversal attacks
            fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
            bf = open(fPrefix + fn, 'wb') # open local zip
            bf.write(fileitem.file.read()) # save upload
            print('<p>The file "' + fn + '" was uploaded successfully</p>')
        else:
            print('<p>No file was uploaded</p>')
    else:
        print('<p>cannot find filename in form</p>') # Get student info and assignment info
        exit()

# For now we will assume zip files until we have decided for sure
with zipfile.ZipFile(fPrefix + fn, 'r') as zip_ref:
    zip_ref.extractall(fPrefix)

# setup pathing for pdf
output_pdf_name = 'studentID_assignment.pdf'
path_to_pdf = '/path/to/resultsDir/' + output_pdf_name # dir for temp storage + name

# Create server command and Call Network for evaluation
cmd = 'ASLNet/ASL-NET/asl_net.py '
cmd += fPrefix + fn.split('.')[0] + ' 1 ' + 'ASLNet/model.hdf5 '
cmd += path_to_pdf

completed = subprocess.run(
    [sys.executable] + cmd.split(),
    stdout=subprocess.PIPE,
)

print(completed.stdout.decode('utf-8'))

# add cover sheet to the results
coversheet.AddCoverSheet(name, id_num, assignment, path_to_pdf)

# give user option to download the pdf results
print("<p>Download PDF Report:<a href=\"ASLNet/pdf_results/" + output_pdf_name + "\" download>Click Here</a></p>")


# Clean Up Work / Delete submission stuff from server
shutil.rmtree(fPrefix + fn.split('.')[0])
os.remove(fPrefix + fn)
