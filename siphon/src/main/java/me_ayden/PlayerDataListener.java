package me_ayden;

import org.bukkit.entity.LivingEntity;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.entity.EntityDamageByEntityEvent;
import org.bukkit.event.entity.EntityDamageEvent;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.event.player.PlayerMoveEvent;

import java.util.HashMap;
import java.util.Map;

public class PlayerDataListener  implements  Listener{
    private final SiphonPlugin plugin;
    private final Map<String, Long> lastAttackTime = new HashMap<>(); // Track last attack times per player

    public PlayerDataListener(SiphonPlugin plugin){
        this.plugin = plugin;
    }
    @EventHandler
    public void onPlayerMove(PlayerMoveEvent event) {
        String playerName = event.getPlayer().getName();
        String from = event.getFrom().toString();
        String to = event.getTo().toString();
        String data = "Player " + playerName + " moved from " + from + " to " + to;

        plugin.savePlayerData(playerName, data);
    }
    @EventHandler
    public void onPlayerDamage(EntityDamageByEntityEvent event) {
        String damager = event.getDamager().getName();
        String entity = event.getEntity().getName();
        String data = "Entity " + entity + " damaged by " + damager + " for " + event.getDamage() + " damage";
        plugin.savePlayerData(entity, data);
        if (event.getDamager() instanceof Player && event.getEntity() instanceof LivingEntity) {
            Player player = (Player) event.getDamager();
            LivingEntity target = (LivingEntity) event.getEntity();

            double distance = player.getLocation().distance(target.getLocation());

            // Normal attack range in Minecraft is about 3 blocks
            if (distance > 3.0) {
                plugin.savePlayerData(player.getName(), "Player hit " + target.getType() + " from " + distance + " blocks away. REACH?");
            }
        }
    }
    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        Player player = event.getPlayer();
        String playerName = player.getName();
        String data = "Player " + playerName + " joined the game with " + player.getPing() + " ms";

        plugin.savePlayerData(playerName, data);
    }
    @EventHandler
    public void onPlayerAttack(EntityDamageByEntityEvent event) {
        if (event.getDamager() instanceof Player) {
            Player player = (Player) event.getDamager();
            String playerName = player.getName();

            long currentTime = System.currentTimeMillis();
            long lastTime = lastAttackTime.getOrDefault(playerName, 0L);
            long timeDiff = currentTime - lastTime;

            // Assuming a normal cooldown of 600ms for sword attacks in Minecraft
            if (timeDiff < 600) {
                plugin.savePlayerData(playerName, "Attacked too fast! Cooldown not respected. Time between attacks: " + timeDiff + "ms.");
            }

            // Update the last attack time
            lastAttackTime.put(playerName, currentTime);
        }
    }
    @EventHandler
    public void onEntityDamage(EntityDamageEvent event) {
        if (event.getEntity() instanceof Player player) {
            if (event.getCause() == EntityDamageEvent.DamageCause.FALL) {
                double fallDistance = player.getFallDistance();
                if (event.getDamage() == 0) {
                    plugin.savePlayerData(player.getName(), "Player fell " + fallDistance + " blocks but took no damage. Possible no-fall cheat.");
                }
            }
        }
    }

}
