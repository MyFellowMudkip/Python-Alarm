# import modules that will be used, these are datetime, the base tkinter set and messagebox, csv and partial (from
# functools). This is so I don't get errors when I used them.
import datetime
from tkinter import *
from tkinter import messagebox
import csv
from functools import partial

# makes/runs the main menu and displays it as the root window. It is called mainMenu when being referred to as a
# variable. It is placed here in the code because it starts the GUI
mainMenu = Tk()

# Titles the top bar of the main menu Alarm GUI. Placed here in the code because it means that the window runs and
# immediately has a name
mainMenu.title("Alarm GUI")


# Function that is built around the ability to create an alarm and show this visually. The function for the button is
# placed above the button that will call it because if the button is pressed it won't know the function unless it is
# before
def alarmMade():
    # Makes a separate window which has the mainMenu as its host and displays it separately. It is also called
    # makeAlarm when being referred to as a variable. It is placed here so the the window immediately shows up and
    # then we can work with it later
    make_alarm = Toplevel()

    # Titles the top bar of the. Placed here in the code because it means that the window runs and
    # immediately has a name
    make_alarm.title("Make Alarm")

    # makes a label on the GUI called pls_name. It is placed on the make_alarm window and will be displayed as Name:.
    # It is placed in the top left corner of the gui and expands 2 columns wide. It is placed here in the code to
    # keep things working from the top left to the top right. Must be before it is used in the function.
    pls_name = Label(make_alarm, text="Name:").grid(row=0, column=0, columnspan=2)

    # makes a entry bar on the gui called insert_name. It is placed on the make_alarm window and will have an auto
    # filled answer of A Simple Alarm. The entry bar is placed one row below the bottom left corner in the GUI but spans
    # 2 columns across. It is placed here in the code just to keep things ordered neatly. Must be before it is used
    # in the function.
    insert_name = Entry(make_alarm, border=10)
    insert_name.insert(0, "A Simple Alarm")
    insert_name.grid(row=1, column=0, columnspan=2)

    # makes a label on the GUI called pls_desc. It is placed on the make_alarm window and will be displayed as
    # Description:. It is placed in the top right corner of the gui and expands 2 columns wide. It is placed here in
    # the code to keep things working from the top left to the bottom right. Must be before it is used in the function.
    pls_desc = Label(make_alarm, text="Description").grid(row=0, column=1, columnspan=2)

    # makes a entry bar on the gui called insert_desc. It is placed on the make_alarm window and will have an auto
    # filled answer of An alarm that is simple. The entry bar is placed one row below the bottom right corner in the
    # GUI but spans 2 columns across. It is placed here in the code just to keep things ordered neatly. Must be
    # before it is used in the function.
    insert_desc = Entry(make_alarm, border=10)
    insert_desc.insert(0, "An alarm that is simple")
    insert_desc.grid(row=1, column=1, columnspan=2)

    # makes a label on the GUI called pls_year. It is placed on the make_alarm window and will be displayed as Year:.
    # It is placed in the middle left of the gui. It is placed here in the code to keep things working from the top
    # left to the bottom right. Must be before it is used in the function.
    pls_year = Label(make_alarm, text="Year:").grid(row=2, column=0)

    # makes a entry bar on the gui called years. It is placed on the make_alarm window and will have an auto filled
    # answer of current year it is now. The entry bar is placed one row label describing it (around the middle left) in
    # the GUI but spans 2 columns across. It is placed here in the code just to keep things ordered neatly. Must be
    # before it is used in the function
    years = Entry(make_alarm, border=10)
    years.insert(0, datetime.datetime.now().year)
    years.grid(row=3, column=0)

    # makes a label on the GUI called pls_month. It is placed on the make_alarm window and will be displayed as
    # Month, in no. form:. It is placed in the middle of the gui. It is placed here in the code to keep things
    # working from the top left to the bottom right. Must be before it is used in the function.
    pls_month = Label(make_alarm, text="Month, in no. form:").grid(row=2, column=1)

    # makes a entry bar on the gui called months. It is placed on the make_alarm window and will have an auto filled
    # answer of current month it is now. The entry bar is placed one row label describing it (around the middle) in
    # the GUI. It is placed here in the code just to keep things ordered neatly. Must be
    # before it is used in the function
    months = Entry(make_alarm, border=10)
    months.insert(0, datetime.datetime.now().month)
    months.grid(row=3, column=1)

    # makes a label on the GUI called pls_day. It is placed on the make_alarm window and will be displayed as
    # Day of Month:. It is placed in the middle of the gui. It is placed here in the code to keep things
    # working from the top left to the bottom right. Must be before it is used in the function.
    pls_day = Label(make_alarm, text="Day of Month:").grid(row=2, column=2)

    # makes a entry bar on the gui called days. It is placed on the make_alarm window and will have an auto filled
    # answer of current day it is now. The entry bar is placed one row label describing it (around the middle right)
    # in the GUI. It is placed here in the code just to keep things ordered neatly. Must be before it is used in the
    # function
    days = Entry(make_alarm, border=10)
    days.insert(0, datetime.datetime.now().day)
    days.grid(row=3, column=2)

    # makes a label on the GUI called pls_hour. It is placed on the make_alarm window and will be displayed as
    # Hour (24h time):. It is placed in the bottom left of the gui. It is placed here in the code to keep things
    # working from the top left to the bottom right. Must be before it is used in the function.
    pls_hour = Label(make_alarm, text="Hour (24h time):").grid(row=5, column=0)

    # makes a entry bar on the gui called hours. It is placed on the make_alarm window and will have an auto filled
    # answer of current hour it is now. The entry bar is placed one row label describing it (or the bottom right corner)
    # in the GUI. It is placed here in the code just to keep things ordered neatly. Must be before it is used in the
    # function
    hours = Entry(make_alarm, border=10)
    hours.insert(0, datetime.datetime.now().hour)
    hours.grid(row=6, column=0)

    # makes a label on the GUI called pls_minute. It is placed on the make_alarm window and will be displayed as
    # Minute, (0 - 59):. It is placed in the bottom right of the gui. It is placed here in the code to keep things
    # working from the top left to the bottom right. Must be before it is used in the function.
    pls_minute = Label(make_alarm, text="Minute, (0 - 59):").grid(row=5, column=1)

    # makes a entry bar on the gui called minutes. It is placed on the make_alarm window and will have an auto filled
    # answer of current minute it is now. The entry bar is placed one row label describing it (or the bottom right
    # corner) in the GUI. It is placed here in the code just to keep things ordered neatly. Must be before it is used
    # in the function
    minutes = Entry(make_alarm, border=10)
    minutes.insert(0, datetime.datetime.now().minute)
    minutes.grid(row=6, column=1)

    # This is a variable outside the function. It is set as a label with but it but is placed nowhere nor does it
    # have anything on it until the set alarm button has been pressed. I made this variable outside because in order
    # to have it change words, it must be defined outside of the function as it must forget the previous words before
    # you can change it.
    alarm_set_response = Label(make_alarm)

    # This is a button that sets an alarm and writes it into the csv file (where it is permanently stored). It also
    # holds the majority of the error testing because you need to make sure you have the correct input to write in.
    def SetAlarm(datetime, alarm_set_response):

        # tests to see if the input of the years is an integer. I did this because if you put anything but an integer
        # into datetime you come out with an error
        try:
            int(years.get())

        # If the input would display and error, display a popup that's is shown as an error, stop the function and
        # continue the GUI as if nothing else happened. I do this because it allows me to prevent the GUI from crashing
        except:
            messagebox.showerror("Error", "You have entered the years incorrectly, please put in an appropriate number")
            return

        # tests to see if the input of the months is an integer. I did this because if you put anything but an integer
        # into datetime you come out with an error
        try:
            int(months.get())

        # If the input was an error, display a popup that's is shown as an error, stop the function and
        # continue the GUI as if nothing else happened. I do this because it allows me to prevent the GUI from crashing
        except:
            messagebox.showerror("Error",
                                 "You have entered the months incorrectly, please put in an appropriate number")
            return
        # tests to see if the input of the days is an integer. I did this because if you put anything but an integer
        # into datetime you come out with an error
        try:
            int(days.get())

        # If the input was an error, display a popup that's is shown as an error, stop the function and
        # continue the GUI as if nothing else happened. I do this because it allows me to prevent the GUI from crashing
        except:
            messagebox.showerror("Error", "You have entered the days incorrectly, please put in an appropriate number")
            return

        # tests to see if the input of the hours is an integer. I did this because if you put anything but an integer
        # into datetime you come out with an error
        try:
            int(hours.get())

        # If the input would display and error, display a popup that's is shown as an error, stop the function and
        # continue the GUI as if nothing else happened. I do this because it allows me to prevent the GUI from crashing
        except:
            messagebox.showerror("Error", "You have entered the hours incorrectly, please put in an appropriate number")
            return

        # tests to see if the input of the months is an integer. I did this because if you put anything but an integer
        # into datetime you come out with an error
        try:
            int(minutes.get())

        # If the input was an error, display a popup that's is shown as an error, stop the function and
        # continue the GUI as if nothing else happened. I do this because it allows me to prevent the GUI from crashing
        except:
            messagebox.showerror("Error",
                                 "You have entered the minutes incorrectly, please put in an appropriate number")
            return

        # tests to see if the input of the months is an integer. I did this because if you put anything but an integer
        # into datetime you come out with an error
        try:
            datetime.datetime(int(years.get()), int(months.get()), int(days.get()), int(hours.get()),
                              int(minutes.get()))

        # If the input was an error, display a popup that's is shown as an error, stop the function and
        # continue the GUI as if nothing else happened. I do this because it allows me to prevent the GUI from crashing
        except:
            messagebox.showerror("Error",
                                 "You have entered the date incorrectly, please put in appropriate numbers")
            return

        # set the response equal to true. This is just so you can still go through the 2nd if statement even if you
        # didnt pass the first
        response = True

        # if the time in the entry are before the current time display a message asking whether the user wants to
        # make the alarm. Then store it as the variable response in boolean. I do this because a alarm set before the
        # current time isn't really an a alarm but i felt like it should still be accepted. If the they say no then
        # make the response false
        if datetime.datetime(int(years.get()), int(months.get()), int(days.get()), int(hours.get()),
                             int(minutes.get())) <= datetime.datetime.now():
            response = messagebox.askyesno("Before the time you know",
                                           "You have just entered a time earlier than now \n "
                                           "Are you sure you want to make this alarm?")

        # if the date is a proper date/time and the response is True
        if datetime.datetime(int(years.get()), int(months.get()), int(days.get()), int(hours.get()),
                             int(minutes.get())) and response == True:

            # set the alarm count to 0, this is because I dont want the alarm count to be exceedingly high each time
            # hit the button
            alarm_count = 0

            # open the csv file out side the project and read it as a series of dictionaries. This is so I can
            # reference each piece of data
            with open("AlarmSettings.csv", "r") as alarmSettings_file:
                csv_alarmSettings = csv.DictReader(alarmSettings_file)

                # for each alarm made already in the csv file, add 1 to the alarm count. This is so I can find out
                # what the ID is.
                for row in csv_alarmSettings:
                    alarm_count = alarm_count + 1

            # clear where the label saying what the alarm is (alarm_set_response) is even if there is nothing there.
            # This prevents the alarm message from being a mess.
            alarm_set_response.grid_forget()

            # then make an label saying that an alarm has been set, includes the data the user has put in. This is
            # just to tell the user that the alarm has been created. it is place at the bottom of the window when called
            alarm_set_response = Label(make_alarm,
                                       text="Your alarm is set for " + hours.get() + ":" + minutes.get() + " on " + days.get() +
                                            "/" + months.get() + "/" + years.get()).grid(row=7, column=0)

            # because a new alarm is about to be made, increase the alarm_count by 1
            alarm_count = alarm_count + 1

            # open the csv file out side the project and write it as a dictionaries but append not over write. Call
            # it alarmSettings_file. This is so we can add a new alarm and be able to reference it
            with open("AlarmSettings.csv", "a") as alarmSettings_file:

                # makes a list of fieldnames which should be used as the key values for the alarm. This is so I dont
                # have to repeated add the keys for each dictionary and only say it once.
                fieldnames = ['ID', 'Name', 'CreatedOn', 'Description', 'EndYears', 'EndMonths', 'EndDays', 'EndHours',
                              'EndMinutes']

                # make a variable called add_alarm, write it as a dictionary in the csv file and use the fieldnames
                # as the keywords. This is so I only have to reference one variable to add each alarm
                add_alarm = csv.DictWriter(alarmSettings_file, fieldnames=fieldnames)

                # add a new dictionary into the csv file. Make each value of the alarm match the key of the alarm and
                # make the ID be the current alarm count. I make it like this so it can easily be referancable when i
                # have to read and process it
                add_alarm.writerow({"ID": alarm_count, "Name": insert_name.get(), "Description": insert_desc.get(),
                                    "CreatedOn": datetime.datetime.now(), "EndYears": years.get(),
                                    "EndMonths": months.get(), "EndDays": days.get(), "EndHours": hours.get(),
                                    "EndMinutes": minutes.get()})

        # if the alarm passes doesnt pass through any if statement and passes though every try/exception, then show
        # an error message as a pop up. This is just an extra layer of security just in case the input does work and
        # it tells the user there is an error in general.
        else:
            messagebox.showerror("Error", "You have just entered an error")

    # this is the button that sets the alarm using the values the user has put in. It is shown on the make_alarm
    # button, has a text called Set Alarm, padding across of 50 pixels and 20 pixels vertically. However its main
    # function is to call the main function and send the nessessary parameters. It is also place in the bottom right
    # corner
    set_alarm_btn = Button(make_alarm, text="Set Alarm", padx=50, pady=20,
                           command=partial(SetAlarm, datetime, alarm_set_response)).grid(row=5, column=2, columnspan=2,
                                                                                         rowspan=2)

    # Function that is built around the ability to read/show an alarm visually. It contains a list of alarms that the
    # user can choose to read. It also enables the user to clear all alarms.


