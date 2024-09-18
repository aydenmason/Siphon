package me_ayden;

import org.bukkit.event.Listener;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.Bukkit;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class SiphonPlugin extends JavaPlugin {
    @Override
    public void onLoad() {}{
        //called when plugin is loaded, but not enabled yet
    }
    @Override
    public void onEnable() {
        // Register event listener
        Bukkit.getPluginManager().registerEvents((Listener) new PlayerDataListener(this), this);

        // Create the data folder if it doesn't exist
        if (!getDataFolder().exists()) {
            getDataFolder().mkdir();
        }

        getLogger().info("Siphon Plugin enabled!");
    }
    @Override
    public void onDisable() {
        getLogger().info("Siphon Plugin disabled!");
    }

    // Function to save player data to a file
    public void savePlayerData(String playerName, String data) {
        File file = new File(getDataFolder(), playerName + "-data.txt");

        // Get the current timestamp
        String timestamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());

        // Append the timestamp to the data
        String dataWithTimestamp = "[" + timestamp + "] " + data;

        try {
            java.nio.file.Files.write(file.toPath(), (dataWithTimestamp + "\n").getBytes(), java.nio.file.StandardOpenOption.APPEND, java.nio.file.StandardOpenOption.CREATE);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}