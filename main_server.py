from flask import Flask, session, flash, request, render_template, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

host = "localhost"
port = 5000
""" INIT DATABASE CONNECTION BELOW! """

#engine = create_engine('sqlite:///sql_database\\AirportRecords.db') # Uncomment this Line For Windows.
engine = create_engine('sqlite:///sql_database/AirportRecords.db') # Uncomment this line for Linux.
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def index():
    projName = ["Flight Records", "", "active"]
    flight_table = db.execute("SELECT * FROM flight_info").fetchall()
    return render_template('index.html', flight_table=flight_table, projName=projName)


@app.route("/addFlight", methods=["POST", "GET"])
def addFlight():
    projName  = ["Add New Flight Records", "", "", "active"]
    if request.method == "POST": 
        departure = request.form.get("departure_loc")
        arrival   = request.form.get("arrival_loc")
        duration  = request.form.get("duration_time")
        if len(departure) < 5 or len(arrival) < 5 or duration == "":
            flash("Invalid User Input! Try Again With Valid Information.", "danger")
        else:
            db.execute("INSERT INTO flight_info(departure, arrival, duration) VALUES ('%s', '%s', %d)" \
            % (departure, arrival, int(duration)))
            db.commit()
            flash("Your Flight Was Added Successfully", "success")
            return redirect(url_for('index'))

    return render_template("add_flight.html", projName=projName)

@app.route("/modifyFlight", methods=["POST", "GET"])
def modifyFlight():
    projName = ["Modify Flight Records", "", "", "", "" ,"active"]
    flight_table = db.execute("SELECT * FROM flight_info").fetchall()
    
    return render_template("modifyFlight.html", flight_table=flight_table, projName=projName)

@app.route("/editFlight", methods=["POST", "GET"])
def editFlight():
    if request.method == "POST":
        departure          = request.form.get("departure_loc")
        arrival            = request.form.get("arrival_loc")
        duration           = request.form.get("duration_time")
        flight_information = request.form.get("selectedFlight")
        flight_id          = flight_information.split(" From:")[0]
        if len(departure) < 5 or len(arrival) < 5 or int(duration) < 40 or int(flight_id) < 0:
            flash("An Error Occoured! User Input Was Invalid!", "danger")
            return redirect(url_for("modifyFlight"))
        else:
            """MYSQL QUERY"""                  # MYSQL QUERY NEEDED <<-- EDITING DATA FROM FLIGHT RECORDS!
            db.execute("UPDATE flight_info set departure='%s', arrival='%s', duration='%d' WHERE id=%d;"\
            % (str(departure), str(arrival), int(duration), int(flight_id)))
            db.commit()
            flash("Changes Made To Your Selected Flight", "success")
    
    return redirect(url_for('index'))


@app.route("/deleteFlight", methods=["POST", "GET"])
def deleteFlight():
    flight_information = request.form.get("deletionInformation")
    
    if len(flight_information) < 10:
        flash("An Error Occoured Please Try Again!", "danger")
        return redirect(url_for('modifyFlight'))
        
    else:
        """ FETCHING DATA FROM FORMS AND FORMATTING FOR MYSQL DATABASE """
        flight_id        = flight_information.split(": ")[1].split(" From")[0]
        flight_departure = flight_information.split("From: ")[1].split(" To")[0]
        flight_arrival   = flight_information.split("To: ")[1].split(" Duration:")[0]
        flight_duration  = flight_information.split("Duration: ")[1]
        
        """ TAKING ACTION EXECUTING DELETE QUERY ON DATABASE """
        db.execute("delete from flight_info Where id='%d' and departure='%s' and arrival='%s' and duration=%d;"\
         % (int(flight_id), str(flight_departure), str(flight_arrival), int(flight_duration)))
        db.commit() # commit all the changes made to database
        flash("Flight Record Removed Successfully", "success")
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.secret_key = os.urandom(128)
    app.run(host=host, port=port, debug=True)