def SeeAlarmsFunct():
    # makes several empty lists related to each of key of the dictionaries in the csv file. This is so I can view any
    # alarm based on its number in the list and then any value based on the list it is.
    IDs = []
    Names = []
    Description = []
    createdTimes = []
    endYears = []
    endMonths = []
    endDays = []
    endHours = []
    endMinutes = []

    # open the csv file and set it too dictionary reader. The file is called alarmSettings_file and the variable that
    # reads it as a dictionary is called csv_alarmSettings. It is read as a dictionary because it means I can show
    # the alarms data without actually knowing what the user inputted in.
    with open("AlarmSettings.csv", "r") as alarmSettings_file:
        csv_alarmSettings = csv.DictReader(alarmSettings_file)

        # for each dictionary in the csv_alarmSettings, add each values' data into the corresponding array. I do this
        # so I can call the alarm based on its ID but I can also call the data within it based on the array I want to
        # use.
        for row in csv_alarmSettings:
            IDs.append(row['ID'])
            Names.append(row['Name'])
            Description.append(row['Description'])
            createdTimes.append(row['CreatedOn'])
            endYears.append(row['EndYears'])
            endMonths.append(row['EndMonths'])
            endDays.append(row['EndDays'])
            endHours.append(row['EndHours'])
            endMinutes.append(row['EndMinutes'])

    # if any of the arrays are empty still, it means that either the csv file has been tampered with incorrectly or
    # noone has made an alarm to read. In which case the alarm file has not got a complete alarm and so the alarm
    # reader file should not be used. It displays a popup describing this aswell. The reason I have done it like this
    # is so that the user doesnt get any errors when reading an alarm.
    if IDs == [] or Names == [] or Description == [] or createdTimes == [] or endYears == [] or endMonths == [] or endDays == [] or endHours == [] or endMinutes == []:
        messagebox.showerror("No Alarms!", "You had an error because you have yet to make a complete alarm yet")

    # if the arrays aren't empty then the alarm is ok to continue the function.
    else:

        # Makes a separate window which has the mainMenu as its host and displays it separately. It is also called
        # AlarmReader when being referred to as a variable. It is placed here so the the window immediately shows up and
        # then we can work with it later
        AlarmReader = Toplevel()

        # Titles the top bar of the. Placed here in the code because it means that the window runs and
        # immediately has a name
        AlarmReader.title("Current Alarms")

        # makes a label on the alarm reader that is a little larger, the same font though and is placed at the top of
        # the alarm. It has a text saying Your preset alarms are:. I made this label so the user knows what the
        # option menu is for.
        alarmList = Label(AlarmReader, text="Your preset alarms are:", font=("Helvetica", 16)).grid(row=0, column=1)

        # makes a variable called clicked which is so the option menu can store whatever ID the user clicks on. This
        # means that the algorithm knows exactly which alarm to show.
        clicked = IntVar()

        # automatically set the clicked variable to the first alarm made. This can be changed through the option menu
        # but it means that if the user immediatly wants to show a alarm, it can show the first one made.
        clicked.set(IDs[0])

        # make an option menu (like the ones you see on a forum) called view_alarms. It is placed directly below the
        # label describing it and only shows options which are the IDs of all the alarms made. Then store this in the
        # variable called clicked.
        view_alarms = OptionMenu(AlarmReader, clicked, *IDs).grid(row=1, column=1)

        # make a function that when the user clicks a button it will display each value of the set alarm that the
        # user picked in the option menu above. I made this so the user can view the details of the alarm he/she
        # created.
        def alarmDetails(clicked, IDs, Names, Description, createdTimes, endYears, endMonths, endDays, endHours,
                         endMinutes):

            # make the selected alarms' ID match the value in the ID array. This is so we can display the alarm that
            # the user picks and not the next alarm the user might have made.
            selectedAlarm = clicked.get() - 1

            # set the time it will end as one solid date/time, instead of a bunch of values.
            endTime = datetime.datetime(int(endYears[selectedAlarm]), int(endMonths[selectedAlarm]),
                                        int(endDays[selectedAlarm]), int(endHours[selectedAlarm]),
                                        int(endMinutes[selectedAlarm]))

            # find the time left by finding the delta time of the time it will end and what it is now. If it is
            # negative it has already passed 'x' long ago. This is so we can display how long is left in the alarm
            # before it will expire.
            time_left = endTime - datetime.datetime.now()

            # makes a gap from the delete button and all the data of the alarm chosen. This is so the user doesnt
            # accidentally delete all the alarms as well as clearly shows the data of the alarm chosen. It is placed
            # between the alarm details and the delete button on the Alarm Reader window
            gap = Label(AlarmReader).grid(row=3, column=1)

            # label just saying that it is displaying all the details of the selected alarm. The font the same but
            # the font size is a little larger. It is placed below the alarm but has a gap larger that normal between
            # it and the delete button. So it can be separated from the delete button and show things in a neater way.
            alarm_title = Label(AlarmReader, text="Alarm Details", font=("Helvetica", 12)).grid(row=4, column=1)

            # displays a message saying representing that the number next to the selected alarms shows its ID. The
            # label is called alarm_id and shows ID:. It is placed on the left side below the alarm_title on the
            # Alarm Reader window.
            alarm_id = Label(AlarmReader, text="ID:                        ").grid(row=5, column=0)

            # displays the selected alarms id. The variable is called alarm_id_ans and is placed on the right side
            # below the alarm details, separated by a gap. This is shown on the Alarm reader window.
            alarm_id_ans = Label(AlarmReader, text=IDs[selectedAlarm]).grid(row=5, column=2)

            # displays a message saying representing that the number next to the selected alarms shows its name. The
            # label is called alarm_name and shows Name:. It is placed on the left side below the alarm_id on the
            # Alarm Reader window.
            alarm_name = Label(AlarmReader, text="Name:                  ").grid(row=6, column=0)

            # displays the selected alarms name. The variable is called alarm_name_ans and is placed on the right side
            # below the alarm id. This is shown on the Alarm reader window.
            alarm_name_ans = Label(AlarmReader, text=Names[selectedAlarm]).grid(row=6, column=2)

            # displays a message saying representing that the number next to it shows the selected alarms
            # description. The label is called alarm_desc and shows Desc:. It is placed on the left side below the
            # alarm_name on the Alarm Reader window.
            alarm_desc = Label(AlarmReader, text="Desc:                    ").grid(row=7, column=0)

            # displays the selected alarms description. The variable is called alarm_desc_ans and is placed on the
            # right side below the alarm name. This is shown on the Alarm reader window.
            alarm_desc_ans = Label(AlarmReader, text=Description[selectedAlarm]).grid(row=7, column=2)

            # displays a message saying representing that the number next to it shows the selected alarms creation
            # date. The label is called alarm_start and shows It was created on:. It is placed on the left side below
            # the alarm_desc on the Alarm Reader window.
            alarm_start = Label(AlarmReader, text="It was created on:").grid(row=8, column=0)

            # displays the selected alarms creation date. The variable is called alarm_start_ans and is placed on the
            # right side below the alarm description. This is shown on the Alarm reader window.
            alarm_start_ans = Label(AlarmReader, text=createdTimes[selectedAlarm]).grid(row=8, column=2)

            # displays a message saying representing that the number next to it shows the selected alarms end date.
            # The label is called alarm_end and shows It will end on:. It is placed on the left side below the
            # alarm_start on the Alarm Reader window.
            alarm_end = Label(AlarmReader, text="It will end on:      ").grid(row=9, column=0)

            # displays the selected alarms end date. The variable is called alarm_end_ans and is placed on the right
            # side below the alarm creation date. This is shown on the Alarm reader window.
            alarm_end_ans = Label(AlarmReader, text=endTime).grid(row=9, column=2)

            # displays a message saying representing that the number next to it shows the selected alarms time delta.
            # The label is called alarm_timedelta and shows It will go off in:. It is placed on the left side below
            # the alarm_end on the Alarm Reader window.
            alarm_timedelta = Label(AlarmReader, text="It will go off in:   ").grid(row=10, column=0)

            # displays the selected alarms time delta. The variable is called alarm_timedelta_ans and is placed on
            # the right side below the alarm end date. This is shown on the Alarm reader window. If the answer is
            # negative then the alarm has already expired.
            alarm_timedelta_ans = Label(AlarmReader, text=time_left).grid(row=10, column=2)

        # a function thats primary purpose is to overwrite all alarms made. I made this so that if the user makes too
        # many alarms and just want to clear the list, he/she can. The function is called delete.
        def delete():

            # open the csv file and call the file alarmSettings_file. Then set it to overwrite the file and store
            # this as the variable csv_alarmSettings.
            with open("AlarmSettings.csv", "w") as alarmSettings_file:
                csv_alarmSettings = csv.writer(alarmSettings_file)

                # makes a list of fieldnames, this will be used as the keys in each dictionary but it is also written
                # as an array at the top of the file so that we dont have to continuously keep writing the keys.
                fieldnames = ['ID', 'Name', 'CreatedOn', 'Description', 'EndYears', 'EndMonths', 'EndDays', 'EndHours',
                              'EndMinutes']

                # write all the fieldnames at the top of the csv file so we dont have to keep writing the keys in and
                # only have to reference it.
                csv_alarmSettings.writerow(fieldnames)

                # then open the file again but set it to make new lines of code instead of overwriting everything.
                # This is so we can put the values that the user puts in, in a separate row. If we didnt do this the
                # input could be thought of as more keys instead of values.
            with open("AlarmSettings.csv", "a") as alarmSettings_file:

                # write and empty row at the bottom of the csv file. This is so we can put the values that the user
                # puts in, in a separate row. If we didnt do this the input could be thought of as more keys instead
                # of values.
                csv_alarmSettings = csv.writer(alarmSettings_file)
                csv_alarmSettings.writerow("")

        # Button allowing the user to choose and show the details of a selected alarm. It has text on it saying
        # Choose Alarm:, padding horizontally of 30 pixels and vertically 10 pixels. When pressed it does the
        # alarmDetails function as well as taking in the variables/arrays of clicked, IDs, Names, Description,
        # createdTimes, endYears, endMonths, endDays, endHours and endMinutes. I made this so the user can view the
        # details of the alarm he/she created. It is shown on the end AlarmReader window below the option menu.
        select_to_see_alarm = Button(AlarmReader, text="Choose Alarm", padx=30, pady=10,
                                     command=partial(alarmDetails, clicked, IDs, Names, Description, createdTimes,
                                                     endYears, endMonths, endDays, endHours, endMinutes
                                                     )).grid(row=2, column=1)

        # Button allowing the user to clear all alarms in the csv file. It has text on it saying Delete All Alarms:,
        # padding horizontally of 30 pixels and vertically 10 pixels. When pressed it does the delete function. I
        # made this so that if the user makes too many alarms and just want to clear the list, he/she can.
        # It is shown on the end AlarmReader window below the choose alarm button.
        delete_alarm = Button(AlarmReader, text="Delete All Alarms", padx=30, pady=10, command=partial(delete)).grid(
            row=11, column=1)

# Labels just expanding the corners of the main menu. I did this purely for aestetics but also to so the user can
# easily see the main menu
enlargen_gui_corner_1 = Label(mainMenu, padx=6, pady=2.5).grid(row=0, column=0)
enlargen_gui_corner_2 = Label(mainMenu, padx=6, pady=2.5).grid(row=3, column=2)

# Button allowing the see the AlarmReader window. It has text on it saying see current alarms:,
# padding horizontally of 64 pixels and vertically 20 pixels. When pressed it does the AlarmReader function. I
# made this so that user can see all alarms. It is shown on the end mainMenu window above the alarmMaker button.
seeAlarms = Button(mainMenu, text="see current alarms", padx=64, pady=20, command=SeeAlarmsFunct).grid(row=1, column=1)

# Button allowing the see the create alarm window. It has text on it saying create alarm:, padding horizontally of 80
# pixels and vertically 20 pixels. When pressed it does the alarmMade function. I made this so that user can see
# all alarms. It is shown on the end mainMenu window below the seeAlarms button.
alarmMaker = Button(mainMenu, text="create alarm", padx=80, pady=20, command=alarmMade).grid(row=2, column=1)

#Finishes the loop that shows the window.
mainMenu.mainloop()
