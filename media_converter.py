# media_converter.py
import sys, os
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QComboBox
)
from PySide6.QtGui import QIcon
from PIL import Image
import imageio.v2 as imageio
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

class MediaConverter(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Converter")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Select a file to convert:")
        layout.addWidget(self.label)

        # Choose file button
        self.choose_btn = QPushButton("Choose File")
        self.choose_btn.clicked.connect(self.choose_file)
        layout.addWidget(self.choose_btn)

        # Output type combo
        self.output_type = QComboBox()
        layout.addWidget(self.output_type)

        # Convert button
        self.convert_btn = QPushButton("Convert")
        self.convert_btn.clicked.connect(self.convert)
        layout.addWidget(self.convert_btn)

        self.status = QLabel("Status: Idle")
        layout.addWidget(self.status)

        self.setLayout(layout)
        self.file_path = None
        self.file_type = None

    def choose_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Media File", "", 
                    "Images (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.dds);;"
                    "Audio (*.mp3 *.wav *.ogg *.flac);;"
                    "Video (*.mp4 *.avi *.mov *.mkv)")
        if file:
            self.file_path = file
            ext = os.path.splitext(file)[1].lower()
            if ext in [".png",".jpg",".jpeg",".bmp",".tiff",".gif",".dds"]:
                self.file_type = "image"
                self.output_type.clear()
                self.output_type.addItems(["png","jpg","jpeg","bmp","tiff","gif","dds"])
            elif ext in [".mp3",".wav",".ogg",".flac"]:
                self.file_type = "audio"
                self.output_type.clear()
                self.output_type.addItems(["mp3","wav","ogg","flac"])
            elif ext in [".mp4",".avi",".mov",".mkv"]:
                self.file_type = "video"
                self.output_type.clear()
                self.output_type.addItems(["mp4","avi","mov","mkv"])
            self.status.setText(f"Selected: {file}")

    def convert(self):
        if not self.file_path:
            self.status.setText("No file selected")
            return
        out_ext = self.output_type.currentText()
        out_file = os.path.splitext(self.file_path)[0] + f".{out_ext}"

        try:
            if self.file_type == "image":
                img = Image.open(self.file_path)
                img.save(out_file)
            elif self.file_type == "audio":
                audio = AudioSegment.from_file(self.file_path)
                audio.export(out_file, format=out_ext)
            elif self.file_type == "video":
                clip = VideoFileClip(self.file_path)
                clip.write_videofile(out_file)
            self.status.setText(f"Converted to {out_file}")
        except Exception as e:
            self.status.setText(f"Error: {e}")
