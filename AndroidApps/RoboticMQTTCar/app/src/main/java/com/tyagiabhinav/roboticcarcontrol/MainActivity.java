package com.tyagiabhinav.roboticcarcontrol;

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
            client = new MqttClient("tcp://192.168.1.4:1883", "AndroidRoboticMQTTCarClient2", persistance);
            client.connect();
        } catch (MqttException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void actionForward(View view) {
        Log.d(TAG, "Move Forward");
        String payload = "FW";
        publish(payload);
    }

    public void actionBackward(View view) {
        Log.d(TAG, "Move Backward");
        String payload = "BW";
        publish(payload);
    }

    public void actionLeft(View view) {
        Log.d(TAG, "Turn Left");
        String payload = "LT";
        publish(payload);
    }

    public void actionRight(View view) {
        Log.d(TAG, "Turn Right");
        String payload = "RT";
        publish(payload);
    }

    public void actionStop(View view) {
        Log.d(TAG, "Stop");
        String payload = "ST";
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
        }
    }
}
