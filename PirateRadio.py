#!/usr/bin/env python3
# Floyd's Dreams of Dylan Pirate Radio
# Author: Jeremy Nelson
# Description: Forked from Wynter Woods (Make Magazine) 

import configparser
import os
import pathlib
import re
import random
import subprocess
import sys
import threading
import time

from lxml import etree

RSS = { "rss": "http://www.itunes.com/dtd/podcast-1.0.dtd" }

class PirateRadio(object):

    def __init__(self, **kwargs):
        self.fm_process = None
        self.on_off = ["off", "on"]
        self.frequency = kwargs.get("frequency", 89.5)
        self.shuffle = kwargs.get("shuffle", False)
        self.repeat_all = kwargs.get("repeat_all", False)
        self.merge_audio_in = kwargs.get("merge_audio_in", False)
        self.play_stereo = kwargs.get("stereo", True)
        self.podcasts = pathlib.Path(
            kwargs.get("podcasts",
            "/home/pi/floyds-dreams-of-dylan/podcasts"))
        self.music_pipe_r, self.music_pipe_w = os.pipe()
        self.microphone_pipe_r, self.microphone_pipe_w = os.pipe()
        self.media_re = re.compile(".(aac|mp3|wav|flac|m4a|ogg|pls|m3u)$")
        self.pls_re = re.compile(".pls$")

    def __play_items__(self, podcast_path):
        with podcast_path.open() as f:
            podcast = etree.parse(f.read())
        items = podcast.findall("rss:channel/rss:item", RSS)
        for item in items:
            print(f"{item.find('rss:title', RSS).text}")
            enclosure = item.find("rss:enclosure", RSS)
            if self.media_re.search(enclosure.attrib.get('url')):
                subprocess.call([
                    "ffmpeg", 
                    "-i", enclosure.attrib.get('url'),
                    "-f", "s16le",
                    "-acodec","pcm_s16le",
                    "-ac", "2" if self.play_stereo else "1" ,
                    "-ar","44100","-"],
                    stdout=self.music_pipe_w, 
                    stderr=dev_null)
		

    def main(self):
        self.daemonize()
        if self.repeat_all:
            while(True):
                self.play_songs()
        else:
            self.play_songs()
            return 0

    def daemonize(self):
        fpid=os.fork()
        if fpid!=0:
            sys.exit(0)



    def build_items(podcast):
        if self.media_re.search(podcast.filename):
            yield podcast

    def podcasts(self):
        for podcast in self.location.iterdir():
            print(f"Podcast is {podcast}")

    def play_songs(self):
        print(f"Playing songs to frequency {self.frequency}")
        print(f"Shuffle is {self.on_off[self.shuffle]}")
        print(f"Repeat All is {self.on_off[self.repeat_all]}")
        print(f"Stereo playback is {self.on_off[self.play_stereo]}")
        if self.shuffle:
            random.shuffle(self.podcasts())
        with open(os.devnull, "w") as dev_null:
            for podcast in self.podcasts.iterdir():
                self.__play_items__(podcast)


    def run_pifm(self, use_audio_in=False):
        with open(os.devnull, "w") as dev_null:
            self.fm_process = subprocess.Popen(
                    ["/root/pifm",
                     "-",str(self.frequency),
                     "44100", "stereo" if play_stereo else "mono"], 
                    stdin=music_pipe_r, 
                    stdout=dev_null)

	

    
if __name__ == "__main__":
    pirate_radio = PirateRadio()
    pirate_radio.main()

