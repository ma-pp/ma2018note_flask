from flask_restplus import fields
from flask import request
from app.note import api


# Get User's folder list
FolderListSch = api.model( 'Folders List', {
                            'url' : fields.String(required=True, description='Link to folder. Based on ID'),
                            'name' : fields.String(required=True, description="Folder's name"),
                            'privacy': fields.String(required=True, description="Folder's privacy")
                            }
                        )

# Post new folder

NewFolderSch = api.model('New Folder', {
                            'name': fields.String(required=True, description="Folder's name"),
                            'description': fields.String(required=True, description="Folder's description")
                            }
                        )
