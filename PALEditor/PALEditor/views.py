"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, json
from PALEditor import app
from flask.ext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'pmc_pal'
app.config['MYSQL_DATABASE_PASSWORD'] = 'y6v!S5TFx4Xq'
app.config['MYSQL_DATABASE_DB'] = 'wwd_archive_locator'
app.config['MYSQL_DATABASE_HOST'] = 'pmc-pal-prod.cluster-cldybekb8ks0.us-west-2.rds.amazonaws.com'
mysql.init_app(app)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'edititem.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/insertitem')
def showSignUp():
    return render_template('edititem.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    asdfsdaf = request.cookies
    # read the posted values from the UI
    _containerPostTitle = request.form['inputPostTitle']
    _containerLabel = request.form['inputContainerLabel']
    _barcode = request.form['inputBarcode']
    _storageunit = request.form['inputStorageUnit']
    _shootdate = request.form['inputShootDate']
    _publicationdate = request.form['inputPublicationDate']
    _unitcode = request.form['inputUnitCode']
    _completedby = request.form['inputCompletedBy']
    _research = request.form['inputResearch']
    _photographer = request.form['inputPhotographer']
    _publication = request.form['inputPublication']
    _season = request.form['inputSeason']
    _designer = request.form['inputDesigner']
    _category = request.form['inputCategory']
    _format = request.form['inputFormat']
    _color = request.form['inputColor']
    _rights = request.form['inputRights']
    _location = request.form['inputLocation']
    _pictured = request.form['inputPictured']
    _description = request.form['inputDescription']
    _notes = request.form['inputNotes']
    _oldbarcode = request.form['inputOldBarcode']
    _quantity = request.form['inputQuantity']
    _uuid = request.form['inputUUID']
    _status = request.form['inputStatus']
    _condition = request.form['inputCondition']
    _favorite = request.form['inputFavorite']
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_insert_posts_metadata_wide',(_containerPostTitle,
                                     _containerLabel,
                                     _barcode,
                                     _storageunit,
                                     _shootdate,
                                     _publicationdate,
                                     _unitcode,
                                     _completedby,
                                     _research,
                                     _photographer,
                                     _publication,
                                     _season,
                                     _designer,
                                     _category,
                                     _format,
                                     _color,
                                     _rights,
                                     _location,
                                     _pictured,
                                     _description,
                                     _notes,
                                     _oldbarcode,
                                     _quantity,
                                     _uuid,
                                     _status,
                                     _condition,
                                     _favorite))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        message = "Metadata Inserted Successfully"
        #return render_template('edititem.html', message=message)
        return json.dumps({'message':'Item created successfully !'})
    else:
        message = "Error : " + str(data[0])
        #return render_template('edititem.html', message=message)
        return json.dumps({'error':str(data[0])})

    