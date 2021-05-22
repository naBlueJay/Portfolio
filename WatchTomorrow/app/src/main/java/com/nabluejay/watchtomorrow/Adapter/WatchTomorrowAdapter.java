package com.nabluejay.watchtomorrow.Adapter;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.CompoundButton;

import androidx.recyclerview.widget.RecyclerView;

import com.nabluejay.watchtomorrow.AddNewShow;
import com.nabluejay.watchtomorrow.MainActivity;
import com.nabluejay.watchtomorrow.Model.WatchTomorrowModel;
import com.nabluejay.watchtomorrow.R;
import com.nabluejay.watchtomorrow.Utils.DatabaseHandler;

import java.util.List;

public class WatchTomorrowAdapter extends RecyclerView.Adapter<WatchTomorrowAdapter.ViewHolder> {

    private List<WatchTomorrowModel> watchTomorrowList;
    private MainActivity activity;
    private DatabaseHandler db;

    public WatchTomorrowAdapter(DatabaseHandler db,MainActivity activity) {
        this.db = db;
        this.activity = activity;
    }

    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType){
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.task_layout, parent, false);
        return new ViewHolder(itemView);
    }

    public void onBindViewHolder(ViewHolder holder, int position){
        db.openDatabase();
        WatchTomorrowModel item = watchTomorrowList.get(position);
        holder.show.setText(item.getShow());
        holder.show.setChecked(toBoolean(item.getStatus()));
        holder.show.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                    db.updateStatus(item.getId(), 1);
                }
                else{
                    db.updateStatus(item.getId(), 0);
                }
            }
        });
    }

    public int getItemCount(){
        return watchTomorrowList.size();
    }

    private boolean toBoolean(int n){

        return n!=0;
    }

    public void setShow(List<WatchTomorrowModel> watchTomorrowList){
        this.watchTomorrowList = watchTomorrowList;
        notifyDataSetChanged();
    }

//    public void setShows(List<WatchTomorrowModel> showList){
//        this.watchTomorrowList = showList;
//    }

    public void editItem(int position){
        WatchTomorrowModel item = watchTomorrowList.get(position);
        Bundle bundle = new Bundle();
        bundle.putInt("id",item.getId());
        bundle.putString("task",item.getShow());
        AddNewShow fragment = new AddNewShow();
        fragment.setArguments(bundle);
        fragment.show(activity.getSupportFragmentManager(), AddNewShow.TAG);
    }
    public static class ViewHolder extends RecyclerView.ViewHolder{
        CheckBox show;

        ViewHolder(View view){
            super(view);
            show = view.findViewById(R.id.watchTomorrowCheckBox);
        }
    }
}
