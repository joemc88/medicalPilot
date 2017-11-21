package com.mcevoy.joe.medicalpilot;

import android.content.Intent;

import com.google.android.gms.iid.InstanceIDListenerService;

/**
 * Created by Joe on 11/09/2017.
 */

public class TokenRefreshListenerService extends InstanceIDListenerService {
    @Override public void onTokenRefresh() { Intent i = new Intent(this, RegistrationIntentService.class); startService(i); }
}
