from flask_restplus import fields
from flask import request
from app.note import api


# For general message
general_message = api.model('General Message',
                           {
                               'message': fields.String(description='Message for general purpose')
                           }
                           )

# Get User's folder list
folder_list= api.model( 'Folders List',
                       {
                            'id' : fields.String(description='Link to folder. Based on ID'),
                            'name' : fields.String(description="Folder's name"),
                            'privacy': fields.String(description="Folder's privacy"),
                            'author': fields.String(description='Folder\'s author'),
                            'created': fields.DateTime(description='Date Created'),
                            'count': fields.Integer(description='Notes in folder')
                       }
                        )

# Post new folder

new_folder = api.model('New Folder',
                       {
                            'name': fields.String(required=True, description="Folder's name"),
                            'description': fields.String(required=True, description="Folder's description"),
                           'privacy': fields.Integer(required=True, description='Folder\'s privacy')
                       }
                        )

# See all notes in a folder
folder_notes = api.model('Notes in a Folder',
                         {
                        'body': fields.String(description='Note\'s message'),
                        'created': fields.String(description='Date created')
                        }
                        )

# Edit folder
edit_folder = api.model('Edit folder name and privacy',
                       {
                       'name': fields.String(description='New Foldername'),
                       'description': fields.String(description='Folder\'s description'),
                       'privacy': fields.Integer(description='New Folder\'s Privacy')
                       }
                       )

# Read a note
note = api.model('Read a note',
                {
                'id' : fields.String(description='Link to folder. Based on ID'),
                'name' : fields.String(description="Folder's name"),
                'privacy': fields.String(description="Folder's privacy"),
                'author': fields.String(description='Folder\'s author'),
                'created': fields.DateTime(description='Date Created'),
                'count': fields.Integer(description='Notes in folder')
                }
                )

# Posting a new note
new_note = api.model('Post a new note',
                     {
                         'title': fields.String(description='Note\'s Title'),
                         'body': fields.String(description='Note\'s content'),
                         'folder': fields.Integer(description='Folder\'s ID')
                     }
)
