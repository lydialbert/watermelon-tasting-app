To-Do

Login (by username only) ✅
Search Form (pick a date {optional time range}) --> Avaiable reservations ✅
    Reservation details:
        Start and end on half hour or hour ✅
        Are 30 mins ✅
        Only 1 per month!
        Only book 1 reservation at a time, add feature of an error message if trying to book two at once
    No reservations --> flash a message saying that ✅
Click on appointment to book an appointment (using javascript for an event listener)
Page that shows all reservations (like my bucketlists page)


Four Pages:
    Login screen ✅
    Page to search for appointments ✅
    Results page to view the results (then click to book an appointment)
    Page to view all schedule appointments (optional - edit/cancel appiontment feature)


Questions:
    database question:

    fname = request.form.get("fname")
    username = request.form.get("username")
    user = crud.login_user(fname)

    if user.username == username:
        return render_template("bookings.html")
    else:
        flash("Incorrect username.")
        return redirect('/')

    calendar question:

    c = calendar.TextCalendar(calendar.SUNDAY)
    c_test = c.formatmonth(2022, 1)