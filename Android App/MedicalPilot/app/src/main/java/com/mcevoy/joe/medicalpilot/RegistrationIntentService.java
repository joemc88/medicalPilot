package com.mcevoy.joe.medicalpilot;

import android.app.IntentService;
import android.content.Intent;
import android.util.Log;
import android.webkit.CookieManager;
import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.gms.gcm.GcmPubSub;
import com.google.android.gms.gcm.GoogleCloudMessaging;
import com.google.android.gms.iid.InstanceID;
import java.util.HashMap;
import java.util.Map;

/** This class is used to register the device with the web app. It gets cookies from the web view and passes them to the register device URL
 *  so the web app will immediately associate the registration with the currently logged in user.
 *
 * **/

public class RegistrationIntentService extends IntentService {

    private String URL = getString(R.string.homepageURL);
    private static final String TAG = "RegIntentService";

    public RegistrationIntentService() {
        super(TAG);
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        try {
            InstanceID instanceID = InstanceID.getInstance(this);
            String token = instanceID.getToken(getString(R.string.gcm_defaultSenderId), GoogleCloudMessaging.INSTANCE_ID_SCOPE, null);
            GcmPubSub subscription = GcmPubSub.getInstance(this); subscription.subscribe(token, "/topics/formReminders", null);
            Log.d("Registration Token", token);
            registerToken(token);
        }catch(Exception e){
            Log.i("Token Error", "Token Failed");
        }
    }


    public void registerToken(final String token) {
        final String cookies = getCookie(URL);

        RequestQueue queue = Volley.newRequestQueue(this);
        String url =URL + "/userAdmin/registerDevice/?token="+token;

        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                       Log.i("Response is: ", response);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.i("Registration error","That didn't work!");
                     }
                }
        ){
            @Override
            public Map<String, String> getHeaders() throws AuthFailureError {
            Map<String, String>  params = new HashMap<>();
            params.put("Cookie", cookies);
            return params;
        }};

        queue.add(stringRequest);
    }

    //retrieve cookies from webview
    public String getCookie(String siteName){
        CookieManager cookieManager = CookieManager.getInstance();
        String cookies = cookieManager.getCookie(siteName);

        return cookies;
    }

}