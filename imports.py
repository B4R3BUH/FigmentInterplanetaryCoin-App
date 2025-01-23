from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy import Config
from plyer import vibrator

import asyncio
import pymysql
from pymysql import cursors

import random
import webbrowser

from datetime import datetime, timedelta