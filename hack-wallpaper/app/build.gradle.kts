plugins {
    id("com.android.application")
}

android {
    namespace = "pl.arvion.hacktheworldwallpaper"
    compileSdk = 36

    defaultConfig {
        applicationId = "pl.arvion.hacktheworld.live2026"
        minSdk = 24
        targetSdk = 35
        versionCode = 3
        versionName = "1.0.2"
    }

    buildTypes {
        debug {
            isMinifyEnabled = false
        }
        release {
            isDebuggable = false
            isMinifyEnabled = false
            isShrinkResources = false
            signingConfig = signingConfigs.getByName("debug")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}
