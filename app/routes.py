<<<<<<< HEAD
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Record
from app.forms import RecordForm
from sqlalchemy import desc

main_bp = Blueprint('main', __name__)

# ------------------------------
# INDEX + ABOUT
# ------------------------------

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')


# ------------------------------
# LIST RECORDS
# ------------------------------

@main_bp.route('/records')
def list_records():
    search_query = request.args.get('q', '').strip()

    query = Record.query
    if search_query:
        query = query.filter(Record.title.contains(search_query))

    records = query.order_by(Record.created_at.desc()).all()

    return render_template('records_list.html', records=records)


# ------------------------------
# SEARCH BY ID (same as SQLite version)
# ------------------------------

@main_bp.route('/records/search', methods=['GET'])
def search_record():
    record_id = request.args.get("record_id", "").strip()

    if not record_id.isdigit():
        flash("Please enter a valid numeric Record ID.", "error")
        return redirect(url_for("main.list_records"))

    record = Record.query.get(record_id)

    if record is None:
        flash("Record ID not found.", "error")
        return redirect(url_for("main.list_records"))

    return redirect(url_for("main.view_record", id=record_id))


# ------------------------------
# CREATE NEW RECORD
# ------------------------------

@main_bp.route('/records/new', methods=['GET', 'POST'])
def create_record():
    form = RecordForm()

    if form.validate_on_submit():
        record = Record(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(record)
        db.session.commit()

        flash('Record created successfully!', 'success')
        return redirect(url_for('main.list_records'))

    return render_template('form.html', form=form, action='Create')


# ------------------------------
# VIEW RECORD DETAILS
# ------------------------------

@main_bp.route('/records/<int:id>')
def view_record(id):
    record = Record.query.get_or_404(id)
    return render_template('record_detail.html', record=record)


# ------------------------------
# EDIT RECORD
# ------------------------------

@main_bp.route('/records/<int:id>/edit', methods=['GET', 'POST'])
def edit_record(id):
    record = Record.query.get_or_404(id)
    form = RecordForm()

    if form.validate_on_submit():
        record.title = form.title.data
        record.content = form.content.data
        db.session.commit()

        flash('Record updated successfully!', 'success')
        return redirect(url_for('main.view_record', id=id))

    if not form.is_submitted():
        form.title.data = record.title
        form.content.data = record.content

    return render_template('form.html', form=form, action='Edit')


# ------------------------------
# DELETE RECORD
# ------------------------------

@main_bp.route('/records/<int:id>/delete', methods=['POST'])
def delete_record(id):
    record = Record.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()

    flash('Record deleted successfully!', 'success')
=======
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Record
from app.forms import RecordForm
from sqlalchemy import desc

main_bp = Blueprint('main', __name__)

# ------------------------------
# INDEX + ABOUT
# ------------------------------

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')


# ------------------------------
# LIST RECORDS
# ------------------------------

@main_bp.route('/records')
def list_records():
    search_query = request.args.get('q', '').strip()

    query = Record.query
    if search_query:
        query = query.filter(Record.title.contains(search_query))

    records = query.order_by(Record.created_at.desc()).all()

    return render_template('records_list.html', records=records)


# ------------------------------
# SEARCH BY ID (same as SQLite version)
# ------------------------------

@main_bp.route('/records/search', methods=['GET'])
def search_record():
    record_id = request.args.get("record_id", "").strip()

    if not record_id.isdigit():
        flash("Please enter a valid numeric Record ID.", "error")
        return redirect(url_for("main.list_records"))

    record = Record.query.get(record_id)

    if record is None:
        flash("Record ID not found.", "error")
        return redirect(url_for("main.list_records"))

    return redirect(url_for("main.view_record", id=record_id))


# ------------------------------
# CREATE NEW RECORD
# ------------------------------

@main_bp.route('/records/new', methods=['GET', 'POST'])
def create_record():
    form = RecordForm()

    if form.validate_on_submit():
        record = Record(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(record)
        db.session.commit()

        flash('Record created successfully!', 'success')
        return redirect(url_for('main.list_records'))

    return render_template('form.html', form=form, action='Create')


# ------------------------------
# VIEW RECORD DETAILS
# ------------------------------

@main_bp.route('/records/<int:id>')
def view_record(id):
    record = Record.query.get_or_404(id)
    return render_template('record_detail.html', record=record)


# ------------------------------
# EDIT RECORD
# ------------------------------

@main_bp.route('/records/<int:id>/edit', methods=['GET', 'POST'])
def edit_record(id):
    record = Record.query.get_or_404(id)
    form = RecordForm()

    if form.validate_on_submit():
        record.title = form.title.data
        record.content = form.content.data
        db.session.commit()

        flash('Record updated successfully!', 'success')
        return redirect(url_for('main.view_record', id=id))

    if not form.is_submitted():
        form.title.data = record.title
        form.content.data = record.content

    return render_template('form.html', form=form, action='Edit')


# ------------------------------
# DELETE RECORD
# ------------------------------

@main_bp.route('/records/<int:id>/delete', methods=['POST'])
def delete_record(id):
    record = Record.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()

    flash('Record deleted successfully!', 'success')
>>>>>>> 4eea04cc5b8ab6a74f0a65f3a68c4f6f847b7739
    return redirect(url_for('main.list_records'))