// panel/server.js
const express = require('express');
const path = require('path');
const passport = require('passport');
const session = require('express-session');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const DiscordStrategy = require('passport-discord').Strategy;

const app = express();

// Serve static files
app.use(express.static(path.join(__dirname, 'html')));
app.use(express.static(path.join(__dirname, 'css')));
app.use(express.static(path.join(__dirname, 'js')));

// Configure session
app.use(session({ secret: 'secret', resave: false, saveUninitialized: true }));

// Initialize Passport
app.use(passport.initialize());
app.use(passport.session());

// Configure Passport to use Google Strategy
passport.use(new GoogleStrategy({
    clientID: 'GOOGLE_CLIENT_ID',
    clientSecret: 'GOOGLE_CLIENT_SECRET',
    callbackURL: "http://localhost:3000/auth/google/callback"
},
    function (accessToken, refreshToken, profile, cb) {
        return cb(null, profile);
    }
));

// Configure Passport to use Discord Strategy
passport.use(new DiscordStrategy({
    clientID: 'DISCORD_CLIENT_ID',
    clientSecret: 'DISCORD_CLIENT_SECRET',
    callbackURL: "http://localhost:3000/auth/discord/callback",
    scope: ['identify', 'email']
},
    function (accessToken, refreshToken, profile, cb) {
        return cb(null, profile);
    }
));

passport.serializeUser((user, done) => {
    done(null, user);
});

passport.deserializeUser((obj, done) => {
    done(null, obj);
});

// Routes
app.get('/auth/google',
    passport.authenticate('google', { scope: ['profile'] }));

app.get('/auth/google/callback',
    passport.authenticate('google', { failureRedirect: '/' }),
    function (req, res) {
        res.redirect('/');
    });

app.get('/auth/discord',
    passport.authenticate('discord'));

app.get('/auth/discord/callback',
    passport.authenticate('discord', { failureRedirect: '/' }),
    function (req, res) {
        res.redirect('/');
    });

app.listen(3000, () => {
    console.log('Server started on http://localhost:3000');
});
