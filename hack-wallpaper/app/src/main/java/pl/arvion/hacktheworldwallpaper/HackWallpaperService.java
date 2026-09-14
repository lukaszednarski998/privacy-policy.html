package pl.arvion.hacktheworldwallpaper;

import android.media.MediaPlayer;
import android.service.wallpaper.WallpaperService;
import android.view.SurfaceHolder;

public class HackWallpaperService extends WallpaperService {
    @Override public Engine onCreateEngine() { return new VideoEngine(); }

    private final class VideoEngine extends Engine {
        private MediaPlayer player;
        private SurfaceHolder holder;
        private boolean visible;

        @Override public void onSurfaceCreated(SurfaceHolder h) {
            super.onSurfaceCreated(h);
            holder = h;
            createPlayer();
        }

        @Override public void onVisibilityChanged(boolean v) {
            visible = v;
            if (v) startPlayer(); else pausePlayer();
        }

        @Override public void onSurfaceDestroyed(SurfaceHolder h) {
            releasePlayer();
            holder = null;
            super.onSurfaceDestroyed(h);
        }

        @Override public void onDestroy() {
            releasePlayer();
            super.onDestroy();
        }

        private void createPlayer() {
            releasePlayer();
            if (holder == null || !holder.getSurface().isValid()) return;
            try {
                player = MediaPlayer.create(HackWallpaperService.this, R.raw.hack_the_world_10s_higher);
                if (player == null) return;
                player.setSurface(holder.getSurface());
                player.setLooping(true);
                player.setVolume(0f, 0f);
                player.setVideoScalingMode(MediaPlayer.VIDEO_SCALING_MODE_SCALE_TO_FIT_WITH_CROPPING);
                if (visible) player.start();
            } catch (Exception e) {
                releasePlayer();
            }
        }

        private void startPlayer() {
            try {
                if (player == null) createPlayer();
                if (player != null && !player.isPlaying()) player.start();
            } catch (Exception ignored) { createPlayer(); }
        }

        private void pausePlayer() {
            try { if (player != null && player.isPlaying()) player.pause(); } catch (Exception ignored) {}
        }

        private void releasePlayer() {
            MediaPlayer p = player;
            player = null;
            if (p == null) return;
            try { p.stop(); } catch (Exception ignored) {}
            try { p.release(); } catch (Exception ignored) {}
        }
    }
}
