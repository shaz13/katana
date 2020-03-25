# parsers.py
import werkzeug
from flask_restplus import reqparse

file_upload = reqparse.RequestParser()
# file_upload.add_argument('xls_file',  
#                          type=werkzeug.datastructures.FileStorage, 
#                          location='files', 
#                          required=False, 
#                          help='XLS file')

file_upload.add_argument('img_file',  
                         type=werkzeug.datastructures.FileStorage, 
                         location='files', 
                         required=True, 
                         help='IMG file MNIST EXAMPLE')