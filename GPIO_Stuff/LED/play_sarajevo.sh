#! /usr/bin/bash

(spotify 1>/dev/null 2>&1 &) && qdbus org.mpris.MediaPlayer2.spotify / org.freedesktop.MediaPlayer2.OpenUri https://open.spotify.com/track/3sBnSBnzpEYKpJYGsAIbup?si=ba67d321046c4e69