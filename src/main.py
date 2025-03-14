import sys
import io
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon, QPainter, QColor, QImage, QPixmap
from PyQt5.QtCore import Qt, QSize

class VoicesSystemTray:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.is_active = False
        self.tray = QSystemTrayIcon()
        self.setup_tray()
        
    def create_active_icon(self):
        # Kırmızı daire ikon oluştur
        size = QSize(32, 32)
        image = QImage(size, QImage.Format.Format_ARGB32)
        image.fill(Qt.transparent)
        
        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(255, 0, 0))  # Kırmızı
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(4, 4, 24, 24)  # Biraz padding bırakıyoruz
        painter.end()
        
        return QIcon(QPixmap.fromImage(image))
    
    def create_passive_icon(self):
        # Köşeleri yuvarlatılmış gri kare ikon oluştur
        size = QSize(32, 32)
        image = QImage(size, QImage.Format.Format_ARGB32)
        image.fill(Qt.transparent)
        
        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(128, 128, 128))  # Gri
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(4, 4, 24, 24, 8, 8)  # Yuvarlatılmış köşeler
        painter.end()
        
        return QIcon(QPixmap.fromImage(image))
    
    def toggle_active_state(self):
        self.is_active = not self.is_active
        self.update_icon()
        
    def update_icon(self):
        icon = self.create_active_icon() if self.is_active else self.create_passive_icon()
        self.tray.setIcon(icon)
        
    def setup_tray(self):
        # İlk ikonu ayarla
        self.update_icon()
        
        # Sol tıklama için sinyal bağlantısı
        self.tray.activated.connect(self.handle_tray_activation)
        
        # Tray ikonunu göster
        self.tray.show()
    
    def handle_tray_activation(self, reason):
        if reason == QSystemTrayIcon.Trigger:  # Sol tıklama
            self.toggle_active_state()
    
    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    voices_tray = VoicesSystemTray()
    voices_tray.run() 