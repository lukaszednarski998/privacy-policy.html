package pl.arvion.hacktheworldwallpaper;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.RectF;
import android.os.Handler;
import android.os.Looper;
import android.service.wallpaper.WallpaperService;
import android.view.SurfaceHolder;
import java.util.Random;

public class CanvasWallpaperService extends WallpaperService {
    @Override public Engine onCreateEngine() { return new EngineImpl(); }

    private final class EngineImpl extends Engine {
        private final Handler handler = new Handler(Looper.getMainLooper());
        private final Paint p = new Paint(Paint.ANTI_ALIAS_FLAG);
        private final Random rnd = new Random(1337);
        private final Runnable frame = this::drawFrame;
        private boolean visible;
        private long start;
        private float[] phase;
        private int[] speed;

        @Override public void onCreate(SurfaceHolder holder) {
            super.onCreate(holder);
            start = System.currentTimeMillis();
            setOffsetNotificationsEnabled(false);
        }

        @Override public void onVisibilityChanged(boolean v) {
            visible = v;
            handler.removeCallbacks(frame);
            if (v) handler.post(frame);
        }

        @Override public void onSurfaceDestroyed(SurfaceHolder holder) {
            visible = false;
            handler.removeCallbacks(frame);
            super.onSurfaceDestroyed(holder);
        }

        @Override public void onDestroy() {
            handler.removeCallbacks(frame);
            super.onDestroy();
        }

        private void drawFrame() {
            if (!visible) return;
            Canvas c = null;
            try {
                c = getSurfaceHolder().lockCanvas();
                if (c != null) render(c);
            } finally {
                if (c != null) getSurfaceHolder().unlockCanvasAndPost(c);
            }
            if (visible) handler.postDelayed(frame, 33L);
        }

        private void render(Canvas c) {
            int w = c.getWidth(), h = c.getHeight();
            c.drawColor(Color.BLACK);
            float t = (System.currentTimeMillis() - start) / 1000f;
            drawGrid(c, w, h);
            drawDigits(c, w, h, t);
            drawTitle(c, w, h);
            drawGlobe(c, w, h, t);
            drawHud(c, w, h, t);
        }

        private void drawGrid(Canvas c, int w, int h) {
            p.setStyle(Paint.Style.STROKE);
            p.setStrokeWidth(1f);
            p.setColor(Color.rgb(35, 0, 0));
            int step = Math.max(38, w / 23);
            for (int x = 0; x < w; x += step) c.drawLine(x, 0, x, h, p);
            for (int y = 0; y < h; y += step) c.drawLine(0, y, w, y, p);
        }

        private void drawDigits(Canvas c, int w, int h, float t) {
            int cols = Math.max(18, w / 34);
            if (phase == null || phase.length != cols) {
                phase = new float[cols];
                speed = new int[cols];
                for (int i = 0; i < cols; i++) {
                    phase[i] = rnd.nextFloat();
                    speed[i] = 34 + rnd.nextInt(75);
                }
            }
            p.setStyle(Paint.Style.FILL);
            p.setTypeface(android.graphics.Typeface.MONOSPACE);
            p.setTextSize(Math.max(18f, w / 35f));
            float colW = w / (float) cols;
            for (int i = 0; i < cols; i++) {
                float off = (phase[i] * h + t * speed[i]) % (h + 420f) - 210f;
                for (int r = -3; r < h / 28 + 8; r++) {
                    float y = off + r * 30f;
                    if (y < -40 || y > h + 40) continue;
                    int alpha = Math.min(215, 80 + ((r + i) % 6 == 0 ? 110 : 0));
                    p.setColor(Color.argb(alpha, 255, 15, 15));
                    c.drawText((((r + i + (int)(t * 3)) & 1) == 0) ? "0" : "1", i * colW + 5, y, p);
                }
            }
        }

