from flask import Blueprint, render_template , request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
from .models import Notes
views = Blueprint("views",__name__)

@views.route("/",methods=["GET","POST"])
@login_required
def home():
    if request.method == 'POST':
        data = request.form.get('note')
        if len(data) < 1:
            flash("Note is to short!", category='error')
        else:
            new_notes = Notes(data=data, user_id=current_user.id)
            flash("Note added", category='success')
            db.session.add(new_notes)
            db.session.commit()
        
    return render_template("home.html",user=current_user)
@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Notes.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})