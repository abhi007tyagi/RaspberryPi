package com.tyagiabhinav.hellomqtt;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import java.io.UnsupportedEncodingException;

public class MainActivity extends AppCompatActivity {

    public static final String TAG = "Hello MQTT Android App";
    private MqttClient client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        try {
            MemoryPersistence persistance = new MemoryPersistence();
            client = new MqttClient("tcp://192.168.1.4:1883", "AndroidClient", persistance);
            client.connect();
        } catch (MqttException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void actionON(View view) {
        Log.d(TAG, " Turn ON the LED");
        String payload = "ON";
        publish(payload);
    }

    public void actionOFF(View view) {
        Log.d(TAG, " Turn OFF the LED");
        String payload = "OFF";
        publish(payload);
    }

    private void publish(String payload) {
        String topic = "topic/led";
        byte[] encodedPayload;
        try {
            encodedPayload = payload.getBytes("UTF-8");
            MqttMessage message = new MqttMessage(encodedPayload);
            client.publish(topic, message);
        } catch (UnsupportedEncodingException | MqttException e) {
            e.printStackTrace();
//        } finally {
//            try {
//                client.disconnect();
//            } catch (MqttException e) {
//                e.printStackTrace();
//            }
        }
    }
}
