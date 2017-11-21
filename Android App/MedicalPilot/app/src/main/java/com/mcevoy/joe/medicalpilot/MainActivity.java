package com.mcevoy.joe.medicalpilot;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.KeyEvent;
import android.webkit.CookieManager;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {
    private WebView myWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myWebView = (WebView) findViewById(R.id.webview);
        if (savedInstanceState != null){
            myWebView.restoreState(savedInstanceState);
        }
        myWebView.setWebViewClient(new WebViewClient(){ @Override
        public void onPageFinished(WebView view, String url){
            String cookies = CookieManager.getInstance().getCookie(url);
            Log.d("called","onpagefinished");

        }});

        myWebView.loadUrl(getString(R.string.homepageURL));

        Intent i = new Intent(this, RegistrationIntentService.class); startService(i);


    }
    protected void onSaveInstanceState(Bundle outState) {
        myWebView.saveState(outState);
    }

    //set up back button to control webview rather than just back out of the app
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (event.getAction() == KeyEvent.ACTION_DOWN) {
            switch (keyCode) {
                case KeyEvent.KEYCODE_BACK:
                    if (myWebView.canGoBack()) {
                        myWebView.goBack();
                    } else {
                        finish();
                    }
                    return true;
            }
        }
        return super.onKeyDown(keyCode, event);
    }


}
