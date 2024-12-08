import streamlit as st
import pandas as pd
from PIL import Image
import os
import glob

# Title

img_files=glob.glob("instockitems/*.jpg")
for imgs in img_files:
  st.image(imgs)
