package com.nabluejay.watchtomorrow;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.nabluejay.watchtomorrow.Adapter.WatchTomorrowAdapter;
import com.nabluejay.watchtomorrow.Model.WatchTomorrowModel;
import com.nabluejay.watchtomorrow.Utils.DatabaseHandler;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MainActivity extends AppCompatActivity implements DialogCloseListener{

    private RecyclerView showsRecyclerView;
    private WatchTomorrowAdapter showsAdapter;
    private FloatingActionButton fab;

    private List<WatchTomorrowModel> showList;
    private DatabaseHandler db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().hide();
        db = new DatabaseHandler(this);
        db.openDatabase();

        showList = new ArrayList<>();

        showsRecyclerView = findViewById(R.id.showsRecyclerView);
        showsRecyclerView.setLayoutManager(new LinearLayoutManager(this));
        showsAdapter = new WatchTomorrowAdapter(db,this);
        showsRecyclerView.setAdapter(showsAdapter);

        fab = findViewById(R.id.fab);

        showList = db.getAllShows();
        Collections.reverse(showList);
        showsAdapter.setShow(showList);

        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AddNewShow.newInstance().show(getSupportFragmentManager(),AddNewShow.TAG);
            }
        });
    }

   @Override
    public void handleDialogClose(DialogInterface dialog){
        showList = db.getAllShows();
        Collections.reverse(showList);
        showsAdapter.setShow(showList);
        showsAdapter.notifyDataSetChanged();
    }
}