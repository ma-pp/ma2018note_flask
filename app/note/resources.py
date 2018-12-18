from flask_restplus import Resource, marshal

from app.note import api
from app.note import serializers as s

@api.route('/folder')
class FolderList(Resource):
    @api.marshal_with(s.folder_list)
    @api.doc(description='Show all folder')
    def get(self):
        data = [
            { 'id':1, 'name':'Folder1', 'privacy': 'private'},
            { 'id':2, 'name':'Folder2', 'privacy': 'public'},
            { 'id':3, 'name':'Folder3', 'privacy': 'contact'}
        ]
        return data

    @api.expect(s.new_folder)
    @api.marshal_with(s.general_message)
    @api.doc(description='Create a new folder')
    def post(self):
        data = request.get_json()
        return marshal(data, FolderListSch),200

@api.route('/folder/<id>')
class FolderNotes(Resource):
    @api.marshal_with(s.folder_notes)
    @api.doc('See all notes in a folder', params={'id': 'Folder ID'})
    def get(self, id):
        data = [
            {'body': 'Note 1', 'created': '2018-09-12'},
            {'body': 'Note 2', 'created': '2018-09-10'}
        ]
        return data

    @api.expect(s.edit_folder)
    @api.marshal_with(s.general_message)
    @api.doc(description='Edit folder attribute', params={'id': 'Folder ID'})
    def put(self, id):
        pass

    @api.marshal_with(s.general_message)
    @api.doc(description='Delete a folder, along with its contents', params={'id': 'Folder ID'})
    def delete(self):
        pass

@api.route('/note')
class PostNote(Resource):
    @api.doc(description='Post a new note')
    @api.expect(s.new_note)
    @api.marshal_with(s.general_message)
    def post(self):
        pass

@api.route('/note/<id>')
class Note(Resource):

    @api.marshal_with(s.note)
    @api.doc(description='Show a content of a note', params={'id': 'Note ID'})
    def get(self, id):
        pass

    @api.marshal_with(s.general_message)
    @api.doc(description='Edit attributes of a note', params={'id': 'Note ID'})
    def put(self, id):
        pass

    @api.marshal_with(s.general_message)
    @api.doc(description='Delete a note', params={'id': 'Note ID'})
    def delete(self, id):
        pass
