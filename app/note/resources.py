from flask_restplus import Resource, marshal

from app.note import api
from app.note.serializers import *

@api.route('/folder')
@api.doc(description="User's Folder List")
class FolderList(Resource):
    @api.marshal_with(FolderListSch)
    def get(self):
        data = [
            { 'id':1, 'name':'Folder1'},
            { 'id':2, 'name':'Folder2'},
            { 'id':3, 'name':'Folder3'}
        ]
        return data

    @api.expect(NewFolderSch)
    def post(self):
        data = request.get_json()
        return marshal(data, FolderListSch),200

