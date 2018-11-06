# Faça um programa que abra e reproduza um arquivo mp3

from pygame import mixer

mixer.init()
mixer.music.load('/Users/fabiochexx/Documents/Estudo/python/mp3/Tuyo.mp3')
mixer.music.play()