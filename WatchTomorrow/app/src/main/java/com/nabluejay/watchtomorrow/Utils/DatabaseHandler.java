package com.nabluejay.watchtomorrow.Utils;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import com.nabluejay.watchtomorrow.Model.WatchTomorrowModel;

import java.util.ArrayList;
import java.util.List;

public class DatabaseHandler extends SQLiteOpenHelper {

    private static final int VERSION = 1;
    // Defines database name
    private static final String NAME = "showListDatabase";
    // defines table name
    private static final String SHOW_TABLE = "show";
    // defines column names
    private static final String ID = "id";
    // The actual stored text
    private static final String SHOW = "show";
    private static final String STATUS = "status";
    // defines query
    private static final String CREATE_SHOW_TABLE = "CREATE TABLE" + SHOW_TABLE + "(" + ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                    + SHOW + "TEXT, " + STATUS + " INTEGER)";

    // This is the actual reference for the SQL database
    private SQLiteDatabase db;

    public DatabaseHandler(Context context){
        super(context, NAME, null, VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db){
        // query to create new table
        db.execSQL(CREATE_SHOW_TABLE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion){
        // Drop the older tables
        db.execSQL("DROP TABLE IF EXISTS" + SHOW_TABLE);
        // Create tables again
        onCreate(db);
    }

    // open database method to work with the database
    public void openDatabase(){
        // Initiates the database
        db = this.getWritableDatabase();
    }

    public void insertTask(WatchTomorrowModel show){
        ContentValues cv = new ContentValues();
        cv.put(SHOW, show.getShow());
        cv.put(STATUS, 0);
        // saves to database
        db.insert(SHOW_TABLE, null, cv);
    }

    // This will get all the entered shows and store them in an Array
    public List<WatchTomorrowModel> getAllShows(){
        List<WatchTomorrowModel> showList = new ArrayList<>();
        Cursor cur = null;
        // This is coded similar to a Thread or MultiProcessor in python
        // Enters and exits database
        db.beginTransaction();
        try{
            // passing through all the perimeters returning all the rows without any criteria
            cur = db.query(SHOW_TABLE, null, null, null, null, null, null, null);
            if(cur != null){
                if(cur.moveToFirst()){
                    do {
                        WatchTomorrowModel show = new WatchTomorrowModel();
                        show.setId(cur.getInt(cur.getColumnIndex(ID)));
                        show.getShow();cur.getString(cur.getColumnIndex(SHOW));
                        show.setStatus(cur.getInt(cur.getColumnIndex(STATUS)));
                        showList.add(show);
                    }while(cur.moveToNext());
                }
            }
        }
        finally {
            db.endTransaction();
            cur.close();
        }
        return showList;
    }

    // Stores weather the task has been checked or not.
    public void updateStatus(int id, int status){
        ContentValues cv = new ContentValues();
        cv.put(STATUS, status);
        db.update(SHOW_TABLE, cv, ID + "+?", new String[] {String.valueOf(id)});
    }

    // This will update the show
    public void updateShow(int id, String show){
        ContentValues cv = new ContentValues();
        cv.put(SHOW, show);
        db.update(SHOW_TABLE, cv, ID + "=?", new String[] {String.valueOf(id)});
    }

    // Function to delete show
    public void deleteShow(int id){
        db.delete(SHOW_TABLE, ID + "=?", new String[] {String.valueOf(id)});
    }
}