        private void drawTitle(Canvas c, int w, int h) {
            float y = h * 0.145f;
            p.setStyle(Paint.Style.FILL);
            p.setTypeface(android.graphics.Typeface.create(android.graphics.Typeface.MONOSPACE, android.graphics.Typeface.BOLD));
            p.setTextAlign(Paint.Align.CENTER);
            p.setTextSize(w * 0.073f);
            p.setColor(Color.rgb(255, 25, 25));
            p.setShadowLayer(18f, 0f, 0f, Color.RED);
            c.drawText("HACK THE WORLD", w / 2f, y, p);
            p.clearShadowLayer();
            p.setStyle(Paint.Style.STROKE);
            p.setStrokeWidth(Math.max(2f, w / 500f));
            p.setColor(Color.rgb(180, 10, 10));
            c.drawRect(w * .08f, y - w * .09f, w * .92f, y + w * .035f, p);
        }

        private void drawGlobe(Canvas c, int w, int h, float t) {
            float cx = w / 2f;
            float cy = h * 0.37f;
            float r = Math.min(w * 0.34f, h * 0.19f);
            p.setStyle(Paint.Style.STROKE);
            p.setStrokeWidth(Math.max(2f, w / 430f));
            p.setColor(Color.rgb(255, 25, 25));
            p.setShadowLayer(12f, 0, 0, Color.RED);
            c.drawCircle(cx, cy, r, p);

            for (int i = -4; i <= 4; i++) {
                float yy = cy + i * r / 5f;
                float half = (float)Math.sqrt(Math.max(0, r * r - (yy - cy) * (yy - cy)));
                c.drawOval(new RectF(cx - half, yy - r * .05f, cx + half, yy + r * .05f), p);
            }

            float rot = (t * 36f) % 360f;
            for (int i = 0; i < 12; i++) {
                double a = Math.toRadians(rot + i * 30f);
                float squeeze = .12f + .88f * Math.abs((float)Math.cos(a));
                c.drawOval(new RectF(cx - r * squeeze, cy - r, cx + r * squeeze, cy + r), p);
            }
            p.clearShadowLayer();

            p.setStyle(Paint.Style.FILL);
            for (int i = 0; i < 170; i++) {
                double lon = Math.toRadians((i * 137.5 + rot) % 360);
                double lat = Math.toRadians(-62 + (i % 30) * 4.2);
                double z = Math.cos(lat) * Math.cos(lon);
                if (z < -.12) continue;
                float x = cx + r * (float)(Math.cos(lat) * Math.sin(lon));
                float y = cy - r * (float)Math.sin(lat);
                p.setColor(Color.argb(130 + (int)(110 * Math.max(0, z)), 255, 20, 20));
                c.drawCircle(x, y, 1.5f + 3f * (float)Math.max(0, z), p);
            }

            p.setStyle(Paint.Style.STROKE);
            p.setStrokeWidth(1.5f);
            p.setColor(Color.rgb(170, 10, 10));
            c.drawCircle(cx, cy, r * 1.13f, p);
            c.drawCircle(cx, cy, r * 1.23f, p);
            c.drawLine(cx - r * 1.35f, cy, cx + r * 1.35f, cy, p);
            c.drawLine(cx, cy - r * 1.35f, cx, cy + r * 1.35f, p);
        }

        private void drawHud(Canvas c, int w, int h, float t) {
            p.setTypeface(android.graphics.Typeface.MONOSPACE);
            p.setStyle(Paint.Style.FILL);
            p.setTextSize(Math.max(13f, w * .022f));
            p.setColor(Color.rgb(220, 20, 20));
            p.setTextAlign(Paint.Align.LEFT);
            String[] left = {"SYSTEM ONLINE", "GLOBAL NETWORK", "DATA STREAM", "SIGNAL ACTIVE", "WORLD MATRIX"};
            float y = h * .58f;
            for (String s : left) { c.drawText(s, w * .06f, y, p); y += p.getTextSize() * 1.7f; }
            p.setTextAlign(Paint.Align.RIGHT);
            String[] right = {"TRACKING", "ANALYZING", "SCANNING", "SYNCING", "RENDERING"};
            y = h * .58f;
            for (String s : right) { c.drawText(s, w * .94f, y, p); y += p.getTextSize() * 1.7f; }
            p.setTextAlign(Paint.Align.CENTER);
            p.setTextSize(Math.max(12f, w * .020f));
            c.drawText("/// CYBER TERMINAL ///  " + ((int)(t * 17) % 100) + "%", w / 2f, h * .525f, p);
        }
    }
}
