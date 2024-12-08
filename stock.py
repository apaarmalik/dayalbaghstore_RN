import streamlit as st
import pandas as pd
from PIL import Image
import os
import glob

# Title

img_fil=glob.glob("instockitems/*.png")
for imgs in img_fil:
  st.image(imgs)
