package com.nabluejay.watchtomorrow;

import android.app.Activity;
import android.content.DialogInterface;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;

import androidx.core.content.ContextCompat;

import com.google.android.material.bottomsheet.BottomSheetDialogFragment;
import com.nabluejay.watchtomorrow.Model.WatchTomorrowModel;
import com.nabluejay.watchtomorrow.Utils.DatabaseHandler;

public class AddNewShow extends BottomSheetDialogFragment {

    public static final String TAG = "ActionBottomDialog";

    private EditText newShowText;
    private Button newShowSaveButton;
    private DatabaseHandler db;

    public static AddNewShow newInstance(){
        return new AddNewShow();
    }

    @Override
    public void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setStyle(STYLE_NORMAL, R.style.DialogStyle);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View view = inflater.inflate(R.layout.new_show, container, false);
        getDialog().getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_RESIZE);
        return view;
    }

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState){
        super.onViewCreated(view, savedInstanceState);
        newShowText = getView().findViewById(R.id.newShowText);
        newShowSaveButton = getView(). findViewById(R.id.newShowButton);

        db = new DatabaseHandler(getActivity());
        db.openDatabase();

        boolean isUpdate = false;
        final Bundle bundle = getArguments();
        if(bundle != null){
            isUpdate = true;
            String show = bundle.getString("show");
            newShowText.setText(show);
            if(show.length()>0){
                newShowSaveButton.setTextColor(ContextCompat.getColor(getContext(),R.color.design_default_color_primary_dark));
            }
        }
        newShowText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                // This disables the save button if you don't have anything in the text box
                if(s.toString().equals("")){
                    newShowSaveButton.setEnabled(false);
                    newShowSaveButton.setTextColor(Color.GRAY);
                }
                else{
                    newShowSaveButton.setEnabled(true);
                    newShowSaveButton.setTextColor(ContextCompat.getColor(getContext(),R.color.design_default_color_primary_dark));
                }
            }

            @Override
            public void afterTextChanged(Editable s) {
            }
        });

        boolean finalIsUpdate = isUpdate;
        newShowSaveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String text = newShowText.getText().toString();
                if(finalIsUpdate){
                    db.updateShow(bundle.getInt("id"), text);
                }
                else{
                    WatchTomorrowModel show = new WatchTomorrowModel();
                    show.setShow(text);
                    show.setStatus(0);
                }
                dismiss();
            }
        });
    }

    @Override
    public void onDismiss(DialogInterface dialog){
        Activity activity = getActivity();
        if(activity instanceof DialogCloseListener){
            ((DialogCloseListener)activity).handleDialogClose(dialog);
        }
    }

}
